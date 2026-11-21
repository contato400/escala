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
