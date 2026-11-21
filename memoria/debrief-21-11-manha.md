# Debriefing ESCALA · 21/11 de madrugada até 09h55 (feito em outra conversa)

## 1. Central no Telegram (passos 1 e 2 do plano-telegram) · PRONTO
- Conta Cloudflare NOVA só da ESCALA (e-mail Victor Augusto), plano grátis. Subdomínio: quaseaconteceu.workers.dev.
- KV `escala-fila` criado. Worker `chefe` no ar em https://chefe.quaseaconteceu.workers.dev com o código de `telegram/worker.js` sem mudança (conferido por hash), KV ligado como `FILA`.
- Bot: @quaseaconteceu_central_bot ("Central Quase Aconteceu"), grupos desligados, descrição "Só responde ao dono". Número do bot: 9100151795.
- Segredos (tipo Secret): TELEGRAM_TOKEN e DONO_ID colados pelo Victor; WEBHOOK_SECRET e FABRICA_KEY gerados aleatórios direto no Cloudflare (ninguém viu).
- Problema resolvido: o token entrou errado duas vezes (com pedaço a mais; depois só a parte depois dos ":"). Diagnóstico por rota temporária que só mostrava o formato, nunca o valor; código restaurado igual ao original.
- /configurar rodou: webhook ok, comandos ok. "Central ligada" chegou. Testados /ajuda, /fila ("Fila vazia") e /produzir teste ("Anotado. A fábrica pega na próxima rodada.") → existe 1 pedido de teste na fila do KV (pode marcar como lido).
- A FABRICA_KEY foi trocada de novo depois dos testes: NINGUÉM sabe o valor atual. No passo 3, gerar uma nova direto no Cloudflare e guardar como segredo de rede do ambiente "escala" (nunca em chat, arquivo ou commit).

## 2. Contas e perfis
- **Facebook**: a página antiga "Método Giro Local" virou **Quase Aconteceu** (facebook.com/quase.aconteceu): nome, @, bio igual à do Instagram, categoria "Criador de conteúdo digital", foto do personagem, capa amarela nova. Removido o link antigo (tinha "luiscorinthianoporto" no endereço). Sem posts antigos. Página ligada ao Instagram @quase.aconteceu.
- **Instagram @quase.aconteceu**: categoria mudada de Educação para Criador de conteúdo digital; removido o telefone público (era o número profissional do Victor) e desligado "exibir informações de contato"; Victor tirou o link antigo da bio no app. Na Central de Contas o Instagram está junto do Facebook pessoal do Victor (ele aceitou); banner de link entre perfis está DESLIGADO (ninguém vê o Facebook dele). NÃO usar "Compartilhar entre perfis" da Central (iria para o perfil pessoal). Compartilhamento automático de Reels para a PÁGINA ligado pelo app ("Compartilhar no Facebook" > página > Sempre compartilhar).
- **YouTube**: todos os vídeos antigos do canal (Coin Master etc.) postos como **privados** em massa (nada apagado). Conferir a aba Shorts se tiver algum.
- **TikTok**: já estava sem vídeos.
- **Metricool** (conta nova da ESCALA, marca com foto do personagem): ligados Instagram (profissional), TikTok (conta pessoal), YouTube e a página do Facebook. Plano grátis: 20 publicações por mês.

## 3. Primeiro post · AGENDADO
- Série 1 parte 1 v2 (aprovada) agendada no Metricool para **21/11 às 10h00**: Instagram como **Reel de teste** (com "partilhar automaticamente com todos"), TikTok público, YouTube Short (título "Ele pediu o cartão dela, e ela já estava com a tesoura | Parte 1 #golpe #shorts", não é para crianças). Rótulo de IA ligado nas 3. Legenda do `postar.md`. Vídeo comprimido para 9,5 MB para subir pelo navegador.
- Risco: abaixo de 1.000 seguidores a Meta pode recusar Reel de teste pela API. Se falhar, postar o Reel de teste pelo app.
- O Facebook ficou fora do Metricool de propósito (Victor quer o compartilhamento automático do Instagram). Conferir se aparece na página; se não, ligar o Facebook no Metricool nos próximos.

## 4. Regras novas decididas hoje
- Instagram: só **Reels de teste** enquanto a conta for pequena; nunca postar o mesmo vídeo também como Reel normal (registrado na `escala-publicacao`).
- Nada ligado ao Victor em nenhum perfil: nome, telefone, link, e-mail.
- Atomicat/domínio próprio só na fase 2 (quando tiver produto); a Atomicat conectada é do Wesley, não usar.
- Estudo do Marcos Maia salvo em `conteudo/estudos/marcos-maia-21-11.md` + skill `escala-hype-e-afiliado` (GTA 6 com conteúdo nosso e afiliado de acessório aprovados para depois; afiliado com modelo de IA depende de decisão do Victor). Itens no `memoria/backlog.md`.

## 5. Próximos passos
1. Medir a parte 1 em 3 h, 24 h e 72 h (views, % que passou dos 2 s, % até o fim, seguidores) e mandar ao Victor.
2. Refazer as partes 2 a 5 no estilo v2 (parte 4 com o furo do limite noturno corrigido) e agendar 1 por dia (fila 20261122-1 a 20261125-1, aguardando Victor).
3. Passo 3 do Telegram: ambiente na nuvem com rede liberada para api.telegram.org e chefe.quaseaconteceu.workers.dev, FABRICA_KEY nova como segredo de rede, tarefa agendada da fábrica (rodar à mão 2 vezes antes) mandando prévia com botões.
4. Passo 4: publicador (Metricool já ligado; avaliar agendar pelo Metricool depois do "Aprova" no Telegram, lembrando o limite de 20 por mês).
5. Motor de animação com boneco (teste de 10 s) e conteúdo de GTA 6.

## 6. Atualização 10h30 (resultado do primeiro post e Instagram)
- **YouTube**: Short publicado às 10h pelo Metricool, público. ✅
- **TikTok**: publicado às 10h pelo Metricool (2 views na primeira conferência). ✅
- **Instagram**: o Reel de teste pelo Metricool FALHOU ("Trial Reel Not Enough Followers"). Pelo app também não deixou: a Meta ainda não liberou Reel de teste para esta conta. O Victor postou a parte 1 como **Reels normal pelo app**. Regra até liberar: Instagram vai em **Reels normal, postado pelo app** (o Metricool só para TikTok e YouTube). Quando a opção de Reel de teste aparecer, voltar à regra de só Reel de teste.
- **Facebook**: só recebe o Reels se o compartilhamento automático do app estiver ligado no post (pelo Metricool não vai). Conferir se a parte 1 apareceu na página.
- **Instagram Plus e Facebook Plus**: o Victor ativou o mês grátis. Não dão selo, nem alcance, nem Reel de teste. Útil: fixar até 6 posts no Instagram (fixar a série em ordem) e mais estatística de Reels no Facebook. CANCELAR antes do fim do mês grátis (~20/12) para não cobrar. Selo verificado só no plano Meta One Essential (US$ 14,99/mês) com documento do dono: não fazer (ligaria a conta ao Victor).
- **Pendente do Victor**: deixar de seguir o perfil do Wesley (kravmagacaveira) na conta do TikTok @quaseaconteceu.br.
- **Metricool**: 20 publicações grátis por mês; a parte 1 usou TikTok e YouTube. Com Instagram pelo app, sobra mais cota.
