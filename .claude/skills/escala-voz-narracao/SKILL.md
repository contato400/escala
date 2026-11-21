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
