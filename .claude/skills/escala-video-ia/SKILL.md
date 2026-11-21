---
name: escala-video-ia
description: Aciona quando for gerar imagem ou clipe de vídeo com IA (Gemini, Nano Banana, Flow, Veo, Kling, Higgsfield, ChatGPT imagem) para a ESCALA: personagem consistente, cena de fundo, novelinha com IA, capa. NÃO aciona para animação desenhada em código (escala-animacao-personagens) nem para editar o vídeo (escala-editor-video).
---
# Imagem e vídeo gerados por IA

Regra de dinheiro: começar pelo grátis. Gerador pago (Higgsfield, Kling) só quando a conta der lucro e o Victor aprovar. Nunca guardar senha de ferramenta.

## Antes de gerar qualquer coisa
- **O que se move, quanto dura, o que se ouve.** "Anime esta imagem" deixa o modelo decidir tudo.
- **Custo lido na tela** antes de clicar e uma linha por tentativa em `projeto/tentativas.md` (ferramenta, modelo, prompt, custo, defeito, decisão). Teto e regra de parada: 3 tentativas sem melhora, muda a abordagem.
- Rascunho em resolução baixa; final só do plano aprovado.

## Prompt
- Descrever **o que a câmera vê, no afirmativo**. Pedido negativo faz aparecer o que foi negado.
- Uma camada nova por tentativa (mesmo modelo, mesma configuração).
- Decisões visíveis no lugar de adjetivos: luz (janela à esquerda, poste amarelo), lente (35 mm, close), época, cor, lugar.
- **Um movimento de câmera por plano**, com velocidade e alvo ("aproxima devagar do rosto dela").
- Primeiro quadro no estado **antes** da ação. Tudo que o prompt cita precisa estar no quadro ou na referência.
- **Nunca pedir texto dentro da imagem.** O texto entra na edição.
- Formato gerado já no tamanho de onde vai (9:16), nunca recortado depois.

## Personagem consistente (novelinha com IA)
1. Ficha de cada personagem em texto (idade, rosto, cabelo, roupa fixa, cores) e uma **imagem-ficha aprovada** (frente, perfil, 3/4).
2. Uma **imagem com o elenco junto** quando a cena tem dois ou mais.
3. Cada cena: primeiro a **imagem da cena** feita a partir da ficha como referência; depois o vídeo **a partir da imagem** (o prompt descreve só o movimento).
4. **Encadear:** o último quadro de um clipe vira o primeiro do seguinte (salvar quadro, nunca print). Quando o lugar muda, gerar um clipe curto de transição ou cortar na ação.
5. Mesma voz para o mesmo personagem sempre.

## Escada de controle (usar o degrau mais baixo que resolve)
Texto para vídeo (explorar, cena sem personagem que volta) → imagem para vídeo → quadro inicial e final (loop, transformação) → elenco de referências (personagem que volta) → vídeo para vídeo → voz e diálogo.

## Onde fazer
- Imagem: Gemini (Nano Banana) ou ChatGPT na conta que o Victor indicar, pelo Chrome; o Victor baixa ou arrasta o arquivo quando a ferramenta não deixa sair direto.
- Vídeo: Flow / Veo nos créditos do plano que o Victor já tiver; clipes de 8 a 10 s encadeados pelo último quadro.
- Higgsfield / Kling: só com OK do Victor e custo previsto por episódio.

## Honestidade
Rosto de pessoa real (famoso, político, vítima) nunca. Personagem fictício pode, sem fingir ser real. Toda peça realista leva rótulo de IA na publicação. Revisar "cara de IA": pele de plástico, mãos, dentes, texto torto, simetria perfeita.
