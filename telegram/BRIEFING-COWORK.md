# Briefing para o chat do Cowork (colar inteiro no outro chat)

Você vai me ajudar num projeto SEPARADO do WG / Krav Magá Caveira. Não misture nada: nenhum arquivo, conta, nome, marca, link ou dado da Caveira ou do Wesley entra aqui, e nada daqui vai para lá.

## O projeto
ESCALA: contas próprias "Quase Aconteceu" (TikTok @quaseaconteceu.br, Instagram @quase.aconteceu, YouTube @quase.aconteceu), logadas no e-mail Victor Augusto. Repositório: github.com/contato400/escala, branch `claude/focused-feynman-emde7i` (se precisar ler, clone ou abra no GitHub). Leia antes: `CLAUDE.md`, `memoria/plano-telegram.md`, `telegram/passo-1.md`, `telegram/passo-2.md`, `.claude/skills/escala-telegram/SKILL.md`.

## O que fazer agora, pelo navegador deste computador, sempre logado no e-mail Victor Augusto
1. **Passo 1** (`telegram/passo-1.md`): conta NOVA no Cloudflare só da ESCALA, com o e-mail Victor Augusto, plano grátis e subdomínio workers.dev (sugestão `quaseaconteceu`). Bot no @BotFather (Telegram Web): nome `Central Quase Aconteceu`, usuário `quaseaconteceu_central_bot` ou parecido, grupos desligados (/setjoingroups Disable), comandos do guia. Id do dono pelo @userinfobot.
2. **Passo 2** (`telegram/passo-2.md`): KV `escala-fila`, Worker `chefe` com o código de `telegram/worker.js` (copiar do repositório SEM mudar nada), vínculo KV com o nome `FILA`, os 4 segredos (tipo Secret), abrir `/configurar?chave=...` uma vez e testar /ajuda, /fila e /produzir teste no bot.

## Regras que não se negociam
- **Token do bot, senha, FABRICA_KEY, WEBHOOK_SECRET e código de verificação NUNCA aparecem no chat, em arquivo, em print ou em commit.** Copie do BotFather ou do gerenciador de senhas direto para o campo do Cloudflare. Se o Victor precisar digitar senha ou código de duas etapas, peça para ele digitar e espere.
- Criar conta, mudar configuração, ligar webhook: avise o Victor do que vai fazer e só siga com o "ok" dele.
- Se algum menu do Cloudflare estiver diferente do guia, descreva o que está vendo e pergunte; não invente.
- Não publique nada nas redes nesta etapa.

## Quando terminar, me devolva (para eu colar no chat da ESCALA)
- Subdomínio workers.dev e endereço do Worker (não são segredo).
- @ do bot (não é segredo).
- Resultado do `/configurar` (`webhook: ok`?) e se o bot respondeu às 3 mensagens de teste.
- O que deu diferente do guia, se algo deu.
Nada de token, chave ou senha nessa resposta.
