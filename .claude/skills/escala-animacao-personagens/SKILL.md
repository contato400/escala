---
name: escala-animacao-personagens
description: Aciona quando for fazer vídeo animado com personagem desenhado (boneco 2D, palito, cartum, série animada narrada, "e se...") feito em código pelo agente, sem gerador de vídeo, na ESCALA. NÃO aciona para vídeo gerado em Flow, Veo ou Kling (escala-video-ia) nem para o motor de celular e golpe (escala-producao-video).
---
# Animação de personagens em código (custo zero de geração)

Formato que mais cresceu em out e nov/2026: personagens simples (boneco 2D, cartum) agindo exatamente o que o narrador diz, às vezes sobre um fundo mais rico. Canais assim relatam dezenas de milhões de views por semana (números dos próprios criadores, não conferidos). A vantagem para nós: **não depende de gerador de vídeo pago**; o agente desenha e anima em código, igual ao nosso motor.

## Como fazemos
- Mesma base do `motor/`: página HTML (SVG ou canvas) que recebe um JSON de cenas e é capturada quadro a quadro pelo Playwright, depois o ffmpeg junta com a voz e o som. Se ficar pesado, usar Remotion (React que vira vídeo) num projeto em `animacao/`.
- **Personagem em peças:** cabeça, olhos, boca, tronco, braços (ombro, cotovelo), pernas (quadril, joelho). Cada peça gira no seu ponto de encaixe. Poses guardadas por nome (`em_pe`, `andando`, `correndo`, `encolhido`, `deitado`, `apontando`, `susto`, `rindo`). Movimento = interpolar entre poses com suavização (ease-in-out), nunca salto.
- **Boca mexendo** pela fala: abrir e fechar conforme o volume da voz naquele quadro (amplitude do WAV), já dá vida.
- **Piscar** a cada 3 a 5 s, respiração leve (tronco sobe 1 a 2 px) quando parado.
- **Nome do personagem** aparece rápido na tela quando ele fala pela primeira vez; cada um tem voz própria.
- **Câmera virtual:** zoom e deslocamento lentos sobre a cena (o quadro "anda"), poucos cortes secos. Corte só na ação.
- **Personagem grande:** ocupa de 50 a 80% da altura da área segura. Personagem pequeno e longe da câmera foi o erro número 1 de quem testou o formato.
- **Protagonista aparece** (em segunda pessoa, o "você" tem corpo: levanta, corre, se esconde).
- Fundo: cenário simples desenhado em camadas (parede, janela, móveis) com parallax leve; ou imagem gerada sem texto e sem pessoas, escurecida, com o boneco por cima.
- Som por objeto e silêncio antes do susto, como em `escala-editor-video`.

## Fluxo de um episódio
1. Roteiro aprovado (`escala-roteiro-serie`) e bíblia lida (`escala-biblia-serie`).
2. Narração gerada primeiro (`escala-voz-narracao`); a duração de cada frase define a duração de cada cena.
3. JSON de cenas: para cada frase, fundo, personagens em cena, pose de cada um, posição, câmera, objeto, som.
4. Prévia de 5 s e folha de quadros; ajustar; só então renderizar tudo (rodar em segundo plano, pode levar 10 a 30 min).
5. Conferência de `escala-editor-video` e fila.

## Primeiro passo prático
Ainda não temos o motor de animação. Antes da primeira série animada: construir `animacao/boneco.html` com um personagem em peças, 8 poses e boca pela voz; renderizar um teste de 10 s e mandar ao Victor. Aprovado, vira componente reutilizado em todas as séries (a ficha visual de cada personagem é só troca de cor, cabelo e roupa).

## Ideias de série para este formato
"Você decide o fim" (sobrevivência, apocalipse leve, mistério na rua), "E se..." (premissa absurda: cada mentira te deixa menor; o botão vermelho na praça), histórias curtas reais e curiosas da história mundial (com fonte), golpes famosos contados como fábula (sem vítima real recente).
