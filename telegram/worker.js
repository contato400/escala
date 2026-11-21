// Chefe da ESCALA no Cloudflare Worker (plano grátis).
// Recebe as mensagens do Telegram, responde SÓ ao dono, guarda a fila no KV e
// manda as prévias da fábrica com botões Aprova / Ajusta / Recusa.
// Não usa IA: comandos e botões fixos. Quem pensa e produz é a fábrica (tarefas agendadas do Claude Code).
//
// Segredos (Cloudflare > Worker > Configurações > Variáveis e segredos, tipo Secret):
//   TELEGRAM_TOKEN  token do @BotFather
//   DONO_ID         Id numérico do Telegram do dono (@userinfobot)
//   WEBHOOK_SECRET  senha aleatória que o Telegram manda em cada aviso
//   FABRICA_KEY     senha aleatória que a fábrica usa para falar com o chefe
// Armazenamento KV ligado com o nome FILA.

const JSON_H = { 'content-type': 'application/json; charset=utf-8' };
const json = (o, status = 200) => new Response(JSON.stringify(o), { status, headers: JSON_H });
const agora = () => new Date().toISOString();

async function tg(env, metodo, corpo) {
  const base = env.TG_API || 'https://api.telegram.org';
  const form = corpo instanceof FormData;
  const r = await fetch(`${base}/bot${env.TELEGRAM_TOKEN}/${metodo}`, {
    method: 'POST',
    headers: form ? undefined : JSON_H,
    body: form ? corpo : JSON.stringify(corpo),
  });
  return r.json().catch(() => ({ ok: false }));
}
const dizer = (env, texto, extra = {}) => tg(env, 'sendMessage', { chat_id: env.DONO_ID, text: texto, ...extra });

const botoes = (id) => ({
  inline_keyboard: [[
    { text: '✅ Aprova', callback_data: `a:${id}` },
    { text: '✏️ Ajusta', callback_data: `j:${id}` },
    { text: '❌ Recusa', callback_data: `r:${id}` },
  ]],
});

async function listar(env, prefixo) {
  const { keys } = await env.FILA.list({ prefix: prefixo });
  const itens = await Promise.all(keys.map(async (k) => ({ chave: k.name, ...(await env.FILA.get(k.name, 'json')) })));
  return itens.sort((a, b) => String(a.criado).localeCompare(String(b.criado)));
}
async function novoPedido(env, tipo, texto, ref) {
  const chave = `pedido:${Date.now()}:${Math.random().toString(36).slice(2, 6)}`;
  await env.FILA.put(chave, JSON.stringify({ tipo, texto, ref: ref || null, criado: agora() }));
  return chave;
}

const AJUDA = [
  'Central Quase Aconteceu. Comandos:',
  '/fila  o que está esperando sua aprovação',
  '/temas  os temas do dia que o radar achou',
  '/produzir <o que quer>  pedir parte ou série nova',
  '/status  números das contas e o que está no ar',
  'Qualquer outra mensagem vai para a fila de pedidos da fábrica.',
].join('\n');

// ---------- Telegram ----------
async function telegram(req, env) {
  if (req.headers.get('X-Telegram-Bot-Api-Secret-Token') !== env.WEBHOOK_SECRET) return new Response('nao', { status: 401 });
  const u = await req.json();
  const de = u.message?.from?.id ?? u.callback_query?.from?.id;
  if (String(de) !== String(env.DONO_ID)) return new Response('ok'); // estranho: ignora em silêncio

  if (u.callback_query) {
    const q = u.callback_query;
    const [acao, id] = String(q.data || '').split(':');
    const chave = `item:${id}`;
    const item = await env.FILA.get(chave, 'json');
    if (!item) {
      await tg(env, 'answerCallbackQuery', { callback_query_id: q.id, text: 'Esse item não está mais na fila.' });
      return new Response('ok');
    }
    const status = { a: 'aprovado', j: 'ajustar', r: 'recusado' }[acao];
    if (!status) return new Response('ok');
    item.status = status; item.decidido = agora();
    await env.FILA.put(chave, JSON.stringify(item));
    await tg(env, 'answerCallbackQuery', { callback_query_id: q.id, text: `Marcado: ${status}` });
    if (q.message) await tg(env, 'editMessageReplyMarkup', { chat_id: q.message.chat.id, message_id: q.message.message_id, reply_markup: { inline_keyboard: [] } });
    if (status === 'aprovado') {
      await novoPedido(env, 'publicar', item.titulo, id);
      await dizer(env, `✅ Aprovado: ${item.titulo}\nVai para a publicação.`);
    } else if (status === 'ajustar') {
      await env.FILA.put('estado:ajuste_de', id);
      await dizer(env, `✏️ O que muda em "${item.titulo}"? Manda numa mensagem só.`);
    } else {
      await dizer(env, `❌ Recusado: ${item.titulo}`);
    }
    return new Response('ok');
  }

  const texto = (u.message?.text || '').trim();
  if (!texto) { await dizer(env, 'Por enquanto só leio texto.'); return new Response('ok'); }
  const [cmd, ...resto] = texto.split(/\s+/);
  const arg = resto.join(' ');
  switch (cmd.split('@')[0].toLowerCase()) {
    case '/start':
    case '/ajuda':
      await dizer(env, AJUDA); break;
    case '/fila': {
      const itens = (await listar(env, 'item:')).filter((i) => i.status === 'aguardando');
      await dizer(env, itens.length ? 'Esperando você:\n' + itens.map((i) => `• ${i.titulo}`).join('\n') : 'Fila vazia. Nada esperando aprovação.');
      break;
    }
    case '/temas':
      await dizer(env, (await env.FILA.get('estado:temas')) || 'O radar ainda não mandou os temas de hoje.'); break;
    case '/status':
      await dizer(env, (await env.FILA.get('estado:status')) || 'Ainda sem números. A fábrica atualiza depois de cada medição.'); break;
    case '/produzir':
      if (!arg) { await dizer(env, 'Manda junto o que quer. Ex.: /produzir parte 2 da série do banco'); break; }
      await novoPedido(env, 'produzir', arg);
      await dizer(env, '📝 Anotado. A fábrica pega na próxima rodada.'); break;
    default: {
      const ajusteDe = await env.FILA.get('estado:ajuste_de');
      if (ajusteDe && !texto.startsWith('/')) {
        await novoPedido(env, 'ajuste', texto, ajusteDe);
        await env.FILA.delete('estado:ajuste_de');
        await dizer(env, '✏️ Ajuste anotado. Volto com a versão nova.');
      } else if (texto.startsWith('/')) {
        await dizer(env, 'Não conheço esse comando.\n\n' + AJUDA);
      } else {
        await novoPedido(env, 'livre', texto);
        await dizer(env, '📝 Anotado na fila da fábrica.');
      }
    }
  }
  return new Response('ok');
}

// ---------- Fábrica (tarefas agendadas do Claude Code) ----------
async function fabrica(req, env, caminho) {
  if (!env.FABRICA_KEY || req.headers.get('X-Fabrica-Key') !== env.FABRICA_KEY) return json({ erro: 'chave' }, 401);

  if (caminho === '/fabrica/previa' && req.method === 'POST') {
    // multipart: id, titulo, legenda, video (arquivo, até 50 MB) | ou JSON {id, titulo, legenda}
    let id, titulo, legenda, video;
    if ((req.headers.get('content-type') || '').includes('multipart/form-data')) {
      const f = await req.formData();
      id = f.get('id'); titulo = f.get('titulo'); legenda = f.get('legenda') || ''; video = f.get('video');
    } else {
      ({ id, titulo, legenda = '' } = await req.json());
    }
    if (!id || !titulo) return json({ erro: 'faltou id ou titulo' }, 400);
    id = String(id).replace(/[^\w.-]/g, '').slice(0, 40);
    await env.FILA.put(`item:${id}`, JSON.stringify({ id, titulo, legenda, status: 'aguardando', criado: agora() }));
    const legendaTg = `🎬 ${titulo}\n\n${legenda}`.slice(0, 1000);
    let r;
    if (video && typeof video !== 'string') {
      const f = new FormData();
      f.append('chat_id', String(env.DONO_ID));
      f.append('video', video, video.name || `${id}.mp4`);
      f.append('caption', legendaTg);
      f.append('supports_streaming', 'true');
      f.append('reply_markup', JSON.stringify(botoes(id)));
      r = await tg(env, 'sendVideo', f);
    } else {
      r = await dizer(env, legendaTg, { reply_markup: botoes(id) });
    }
    return json({ ok: !!r.ok, id, telegram: r.ok ? 'enviado' : r.description || 'falhou' }, r.ok ? 200 : 502);
  }

  if (caminho === '/fabrica/pedidos' && req.method === 'GET') {
    return json({ pedidos: await listar(env, 'pedido:'), itens: await listar(env, 'item:') });
  }

  if (caminho === '/fabrica/lido' && req.method === 'POST') {
    // {pedidos: [chaves], itens: [ids]} -> apaga do KV o que a fábrica já processou
    const { pedidos = [], itens = [] } = await req.json();
    await Promise.all([
      ...pedidos.filter((k) => String(k).startsWith('pedido:')).map((k) => env.FILA.delete(k)),
      ...itens.map((i) => env.FILA.delete(`item:${i}`)),
    ]);
    return json({ ok: true });
  }

  if (caminho === '/fabrica/estado' && req.method === 'POST') {
    // {temas?, status?, aviso?}
    const { temas, status, aviso } = await req.json();
    if (temas) await env.FILA.put('estado:temas', String(temas).slice(0, 4000));
    if (status) await env.FILA.put('estado:status', String(status).slice(0, 4000));
    if (aviso) await dizer(env, String(aviso).slice(0, 4000));
    return json({ ok: true });
  }
  return json({ erro: 'rota' }, 404);
}

// ---------- Configurar o webhook (abrir uma vez no navegador) ----------
async function configurar(req, env) {
  const url = new URL(req.url);
  if (!env.FABRICA_KEY || url.searchParams.get('chave') !== env.FABRICA_KEY) return json({ erro: 'chave' }, 401);
  const webhook = await tg(env, 'setWebhook', {
    url: `${url.origin}/telegram`, secret_token: env.WEBHOOK_SECRET,
    allowed_updates: ['message', 'callback_query'], drop_pending_updates: true,
  });
  const comandos = await tg(env, 'setMyCommands', { commands: [
    { command: 'fila', description: 'O que está esperando sua aprovação' },
    { command: 'temas', description: 'Os temas do dia que o radar achou' },
    { command: 'produzir', description: 'Pedir uma parte ou série nova' },
    { command: 'status', description: 'Números das contas e o que está no ar' },
  ] });
  if (webhook.ok) await dizer(env, 'Central ligada. Manda /ajuda para ver os comandos.');
  return json({ webhook: webhook.ok ? 'ok' : webhook.description, comandos: comandos.ok ? 'ok' : comandos.description });
}

export default {
  async fetch(req, env) {
    const caminho = new URL(req.url).pathname;
    try {
      if (caminho === '/telegram' && req.method === 'POST') return await telegram(req, env);
      if (caminho.startsWith('/fabrica/')) return await fabrica(req, env, caminho);
      if (caminho === '/configurar') return await configurar(req, env);
      return new Response('Central Quase Aconteceu: ok');
    } catch (e) {
      return json({ erro: 'interno' }, 500); // sem detalhe para fora
    }
  },
};
