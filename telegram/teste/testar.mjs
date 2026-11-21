// Teste local do worker.js com KV e Telegram falsos. Uso: node telegram/teste/testar.mjs
import worker from '../worker.js';
const kv = new Map();
const FILA = {
  get: async (k, t) => (kv.has(k) ? (t === 'json' ? JSON.parse(kv.get(k)) : kv.get(k)) : null),
  put: async (k, v) => kv.set(k, v), delete: async (k) => kv.delete(k),
  list: async ({ prefix }) => ({ keys: [...kv.keys()].filter((k) => k.startsWith(prefix)).map((name) => ({ name })) }),
};
const env = { FILA, TELEGRAM_TOKEN: 'T', DONO_ID: '111', WEBHOOK_SECRET: 'W', FABRICA_KEY: 'F' };
const enviados = [];
globalThis.fetch = async (url, op) => {
  const metodo = url.split('/').pop();
  const corpo = op.body instanceof FormData ? Object.fromEntries([...op.body.entries()].map(([k, v]) => [k, typeof v === 'string' ? v : `<arquivo ${v.size}b>`])) : JSON.parse(op.body);
  enviados.push({ metodo, corpo }); return new Response(JSON.stringify({ ok: true, result: {} }));
};
const B = 'https://chefe.x.workers.dev';
const tgMsg = (de, text, sec = 'W') => worker.fetch(new Request(B + '/telegram', { method: 'POST', headers: { 'X-Telegram-Bot-Api-Secret-Token': sec }, body: JSON.stringify({ message: { from: { id: de }, chat: { id: de }, text } }) }), env);
const tgBot = (de, data) => worker.fetch(new Request(B + '/telegram', { method: 'POST', headers: { 'X-Telegram-Bot-Api-Secret-Token': 'W' }, body: JSON.stringify({ callback_query: { id: 'q', from: { id: de }, data, message: { chat: { id: de }, message_id: 9 } } }) }), env);
const fab = (cam, op = {}, chave = 'F') => worker.fetch(new Request(B + cam, { ...op, headers: { 'X-Fabrica-Key': chave, ...(op.headers || {}) } }), env);
let falhas = 0; const ok = (c, n) => { console.log((c ? 'OK   ' : 'FALHA ') + n); if (!c) falhas++; };
const ultimo = () => enviados.at(-1);

ok((await tgMsg(111, '/start', 'errado')).status === 401, 'webhook com segredo errado é recusado');
enviados.length = 0; await tgMsg(999, '/fila'); ok(enviados.length === 0, 'estranho é ignorado (nada enviado)');
await tgMsg(111, '/ajuda'); ok(ultimo().corpo.text.includes('/produzir'), 'dono recebe a ajuda');
await tgMsg(111, '/fila'); ok(ultimo().corpo.text.startsWith('Fila vazia'), '/fila vazia');
await tgMsg(111, '/produzir'); ok(ultimo().corpo.text.includes('Manda junto'), '/produzir sem texto pede o texto');
await tgMsg(111, '/produzir parte 2 da série do banco'); ok([...kv.keys()].some((k) => k.startsWith('pedido:')), '/produzir vira pedido');
await tgMsg(111, 'faz uma série de golpe do INSS'); ok([...kv.values()].some((v) => v.includes('INSS')), 'texto livre vira pedido');
await tgMsg(111, '/xyz'); ok(ultimo().corpo.text.includes('Não conheço'), 'comando desconhecido');
ok((await fab('/fabrica/pedidos', {}, 'errada')).status === 401, 'fábrica com chave errada é recusada');
const f = new FormData(); f.append('id', 's01p2'); f.append('titulo', 'Série 1 parte 2'); f.append('legenda', 'Legenda teste'); f.append('video', new Blob([new Uint8Array(2048)], { type: 'video/mp4' }), 'p2.mp4');
let r = await fab('/fabrica/previa', { method: 'POST', body: f }); ok(r.status === 200 && ultimo().metodo === 'sendVideo' && ultimo().corpo.video.includes('2048'), 'prévia com vídeo vai por sendVideo com botões');
ok(JSON.parse(ultimo().corpo.reply_markup).inline_keyboard[0].length === 3, '3 botões na prévia');
await tgMsg(111, '/fila'); ok(ultimo().corpo.text.includes('parte 2'), '/fila mostra a prévia esperando');
await tgBot(999, 'a:s01p2'); ok(JSON.parse(kv.get('item:s01p2')).status === 'aguardando', 'botão apertado por estranho não muda nada');
await tgBot(111, 'j:s01p2'); ok(JSON.parse(kv.get('item:s01p2')).status === 'ajustar', 'botão Ajusta marca ajustar');
await tgMsg(111, 'troca a voz do golpista'); ok([...kv.values()].some((v) => v.includes('"ajuste"') && v.includes('s01p2')), 'mensagem seguinte vira ajuste ligado ao item');
await tgBot(111, 'a:s01p2'); ok(JSON.parse(kv.get('item:s01p2')).status === 'aprovado' && [...kv.values()].some((v) => v.includes('"publicar"')), 'Aprova marca aprovado e cria pedido de publicar');
await tgBot(111, 'a:naoexiste'); ok(ultimo().metodo === 'answerCallbackQuery', 'botão de item sumido responde sem quebrar');
r = await (await fab('/fabrica/pedidos')).json(); ok(r.pedidos.length === 4 && r.itens.length === 1, 'fábrica lê 4 pedidos e 1 item');
await fab('/fabrica/lido', { method: 'POST', body: JSON.stringify({ pedidos: r.pedidos.map((p) => p.chave), itens: ['s01p2'] }) });
r = await (await fab('/fabrica/pedidos')).json(); ok(r.pedidos.length === 0 && r.itens.length === 0, 'lido apaga o que foi processado');
await fab('/fabrica/estado', { method: 'POST', body: JSON.stringify({ temas: '1. Golpe do INSS', aviso: 'Temas prontos' }) });
ok(ultimo().corpo.text === 'Temas prontos', 'aviso chega ao dono');
await tgMsg(111, '/temas'); ok(ultimo().corpo.text.includes('INSS'), '/temas mostra o que a fábrica mandou');
ok((await worker.fetch(new Request(B + '/configurar?chave=errada'), env)).status === 401, 'configurar com chave errada é recusado');
r = await (await worker.fetch(new Request(B + '/configurar?chave=F'), env)).json(); ok(r.webhook === 'ok' && enviados.some((e) => e.metodo === 'setWebhook' && e.corpo.secret_token === 'W' && e.corpo.url === B + '/telegram'), 'configurar liga o webhook com o segredo');
// --- conversa com IA (vinculação AI simulada) ---
const chamadasIA = [];
env.AI = { run: async (modelo, op) => { chamadasIA.push(op); const u = op.messages.at(-1).content;
  if (u.includes('quebra')) throw new Error('fora do ar');
  if (u.includes('GTA')) return { response: 'Fechado, vou pedir uma série de GTA 6 para hoje à tarde — com história nossa.\nACAO: produzir :: série curta sobre GTA 6 para hoje' };
  if (u.includes('voz')) return { response: 'Entendi, a voz do narrador ficou robótica. Passo para a fábrica trocar.\nACAO: ajuste :: voz do narrador mais natural' };
  return { response: 'Tudo certo por aqui. A fábrica traz os números na próxima rodada.\nACAO: nenhuma' }; } };
kv.clear();
await tgMsg(111, 'quero uma série de GTA 6 hoje');
ok(ultimo().corpo.text.startsWith('Fechado') && !ultimo().corpo.text.includes('ACAO') && !ultimo().corpo.text.includes('—'), 'IA responde natural, sem a marcação e sem travessão');
ok([...kv.values()].some((v) => v.includes('"produzir"') && v.includes('GTA 6')), 'IA classifica como produzir e vira pedido');
await tgMsg(111, 'não gostei da voz');
ok([...kv.values()].some((v) => v.includes('"ajuste"') && v.includes('mensagem original')), 'IA classifica correção como ajuste com a mensagem original');
await tgMsg(111, 'como estamos?');
ok(chamadasIA.at(-1).messages.length >= 5, 'IA recebe o histórico da conversa');
ok(chamadasIA.at(-1).messages[0].content.includes('Contexto agora'), 'IA recebe o contexto da fila');
await tgMsg(111, 'isso quebra a IA');
ok(ultimo().corpo.text.includes('Anotado'), 'IA fora do ar: bot ainda responde e anota');
r = await (await fab('/fabrica/pedidos')).json(); ok(r.conversa.length >= 6 && r.pedidos.length === 4, 'fábrica lê a conversa e os 4 pedidos');
await tgMsg(999, 'oi'); ok(chamadasIA.length === 4, 'estranho não gasta IA');

// --- correções da leitura dos livros 18 e 19 ---
kv.clear();
await worker.fetch(new Request(B + '/telegram', { method: 'POST', headers: { 'X-Telegram-Bot-Api-Secret-Token': 'W' }, body: JSON.stringify({ message: { from: { id: 111 }, chat: { id: 111 }, caption: 'views de hoje', photo: [{ file_id: 'pequena' }, { file_id: 'GRANDE' }] } }) }), env);
ok([...kv.values()].some((v) => v.includes('"print"') && v.includes('GRANDE') && v.includes('views de hoje')), 'print vira pedido com o maior tamanho e a legenda');
ok(ultimo().corpo.text.includes('Print recebido'), 'bot confirma o print');
const semDono = { ...env, DONO_ID: undefined }; enviados.length = 0;
await worker.fetch(new Request(B + '/telegram', { method: 'POST', headers: { 'X-Telegram-Bot-Api-Secret-Token': 'W' }, body: JSON.stringify({ message: { chat: { id: 5 }, text: '/fila' } }) }), semDono);
ok(enviados.length === 0, 'sem DONO_ID configurado ninguém é atendido');
const quebrado = { ...env, FILA: { ...env.FILA, put: async () => { throw new Error('kv fora'); } } };
r = await worker.fetch(new Request(B + '/telegram', { method: 'POST', headers: { 'X-Telegram-Bot-Api-Secret-Token': 'W' }, body: JSON.stringify({ message: { from: { id: 111 }, chat: { id: 111 }, text: 'oi' } }) }), quebrado);
ok(r.status === 200, 'erro interno responde 200 ao Telegram (sem reenvio)');
const fetchAntes = globalThis.fetch;
globalThis.fetch = async (url, op) => url.includes('/getFile') ? new Response(JSON.stringify({ ok: true, result: { file_path: 'photos/a.jpg' } })) : url.includes('/file/botT/photos/a.jpg') ? new Response('IMG', { headers: { 'content-type': 'image/jpeg' } }) : fetchAntes(url, op);
r = await fab('/fabrica/arquivo/GRANDE'); ok(r.status === 200 && (await r.text()) === 'IMG', 'fábrica baixa o print pelo Worker');
globalThis.fetch = fetchAntes;
ok((await fab('/fabrica/arquivo/GRANDE', {}, 'errada')).status === 401, 'baixar print sem chave é recusado');

console.log(falhas ? `\n${falhas} falha(s)` : '\nTudo certo'); process.exit(falhas ? 1 : 0);
