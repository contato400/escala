# Passagem

## 21/11 madrugada · skills para o projeto
- Pedido: levar para cá todas as skills úteis (editor de vídeo, criação, pensar fora da caixa), usando os 20 livros da Mestres Play e pesquisa no YouTube.
- Feito: 8 skills novas da ESCALA (editor-video, ganchos-retencao, biblia-serie, animacao-personagens, video-ia, voz-narracao, ideias-fora-da-caixa, memoria) + escala-oferta; copiadas reels-para-carrossel, carrosseis-tweet-tedson, omegaprompt, ebook-profissional, ui-ux-pro-max; ferramenta `ferramentas/estudar_referencia.py` (testada). Índice no CLAUDE.md seção 6; fichas dos agentes apontam para as skills.
- Pesquisa YouTube (último mês): séries animadas em código com voto do público, bonecos 2D "e se...", novelinha com personagem consistente, edição pelo Claude Code com plano de edição e guia de estilo.
- Pendente: construir `animacao/boneco.html` (motor de animação) e testar 10 s.

## 21/11/2026 · dia 2 (aquecimento + série 1)
- **Pedido:** orientar o aquecimento das contas e montar a série 1 com 5 partes.
- **Feito:** guia `conteudo/aquecimento.md`; arco `conteudo/serie-01-a-ligacao/serie.md` (fatos com fonte); `montar.py` gera os 5 JSON; 5 MP4 renderizados (61,8 a 66,9 s) + capas + folhas de conferência; `legendas.md`; fila em `aprovacao/fila.md`. Motor corrigido (caminhos da máquina antiga, voz Gemini opcional, Chromium, `limpar_bolhas`, voz `neto`).
- **Pendente:** "aprova" do Victor para a série; prints do Creator Search Insights (prova do tema no TikTok); decisão de conta profissional no Instagram; publicar 23/11 e o analista medir 24 h e 72 h.
- **Verificado:** folhas de conferência das 5 partes olhadas (legenda inteira, área segura, português); MP4 1080x1920 30 fps, 61,8 a 67 s, som desde o quadro 0, volume médio -18 dB, comprimidos para ~25 MB (crf 22, agora padrão do motor). Não ouvi o áudio (sem fone aqui): o Victor deve assistir a parte 1 inteira antes de aprovar.
- **Atenção:** prova de viral do tema ainda fraca no YouTube (muitos vídeos do assunto no mês, mas poucas views, quase todos longos). Confirmar no TikTok.

## 21/11/2026 · Telegram passo 1
- **Pedido:** guiar a criação da conta nova do Cloudflare e do bot no @BotFather (plano em `memoria/plano-telegram.md`).
- **Feito:** guia `telegram/passo-1.md`; andamento anotado no plano.
- **Pendente:** Victor fazer as partes A e B e mandar subdomínio workers.dev + @ do bot; aí começa o passo 2 (código do Worker). Também pausado a pedido: recriar a parte 1 da série 1 com as skills novas (pedido interrompido, retomar quando o Victor quiser).
- **Verificado:** nada a testar ainda (depende de ação do Victor). Os nomes dos menus do Cloudflare podem variar com a versão do painel; o guia cita os dois nomes.

## 21/11/2026 · parte 1 v2 (skills novas)
- **Pedido:** refazer a parte 1 seguindo as skills novas, para comparar.
- **Feito:** bíblia `conteudo/series/a-ligacao/biblia.md`; v2 em `conteudo/2026-11-21/s01p1-v2/` (entregas: MP4 69 s + capa; projeto: JSON e folha; `comparacao.md`). Motor ganhou abertura clara, chamada atendida, silêncio antes de revelação, grave só no impacto, sem_teclas, loudnorm. Lições nas skills de voz e produção.
- **Decisões pendentes:** postar v1 ou v2 como parte 1; se v2, refazer as partes 2 a 5 no mesmo estilo e corrigir o furo da parte 4.
- **Verificado:** folha a cada 3 s olhada; transcrição do MP4 confere com o roteiro (Whisper ainda escreve "Nade" para Neide e "Cordo" no 1º segundo; fonema da voz está certo e o áudio cru transcreve "Corta"); -15,4 LUFS, pico -0,3 dB; 1080x1920 30 fps.

## 21/11/2026 · aprovação da v2 e pedido de zerar e postar
- **Pedido:** Victor aprovou a v2 da parte 1 e pediu para zerar as 3 contas (apagar ou arquivar tudo) e postar o vídeo nas 3, antes do bot.
- **Bloqueio:** esta sessão não tem acesso às contas. O Metricool só tem a marca do Wesley (proibido usar) e nenhum computador do Victor está conectado (a publicação é pelo navegador logado). Não foi apagado nem postado nada.
- **Feito:** passo a passo em `conteudo/2026-11-21/s01p1-v2/postar.md` (zerar escondendo: arquivar no Instagram, "Somente eu" no TikTok, "Privado" no YouTube; postar com legenda e etiqueta de IA). Fila atualizada: v2 APROVADO; partes 2 a 5 vão ser refeitas no estilo v2, uma por dia a partir de 22/11.
- **Pendente:** Victor zerar e postar e mandar os links; refazer as partes 2 a 5 (v2) e corrigir o furo da parte 4; Telegram passo 1.
- **Atenção:** postar hoje encurta o aquecimento (a skill de crescimento pede 2 a 3 dias consumindo o tema antes). Victor decidiu postar.

## 21/11/2026 · Telegram passo 2 adiantado
- **Pedido:** focar no bot (skills, agentes, bot) e deixar a publicação para depois; Victor disse ter ligado o Remote Control.
- **Feito:** Worker do chefe, testes, script da fábrica, guia do passo 2, skill `escala-telegram`, índice no CLAUDE.md, ficha do chefe, plano atualizado.
- **Verificado:** 23 testes do Worker passando; `central.py` testado contra o Worker local (prévia com vídeo de 23 MB, aviso, pedidos, chave errada recusada, lido). Não testado contra o Telegram de verdade (depende dos passos 1 e 2 do Victor).
- **Pendente:** Victor fazer passo 1 e 2 e mandar "Chefe ok" + endereço; aí pedir a FABRICA_KEY por formulário seguro (request_credential, host do Worker, cabeçalho X-Fabrica-Key) e liberar api do Worker no ambiente; passo 3 (tarefa agendada). Remote Control: lista de computadores desta sessão continua vazia. Conta nova no Metricool para a publicação (decisão do Victor, depois do bot). Parte 2 v2 para amanhã.

## 21/11/2026 · junção com a conversa da manhã (debrief)
- **Pedido:** puxar o main, ler `memoria/debrief-21-11-manha.md`, atualizar estado e passagem, juntar com o branch `claude/focused-feynman-emde7i` e listar os próximos passos.
- **Feito:** merge do main no branch (conflitos em `aprovacao/fila.md` e `memoria/estado.md` resolvidos juntando os dois lados com o estado real). Fila: parte 1 PUBLICADA 21/11 10h; partes 2 a 5 a refazer em v2, 1 por dia às 10h a partir de 22/11; conta profissional do Instagram FEITO. Estado: Telegram no ar, Facebook virou Quase Aconteceu, Metricool novo, primeiro post, Instagram/Facebook Plus a cancelar até ~20/12, pendência de deixar de seguir o Wesley no TikTok.
- **Correção no plano do passo 3:** a fábrica não precisa de api.telegram.org: ela só fala com o Worker (`ferramentas/central.py`); o token fica no Cloudflare. Basta liberar `chefe.quaseaconteceu.workers.dev` no ambiente "escala" e guardar a FABRICA_KEY nova como segredo de rede (cabeçalho X-Fabrica-Key).
- **Verificado:** Worker não responde daqui (rede do ambiente ainda não libera o host: esperado). Métricas da parte 1 não lidas: o conector Metricool desta sessão mostrou só a marca do Wesley; precisa religar o conector na conta nova ou o Victor mandar os números.
- **Pendente:** ver "Próximos passos" na resposta de 21/11 (ordem: medir parte 1, deixar de seguir Wesley, parte 2 v2, passo 3, partes 3 a 5, publicador pelo Metricool, cancelar Plus).

## 21/11/2026 · tarde: bot que conversa, sem nicho, passo 3, GTA 6
- **Pedido:** passo 3 (endereço do Worker + chave), métricas por print, PR, bot autônomo que conversa, social media que segue o que viraliza em cada rede sem nicho, 2 posts por dia (1 Metricool de manhã, 1 o Victor à tarde), vídeo de GTA 6 hoje, ler 20 e-books depois.
- **Feito:** host do Worker liberado + variável ESCALA_CENTRAL; chave pedida pelo formulário (está sendo recusada: valor não bate, guia clique por clique em `telegram/passo-3.md`); PR contato400/escala#1; Worker com conversa por Workers AI (31 testes); skill `escala-social-media` (cérebro, sem nicho, divisão de postagem, variar visual); trava de nicho e de "dica" tirada das skills de radar e roteiro, do KIT, do bot e do motor (etiqueta configurável); pesquisa de estratégia (YouTube, ferramentas, políticas, GTA 6) e radar do dia; série 2 GTA 6 parte 1 (golpe da chave) feita e recortada sem os cartões de dica; bíblia em `conteudo/series/gta6-chave/`.
- **Pendente:** Victor fazer o passo 3 (código novo, vinculação AI, trocar a chave) e dizer "chave trocada"; reabrir o formulário; 1ª rodada da fábrica à mão mandando prévia; tarefa agendada; vídeo de GTA 6 no que viraliza (notas/polêmica, finais, segredos) com visual novo; motor de cenas com imagem grátis (FLUX pelo Worker); ler os 20 e-books; links de desenho bíblico que o Victor viu.
- **Verificado:** 31 testes do Worker; Worker responde 200 daqui; chave 401 (valor diferente); radar com números do TranscriptAPI.

## 21/11/2026 · leitura dos 31 arquivos do Drive e skills novas
- **Pedido:** ler inteiros os 31 arquivos da pasta do Drive (20 e-books, 5 guias, guia 100 skills, 5 zips) e criar as skills que fazem sentido.
- **Feito:** download direto (hosts drive.google.com e drive.usercontent.google.com liberados no ambiente; pasta NÃO aberta para edição pública); 12 leitores leram tudo (1,2 mi palavras) e deixaram notas em `conteudo/estudos/livros/`; 5 redatores criaram 8 skills (rotinas-autonomas, seguranca, medicao-e-teste, revisor, direcao-cena, conformidade-plataformas, custos, pedir-a-ia) e ampliaram 14; `ferramentas/conferir_texto.py`; `memoria/pronuncia.md`, `versoes.md`, `acessos.md`, `reversao.md`, `testes-bot.md`, `registro-rodadas.csv`; índice do CLAUDE.md. Worker: Aprova duplicado, update repetido, duas chaves na troca, /pausa e /retomar, sinal de vida da rodada e alerta por Cron (44 testes).
- **Decisões do Victor pendentes:** ver resposta de 21/11 (porta-voz fictício, área segura, indicadores, gerador com referência para personagem, gasto pago, hooks de trava, separar radar, Cron, assinatura na Greenn).
- **Verificado:** 44 testes do Worker; conferir_texto sem travessão nas skills; notas conferidas até a última linha pelos leitores. Não verificado: hooks de trava em tarefa agendada na nuvem; termos de uso de Flow, FLUX, Piper, Veo, Nano Banana.

## 21/11/2026 · decisões do Victor (tarde)
- Passo 3: Victor vai fazer pelo chat do Cowork com `telegram/BRIEFING-PASSO-3-COWORK.md` + worker.js anexado; depois avisa "chave trocada" e aqui reabre o formulário da FABRICA_KEY.
- GTA 6 parte 1: RECUSADO ("não gostei"). Motivo não detalhado: perguntar o que não agradou antes do próximo de GTA.
- Porta-voz fictício (livro 13): LIBERADO no desenho do livro (informa e convida, nunca depoimento, tarja "Personagem criado com IA", conta separada).
- Área segura: Y 285 a 1248 (regra do livro 09), em editor, revisor, produção e CLAUDE.md.
- Geradores: Victor assina Gemini Pro (Nano Banana + Flow/Veo) e ChatGPT Plus; Nano Banana é o principal para âncora de personagem, Flow para clipe.
- 7 indicadores da escala-medicao-e-teste: aprovados.
- Travas técnicas: explicado; testar numa rodada antes de ligar (pendente).
- Link do PR dá 404 para o Victor: repositório privado; abrir logado no GitHub da conta dona de contato400/escala.

## 21/11/2026 · passo 3 concluído
- Chave trocada pelo Victor; formulário salvo; `central.py pedidos` respondeu (pedidos e conversa visíveis; IA do bot conversando).
- Rodada manual 1: aviso respondendo a pergunta de 13h11 (Insta/Facebook), prévia "TESTE" com vídeo e botões enviada (id teste-central), 4 pedidos de teste lidos, `--rodada` registrado, linha em `memoria/registro-rodadas.csv`.
- Pendente: Victor apertar um botão na prévia de teste; rodada manual 2 com vídeo real; criar a tarefa agendada.
