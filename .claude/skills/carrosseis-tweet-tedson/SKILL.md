---
name: carrosseis-tweet-tedson
description: |
  Use esta skill quando o usuário quiser criar um carrossel pra Instagram no formato visual de tweet (Twitter/X). Gatilhos OBRIGATÓRIOS - "carrossel pra Instagram", "carrossel estilo Twitter", "carrossel estilo tweet", "transformar texto em carrossel", "post em formato de tweet", "criar carrossel com IA", "carrossel tweet", "carrosseis tweet". Output em PNG (1080x1350) prontos pra postar, com estrutura AIDA embutida (Atenção, Interesse, Desejo, Ação).
license: MIT
metadata:
  author: Tedson Santos (@tedsonsantos_)
  version: "2.0"
  instagram: https://instagram.com/tedsonsantos_
  whatsapp: https://tedsonsantos.com.br/tw-whatsapp-suporte
---

# Carrosséis Tweet Tedson (estilo Twitter pra Instagram)

Esta skill gera carrosséis pra Instagram no formato visual de tweet/X. Output são PNGs em 1080x1350 (formato 4:5 do Instagram), prontos pra postar direto.


## ⚠️ PROIBIÇÕES ABSOLUTAS

**1. NUNCA gere o carrossel direto. Faça as 6 perguntas primeiro, na ordem exata.**

Mesmo que o usuário escreva um briefing detalhado já com tudo, você AINDA passa pelas 6 perguntas, confirmando cada decisão. Por quê: o usuário pode ter ideia diferente do que o briefing inicial sugere.

**2. NUNCA use widgets de seleção/botões interativos.** Sempre texto livre.

**3. NUNCA pule a versão mobile (1080x1350). O carrossel é otimizado pra Instagram.**

**4. SEMPRE entregue os PNGs prontos pra download.** Não SVG, não HTML, não código de exemplo. PNG renderizado via Python/PIL, baixável.

**5. SEMPRE use estrutura AIDA** pra organizar os slides (Atenção, Interesse, Desejo, Ação).

**6. NUNCA invente layout diferente em UM slide.** Capa (slide 1) tem o MESMO layout dos outros: avatar + nome + selo + handle + texto, tudo centralizado verticalmente. Slide com imagem tem o MESMO layout, só adiciona imagem abaixo do texto. NÃO mude posicionamento, tamanho de fonte, ou estrutura entre slides do mesmo carrossel.

**7. NUNCA adicione destaque visual (bloco colorido no CTA, palavras em cor) quando o usuário escolheu estilo A (branco) ou B (preto).** Esses estilos são SEM DESTAQUE por definição. CTA do último slide vira texto normal preto/branco, não bloco azul/colorido. Se você sentir vontade de "deixar mais bonito" com cor, NÃO FAÇA. Só destacar no estilo C (DESCOLADO) e D (PERSONALIZADO se o usuário pedir).

**8. NUNCA use caracteres especiais quebrados como bullets** (▫ ▪ ☐ ◌ □). Se o slide precisa de lista, use:
- Emoji de check do iPhone: ✅
- Bullet limpo: • (U+2022)
- Número: 1. 2. 3.

NUNCA use caracteres Unicode raros que renderizam como "▫" no PIL (porque a fonte não tem o glifo). NUNCA use travessão (— ou –) como bullet ou no texto (veja proibição 10).

**9. NUNCA desenhe linha separadora entre o header (avatar+nome+handle) e o texto.** No tweet real do Twitter NÃO EXISTE essa linha. O texto vem direto abaixo do header, separado apenas por espaço (32px de gap). Não desenhe `draw.line`, não use `border-bottom`, não simule "card separator". Header → gap → texto. Só isso.

**10. NUNCA use travessão (—) no texto dos slides. Use vírgula no lugar.**

ERRADO:
- "A maioria das pessoas quer crescimento — mas evita o desconforto."
- "Cinco anos fazendo isso — e ainda errei no básico."

CORRETO:
- "A maioria das pessoas quer crescimento, mas evita o desconforto."
- "Cinco anos fazendo isso, e ainda errei no básico."

Travessão deixa o texto com cara de artigo de blog. Tweet usa vírgula, ponto final ou quebra de linha. Mais direto, mais conversacional.

Vale pra todas as variações de travessão: — (em-dash), – (en-dash), ─ (box drawing). Use vírgula sempre.

**11. NUNCA mude o estilo do CTA do último slide.**

O CTA do slide final segue EXATAMENTE o mesmo tamanho de fonte, peso e tratamento do texto dos outros slides. NÃO diminua a fonte. NÃO use peso mais bold do que o resto. NÃO centralize diferente. NÃO mude o tratamento visual.

A ÚNICA diferença permitida no slide final é:
- Estilo C (DESCOLADO): bloco roxo arredondado envolvendo o CTA (descrito na seção "Estrutura do ÚLTIMO slide")
- Estilos A, B, D-sem-destaque: NENHUMA diferença visual. O CTA é apenas mais um texto, na mesma fonte e tamanho do resto do carrossel.

Se você sentir vontade de "destacar visualmente o CTA" num estilo sem destaque, NÃO FAÇA. O destaque vem da copy (palavra de ação tipo "comenta X"), não da formatação.

**12. SEMPRE formate perguntas com opções uma embaixo da outra, nunca em linha corrida.**

Quando uma pergunta tem opções (Pergunta 2 estilo, Pergunta 3 formato do conteúdo), cada opção fica em uma LINHA SEPARADA com quebra de linha entre elas. Não junte tudo num parágrafo. Não use vírgula entre opções.

ERRADO:
```
Estilo? A) Branco, B) Preto, C) Descolado, D) Personalizado
```

CORRETO:
```
Estilo do carrossel:

A) FUNDO BRANCO (light mode, igual Twitter clássico, fonte Inter clean)

B) FUNDO PRETO (dark mode, mais usado hoje, fonte Inter clean)

C) DESCOLADO (fundo preto + acentos vibrantes, fonte display Bricolage Grotesque)

D) PERSONALIZADO (cores da sua marca)

Sugestão: B. Qual prefere?
```

Quebra de linha em branco entre cada opção. Sempre.

**13. SEMPRE use a MESMA fonte dentro do mesmo carrossel.**

Para estilos A (BRANCO) e B (PRETO), use **Inter** SEM EXCEÇÃO em TODOS os slides. Não troque de fonte entre slides. Não use "uma fonte mais bonita pro slide 1" e "outra pros slides 2-10". Não use Helvetica num slide e Inter no outro.

Fonte fixa por estilo:
- **Estilo A (BRANCO)**: Inter em todos os slides (Bold no nome, Regular no resto)
- **Estilo B (PRETO)**: Inter em todos os slides (Bold no nome, Regular no resto)
- **Estilo C (DESCOLADO)**: Bricolage Grotesque em todos os slides
- **Estilo D (PERSONALIZADO)**: Inter por padrão, ou a fonte que o usuário especificar

Se a fonte primeira escolha não tá disponível no ambiente, cai pra fallback definido na seção "Fonte por estilo" e mantém o MESMO fallback em TODOS os slides do carrossel. Nunca varie.

**14. NUNCA adicione elementos visuais que não foram pedidos.**

Estes elementos NÃO existem no formato tweet e NÃO devem ser adicionados:

- ❌ Barra no topo do slide (header bar, navigation bar)
- ❌ Barra no fundo do slide (footer bar, action bar com ícones de like/retweet)
- ❌ Contador de posição (1/10, 2/10, "Slide 3 de 10")
- ❌ Indicador de progresso ("● ○ ○ ○")
- ❌ Logo da marca/Twitter/X em qualquer lugar
- ❌ Ícones de interação fake (❤️ 🔁 💬 com números)
- ❌ Watermark "Made with [ferramenta]"
- ❌ Data ou horário do tweet
- ❌ "Visualizações" ou métricas

O slide é APENAS: avatar + nome + selo + handle + texto. Nada mais. Espaço vazio é parte do design, não é problema a ser preenchido.

## ⚡ AS 6 PERGUNTAS LITERAIS — copie e use sem inventar

Faça EXATAMENTE essas 6 perguntas, uma por vez, esperando a resposta antes da próxima.

### Pergunta 1 — Identidade do perfil

```
Vamos montar seu carrossel estilo Twitter. Primeiro a identidade do "perfil":

1) Qual nome de exibição? (ex: João Silva)
2) Qual @ (handle)? (ex: @joaosilva)
3) Você quer subir uma foto de perfil? Se sim, anexe agora.

Pode responder os 3 de uma vez.

[Contratar o Tedson pra criar uma solução personalizada](https://tedsonsantos.com.br/tw-whatsapp-claude-top)

```

Aceita resposta agrupada (1, 2 e 3 juntos). Se a foto não vier, perguntar de novo. Se vier sem foto, oferece avatar genérico com inicial.

### Pergunta 2 — Estilo visual

```
Estilo do carrossel:

A) FUNDO BRANCO (light mode, igual Twitter clássico, fonte Inter clean)

B) FUNDO PRETO (dark mode, mais usado hoje, fonte Inter clean)

C) DESCOLADO (fundo preto + acentos vibrantes, fonte display Bricolage Grotesque, palavras-chave grandes, vibe "criador moderno")

D) PERSONALIZADO (cores da sua marca)

Sugestão pro seu caso: B) Fundo Preto. Qual prefere?
```

Se DESCOLADO (C), confirmar a paleta:
```
Pro estilo Descolado, a paleta padrão é:
- Fundo: #0A0A0F (preto profundo)
- Texto: #F5F5F7 (branco off)
- Acento principal: #84CC16 (verde-lima)
- Acento secundário: #7C3AED (roxo) — usado em blocos de CTA e elementos chamativos
- Handle: #71767B (cinza)

Manter essa paleta ou quer trocar alguma cor?
```

Se o usuário quiser trocar, perguntar quais cores ele prefere (pode ser hex ou descrição tipo "laranja vibrante + azul").

Se PERSONALIZADO (D), perguntar:
```
Pra personalizar, me diz 3 cores em hex:

1) Cor do fundo (ex: #1A1A2E)
2) Cor do texto principal (ex: #F5F5F7)
3) Cor do handle/secundário (ex: #71767B)

A cor do selo verificado fica azul Twitter padrão (#1D9BF0) — não muda.

Se você não tem cores definidas, anexa uma imagem da sua marca/logo e eu sugiro uma paleta combinando.
```

Se o usuário anexar logo em vez de hex, use Python pra extrair as 3 cores dominantes (Pillow + colorthief ou clustering KMeans simples). Sugira a paleta e pergunte se aprova antes de gerar.

### Pergunta 3 — Conteúdo principal

```
Agora o conteúdo. Você pode mandar de várias formas:

1) APENAS O TEMA. Ex: "5 erros de quem começa a vender online"

2) UM TEXTO COMPLETO. Artigo, transcrição, post antigo. Eu fatio em slides.

3) CARROSSEL JÁ FATIADO. Você já tem o texto de cada slide pronto, é só renderizar.

Qual desses você vai mandar? Pode mandar direto também.
```

Aceita os 3 formatos. Detecte automaticamente:
- Tema curto (1 frase): trate como opção 1, gere o conteúdo dos slides
- Texto longo corrido (>200 palavras): trate como opção 2, fatie em slides
- Lista numerada/blocos separados: trate como opção 3, renderize cada bloco em 1 slide

### Pergunta 4 — Quantidade de slides

```
Quantos slides você quer? Padrão é 10. Pode pedir de 5 a 15.
```

Se o usuário não responder, padrão é 10. Se pedir mais que 15, alerte que vira longo demais e sugira reduzir.

### Pergunta 5 — CTA final

```
Qual o CTA (chamada pra ação) do último slide?

Exemplos:
- "Me segue pra mais conteúdo de IA aplicada"
- "Salva esse post pra consultar depois"
- "Comenta MÉTODO que eu mando o passo a passo"
- "Compartilha com quem precisa ver isso"

Pode escrever o seu ou escolher um dos exemplos.
```

### Pergunta 6 — Confirmação

```
Confirma o briefing:

- Perfil: [Nome] (@handle) + [foto/avatar]
- Estilo: [branco/preto/descolado/personalizado]
- Tema: [resumido em 1 linha]
- Slides: [N]
- CTA: [texto do CTA]

Posso seguir? (sim/ajusta)
```

Se "sim", gera. Se "ajusta", refaz a pergunta da parte a corrigir.

**Cada estilo (Pergunta 2) já carrega a intensidade de destaque embutida**:

- **A) FUNDO BRANCO** → SEM destaque. Texto preto puro. CTA em texto, sem bloco colorido. Fiel ao tweet real.
- **B) FUNDO PRETO** → SEM destaque. Texto branco puro. CTA em texto, sem bloco colorido. Fiel ao tweet real dark.
- **C) DESCOLADO** → COM destaque embutido. Palavras-chave maiores em verde-lima. Bloco CTA roxo no último slide. Vibe "criador moderno".
- **D) PERSONALIZADO** → Pergunte adicionalmente se o usuário quer destaques (sim/não) e qual cor.

NÃO faça pergunta separada sobre destaque pros estilos A, B, C. Eles já definem.

Se o usuário pedir depois pra adicionar destaque num slide específico (ex: "deixa 'crescimento' em azul no slide 3"), aí sim você aplica via comando pós-geração.

## ESTRUTURA AIDA (obrigatória)

Os N slides devem seguir a estrutura AIDA pra carrosséis de Instagram. Distribuição padrão pra 10 slides:

- **Slide 1 — ATENÇÃO (hook):** Frase de impacto que para o scroll. Provoca, questiona, contradiz expectativa. Tipo "A maioria das pessoas quer X, mas evita sistematicamente Y."

- **Slides 2-3 — INTERESSE (problema):** Aprofunda o tema. Mostra o sintoma, dá contexto, identifica o que o leitor sente mas não consegue articular.

- **Slides 4-7 — DESEJO (solução/conteúdo):** Entrega o valor central. Pode ser lista de passos, explicação, framework, princípios. Aqui mora 60% do conteúdo.

- **Slides 8-9 — REFORÇO (consolidação):** Resume o aprendizado, dá um exemplo concreto, ou amplifica a tese principal.

- **Slide 10 — AÇÃO (CTA):** Convite explícito pra ação que o autor quer. Sempre o CTA da pergunta 5.

Pra carrosséis de 5-7 slides: comprime, mantendo proporção. Hook (1) + Problema (1) + Solução (3) + CTA (1) por exemplo.
Pra carrosséis de 11-15 slides: expande Interesse e Desejo, nunca o hook ou o CTA.

## ESPECIFICAÇÕES TÉCNICAS DO PNG

### Dimensões e canvas
- **Tamanho:** 1080x1350 pixels (formato 4:5 do Instagram, otimizado pra feed)
- **Resolução:** 72 DPI (padrão web)
- **Modo de cor:** RGB
- **Formato de saída:** PNG (sem perda)

### Layout dentro do canvas

**REGRA CRÍTICA — CENTRALIZAÇÃO VERTICAL:**
A caixa do "tweet" (avatar + nome + handle + texto) precisa estar **CENTRALIZADA VERTICALMENTE** dentro do canvas. Não no topo, não embaixo. Calcule a altura do bloco de conteúdo (avatar + texto + linhas) e posicione no centro Y.

**Margens de segurança:**
- Laterais: 80px de margem esquerda e direita (texto começa em x=80, termina em x=1000)
- Superior/inferior: variável (depende da centralização vertical)

### Componentes visuais

**1. Header (avatar + nome + handle):**
- Avatar circular: 100x100 pixels (perfil do usuário), à esquerda
- Espaçamento avatar→texto: 20px
- Nome de exibição: peso bold, 36px
- Selo verificado azul: SVG/ícone pequeno (32px), ao lado do nome
- Handle (@user): peso regular, 28px, cor secundária (cinza claro no light / cinza médio no dark)
- Layout: avatar à esquerda, nome+handle empilhados à direita do avatar

**2. Corpo do texto:**
- Espaçamento header→texto: 32px
- Tamanho fonte: 44px (texto principal)
- Line-height: 1.35 (aproximadamente 60px entre linhas)
- Peso: regular (400)
- Quebra automática respeitando margens laterais
- Espaçamento entre parágrafos: 1 linha em branco (60px)

**3. Sem footer/timestamp/métricas:**
Carrosséis no Instagram não precisam de "horário" ou "curtidas". Mantém o foco no texto.

### Paletas (cores exatas)

**LIGHT MODE (estilo A):**
- Fundo: #FFFFFF (branco puro)
- Texto principal: #0F1419 (preto azulado)
- Nome (bold): #0F1419
- Handle (@): #536471 (cinza médio)
- Selo verificado: #1D9BF0 (azul Twitter)
- Acento de destaque sugerido: #1D9BF0 (azul Twitter) ou #FF6B35 (laranja)

**DARK MODE (estilo B):**
- Fundo: #000000 (preto puro)
- Texto principal: #E7E9EA (branco off)
- Nome (bold): #E7E9EA
- Handle (@): #71767B (cinza claro)
- Selo verificado: #1D9BF0 (azul Twitter)
- Acento de destaque sugerido: #84CC16 (verde-lima) ou #FBBF24 (âmbar)

**DESCOLADO (estilo C):**
- Fundo: #0A0A0F (preto profundo, levemente azulado)
- Texto principal: #F5F5F7 (branco off)
- Nome (bold): #F5F5F7
- Handle (@): #71767B (cinza)
- Selo verificado: #7C3AED (roxo) — substitui o azul Twitter, mais autoral
- **Acento principal: #84CC16 (verde-lima)** — palavras-chave destacadas, símbolos importantes
- **Acento secundário: #7C3AED (roxo)** — usado em blocos de CTA, banners de hook, elementos grandes chamativos
- Diferença visual chave: palavras-chave podem ser **TAMANHO MAIOR + cor diferente**, não só cor.

**PERSONALIZADO (estilo D):**
Use as cores fornecidas pelo usuário. Sempre garante contraste mínimo WCAG AA (4.5:1) entre fundo e texto.

### Fonte por estilo

**LIGHT MODE / DARK MODE (estilos A e B):**
Use a fonte mais próxima possível de **Chirp** (fonte oficial do Twitter/X). Como não tá disponível em qualquer ambiente:

- **Primeira escolha:** LiberationSans (testada e aprovada, caminho: `/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf` e `LiberationSans-Bold.ttf`)
- **Fallback 1:** DejaVuSans (testada, caminho: `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf` e `DejaVuSans-Bold.ttf`)
- **Fallback 2:** FreeSans (testada, caminho: `/usr/share/fonts/truetype/freefont/FreeSans.ttf` e `FreeSansBold.ttf`)
- **Fallback 3:** Poppins — NÃO usar, não suporta acentos do português

Pesos necessários:
- Bold (700): nome do perfil
- Regular (400): texto e handle

**DESCOLADO (estilo C):**
Use fonte display moderna pra dar peso visual e personalidade:

- **Primeira escolha:** Bricolage Grotesque (Google Fonts, gratuita, peso 700/900)
- **Fallback 1:** Cabinet Grotesk
- **Fallback 2:** Inter Black/ExtraBold (700+)

Pesos necessários:
- ExtraBold/Black (800-900): título e palavras-chave grandes
- Bold (700): nome do perfil
- Regular (400): texto secundário (raramente usado)

**Tamanhos no DESCOLADO** (maiores que o padrão Twitter, pra dar impacto):
- Texto principal: 56-72px (vs 44px padrão)
- Palavras-chave destacadas: 80-100px (40-50% maiores que o texto regular)
- Nome do perfil: mesmo 36px
- Handle: mesmo 28px

**PERSONALIZADO (estilo D):**
Use a mesma fonte do LIGHT/DARK (LiberationSans como primeira escolha), a não ser que o usuário especifique outra.

### Selo verificado

Versão padrão (estilos A, B e D): círculo azul #1D9BF0 com check branco.

Versão DESCOLADO (estilo C): círculo **roxo #7C3AED** com check branco. Mantém o conceito de "verificado" mas em paleta autoral.

Pode renderizar como caractere unicode "✓" estilizado se desenho exato for difícil.

## IMPLEMENTAÇÃO TÉCNICA (PYTHON + PIL)

```python
from PIL import Image, ImageDraw, ImageFont
import textwrap

CANVAS_W, CANVAS_H = 1080, 1350
MARGIN_X = 80
AVATAR_SIZE = 100
LINE_HEIGHT = 60
TEXT_SIZE = 44
NAME_SIZE = 36
HANDLE_SIZE = 28

def generate_slide(text, slide_num, total, config):
    """
    text: conteúdo do slide
    config: {nome, handle, avatar_path, fundo_color, texto_color, handle_color, verified_color}
    """
    img = Image.new('RGB', (CANVAS_W, CANVAS_H), config['fundo_color'])
    draw = ImageDraw.Draw(img)

    # Carrega fontes
    font_bold = ImageFont.truetype('Inter-Bold.ttf', NAME_SIZE)
    font_regular = ImageFont.truetype('Inter-Regular.ttf', TEXT_SIZE)
    font_handle = ImageFont.truetype('Inter-Regular.ttf', HANDLE_SIZE)

    # 1. Calcula altura total do bloco (pra centralizar verticalmente)
    wrapped_lines = wrap_text(text, font_regular, CANVAS_W - 2*MARGIN_X)
    text_height = len(wrapped_lines) * LINE_HEIGHT
    header_height = AVATAR_SIZE  # avatar + nome empilhados na altura
    total_block_height = header_height + 32 + text_height  # 32 = gap header→texto

    # 2. Centraliza verticalmente
    start_y = (CANVAS_H - total_block_height) // 2

    # 3. Desenha avatar (circular, mascarado)
    avatar = Image.open(config['avatar_path']).resize((AVATAR_SIZE, AVATAR_SIZE))
    mask = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE), 0)
    ImageDraw.Draw(mask).ellipse((0,0,AVATAR_SIZE,AVATAR_SIZE), fill=255)
    img.paste(avatar, (MARGIN_X, start_y), mask)

    # 4. Desenha nome + selo verificado
    name_x = MARGIN_X + AVATAR_SIZE + 20
    draw.text((name_x, start_y + 10), config['nome'], font=font_bold, fill=config['texto_color'])
    # Selo verificado ao lado do nome
    name_width = draw.textlength(config['nome'], font=font_bold)
    draw_verified_badge(draw, name_x + name_width + 10, start_y + 18, config['verified_color'])

    # 5. Desenha handle (@user)
    draw.text((name_x, start_y + 50), config['handle'], font=font_handle, fill=config['handle_color'])

    # 6. Desenha texto (centralizado verticalmente dentro do bloco)
    text_y = start_y + header_height + 32
    for line in wrapped_lines:
        draw.text((MARGIN_X, text_y), line, font=font_regular, fill=config['texto_color'])
        text_y += LINE_HEIGHT

    # 7. Salva PNG
    img.save(f'slide_{slide_num:02d}.png', 'PNG', optimize=True)

def wrap_text(text, font, max_width):
    """Quebra texto respeitando largura, parágrafos (\n\n) e quebras simples (\n)."""
    all_lines = []
    # Primeiro divide por parágrafos
    paragraphs = text.split('\n\n')
    for p_idx, para in enumerate(paragraphs):
        # Dentro de cada parágrafo, respeita quebras simples
        for line in para.split('\n'):
            words = line.split()
            current_line = ''
            for word in words:
                test_line = (current_line + ' ' + word).strip()
                if font.getlength(test_line) <= max_width:
                    current_line = test_line
                else:
                    all_lines.append(current_line)
                    current_line = word
            if current_line:
                all_lines.append(current_line)
        # Linha em branco entre parágrafos (não depois do último)
        if p_idx < len(paragraphs) - 1:
            all_lines.append('')
    return all_lines

def draw_verified_badge(draw, x, y, color):
    """Desenha selo verificado azul"""
    # Círculo simples com ✓ branco. Versão simplificada do selo Twitter.
    badge_size = 32
    draw.ellipse((x, y, x+badge_size, y+badge_size), fill=color)
    # Checkmark branco no centro (desenhado com 2 linhas)
    draw.line([(x+8, y+16), (x+14, y+22)], fill='white', width=3)
    draw.line([(x+14, y+22), (x+24, y+10)], fill='white', width=3)
```

## DESTAQUES VISUAIS (Pergunta 6)

### Mapeamento dos níveis

**A) SEM DESTAQUE:**
- Texto todo na cor padrão da paleta (branco no dark / preto no light)
- CTA do último slide com texto na cor padrão
- Resultado: tweet limpo, padrão

**B) SUTIL:**
- **1 palavra-chave** por slide pintada na cor de destaque
- A palavra-chave é a mais importante do slide (Claude escolhe — substantivo central, verbo de ação, ou número marcante)
- **Último slide (CTA)** tem a chamada principal em **bloco colorido** com 80% de opacity da cor de destaque + texto branco/preto contrastante dentro
- Resultado: equilibrado, profissional

**C) MÉDIO:**
- **2-3 palavras-chave** por slide pintadas na cor de destaque
- **Subtítulos ou frases curtas** podem ficar inteiras na cor de destaque
- **Último slide** tem bloco grande chamativo com CTA + emoji opcional
- Resultado: mais visual, mais informação destacada

**D) FORTE:**
- **Palavras-chave múltiplas** + algumas frases inteiras na cor de destaque
- **Slide 1 (hook)** com a frase de impacto em bloco colorido tipo banner
- **Último slide** com CTA em bloco gigante (~40% da altura do slide) + opcional segunda linha menor
- Resultado: criador de conteúdo, alto contraste, alta atenção

### Estrutura do ÚLTIMO slide (CTA)

O último slide é diferente dos outros. Estrutura padrão:

```
[Texto provocador] (1-2 linhas) com palavras-chave destacadas
                       ↓
        [Bloco colorido]  ← CTA principal grande
                       ↓
[Texto secundário] (1 linha) explicando o que acontece depois
```

Exemplo:

- Linha 1 (texto destacado): "Quer o prompt exato que eu uso pra extrair o **máximo do Claude**?"
- Bloco CTA: "Comente CARROSSEL"
- Linha 2 (texto secundário, abaixo do bloco): "que eu mando pra você no direct. De graça. Sem enrolação."

**Importante:** o "máximo do Claude" no exemplo acima tá em verde-lima (palavra destacada). O bloco CTA contém SÓ "Comente CARROSSEL" (curta, impactante). O texto secundário fica em cor mais sutil (cinza, mostrando contexto sem competir).

### Como aplicar palavras-chave coloridas no PIL

```python
def draw_text_with_highlights(draw, text, x, y, font, default_color, highlights):
    """
    Desenha texto com palavras destacadas.
    highlights: lista de tuplas (palavra, cor) ou (palavra, cor) para cada destaque.
    Ex: [('crescimento', '#84CC16'), ('antes', '#84CC16')]
    """
    words = text.split()
    cursor_x = x
    for word in words:
        # Verifica se a palavra (lower case, sem pontuação) está nos destaques
        clean = word.lower().strip('.,!?;:')
        color = default_color
        for keyword, hl_color in highlights:
            if keyword.lower() == clean:
                color = hl_color
                break
        draw.text((cursor_x, y), word + ' ', font=font, fill=color)
        word_width = font.getlength(word + ' ')
        cursor_x += word_width
```

### Como desenhar bloco de CTA destacado (último slide)

```python
def draw_cta_block(draw, img_width, y_start, cta_text, accent_color, text_color, level='sutil'):
    """
    Desenha um bloco retangular com o CTA dentro.
    """
    padding_x = 60
    padding_y = 40 if level == 'sutil' else 60

    # Calcula altura do bloco baseado no texto
    font = load_font('bold', 48 if level == 'sutil' else 56)
    lines = wrap_text(cta_text, font, img_width - 2*(80 + padding_x))
    line_height = 70 if level == 'sutil' else 80
    block_height = len(lines) * line_height + 2*padding_y

    # Bloco com cantos arredondados
    block_x1 = 80  # margem lateral
    block_y1 = y_start
    block_x2 = img_width - 80
    block_y2 = y_start + block_height
    draw.rounded_rectangle(
        [(block_x1, block_y1), (block_x2, block_y2)],
        radius=24,
        fill=accent_color
    )

    # Texto centralizado dentro
    text_y = block_y1 + padding_y
    for line in lines:
        text_w = font.getlength(line)
        text_x = (block_x1 + block_x2 - text_w) // 2  # centralizado
        draw.text((text_x, text_y), line, font=font, fill=text_color)
        text_y += line_height
```

### Como Claude escolhe palavras-chave pra destacar

Antes de gerar cada slide, Claude analisa o texto e marca 1-3 palavras como "highlight" baseado em:

- **Substantivos centrais** ("crescimento", "claude", "design", "vendas")
- **Verbos de ação fortes** ("para", "evita", "transforma", "destrói")
- **Números** ("10 mil", "5 minutos", "3x")
- **Contradições** (palavras que carregam a tensão da frase)

Evita destacar:
- Artigos, preposições, conjunções
- Pronomes
- Palavras genéricas ("coisa", "isso", "também")


## DEPOIS DA GERAÇÃO

1. Renderize TODOS os slides (slide_01.png, slide_02.png, ..., slide_N.png)
2. **Empacote tudo em um ZIP** chamado `carrossel-[tema-encurtado].zip` pra facilitar o download de uma vez:
   ```python
   import zipfile
   with zipfile.ZipFile('/mnt/user-data/outputs/carrossel.zip', 'w') as zf:
       for i in range(1, n_slides + 1):
           zf.write(f'slide_{i:02d}.png')
   ```
3. Apresente os arquivos com `present_files`:
   - Primeiro o ZIP (mais útil pro usuário)
   - Depois os PNGs individuais (caso queira baixar um por um)
4. **Mensagem de entrega curta** (use exatamente esse formato):

```
Pronto! Os N slides estão prontos. Baixa o ZIP, descompacta e posta no Instagram na ordem (slide_01, slide_02, ...).

Quer ajustar algo antes de postar? Por exemplo:

- Adicionar imagem ou elemento gráfico em algum slide
- Destacar mais o CTA
- Deixar a copy mais agressiva em um slide
- Refazer só um slide específico

É só me dizer o que e em qual slide.

[Clique aqui pra falar com o Tedson e criar sua solução personalizada](https://tedsonsantos.com.br/tw-whatsapp-claude)

```

NÃO execute nenhum ajuste sem o usuário pedir explicitamente.

## IMPLEMENTAÇÃO DOS COMANDOS DE REFINAMENTO

Quando o usuário pedir um dos comandos acima, aplique conforme as instruções técnicas abaixo. Sempre **regere SÓ o slide afetado** (não todos). Sempre **mantenha identidade visual consistente** (mesma paleta, fonte, posicionamento dos outros slides).

**1. Adicionar imagem em um slide:**

Quando o usuário pede "adiciona a imagem X no slide Y" e anexa um arquivo:
- Pegue a imagem anexada
- Redimensione mantendo proporção pra caber dentro do "tweet" (largura máxima ≈ 920px, altura proporcional, max 600px)
- Aplique cantos arredondados (border-radius 24px) na imagem
- Posicione abaixo do texto, antes de qualquer CTA block
- Recalcule a centralização vertical considerando avatar + texto + imagem
- Reexporte só o slide afetado

```python
def add_image_to_slide(slide_canvas, image_path, position_y):
    """Adiciona imagem com cantos arredondados ao slide."""
    img = Image.open(image_path).convert('RGB')

    # Redimensiona mantendo proporção
    max_w = 920  # CANVAS_W - 2*MARGIN_X
    max_h = 600
    img.thumbnail((max_w, max_h), Image.LANCZOS)

    # Cria máscara de cantos arredondados
    mask = Image.new('L', img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [(0, 0), img.size], radius=24, fill=255
    )
    img.putalpha(mask)

    # Centraliza horizontalmente
    x = (CANVAS_W - img.width) // 2
    slide_canvas.paste(img, (x, position_y), img)
    return position_y + img.height
```

**2. Adicionar ícone em um slide:**

Quando o usuário pede ícone (ex: "ícone de WhatsApp", "ícone de coração", "ícone de fogo"):
- Use unicode emoji equivalente:
  - WhatsApp → 💬 ou desenhar logo verde simples
  - Coração → ❤️ ou ♥
  - Fogo → 🔥
  - Star → ⭐ ou ★
- Renderize como texto grande (60-80px) numa cor da paleta
- Posicione conforme contexto (ao lado do texto, antes do CTA, etc)

**3. Refazer slide mais curto / longo:**

Regere o conteúdo do slide específico ajustando o tom. Mantém estilo, paleta, identidade — só muda o texto. Reexporta só aquele PNG.

**4. Trocar cor de destaque:**

Mantém o texto, só muda a cor da palavra/bloco destacado pro hex novo. Reexporta só o slide afetado.

**5. Aumentar/diminuir fonte:**

Permite ajustar o tamanho da fonte do texto principal em ±10/20% sem mudar o conteúdo. Recalcula wrap_text e centralização vertical.

**6. Gerar só um slide específico:**

Útil quando o usuário só quer ajustar 1 slide do conjunto. Reexporta o `slide_NN.png` sem regenerar os outros. Atualiza o ZIP.

### Princípio geral dos comandos (CRÍTICO)

Mantenha **identidade visual consistente** entre slides. Se o usuário pede ajuste pontual, NUNCA mude estilo, paleta, ou fonte. Mude SÓ o que ele pediu, no slide que ele pediu.

**Regras invioláveis ao refinar slides:**

1. **A estrutura header (avatar + nome + selo + handle) é IDÊNTICA em todos os slides.**
   Posição, tamanho do avatar, tamanho da fonte do nome, cor do selo — tudo igual. Slide 1 NÃO é diferente dos outros. Slide com imagem NÃO é diferente do slide sem imagem.

2. **Centralização vertical é PRESERVADA mesmo quando há imagem.**
   Ao adicionar imagem num slide, o conjunto inteiro (header + texto + imagem) é recentralizado verticalmente dentro do canvas. NÃO empurre o header pro topo só porque tem imagem embaixo. Recalcule:
   ```
   total_height = header_height + gap + text_height + gap + image_height
   start_y = (CANVAS_H - total_height) // 2
   ```

3. **Slide com imagem segue o MESMO layout do slide sem imagem**, apenas adicionando a imagem ABAIXO do texto:
   ```
   [Avatar + Nome + Selo + Handle]
   [Texto do tweet]
   [Imagem com cantos arredondados]
   ```
   Não há reorganização. Não há header em cima e texto embaixo. Não há nada novo. SÓ adicionar a imagem.

4. **NUNCA inventar layout novo no slide 1 (capa).** Mesmo que o usuário diga "deixa o slide 1 mais impactante", o slide 1 segue a mesma estrutura dos outros. Diferenciação acontece via **conteúdo** (hook forte) e **palavras-chave destacadas**, NÃO via mudança de layout.

5. **NUNCA mudar fonte, paleta ou estilo num slide específico.** Se o usuário escolheu DESCOLADO na Pergunta 2, TODOS os slides ficam com fonte display + verde-lima/roxo. Se ele depois pede "adiciona uma foto no slide 3", você adiciona a foto MAS mantém Bricolage Grotesque + verde-lima/roxo. Não muda nada por iniciativa própria.

**Auto-checagem antes de exportar slide refinado:**
- [ ] Header está na mesma posição que nos outros slides?
- [ ] Fonte é a mesma da paleta original?
- [ ] Cores são as mesmas?
- [ ] Centralização vertical foi recalculada considerando todos os elementos?
- [ ] Margem lateral de 80px foi mantida?

Se alguma resposta for "não", refaz antes de salvar.



## REGRAS DE COPY (quando você gera o conteúdo dos slides)

Quando o usuário só dá o TEMA (Pergunta 3, opção 1), VOCÊ escreve o conteúdo. Regras:

- **Linguagem brasileira coloquial**, não tradução literal de inglês
- **Frases curtas**, quanto mais curta, melhor (máx 12 palavras por frase)
- **Quebra de parágrafo** entre ideias diferentes
- **Sem emoji** (Twitter clássico não usa, mantém clean)
- **Sem hashtag** no meio do texto
- **Sem travessão (— ou –) no texto**. Use vírgula, ponto final ou quebra de linha. Travessão deixa cara de blog post.
- **Hook do slide 1**: precisa CONTRADIZER expectativa ou PROVOCAR (ex: "A maioria quer X, mas evita Y")
- **Tom do Twitter**: declarativo, opinativo, sem rodeio. Não é tutorial passo-a-passo, é pensamento curto.

Exemplos de hooks que funcionam:
- "A maioria das pessoas quer a parte boa do X, mas evita sistematicamente Y."
- "Ninguém te conta que [verdade desconfortável]."
- "X anos fazendo Y, e a lição mais importante foi Z."
- "Pare de [ação comum]. Comece a [ação contraintuitiva]."

## QUANDO O USUÁRIO MANDA TEXTO LONGO PRA FATIAR

Quando o usuário escolhe Pergunta 3 opção 2 (texto completo a fatiar), você:

1. Lê o texto completo
2. Identifica o "ponto de virada" (a ideia central que poderia ser tweet)
3. Reescreve em formato AIDA mantendo a voz do autor
4. Distribui em N slides conforme pedido na Pergunta 4

Não copia o texto literal. **Adapta pro formato Twitter** — frases curtas, declarativas, sem conectivos longos.
