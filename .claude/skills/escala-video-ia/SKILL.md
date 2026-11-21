---
name: escala-video-ia
description: Aciona quando for gerar imagem ou clipe de vídeo com IA (Gemini, Nano Banana, Flow, Veo, Kling, Higgsfield, ChatGPT imagem) para a ESCALA: personagem consistente, cena de fundo, novelinha com IA, capa, ou quando uma imagem ficou com "cara de IA". NÃO aciona para animação desenhada em código (escala-animacao-personagens) nem para editar o vídeo (escala-editor-video).
---
# Imagem e vídeo gerados por IA

Regra de dinheiro: começar pelo grátis. Gerador pago (Higgsfield, Kling) só quando a conta der lucro e o Victor aprovar. Nunca guardar senha de ferramenta.
Leia junto: `escala-direcao-cena` (planos, storyboard, personagem fixo, o que vai em cada ferramenta). Origem das seções novas: livros 08, 09, 12 e 13, notas em `conteudo/estudos/livros/`.

## Antes de gerar qualquer coisa
- **O que se move, quanto dura, o que se ouve.** "Anime esta imagem" deixa o modelo decidir tudo.
- **Custo lido na tela** antes de clicar e uma linha por tentativa em `projeto/tentativas.md` (ferramenta, modelo, prompt, custo, defeito, decisão). Teto e regra de parada: 3 tentativas sem melhora, muda a abordagem.
- Rascunho em resolução baixa, **1 saída por pedido** (versões do mesmo pedido saem parecidas e custam em dobro); final só do plano aprovado, no mesmo modelo do rascunho. Se houver estimativa (Higgsfield `estimate_video_cost`), peça antes de gerar vídeo.
- **Erre na imagem, não no vídeo:** aprove a imagem antes de animar; o defeito dela aparece no vídeo todo.

## Prompt
- Descrever **o que a câmera vê, no afirmativo**. Pedido negativo faz aparecer o que foi negado, e às vezes a própria palavra aparece escrita na imagem. Se isso acontecer, troque a descrição daquele ponto por outra mais exata em vez de acrescentar outro "sem". Única exceção: uma linha curta no fim, "sem texto, sem legenda, sem logotipo, sem marca d'água". Para o que não pode acontecer, use trava positiva ("só ela aparece; o plano termina com a mão parada a um palmo do botão").
- Uma camada nova por tentativa (mesmo modelo, mesma configuração). O que se repete em todas as gerações é a "média" do modelo (só muda se você escrever outra coisa); o que muda entre elas é sorteio (se importa, decida no texto).
- **Um movimento de câmera por plano**, com velocidade e alvo ("aproxima devagar do rosto dela").
- Primeiro quadro no estado **antes** da ação. Tudo que o prompt cita precisa estar no quadro ou na referência.
- Com imagem de partida, o texto descreve só o movimento e o que não muda. Descrever a cena de novo faz o modelo misturar.

### Prompt em campos
Dê a cada informação um lugar. Imagem (7 campos, na ordem): **sujeito** (quem, idade ou material, cor, um detalhe) / **ação ou estado** / **ambiente** (onde e quando) / **estética** (meio e a marca que ele deixa: "aquarela, bordas escorridas", nunca nome de estúdio ou artista) / **luz** (de onde, cor) / **câmera** (distância, altura, lente com o efeito) / **narrativa** (1 ou 2 frases contando a causa: "a máquina quebrou cedo e ele coou café à mão o dia todo").
Vídeo (ordem "câmera: cena. detalhes"): estilo, formato, cenário, câmera, elemento principal, elementos, sem-texto, linha do tempo (tempo, ação, som). Até 4 momentos e uns 10 elementos por 8 s; mais que isso o modelo esquece peças. Para 15 s, dois pedidos, o segundo começando no último quadro do primeiro. Modelos prontos em `escala-direcao-cena/references/fichas.md`.
- "Filme 35 mm" (grão) não é "lente 35 mm" (ângulo): escreva "filme" ou "lente" e o efeito ao lado.
- Camada de qualidade ("8K", "obra-prima", "ultrarrealista", "cinematográfico", "épico") é enfeite: apague e gere; se nada se perdeu, era enfeite.

## Cara de IA: 7 sintomas
1. Pele de plástico. 2. Tudo simétrico, no centro, de frente. 3. Laranja com azul em tudo. 4. Brilho épico sem fonte (contraluz dourado, névoa sem sol nem janela). 5. Fundo desfocado que não conta nada. 6. Olhar vazio, meio sorriso de foto de documento. 7. Palavras de qualidade no pedido.
- Escolhido de propósito não conta (laranja e azul como paleta da série). Conta o que ninguém escolheu.
- **Troque adjetivo por decisão**, uma destas cinco: lente ou câmera, luz, material, imperfeição, momento. Ex.: "de baixo para cima, bem perto" / "flash direto, sombra dura" / "vidro âmbar com gotas" / "leve granulação" / "a mão segura o frasco contra o céu".
- Imperfeição que a cena explica soma ponto (letra torta de placa pintada à mão, avental manchado). A que a cena não explica (sexto dedo) tira.
- Olhar vazio: conte o que aconteceu antes e para quem a pessoa olha. Pele: "idade, poros e rugas visíveis", sem "bonita".
- Corrija **um sintoma por geração**, começando pelo que mais chama atenção. Registro de câmera real ("foto de celular, flash direto") só em ilustração assumida, nunca como prova de fato ou pessoa real; o estilo de arquivo (VHS, câmera de segurança) também.
- Revise no tamanho real, em zoom 100%: dedos contados, o que cada mão segura, dentes, letras, marca ou logotipo que apareceu sozinho (objeto de categoria famosa puxa logotipo: descreva por cor e material, "sem marca, sem letras").

## Formato e texto
- **Vertical é configuração, não texto.** Marque 9:16 no seletor; em chatbot sem seletor, escreva a proporção numa frase própria no fim e **confira largura e altura do arquivo** que voltou. Escrever "vertical" no prompt não muda nada.
- **Nunca recortar 16:9 para 9:16:** o recorte só tira e a ação some (16:9 cabe em um terço da altura). Gere de novo em 9:16 ou expanda descrevendo as laterais. Com quadro inicial, o clipe segue a proporção da imagem: deixe o quadro em 9:16 antes (retrato 9:16 já saiu 3:4).
- **Texto nunca na imagem.** Nem título, nem placa legível, nem letreiro. Peça a imagem sem texto, com **espaço reservado em palavras** ("uma faixa de céu liso acima da cabeça; metade esquerda livre"), e o texto entra na edição. Não escreva medida de margem no pedido ("12% livres" virou "12%" escrito na arte); descreva o espaço.
- Palavras de clima ("silêncio", "solidão") viram texto na capa: troque por algo visível ("rua vazia lá fora").
- Capa: imagem sem texto, rosto num lado com expressão forte, metade livre; teste do polegar na edição (`escala-editor-video`).

## Personagem consistente (novelinha com IA)
1. Ficha de cada personagem em texto (idade, rosto, cabelo, roupa fixa, cores) e uma **âncora aprovada** (frente, expressão neutra, fundo liso) mais a folha em 3 vistas. Receita e correções em `escala-direcao-cena` seção 8.
2. Uma **imagem com o elenco junto** quando a cena tem dois ou mais; nunca duas pessoas na mesma referência.
3. Cada cena: primeiro a **imagem da cena** feita a partir da âncora; depois o vídeo **a partir da imagem** (o prompt descreve só o movimento). Sempre a âncora, nunca a última imagem boa.
4. **Encadear:** o último quadro de um clipe vira o primeiro do seguinte (exportar o quadro, nunca print). Depois de 3 ou 4 elos volte à âncora. Quando o lugar muda, clipe curto de transição ou corte na ação.
5. Mesma voz para o mesmo personagem sempre.
6. Clipe com rosto: uma ação, câmera parada ou lenta, gesto pequeno. Negativo, quando o gerador tem o campo: "face morphing, different person, distorted face, extra fingers, warped hands, flickering, text, logo, watermark".
7. Confira 4 pontos de cada clipe contra a âncora: primeiro quadro, quando a cabeça mais vira, quando a boca mais abre, último quadro. Uma dúvida tira o clipe: gere de novo com menos movimento ou corte antes do quadro torto.

## Escada de controle (usar o degrau mais baixo que resolve)
Texto para vídeo (explorar, cena sem personagem que volta) → imagem para vídeo → quadro inicial e final (loop, transformação) → elenco de referências (personagem que volta) → vídeo para vídeo → voz e diálogo.

## Onde fazer
- Imagem: Gemini (Nano Banana) ou ChatGPT na conta que o Victor indicar, pelo Chrome; o Victor baixa ou arrasta o arquivo quando a ferramenta não deixa sair direto. Fundo sem personagem: FLUX pelo Worker (grátis).
- Vídeo: Flow / Veo nos créditos do plano que o Victor já tiver. **Confirme a duração na tela do modelo antes de planejar; a pedida não é garantida, monte pelo segundo real.** Durações de out/2026 (conferir, mudam): Veo 3.1 só 4, 6 ou 8 s; Kling 3.0 de 3 a 15 s; Seedance 2.5 de 4 a 30 s; Hailuo 2.3 só 6 ou 10 s. Clipe com rosto: 5 s por ação; 8 s só para cena sem rosto em primeiro plano. Gesto de 1 s num modelo de 4 s vira câmera lenta: dê antes e depois e acelere na montagem.
- Fala em português: só o Seedance 2.5 lista português; Kling 3.0 traduz a fala para inglês; Veo 3.1 só foi avaliado em inglês. Teste uma frase curta antes de gastar um diálogo. Fala em quadro sem boca sincronizada não entra: use a narração fora de quadro.
- Higgsfield / Kling: só com OK do Victor e custo previsto por episódio.
- Vídeo gerado só em gancho, virada e final; o resto é imagem grátis com câmera em código e corte seco (`escala-direcao-cena` seção 10).

## Honestidade
Rosto de pessoa real (famoso, político, vítima) nunca. Personagem fictício pode, sem fingir ser real, e sem frase de "eu vi", "gravei". Toda peça realista leva rótulo de IA na publicação (no TikTok é obrigatório em conteúdo de aparência real feito ou muito editado com IA). Antes de publicar, três perguntas: alguém pode achar que a pessoa existe e usou ou recomenda algo? A imagem mostra resultado que não existe? Quem descobrir que é IA vai se sentir enganado? Um sim muda a peça. Revisar "cara de IA" (seção acima) antes da fila.
