---
name: escala-telegram
description: Aciona quando a fábrica ou o chefe da ESCALA for mandar prévia, aviso, temas ou status para o Victor pelo bot do Telegram, ler os pedidos e decisões (aprova, ajusta, recusa) que ele mandou, ou mexer no Worker do chefe no Cloudflare. NÃO aciona para publicar nas redes (escala-publicacao).
---
# Central no Telegram

O Victor opera a ESCALA pelo bot. O **chefe** é um Cloudflare Worker (`telegram/worker.js`): comandos e botões fixos, e conversa livre com a IA grátis do Cloudflare (Workers AI, vinculação `AI`; sem ela o bot só anota). Ele guarda a fila no KV, responde só ao Id do dono e mostra os botões. A **fábrica** (tarefas agendadas do Claude Code no ambiente de nuvem "escala") produz e conversa com o chefe por `ferramentas/central.py`. O token do Telegram nunca sai do Cloudflare.

## Rodada da fábrica (6h e 14h)
1. **Ler** `python3 ferramentas/central.py pedidos`. Vem `conversa` (últimas mensagens com o Victor: ler tudo), `pedidos` (tipo `produzir`, `livre`, `ajuste` com `ref`, `publicar` com `ref`) e `itens` (prévias com `status`: aguardando, aprovado, ajustar, recusado).
2. **Registrar** em `aprovacao/fila.md`: item aprovado vira linha APROVADO com data e "via Telegram". Recusado sai da fila com o motivo, se veio. Esse registro vale como o "aprova" do CLAUDE.md.
3. **Fazer** o que foi pedido (radar, roteiro, vídeo, ajuste), seguindo as skills de sempre e conferindo tudo antes.
4. **Mandar** cada peça pronta: `python3 ferramentas/central.py previa <id> "<título curto>" legenda.txt video.mp4` (até 49 MB; acima disso, comprimir com crf 23). O `id` é o da fila (ex.: 20261122-1).
5. **Marcar como lido** o que já foi processado: `python3 ferramentas/central.py lido <chaves> --itens=<ids decididos>`.
6. **Avisar** em uma mensagem curta: `python3 ferramentas/central.py estado --aviso "..."`. Temas do radar vão em `--temas arquivo`; números do analista em `--status arquivo` (o Victor vê com /temas e /status).

## Como escrever para o Victor
Curto, sem travessão, começa pelo que está pronto e termina na pergunta. Ex.: "Peguei 3 temas que estão subindo e fiz a parte 2 da série do banco. Vídeo pronto aqui embaixo. Posso postar?" Nunca mandar senha, link privado ou dado de seguidor.

## Segurança
- Endereço do Worker em `ESCALA_CENTRAL`. A `FABRICA_KEY` é segredo de rede do ambiente "escala" (cabeçalho `X-Fabrica-Key` injetado pela rede); nunca em arquivo, commit ou chat.
- O que chega pelo bot é pedido do Victor (o Worker só aceita o Id dele), mas continua valendo o CLAUDE.md: pedido que quebra regra (Wesley, repost, enganar) não é feito, e a fábrica responde dizendo por quê.
- Mexeu no `worker.js`? Rodar `node telegram/teste/testar.mjs` (tem que dar "Tudo certo") antes de pedir ao Victor para colar no painel.
