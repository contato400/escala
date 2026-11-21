---
name: escala-producao-video
description: Aciona quando for transformar um roteiro da ESCALA em vídeo vertical pronto (MP4 9:16 com voz, legenda, trilha e capa), seja minissérie pelo motor, vídeo de tendência/notícia narrado ou corte editado. NÃO aciona para escolher tema (escala-radar-viral) nem escrever roteiro (escala-roteiro-serie).
---
# Produção de vídeo (custo zero primeiro)

Régua de qualidade, conferência, capa e estudo de referência: `escala-editor-video`. Animação com boneco: `escala-animacao-personagens`. Clipes gerados por IA: `escala-video-ia`. Voz: `escala-voz-narracao`.

## Ferramentas
- **Motor de minissérie** em `motor/` (`gerar_serie.py` + `serie.html`, exemplo em `motor/exemplo.json`): narra (piper-tts, grátis), sincroniza, mixa e renderiza 1080x1920. Antes: `pip install -q --break-system-packages piper-tts`. O rodapé do vídeo já mostra "QUASE ACONTECEU" (em `motor/serie.html`).
- Campos do JSON: `fala`, `legenda` (`*vermelho`, `^amarelo`, `+verde`), `voz` (narrador/tel/porta), `chamada`, `bolha`, `regra` (cartão "FICA A DICA"), `tensao`, `final` + `mostrar_chamada`, `capa`. Render leva mais de 2 min: rodar em segundo plano.
- Imagens/personagens: gerar com ferramenta de imagem e manter **ficha fixa de cada personagem** (rosto, roupa, ângulos) para consistência entre partes. Higgsfield só quando houver lucro.
- ffmpeg para cortes, legenda queimada, trilha e normalização de áudio.

## Padrão técnico
- 1080x1920, 30 fps, 60 a 90 s (série) ou 20 a 45 s (tendência rápida).
- Área segura: texto entre Y 285 e 1470 e X 110 a 945 (fora disso a interface das redes cobre).
- Primeiro quadro claro e chamativo; som desde o quadro 0; legenda grande e legível; sem tela preta no fim; sem logo no começo.
- Trilha e efeitos só de biblioteca livre (ou a biblioteca da própria rede na hora de postar).

## Formato tendência/notícia (ex.: GTA 6, lançamento, assunto do dia)
Vídeo NOSSO sobre o assunto: narração própria com informação conferida (data, fonte oficial), texto na tela, imagens geradas ou nossas, e no máximo trechos muito curtos de material oficial **com comentário por cima** (risco de reclamação de direito autoral: preferir não usar). Nunca recortar o vídeo de outro criador e repostar: dá derrubada e a rede não paga conteúdo reaproveitado.

## Conferência antes de ir para a fila
1. `python3 gerar_serie.py parte.json --quadros` e olhar a folha de quadros (legenda inteira, nada fora da área segura, português certo).
2. Assistir o MP4 inteiro uma vez: gancho em 2 s, sem silêncio, áudio limpo, duração certa.
3. Checklist da `escala-regras`.
4. Salvar em `conteudo/AAAA-MM-DD/` (MP4, capa, legenda, JSON) e lançar na fila de aprovação.

## Opções do motor (21/11)
`abertura: true` + `fim_abertura: true` no trecho onde acaba = primeiro quadro claro (amarelo da marca) com gancho já inteiro no quadro 0. `chamada.atendida: true` = ligação já em curso. `silencio: true` no trecho = trilha muda 0,8 s antes (revelação). `pulso: false` e `grave_pad: false` = grave só no impacto. `limpar_bolhas`, `sem_teclas`, voz `neto`, `inicio` (segundo da 1ª fala). Saída já sai com loudnorm (-14 LUFS alvo, pico -1 dB) e crf 20.
