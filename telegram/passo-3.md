# Passo 3: bot que conversa + fábrica ligada

Tempo: uns 10 minutos no painel do Cloudflare (Worker `chefe`). Pode pedir para o chat do Cowork fazer com você.

## 1. Código novo (o bot passa a conversar)
Worker `chefe` > **Editar código** > apague tudo > cole o `telegram/worker.js` novo (mando o arquivo) > **Implantar**.
O que muda: você escreve normal ("não gostei da voz", "faz uma série de GTA 6 pra hoje", "como estamos?") e ele responde como um colega, entende se é correção, pedido ou pergunta e passa para a fábrica. Comandos e botões continuam iguais. Testado: 31 testes, 8 deles da conversa.

## 2. Ligar a IA grátis do Cloudflare
Worker `chefe` > **Configurações** > **Vinculações (Bindings)** > **Adicionar** > **Workers AI** > nome da variável: `AI` (maiúsculo) > Salvar > Implantar se pedir.
Custo: zero dentro da cota grátis diária do Cloudflare (sobra para centenas de mensagens por dia). Se a cota acabar num dia, o bot não para: só volta a responder "Anotado" até o dia seguinte.

## 3. Acertar a chave da fábrica (está sendo recusada)
A chave que você colou no formulário da nuvem não está batendo com a do Cloudflare. Para acertar sem erro:
1. Gere uma senha nova no gerenciador (32 caracteres, só letras e números) e guarde lá.
2. Cloudflare: Worker `chefe` > Configurações > Variáveis e segredos > `FABRICA_KEY` > **editar** > cole > salvar > **Implantar**.
3. Me avise "chave trocada": eu abro o formulário de novo e você cola **a mesma** senha.

## 4. Testar
No Telegram, mande para o bot: "oi, o que você faz?" e "quero uma série de GTA 6 pra hoje". Ele tem que responder com frase própria (não só "Anotado").
