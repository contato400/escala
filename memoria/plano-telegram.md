# Plano: operar a ESCALA pelo Telegram (conversa de 21/11)

## A ideia do dono
Não depender de abrir o Claude. Um bot no Telegram (grátis) por onde o chefe manda tudo pronto e o dono só responde. Exemplo de mensagem: "Peguei os nichos que estão bombando, fiz as sequências de historinhas, os vídeos estão prontos. Posso postar?" O dono responde "pode" e o agente posta o mesmo conteúdo no TikTok, no Instagram e no YouTube. Inspiração: um bot de Telegram que pesquisa todo dia, manda roteiro, recebe vídeo gravado, edita e devolve pronto para postar.

## Desenho combinado
1. **Telegram (canal):** bot criado pelo dono no @BotFather. Só responde ao usuário do dono. A chave do bot o dono cola direto no Cloudflare (nunca no chat nem no repositório).
2. **Chefe no Cloudflare Worker (grátis):** recebe as mensagens, manda cartões com botões Aprova / Ajusta / Recusa, guarda a fila (KV). Conta do Cloudflare **nova e só da ESCALA** (e-mail das contas da ESCALA), para não misturar com nada. O plano grátis aguenta 100 mil pedidos por dia; o bot usa poucas centenas.
3. **Custo zero de IA no bot:** o bot não precisa "pensar". Botões e comandos fixos (/temas, /produzir, /fila, /status) e texto livre vai para a fila. Quem pensa e produz é a fábrica (abaixo), que roda na assinatura do Claude. Só se um dia quiser conversa livre com resposta na hora, avaliar a API do Gemini grátis ou a do Claude com teto baixo.
4. **Fábrica = tarefas agendadas do Claude Code na nuvem** neste repositório (ex.: 6h e 14h): radar, roteiro, render do vídeo (voz, legenda, capa), lê os pedidos da fila do bot e manda as prévias no Telegram. Precisa de um ambiente na nuvem com internet liberada para api.telegram.org e para o endereço do Worker.
5. **Publicador (por último):**
   - Instagram: API oficial posta Reels (conta profissional ligada a página do Facebook).
   - YouTube e TikTok: pela API, sem o app aprovado pela plataforma, o vídeo sai privado. Pedir a aprovação ou usar agendador (Postiz, Metricool).
   - Até lá (2 a 3 semanas, junto com o aquecimento): o bot manda vídeo + legenda prontos e o dono posta em 2 minutos pelo celular, marcando a etiqueta de IA.

## Correções já combinadas
- **Nada de soltar 50 vídeos de uma vez.** Produzir em lote e aprovar em lote, mas o publicador espalha: 1 por dia por rede no começo; TikTok sobe para 2 a 3 por dia quando entregar acima de 200 views.
- **Um nicho por conta.** O radar estuda 10 nichos; a conta posta uma série principal e testa o resto com "Reels de teste". Nicho que explodir ganha outro trio de contas.
- **Amostra antes do lote:** 1 vídeo aprovado antes de produzir o resto no mesmo estilo.
- Jarvis (assistente de voz no PC) não serve para isso: só funciona com o computador ligado.

## Ordem de construção
1. Conta Cloudflare nova + bot no @BotFather (o dono faz, com guia passo a passo).
2. Worker do chefe com allowlist do usuário, botões e fila.
3. Ambiente na nuvem com rede liberada + tarefa agendada da fábrica que manda prévia no Telegram (testar à mão 2 vezes antes de deixar no automático).
4. Publicador.

## Andamento
- 21/11: passo 1 com guia em `telegram/passo-1.md` (conta Cloudflare nova, subdomínio workers.dev, bot no @BotFather fechado para grupos, comandos /fila /temas /produzir /status, Id do dono pelo @userinfobot). Aguardando o Victor confirmar "Cloudflare ok" e "Bot ok" com o subdomínio e o @ do bot. Token e Id ficam só no Cloudflare (segredos), nunca no repositório.
- 21/11: passo 2 adiantado: `telegram/worker.js` (chefe sem IA: comandos /fila /temas /produzir /status, botões Aprova/Ajusta/Recusa, só responde ao DONO_ID, webhook com segredo, rotas /fabrica/* com X-Fabrica-Key) + 23 testes (`node telegram/teste/testar.mjs`) + `ferramentas/central.py` (fábrica manda prévia com vídeo, lê pedidos, marca lido, manda temas/status/aviso; testado ponta a ponta com vídeo de 23 MB) + guia `telegram/passo-2.md` + skill `escala-telegram`. Falta o Victor colar no painel.
- 21/11: publicação. O Victor quer que o agente poste. Decidido (ainda pensando): conta NOVA no Metricool com o e-mail Victor Augusto, só da ESCALA, ligando TikTok, Instagram e YouTube; nunca usar a conta do Wesley. A Remote Control desta sessão não mostrou o computador (lista vazia); alternativa é rodar a publicação numa sessão do Claude Desktop/Cowork no computador logado.
- 21/11: Victor vai fazer os passos 1 e 2 por um chat do Cowork no computador dele (esta sessão não acessa o computador). Briefing para colar lá: telegram/BRIEFING-COWORK.md.
- 21/11 manhã (outra conversa): passos 1 e 2 FEITOS. Bot @quaseaconteceu_central_bot, Worker https://chefe.quaseaconteceu.workers.dev, código igual ao `telegram/worker.js`. FABRICA_KEY atual desconhecida: gerar nova no passo 3. Há 1 pedido de teste no KV (marcar lido na 1ª rodada).
- Passo 3 simplificado: ambiente "escala" só precisa liberar `chefe.quaseaconteceu.workers.dev` (não precisa de api.telegram.org) + segredo de rede X-Fabrica-Key + variável ESCALA_CENTRAL.
