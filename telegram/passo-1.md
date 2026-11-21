# Passo 1: conta nova do Cloudflare + bot no Telegram

Tempo: uns 15 minutos. Custo: zero. Tudo pelo celular ou computador.
Regra de ouro: **a chave do bot (o token) nunca vai para o chat, para o repositório nem para print.** Ela fica guardada no próprio @BotFather até o passo 2, quando você cola direto no Cloudflare.

---

## Parte A · Conta nova do Cloudflare (só da ESCALA)

1. Abra uma janela anônima no navegador (assim não entra logado em outra conta) e vá em **dash.cloudflare.com/sign-up**.
2. E-mail: o das contas da ESCALA (Victor Augusto). Senha: uma nova, forte, só para essa conta. Guarde no gerenciador de senhas do celular, não em arquivo.
3. Abra o e-mail de confirmação e clique no link.
4. Se ele perguntar o que você quer fazer ou pedir um site/domínio: **pule** ("Skip" ou "Explorar"). Não precisa de domínio e não precisa de cartão.
5. Ligue a verificação em duas etapas: foto do perfil (canto superior direito) > **Meu perfil** > **Autenticação** > **Autenticação de dois fatores** > use o app autenticador do celular. Guarde os códigos de recuperação no gerenciador de senhas.
6. No menu da esquerda, clique em **Compute (Workers)** ou **Workers e Pages** (o nome muda conforme a versão do painel).
7. Ele vai pedir para escolher um **subdomínio workers.dev**. Sugestão: `quaseaconteceu` (se estiver ocupado: `quase-aconteceu` ou `qa-escala`). O endereço do chefe vai ficar algo como `chefe.quaseaconteceu.workers.dev`.
8. Confira o plano: tem que estar **Gratuito (Free)**. Não assine nada.
9. Pare aí. Não precisa criar Worker ainda (é o passo 2).

**Me mande só:** "Cloudflare ok" e o subdomínio que ficou (ex.: quaseaconteceu.workers.dev). O subdomínio não é segredo.

---

## Parte B · Bot no @BotFather

Use o Telegram da conta que vai **mandar no bot** (a sua). Só ela vai poder falar com ele.

1. No Telegram, procure **@BotFather** (tem selo azul de verificado; cuidado com cópias) e toque em **Iniciar**.
2. Mande `/newbot`.
3. Nome (aparece no topo da conversa, pode mudar depois): `Central Quase Aconteceu`
4. Usuário (único, tem que terminar em `bot`): tente `quaseaconteceu_central_bot`. Se estiver ocupado: `quase_aconteceu_chefe_bot` ou `qa_escala_bot`.
5. O BotFather responde com uma mensagem que contém o **token** (uma sequência tipo `números:letras`).
   **Não copie, não print, não mande para ninguém.** Deixe lá. Quando precisar no passo 2, você pega de novo com `/mybots` > escolher o bot > **API Token**.
6. Ainda no BotFather, deixe o bot fechado:
   - Mande `/setjoingroups`, escolha o bot, toque em **Disable** (ninguém consegue colocar o bot em grupo).
7. Cadastre os comandos (para aparecerem no menu do bot). Mande `/setcommands`, escolha o bot e cole exatamente isto:
   ```
   fila - O que está esperando sua aprovação
   temas - Os temas do dia que o radar achou
   produzir - Pedir uma parte ou série nova
   status - Números das contas e o que está no ar
   ```
8. Opcional: `/setuserpic` e mande a foto `perfil-quase-aconteceu.png` (a mesma dos perfis). `/setdescription`: `Central da Quase Aconteceu. Só responde ao dono.`
9. Seu número de usuário do Telegram (o chefe vai usar para responder **só** a você): procure **@userinfobot**, toque em Iniciar e ele mostra seu **Id** (só números). Anote no gerenciador de senhas junto com a conta do Cloudflare. Você vai colar esse número no Cloudflare no passo 2. Não precisa mandar aqui.

**Me mande só:** "Bot ok" e o @ do bot (ex.: @quaseaconteceu_central_bot). O @ não é segredo.

---

## Se o token vazar (mandou no chat, printou, colou errado)
No @BotFather: `/mybots` > escolha o bot > **API Token** > **Revoke current token**. A chave antiga para de funcionar na hora e ele te dá uma nova.

## O que vem no passo 2 (para você já saber)
Eu escrevo o código do chefe (Worker) aqui no repositório. Você cria o Worker no painel, cola o código, e em **Configurações > Variáveis e segredos** cria três segredos do tipo **Secret**:
- `TELEGRAM_TOKEN`: o token do BotFather.
- `DONO_ID`: o seu Id do @userinfobot.
- `WEBHOOK_SECRET`: uma senha aleatória que o painel não mostra de novo (eu te digo como gerar).
Depois cria um armazenamento **KV** chamado `FILA` para guardar a fila de aprovação. Tudo dentro do plano grátis.
