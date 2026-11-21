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

## Padrões com função (livro 10, notas em `conteudo/estudos/livros/10-maquina-de-edicao.md`)
Regra: cada elemento que entra ajuda a entender o que está sendo dito naquele momento. Teste: tire o elemento; se o público entende igual, ele sai. Leia junto: `escala-direcao-cena`, `escala-editor-video`.
- **Sincronizar pela fala real, nunca por segundo fixo.** Escreva qual imagem ou palavra entra em qual palavra falada; a duração da voz já está no JSON. Para inserção no meio da frase, marque a palavra-âncora (nosso: `{img:chave}` antes da palavra, tempo calculado pela posição). Uma inserção principal por vez.
- **Tipografia cinética:** a palavra entra por máscara horizontal, letra a letra com atraso curto, o sublinhado acompanha a fala, fica legível antes de sair e não treme. No máximo 2 títulos curtos por trecho. Cartão leva palavra-chave, nunca o parágrafo. Segure cada palavra meio segundo a mais que o instinto pede. Preserve acentos.
- **Palavra atrás do personagem:** camadas de trás para frente: fundo, palavra, personagem em PNG com alfa, destaques pequenos à frente. Como o boneco já é peça própria, a oclusão é trivial (nosso). Parallax com deslocamentos curtos e coerentes. Se ninguém lê a palavra antes de o personagem passar, o efeito falhou: a leitura vem antes do efeito.
- **Moldura que abre espaço:** o personagem começa em tela cheia; quando a fala lista 3 etapas ou itens, ele vai para uma moldura no canto inferior direito (começar com uns 42% da largura e 34% da altura, cantos arredondados, borda fina, sombra suave) e o resto da tela vira quadro para cartões. Destaque um cartão por vez e apague os outros; ao final ligue-os com linha ou seta. Na conclusão ou no convite, o personagem volta à tela cheia. Não deixe o vídeo inteiro na moldura. Para boneco em código, mantenha o personagem centralizado e legível dentro dela (nosso).
- **Recorte de personagem gerado por IA** (imagem parada): teste com cabelo, mãos e ombros sobre fundo claro e sobre fundo escuro (aparecem halo, borda tremendo, parte sumindo). Guarde o recorte aprovado em PNG com alfa e não reprocesse quando só muda o texto. H.264 não guarda transparência.
- **3D simples (Three.js na página do motor), a testar (nosso):** todo movimento calculado pelo quadro atual, `render(t)`, nunca relógio próprio. Faça primeiro o teste de 5 s renderizado, com oclusão e sombra, e meça o tempo de render sem GPU. Aprovado, vira padrão; se não, não monte o resto em cima.
- Padrão aprovado vira arquivo de regras (`conteudo/estilos/<nome>.md`) separado dos textos e tempos da peça. No vídeo seguinte copie o padrão e refaça voz, sincronia e a amostra de 10 a 15 s antes do episódio inteiro.

## Fluxo de um episódio
1. Roteiro aprovado (`escala-roteiro-serie`) e bíblia lida (`escala-biblia-serie`).
2. Narração gerada primeiro (`escala-voz-narracao`); a duração de cada frase define a duração de cada cena.
3. JSON de cenas: para cada frase, fundo, personagens em cena, pose de cada um, posição, câmera, objeto, som.
4. **Teste de 5 s renderizado em vídeo** (não quadro parado, não prévia) de cada padrão novo, com som, no tamanho de celular. Quadro parado confere posição, não sincronia. Ajustar; só então renderizar tudo (rodar em segundo plano, pode levar 10 a 30 min).
5. Conferência de `escala-editor-video` e fila. Relatar só o intervalo e o arquivo realmente conferidos.

## Primeiro passo prático
Ainda não temos o motor de animação. Antes da primeira série animada: construir `animacao/boneco.html` com um personagem em peças, 8 poses e boca pela voz; renderizar um teste de 10 s e mandar ao Victor. Ele também serve de teste de 5 s dos padrões acima (moldura, palavra atrás do boneco, tipografia cinética). Aprovado, vira componente reutilizado em todas as séries (a ficha visual de cada personagem é só troca de cor, cabelo e roupa).

## Ideias de série para este formato
"Você decide o fim" (sobrevivência, apocalipse leve, mistério na rua), "E se..." (premissa absurda: cada mentira te deixa menor; o botão vermelho na praça), histórias curtas reais e curiosas da história mundial (com fonte), golpes famosos contados como fábula (sem vítima real recente).
