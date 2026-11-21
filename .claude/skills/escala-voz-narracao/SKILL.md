---
name: escala-voz-narracao
description: Aciona quando for gerar narração, voz de personagem, diálogo ou ajustar o texto para ser ouvido nos vídeos da ESCALA. NÃO aciona para escrever o roteiro inteiro (escala-roteiro-serie).
---
# Voz e narração

## Texto escrito para ouvir
- 140 a 160 palavras por minuto. Frase curta, uma ideia por frase, pausa antes da revelação.
- Ler em voz alta (ou ouvir a prévia) e cortar o que tropeça. Número por extenso quando ajuda ("três batidas").
- Segunda pessoa ("você abre a porta") prende mais em série de sobrevivência e mistério.

## Vozes (custo zero primeiro)
1. **Piper** (grátis, roda aqui): `pip install -q --break-system-packages piper-tts`; voz `pt_BR-faber-medium` (masculina). `--length-scale 0.95` deixa um pouco mais rápido. É a reserva sempre disponível.
2. **Gemini TTS** (aistudio.google.com, "Generate speech"), se o Victor tiver acesso numa conta separada da ESCALA: soa bem mais humano. Mandar **só o texto**, sem instrução de estilo (às vezes ele lê a instrução em voz alta). Cota grátis acaba depois de 10 a 15 falas no dia: gerar só o que vai usar e guardar.
3. ElevenLabs e voz clonada: só com lucro e OK do Victor. Nunca clonar voz de pessoa real nem a do Victor.
- **Voz fixa por personagem** e uma voz fixa de narrador por série (vira identidade).
- Personagem ao telefone: filtro de telefone (passa-faixa 300 a 3400 Hz). Do outro lado da porta: abafado (passa-baixa).

## Conferência
- Transcrever cada áudio com faster-whisper (modelo small, `language="pt"`) e comparar com o roteiro: frase a mais no começo, palavra trocada, nome errado.
- loudnorm na mixagem; voz sempre acima da trilha; pico perto de -1 dB.
- A duração da voz define a duração da cena (o motor recalcula).

## Pronúncia: `memoria/pronuncia.md`
Lista de palavras com a grafia que a voz pronuncia certo (ex.: chip, chipe; PlayStation, pleisteixon). **Antes de gerar a voz, consulte a lista e troque na fala; a legenda mantém a grafia normal.** Palavra nova que a transcrição mostrar errada entra na lista no mesmo dia, com o fonema conferido. O revisor (`escala-revisor`) usa a mesma lista ao ouvir o vídeo.

## Lições (21/11, parte 1 v2)
- Piper lê "chip" como "xip": escrever **"chipe"** na fala (a legenda continua "chip"). Antes de renderizar palavra estrangeira, conferir o fonema: `PiperVoice.load(...).phonemize("palavra")`.
- Cliques de digitação da bolha em cima da primeira fala comem a consoante do começo ("Corta" virou "Porta"). Na fala do gancho, usar `"sem_teclas": true` no trecho. (21/11: o motor agora começa os cliques 0,35 s depois da fala em toda bolha; a transcrição do GTA 6 mostrou o mesmo erro no anúncio: "GTA" virou "Tá".)
- Whisper aqui: `HF_HUB_DISABLE_XET=1` para baixar o modelo e decodificar o áudio com ffmpeg para um array (o `av` instalado não abre arquivo). Nome próprio (Neide) o Whisper erra mesmo com fonema certo: conferir o fonema antes de mexer.
