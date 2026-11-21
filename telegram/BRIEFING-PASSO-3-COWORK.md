# Para colar no chat do Cowork (passo 3 do bot da ESCALA)

Cole este texto inteiro no chat do Cowork e anexe junto o arquivo **worker.js** (o último que o Claude da ESCALA mandou; ele começa com "// Chefe da ESCALA no Cloudflare Worker").

---

Você vai me ajudar a atualizar o bot do Telegram da ESCALA no Cloudflare, pelo navegador deste computador. É um projeto separado do WG / Krav Magá Caveira: não misture nada.

## Regras
- Use o navegador logado na conta do Cloudflare da ESCALA (e-mail Victor Augusto). Se aparecer outra conta, pare e me avise.
- **Nunca** leia em voz alta, copie para o chat, salve em arquivo ou mostre em print qualquer token, senha ou chave. Quando um campo de segredo precisar de valor, **pare e me peça para colar**. Eu colo, você continua.
- Antes de cada **Implantar/Deploy**, me diga em 1 linha o que vai implantar e espere meu "ok".
- Se um menu estiver diferente do que está aqui, descreva o que aparece e pergunte. Não invente.

## O que fazer, em ordem

### 1. Abrir o Worker
dash.cloudflare.com > menu da esquerda **Compute (Workers)** (ou **Workers e Pages**) > clicar em **chefe**.

### 2. Colar o código novo
1. Botão **Editar código** (ícone `</>`, em cima à direita).
2. No editor: selecionar tudo (Ctrl+A), apagar, colar o conteúdo inteiro do **worker.js** anexado.
3. Conferir que a primeira linha é `// Chefe da ESCALA no Cloudflare Worker (plano grátis).` e que a última parte tem `export default {`.
4. Me avisar e, com meu ok, clicar em **Implantar**. Voltar para a página do Worker.

### 3. Ligar a IA grátis
Aba **Configurações** > seção **Vinculações** (Bindings) > **Adicionar** > **Workers AI** > nome da variável: `AI` (maiúsculo) > salvar/implantar.
Conferir: na lista de vinculações devem aparecer `FILA` (KV namespace) e `AI` (Workers AI).

### 4. Ligar o alerta automático
Aba **Configurações** > **Gatilhos** (Triggers) > **Gatilhos Cron** (Cron Triggers) > **Adicionar** > expressão `0 */3 * * *` > salvar.

### 5. Trocar a chave da fábrica (aqui EU colo, você só navega)
1. Aba **Configurações** > **Variáveis e segredos** > linha **FABRICA_KEY** > editar (lápis ou 3 pontinhos).
2. **Pare e me diga: "pode colar a chave nova no campo".** Eu gero a senha no meu gerenciador de senhas (32 letras e números, sem símbolo) e colo. Não olhe nem repita o valor.
3. Conferir que o tipo continua **Secret**. Com meu ok, salvar e implantar.

### 6. Testar
Abrir o Telegram Web (web.telegram.org) na conversa com **@quaseaconteceu_central_bot** e mandar, uma de cada vez:
- `/ajuda` (tem que listar comandos, incluindo /pausa)
- `oi, o que você faz?` (tem que responder com frase própria, não só "Anotado")
- `/pausa` e depois `/retomar` (tem que confirmar os dois)
Se a resposta de "oi" for só "Anotado na fila da fábrica", a vinculação `AI` não pegou: volte ao item 3.

## O que me devolver (sem nenhuma chave)
- Item por item: feito / deu diferente (o quê).
- As respostas que o bot deu nos testes.
- Lembrete final para mim: "agora avise o Claude da ESCALA: chave trocada".
