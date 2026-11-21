# Passo 2: ligar o chefe no Cloudflare

Precisa do passo 1 feito (conta Cloudflare + bot). Tempo: uns 15 minutos. Tudo pelo painel, sem instalar nada.
O código está pronto e testado em `telegram/worker.js` (23 testes em `telegram/teste/testar.mjs`).

## 1. Criar o armazenamento da fila (KV)
1. Painel do Cloudflare > **Armazenamento e bancos de dados** > **KV** (às vezes aparece como "Workers KV").
2. **Criar** > nome: `escala-fila` > Adicionar.

## 2. Criar o Worker
1. **Compute (Workers)** ou **Workers e Pages** > **Criar** > **Worker** > comece pelo modelo "Hello World".
2. Nome: `chefe` > **Implantar**.
3. Toque em **Editar código**, apague tudo e cole o conteúdo de `telegram/worker.js` (eu te mando o arquivo). **Implantar**.
4. Anote o endereço que aparece (ex.: `https://chefe.quaseaconteceu.workers.dev`). Ele não é segredo.

## 3. Ligar o KV ao Worker
Worker `chefe` > **Configurações** > **Vinculações (Bindings)** > **Adicionar** > **Namespace KV**:
- Nome da variável: `FILA` (exatamente assim, maiúsculo)
- Namespace: `escala-fila`

## 4. Os 4 segredos
Worker `chefe` > **Configurações** > **Variáveis e segredos** > **Adicionar**, sempre com tipo **Secret** (fica escondido, nem você vê de novo):

| Nome | Valor |
|---|---|
| `TELEGRAM_TOKEN` | o token do @BotFather (`/mybots` > seu bot > API Token) |
| `DONO_ID` | seu Id do @userinfobot (só números) |
| `WEBHOOK_SECRET` | uma senha aleatória (veja abaixo) |
| `FABRICA_KEY` | outra senha aleatória, diferente da de cima |

Como gerar senha aleatória: no gerenciador de senhas do celular, "gerar senha", 32 caracteres, **só letras e números** (sem símbolo). Guarde as duas lá.
Depois de salvar os 4, toque em **Implantar** de novo se o painel pedir.

## 5. Ligar o bot ao Worker (uma vez)
No navegador, abra:
```
https://SEU-ENDERECO.workers.dev/configurar?chave=SUA_FABRICA_KEY
```
(troque pelo seu endereço e pela FABRICA_KEY). Tem que aparecer `"webhook":"ok"` e o bot te manda "Central ligada" no Telegram.
Depois disso, apague esse endereço do histórico do navegador (ele tem a chave).

## 6. Testar
No Telegram, mande para o bot: `/ajuda`, `/fila` e `/produzir teste`. Ele tem que responder às três.
Peça para alguém de confiança mandar qualquer coisa para o bot: ele **não pode responder** nada.

## 7. Me mande
"Chefe ok" + o endereço do Worker. A FABRICA_KEY eu peço por um formulário seguro da nuvem (ela vai para a rede do ambiente "escala", nunca pelo chat). Aí começa o passo 3: a fábrica mandando prévia de verdade.
