# Passo 4: trocar a IA do bot pelo Gemini (uns 5 minutos)

O código novo do bot (worker.js) já sabe usar o Gemini. Se o Gemini falhar ou passar do limite do dia, ele volta sozinho para a IA grátis do Cloudflare.
Pode fazer sozinho ou colar este texto no chat do Cowork (ele navega, você cola a chave quando ele pedir).

## A. Pegar a chave no Google AI Studio
1. Abra **aistudio.google.com** logado na conta Google que você quer usar (pode ser a mesma do Gemini Pro).
2. No menu da esquerda, clique em **Get API key** (ou "Obter chave de API").
3. **Create API key** > se pedir projeto, escolha "Create API key in new project".
4. Aparece a chave (começa com "AIza..."). Clique para copiar. **Não mande no chat, não tire print.**
5. Não precisa ativar faturamento: o plano grátis basta para o bot.

## B. Colar no Cloudflare
1. dash.cloudflare.com > Compute (Workers) > **chefe** > aba **Configurações** > **Variáveis e segredos** > **Adicionar**.
2. Tipo: **Secret**. Nome: `GEMINI_KEY` (exatamente assim). Valor: cole a chave. Salvar/Implantar.

## C. Colar o código novo
Worker `chefe` > **Editar código** > apagar tudo > colar o `worker.js` novo (o que mandei agora) > **Implantar**.

## D. Testar
No Telegram, mande para o bot: "me explica em 2 frases o que você faz". A resposta deve vir mais natural que antes. Se vier só "Anotado", confira o nome `GEMINI_KEY`.

## Depois (vozes do Gemini nos vídeos)
A mesma chave pode dar as vozes do Gemini (bem mais naturais que a voz atual) para a fábrica. Para isso eu abro um formulário seguro aqui e você cola a mesma chave; ela fica na rede da nuvem e eu nunca vejo. Me avise quando quiser.
