---
name: ebook-profissional
description: >
  Gera E-books profissionais de 50 páginas em formato .docx com capa bonita, sumário funcional,
  gráficos, paleta de cores personalizada e formatação pronta para venda. Use este skill SEMPRE
  que o usuário pedir: 'criar ebook', 'gerar ebook', 'fazer ebook', 'e-book profissional',
  'ebook para venda', 'ebook formatado', ou qualquer variação. O skill solicita a paleta de
  cores do usuário, o tema/assunto, e gera automaticamente um ebook completo e profissional com
  ~50 páginas, incluindo capa, sumário, capítulos, gráficos matplotlib embutidos como imagens,
  citações destacadas, tabelas e rodapés. Produz um .docx pronto para download, impressão e venda.
---

# Skill: E-book Profissional

## Visão geral

Este skill cria E-books de alta qualidade com ~50 páginas em .docx usando `docx` (Node.js) para
estrutura e `matplotlib` (Python) para gráficos embutidos como imagens PNG. O resultado é
profissional, com capa, sumário clicável, capítulos bem formatados e paleta de cores consistente.

---

## Etapa 0 — Coletar informações antes de começar

**Sempre perguntar ao usuário:**

1. **Tema/assunto** do ebook (ex: "Marketing Digital para Médicos", "Gestão Financeira", etc.)
2. **Paleta de cores** — pedir HEX ou descrição (ex: "azul e dourado", "#1A3A5C e #C9A84C")
3. **Público-alvo** (ex: médicos estetas, empreendedores, iniciantes)
4. **Tom** — formal, inspirador, técnico, prático

Se o usuário não fornecer paleta, **sugerir 3 opções pré-definidas**:
- 🔵 Profissional Azul: `#1A3A5C` (primária), `#2E86C1` (secundária), `#F0F8FF` (fundo)
- 🟢 Saúde Verde: `#1B4332` (primária), `#52B788` (secundária), `#F0FFF4` (fundo)  
- 🟡 Premium Dourado: `#2C2C2C` (primária), `#C9A84C` (secundária), `#FFFFF0` (fundo)

---

## Etapa 1 — Gerar gráficos com matplotlib

Antes de criar o .docx, gerar os gráficos em Python e salvar como PNG em `/tmp/ebook_charts/`.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

os.makedirs('/tmp/ebook_charts', exist_ok=True)

# Usar as cores da paleta do usuário
PRIMARY = "#1A3A5C"    # substituir pela cor primária do usuário
SECONDARY = "#2E86C1"  # substituir pela cor secundária
ACCENT = "#C9A84C"     # substituir pelo acento

def chart_style(ax, title):
    ax.set_facecolor('#FAFAFA')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.set_title(title, fontsize=13, fontweight='bold', color=PRIMARY, pad=15)
    ax.tick_params(colors='#555555')

# Gráfico 1: Barras - ex: crescimento/comparativo
fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
categorias = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
valores = [35, 48, 52, 67, 71, 89]
bars = ax.bar(categorias, valores, color=SECONDARY, edgecolor='white', linewidth=1.5, width=0.6)
for bar, val in zip(bars, valores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            f'{val}%', ha='center', va='bottom', fontsize=9, fontweight='bold', color=PRIMARY)
chart_style(ax, 'Crescimento ao Longo do Tempo')
ax.set_ylabel('Taxa (%)', color='#555555')
ax.set_ylim(0, 105)
plt.tight_layout()
plt.savefig('/tmp/ebook_charts/chart_barras.png', bbox_inches='tight', facecolor='white')
plt.close()

# Gráfico 2: Pizza - distribuição
fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
labels = ['Estratégia', 'Execução', 'Análise', 'Melhoria']
sizes = [35, 30, 20, 15]
colors_pie = [PRIMARY, SECONDARY, ACCENT, '#A8DADC']
explode = (0.05, 0.05, 0.05, 0.05)
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors_pie,
                                    autopct='%1.0f%%', shadow=False, startangle=90,
                                    textprops={'fontsize': 10})
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax.set_title('Distribuição de Esforços', fontsize=13, fontweight='bold', color=PRIMARY, pad=15)
plt.tight_layout()
plt.savefig('/tmp/ebook_charts/chart_pizza.png', bbox_inches='tight', facecolor='white')
plt.close()

# Gráfico 3: Linha - evolução/tendência
fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
x = np.arange(1, 13)
y_antes = [20, 22, 21, 25, 24, 26, 28, 27, 30, 29, 31, 32]
y_depois = [20, 28, 35, 45, 52, 61, 68, 74, 79, 85, 90, 95]
ax.plot(x, y_antes, color='#AAAAAA', linewidth=2, linestyle='--', label='Antes', marker='o', markersize=4)
ax.plot(x, y_depois, color=SECONDARY, linewidth=2.5, label='Depois', marker='o', markersize=4)
ax.fill_between(x, y_antes, y_depois, alpha=0.15, color=SECONDARY)
chart_style(ax, 'Evolução de Resultados (12 meses)')
ax.set_ylabel('Resultado (%)', color='#555555')
ax.set_xlabel('Mês', color='#555555')
ax.legend(framealpha=0.9)
ax.set_ylim(0, 110)
plt.tight_layout()
plt.savefig('/tmp/ebook_charts/chart_linha.png', bbox_inches='tight', facecolor='white')
plt.close()

# Gráfico 4: Horizontal - ranking/comparativo
fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
itens = ['Fator A', 'Fator B', 'Fator C', 'Fator D', 'Fator E']
scores = [92, 85, 78, 70, 63]
colors_bar = [PRIMARY if s >= 85 else SECONDARY if s >= 75 else ACCENT for s in scores]
bars = ax.barh(itens, scores, color=colors_bar, edgecolor='white', linewidth=1)
for bar, val in zip(bars, scores):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{val}', va='center', fontsize=10, fontweight='bold', color='#333333')
chart_style(ax, 'Ranking de Fatores de Sucesso')
ax.set_xlabel('Score', color='#555555')
ax.set_xlim(0, 105)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig('/tmp/ebook_charts/chart_horizontal.png', bbox_inches='tight', facecolor='white')
plt.close()

print("Gráficos gerados com sucesso!")
```

---

## Etapa 2 — Criar o .docx com Node.js

### Estrutura do E-book (50 páginas)

```
Capa (1 pg)
Sumário / Índice (2 pg)
Introdução (2 pg)
Capítulo 1: Fundamentos (5 pg) + gráfico
Capítulo 2: Estratégia (6 pg) + gráfico
Capítulo 3: Implementação (6 pg) + tabela
Capítulo 4: Resultados (6 pg) + gráfico
Capítulo 5: Ferramentas e Recursos (5 pg) + tabela
Capítulo 6: Casos Práticos (5 pg) + gráfico
Capítulo 7: Próximos Passos (4 pg)
Conclusão (3 pg)
Referências (2 pg)
Sobre o Autor (1 pg)
Contracapa (1 pg)
```

### Script principal — `/home/claude/ebook_generator.js`

```javascript
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        ImageRun, Header, Footer, AlignmentType, HeadingLevel, BorderStyle,
        WidthType, ShadingType, VerticalAlign, SimpleField, PageBreak,
        LevelFormat, TabStopType, TabStopPosition, TableOfContents } = require('docx');
const fs = require('fs');

// ============================================================
// CONFIGURAÇÃO — alterar conforme paleta do usuário
// ============================================================
const TEMA = "Seu Tema Aqui";
const SUBTITULO = "Subtítulo Descritivo";
const AUTOR = "Nome do Autor";
const PRIMARY_HEX = "1A3A5C";    // sem #
const SECONDARY_HEX = "2E86C1"; // sem #
const ACCENT_HEX = "C9A84C";    // sem #
const BG_LIGHT = "EFF6FF";      // fundo claro para blocos
const YEAR = new Date().getFullYear();

// ============================================================
// HELPERS
// ============================================================

// Parágrafo de texto padrão
function para(text, options = {}) {
  const { bold = false, italic = false, size = 22, color = "2C2C2C",
          spacing = 280, align = AlignmentType.JUSTIFIED, indent = 0 } = options;
  return new Paragraph({
    alignment: align,
    spacing: { after: spacing, line: 340 },
    indent: indent ? { left: indent } : undefined,
    children: [new TextRun({ text, bold, italic, size, color, font: "Georgia" })]
  });
}

// Parágrafo em branco (espaçador)
function blank(size = 160) {
  return new Paragraph({ spacing: { after: size } });
}

// Separador decorativo
function divider(color = SECONDARY_HEX) {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color, space: 1 } },
    children: [new TextRun("")]
  });
}

// Bloco de citação / destaque
function callout(text, bgColor = BG_LIGHT, borderColor = SECONDARY_HEX) {
  return new Table({
    width: { size: 9000, type: WidthType.DXA },
    columnWidths: [200, 8800],
    borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
               left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
               insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE } },
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: 200, type: WidthType.DXA },
          shading: { fill: borderColor, type: ShadingType.CLEAR },
          margins: { top: 0, bottom: 0, left: 0, right: 0 },
          children: [new Paragraph({ children: [new TextRun("")] })]
        }),
        new TableCell({
          width: { size: 8800, type: WidthType.DXA },
          shading: { fill: bgColor, type: ShadingType.CLEAR },
          margins: { top: 160, bottom: 160, left: 240, right: 240 },
          children: [new Paragraph({
            children: [new TextRun({ text, italic: true, size: 22, color: PRIMARY_HEX, font: "Georgia" })],
            spacing: { after: 0 }
          })]
        })
      ]
    })]
  });
}

// Imagem incorporada
function embedImage(path, widthEMU = 5400000, heightEMU = 3000000) {
  if (!fs.existsSync(path)) return blank();
  const imageBuffer = fs.readFileSync(path);
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 240, after: 240 },
    children: [new ImageRun({
      data: imageBuffer,
      transformation: { width: Math.round(widthEMU/9144), height: Math.round(heightEMU/9144) },
      type: "png"
    })]
  });
}

// Tabela de dados
function dataTable(headers, rows, colWidths) {
  const totalWidth = colWidths.reduce((a, b) => a + b, 0);
  const headerRow = new TableRow({
    tableHeader: true,
    children: headers.map((h, i) => new TableCell({
      width: { size: colWidths[i], type: WidthType.DXA },
      shading: { fill: PRIMARY_HEX, type: ShadingType.CLEAR },
      margins: { top: 100, bottom: 100, left: 150, right: 150 },
      verticalAlign: VerticalAlign.CENTER,
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: h, bold: true, color: "FFFFFF", size: 20, font: "Arial" })]
      })]
    }))
  });
  const dataRows = rows.map((row, ri) => new TableRow({
    children: row.map((cell, ci) => new TableCell({
      width: { size: colWidths[ci], type: WidthType.DXA },
      shading: { fill: ri % 2 === 0 ? "FFFFFF" : BG_LIGHT, type: ShadingType.CLEAR },
      margins: { top: 80, bottom: 80, left: 150, right: 150 },
      children: [new Paragraph({
        children: [new TextRun({ text: String(cell), size: 20, color: "2C2C2C", font: "Arial" })]
      })]
    }))
  }));
  return new Table({
    width: { size: totalWidth, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [headerRow, ...dataRows]
  });
}

// Título de capítulo com numeração
function chapterTitle(num, title) {
  return [
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 480, after: 60 },
      children: [
        new TextRun({ text: `Capítulo ${num}`, size: 20, color: SECONDARY_HEX, bold: false, font: "Arial" }),
      ]
    }),
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 0, after: 240 },
      children: [new TextRun({ text: title, size: 36, bold: true, color: PRIMARY_HEX, font: "Arial" })]
    }),
    divider()
  ];
}

// Subtítulo H2
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 320, after: 120 },
    children: [new TextRun({ text, size: 26, bold: true, color: PRIMARY_HEX, font: "Arial" })]
  });
}

// Lista com bullets
function bulletList(items) {
  return items.map(item => new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 120 },
    children: [new TextRun({ text: item, size: 22, color: "2C2C2C", font: "Georgia" })]
  }));
}

// Quebra de página
function pageBreak() {
  return new Paragraph({
    children: [new PageBreak()],
    spacing: { after: 0 }
  });
}

// ============================================================
// CONTEÚDO — CAPA
// ============================================================
function buildCover() {
  return [
    // Bloco colorido superior
    new Table({
      width: { size: 9360, type: WidthType.DXA },
      columnWidths: [9360],
      rows: [new TableRow({ children: [new TableCell({
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: PRIMARY_HEX, type: ShadingType.CLEAR },
        margins: { top: 2880, bottom: 2880, left: 720, right: 720 },
        verticalAlign: VerticalAlign.CENTER,
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { after: 240 },
            children: [new TextRun({ text: TEMA.toUpperCase(), bold: true, size: 52, color: "FFFFFF", font: "Arial" })]
          }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { after: 480 },
            children: [new TextRun({ text: SUBTITULO, size: 28, color: "D0E8FF", font: "Georgia", italic: true })]
          }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { after: 0 },
            children: [new TextRun({ text: "━━━━━━━━━━━━", size: 24, color: ACCENT_HEX, font: "Arial" })]
          }),
        ]
      })]})],
    }),
    blank(480),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 120 },
      children: [new TextRun({ text: AUTOR, size: 28, bold: true, color: PRIMARY_HEX, font: "Arial" })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 480 },
      children: [new TextRun({ text: `${YEAR} · Todos os direitos reservados`, size: 18, color: "888888", font: "Arial" })]
    }),
    pageBreak(),
  ];
}

// ============================================================
// SUMÁRIO
// ============================================================
function buildTOC() {
  return [
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 0, after: 480 },
      children: [new TextRun({ text: "Sumário", size: 40, bold: true, color: PRIMARY_HEX, font: "Arial" })]
    }),
    new TableOfContents("Sumário", {
      hyperlink: true,
      headingStyleRange: "1-2",
      stylesWithLevels: [
        { styleId: "Heading1", level: 1 },
        { styleId: "Heading2", level: 2 },
      ],
    }),
    pageBreak(),
  ];
}

// ============================================================
// PÁGINAS DE CONTEÚDO (adaptar para o tema real)
// ============================================================

function buildIntro() {
  return [
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 0, after: 240 },
      children: [new TextRun({ text: "Introdução", size: 36, bold: true, color: PRIMARY_HEX, font: "Arial" })]
    }),
    divider(),
    para(`Bem-vindo a este guia completo sobre ${TEMA}. Este material foi cuidadosamente desenvolvido para oferecer uma jornada de aprendizado estruturada, prática e transformadora.`),
    para("Ao longo das próximas páginas, você encontrará conceitos fundamentais apresentados de forma clara, estratégias comprovadas por dados e casos reais, além de ferramentas prontas para aplicação imediata."),
    blank(),
    h2("Como usar este material"),
    para("Este ebook foi organizado de forma progressiva. Cada capítulo constrói sobre o anterior, criando uma base sólida de conhecimento. Recomendamos a leitura na sequência apresentada, mas sinta-se livre para consultar capítulos específicos conforme sua necessidade."),
    callout("💡 Dica: reserve um caderno ou abra um documento para anotar seus insights e planos de ação enquanto lê. A transformação começa na ação."),
    blank(),
    h2("O que você vai aprender"),
    ...bulletList([
      "Os fundamentos essenciais que sustentam todo o restante do conhecimento",
      "Estratégias testadas e validadas por profissionais de alta performance",
      "Como implementar mudanças de forma gradual e sustentável",
      "Ferramentas e recursos para acelerar seus resultados",
      "Como medir e otimizar continuamente seu progresso"
    ]),
    pageBreak(),
  ];
}

// Capítulo genérico reutilizável
function buildChapter(num, title, sections, chartPath = null, tableData = null) {
  const content = [...chapterTitle(num, title)];
  
  for (const section of sections) {
    if (section.h2) content.push(h2(section.h2));
    if (section.paras) section.paras.forEach(p => content.push(para(p)));
    if (section.bullets) content.push(...bulletList(section.bullets));
    if (section.callout) content.push(callout(section.callout), blank());
    content.push(blank(120));
  }
  
  if (chartPath) {
    content.push(h2("Análise Visual"));
    content.push(embedImage(chartPath, 580, 320));
    content.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 240 },
      children: [new TextRun({ text: `Figura ${num}: Análise gráfica dos dados apresentados neste capítulo`, italic: true, size: 18, color: "888888", font: "Arial" })]
    }));
  }
  
  if (tableData) {
    content.push(h2(tableData.title));
    content.push(dataTable(tableData.headers, tableData.rows, tableData.colWidths));
  }
  
  content.push(pageBreak());
  return content;
}

// ============================================================
// MONTAR O DOCUMENTO
// ============================================================

const allSections = [
  ...buildCover(),
  ...buildTOC(),
  ...buildIntro(),

  // Cap 1
  ...buildChapter(1, "Fundamentos Essenciais", [
    { h2: "A Base de Tudo", paras: [
      "Todo resultado extraordinário começa com fundamentos sólidos. Antes de avançar para estratégias complexas, é essencial compreender os princípios que regem o sucesso nesta área.",
      "Profissionais que tentam pular esta etapa invariavelmente encontram dificuldades nas fases avançadas. O tempo investido nos fundamentos é sempre recuperado com juros."
    ]},
    { callout: "\"O sucesso não é acidental. É o resultado de intenção, esforço, aprendizado inteligente e persistência.\"" },
    { h2: "Os 5 Pilares Fundamentais", bullets: [
      "Clareza de propósito e objetivos mensuráveis",
      "Consistência nas ações diárias, mesmo que pequenas",
      "Mentalidade de crescimento e abertura ao aprendizado",
      "Sistemas e processos bem estruturados",
      "Métricas e indicadores para medir o progresso"
    ]},
    { h2: "Aplicação Prática", paras: [
      "Cada pilar deve ser cultivado de forma integrada. Não adianta ter clareza sem consistência, ou processos sem métricas. A sinergia entre os pilares é o que cria resultados exponenciais.",
      "Nos próximos capítulos, vamos explorar como cada um desses pilares se manifesta na prática e como você pode desenvolver cada um deles de forma estruturada."
    ]}
  ], '/tmp/ebook_charts/chart_barras.png'),

  // Cap 2
  ...buildChapter(2, "Estratégia e Planejamento", [
    { h2: "Por que a Estratégia Importa", paras: [
      "Sem estratégia, a energia se dispersa em múltiplas direções sem criar impacto real. Uma boa estratégia concentra recursos e esforços nos pontos de maior alavancagem.",
      "A diferença entre profissionais medianos e os de alta performance geralmente não está no talento ou no esforço bruto, mas na qualidade da estratégia que adotam."
    ]},
    { h2: "Construindo sua Estratégia", bullets: [
      "Diagnóstico: onde você está hoje e onde quer chegar",
      "Análise de gaps: o que está faltando para atingir seus objetivos",
      "Priorização: quais ações têm maior impacto com menor esforço",
      "Cronograma: quando cada ação será executada",
      "Revisão: como e quando você vai avaliar e ajustar"
    ]},
    { callout: "💡 Uma estratégia boa executada com excelência supera uma estratégia perfeita executada de forma mediana." },
    { h2: "Armadilhas Estratégicas Comuns", paras: [
      "Muitos profissionais caem em armadilhas que sabotam até as melhores estratégias. Conhecê-las é o primeiro passo para evitá-las.",
      "A armadilha mais comum é a perfeitomania: esperar o momento ideal para agir. A segunda é a dispersão: querer fazer tudo ao mesmo tempo sem foco."
    ]}
  ], '/tmp/ebook_charts/chart_pizza.png'),

  // Cap 3
  ...buildChapter(3, "Implementação e Execução", [
    { h2: "Da Teoria à Prática", paras: [
      "Implementação é onde a maioria das estratégias falha ou triunfa. Não é falta de conhecimento que para as pessoas — é a dificuldade de transformar intenção em ação consistente.",
      "Neste capítulo, vamos detalhar um método passo a passo para implementar o que você aprendeu de forma estruturada e sustentável."
    ]},
    { h2: "O Método de Implementação em 4 Fases", bullets: [
      "Fase 1 — Preparação (semana 1-2): configure seu ambiente e defina seus primeiros marcos",
      "Fase 2 — Início (semana 3-4): execute as primeiras ações e colete dados iniciais",
      "Fase 3 — Aceleração (mês 2-3): escale o que está funcionando e elimine o que não traz resultado",
      "Fase 4 — Otimização (mês 4+): refine continuamente com base em dados reais"
    ]},
    { callout: "Progresso imperfeito supera perfeição paralisante. Comece agora, ajuste no caminho." },
    { h2: "Gestão de Obstáculos", paras: [
      "Todo processo de implementação encontra obstáculos. A questão não é se vão aparecer, mas quando e como você vai lidar com eles.",
      "Profissionais bem preparados antecipam os principais obstáculos e têm planos de contingência. Este simples hábito reduz dramaticamente o impacto de imprevistos."
    ]}
  ], null, {
    title: "Cronograma de Implementação",
    headers: ["Fase", "Período", "Principais Ações", "Métrica de Sucesso"],
    rows: [
      ["Preparação", "Sem. 1-2", "Setup e planejamento detalhado", "Plano concluído"],
      ["Início", "Sem. 3-4", "Primeiras execuções e testes", "3 ações/dia"],
      ["Aceleração", "Mês 2-3", "Escala do que funciona", "+50% volume"],
      ["Otimização", "Mês 4+", "Refinamento contínuo", "KPI's no verde"]
    ],
    colWidths: [1800, 1600, 3600, 2360]
  }),

  // Cap 4
  ...buildChapter(4, "Medindo Resultados", [
    { h2: "O que Não se Mede Não se Melhora", paras: [
      "Métricas são o GPS do seu progresso. Sem elas, você está navegando no escuro, confiando apenas em intuições que podem ser enganosas.",
      "Mas não basta medir — é preciso medir as coisas certas. Existem métricas de vaidade (que parecem boas, mas não indicam progresso real) e métricas de tração (que realmente importam)."
    ]},
    { h2: "KPIs Essenciais", bullets: [
      "Taxa de conversão: qual % das tentativas resulta em sucesso",
      "Tempo médio de ciclo: quanto tempo leva para completar um ciclo completo",
      "Custo por resultado: quanto cada resultado custa em recursos",
      "ROI: retorno sobre o investimento realizado",
      "NPS: nível de satisfação e probabilidade de recomendação"
    ]},
    { callout: "📊 Defina seus KPIs antes de começar. Mudar as métricas no meio do caminho invalida comparações." },
    { h2: "Ciclo de Melhoria Contínua", paras: [
      "Com as métricas certas em mãos, você pode entrar no ciclo virtuoso de melhoria contínua: medir, analisar, ajustar e medir novamente.",
      "Equipes que praticam este ciclo com disciplina consistentemente superam as que confiam apenas na experiência acumulada."
    ]}
  ], '/tmp/ebook_charts/chart_linha.png'),

  // Cap 5
  ...buildChapter(5, "Ferramentas e Recursos", [
    { h2: "O Ecossistema de Ferramentas", paras: [
      "Vivemos em uma era de abundância de ferramentas. O desafio não é encontrá-las, mas escolher as certas e usá-las com eficiência para não criar mais complexidade do que valor.",
      "Neste capítulo, apresentamos uma curadoria das ferramentas mais relevantes, organizadas por categoria e nível de necessidade."
    ]},
    { h2: "Categorias de Ferramentas", bullets: [
      "Produtividade e organização: gestão de tarefas, projetos e tempo",
      "Comunicação: ferramentas para colaboração eficiente",
      "Análise e dados: plataformas para coletar e interpretar métricas",
      "Automação: soluções para automatizar tarefas repetitivas",
      "Aprendizado: recursos para desenvolvimento contínuo"
    ]},
    { callout: "🛠 Comece com o mínimo necessário. É melhor usar 3 ferramentas muito bem do que 15 de forma superficial." },
  ], null, {
    title: "Ferramentas Recomendadas por Categoria",
    headers: ["Categoria", "Ferramenta", "Para que serve", "Investimento"],
    rows: [
      ["Organização", "Notion", "Gestão de projetos e notas", "Gratuito/Pago"],
      ["Comunicação", "Slack", "Comunicação em equipe", "Gratuito/Pago"],
      ["Análise", "Google Analytics", "Métricas de tráfego", "Gratuito"],
      ["Automação", "Zapier", "Integrações automáticas", "Pago"],
      ["CRM", "HubSpot", "Gestão de relacionamentos", "Gratuito/Pago"]
    ],
    colWidths: [1800, 1800, 3360, 2400]
  }),

  // Cap 6
  ...buildChapter(6, "Casos Práticos e Exemplos Reais", [
    { h2: "A Importância dos Casos Reais", paras: [
      "Teoria sem exemplos práticos é como um mapa sem localização. Os casos apresentados neste capítulo foram selecionados por representarem situações comuns que você provavelmente enfrentará.",
      "Analisamos tanto os sucessos quanto os fracassos — porque aprender com erros alheios é uma das formas mais eficientes de acelerar o próprio desenvolvimento."
    ]},
    { h2: "Caso 1: De Zero a Resultados em 90 Dias", paras: [
      "Profissional iniciante, sem experiência prévia na área, aplicou o método descrito neste ebook de forma disciplinada. Em 90 dias, atingiu resultados que a maioria leva um ano para alcançar.",
      "O diferencial não foi talento especial, mas a aplicação consistente dos fundamentos e a disposição para medir e ajustar rapidamente."
    ]},
    { callout: "🏆 Caso real: aplicando apenas 3 das técnicas deste capítulo, profissionais conseguiram aumentar seus resultados em média 73% nos primeiros 60 dias." },
    { h2: "Caso 2: Recuperando Resultados em Queda", paras: [
      "Nem tudo é trajetória de crescimento linear. Este caso mostra como usar as ferramentas de diagnóstico do Capítulo 4 para identificar o que estava errado e fazer correções de curso.",
      "A capacidade de diagnosticar problemas rapidamente e ajustar a rota é uma das habilidades mais valiosas que você pode desenvolver."
    ]}
  ], '/tmp/ebook_charts/chart_horizontal.png'),

  // Cap 7
  ...buildChapter(7, "Próximos Passos", [
    { h2: "Você Chegou até Aqui — E Agora?", paras: [
      "Parabéns por ter chegado até este ponto! Isso já coloca você em um grupo seleto de pessoas que não apenas adquirem conhecimento, mas o absorvem com profundidade.",
      "Mas conhecimento sem ação não gera resultado. O verdadeiro valor deste ebook se manifesta quando você começa a aplicar o que aprendeu."
    ]},
    { h2: "Seu Plano de Ação em 30 Dias", bullets: [
      "Dias 1-3: Revise os pontos mais importantes de cada capítulo e faça suas anotações",
      "Dias 4-7: Defina seus 3 principais objetivos dos próximos 90 dias",
      "Dias 8-14: Inicie a implementação das estratégias do Capítulo 3",
      "Dias 15-21: Configure suas métricas e comece a medir",
      "Dias 22-30: Faça sua primeira revisão e ajuste o plano"
    ]},
    { callout: "🚀 A única diferença entre quem você é hoje e quem você quer ser é o que você vai fazer a partir de agora." },
    { h2: "Mantendo o Momentum", paras: [
      "Começar é mais fácil do que manter. O segredo para a consistência está em criar sistemas que funcionem mesmo quando a motivação não está no pico.",
      "Utilize os rituais e rotinas descritos ao longo deste material para construir hábitos que sustentem seu crescimento a longo prazo."
    ]}
  ]),

  // Conclusão
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 0, after: 240 },
    children: [new TextRun({ text: "Conclusão", size: 36, bold: true, color: PRIMARY_HEX, font: "Arial" })]
  }),
  divider(),
  para(`Chegamos ao final desta jornada por ${TEMA}. Esperamos que cada capítulo tenha contribuído para expandir sua visão e seu repertório de estratégias.`),
  para("Lembre-se: o aprendizado é um processo contínuo. Este ebook é um ponto de partida, não um destino. Continue aprendendo, testando e refinando suas abordagens."),
  blank(),
  callout("O melhor momento para começar foi ontem. O segundo melhor momento é agora."),
  blank(),
  para("Desejamos muito sucesso na sua jornada. Que cada página deste material tenha plantado sementes que florescerão em resultados extraordinários."),
  blank(),
  new Paragraph({
    alignment: AlignmentType.RIGHT,
    spacing: { after: 120 },
    children: [new TextRun({ text: `Com carinho,`, italic: true, size: 22, color: "555555", font: "Georgia" })]
  }),
  new Paragraph({
    alignment: AlignmentType.RIGHT,
    spacing: { after: 480 },
    children: [new TextRun({ text: AUTOR, bold: true, size: 24, color: PRIMARY_HEX, font: "Arial" })]
  }),
  pageBreak(),

  // Sobre o autor
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 0, after: 240 },
    children: [new TextRun({ text: "Sobre o Autor", size: 36, bold: true, color: PRIMARY_HEX, font: "Arial" })]
  }),
  divider(),
  para(`${AUTOR} é especialista em ${TEMA}, com anos de experiência ajudando profissionais a alcançarem resultados extraordinários. Combina conhecimento teórico sólido com aplicação prática comprovada.`),
  para("Através de mentorias, cursos e conteúdos, já impactou centenas de profissionais que transformaram sua relação com os temas abordados neste material."),
  blank(),
  h2("Conecte-se"),
  ...bulletList([
    "Instagram: @seuarroba",
    "LinkedIn: linkedin.com/in/seuperfil",
    "Site: www.seusite.com.br",
    "E-mail: contato@seusite.com.br"
  ]),
  pageBreak(),
];

// ============================================================
// DOCUMENTO FINAL
// ============================================================
const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Georgia", size: 22, color: "2C2C2C" } }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Arial", color: PRIMARY_HEX },
        paragraph: { spacing: { before: 480, after: 240 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: PRIMARY_HEX },
        paragraph: { spacing: { before: 320, after: 120 }, outlineLevel: 1 }
      }
    ]
  },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } },
                 run: { color: SECONDARY_HEX, bold: true } } }]
    }]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    headers: {
      default: new Header({
        children: [
          new Paragraph({
            border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: SECONDARY_HEX, space: 1 } },
            spacing: { after: 120 },
            children: [
              new TextRun({ text: TEMA, size: 18, color: "888888", font: "Arial" }),
              new TextRun({ text: `  ·  `, size: 18, color: ACCENT_HEX, font: "Arial" }),
              new TextRun({ text: AUTOR, size: 18, color: "888888", font: "Arial" })
            ]
          })
        ]
      })
    },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            border: { top: { style: BorderStyle.SINGLE, size: 4, color: SECONDARY_HEX, space: 1 } },
            spacing: { before: 120 },
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: `${YEAR} © ${AUTOR} — Todos os direitos reservados  |  Página `, size: 18, color: "888888", font: "Arial" }),
              new SimpleField("PAGE")
            ]
          })
        ]
      })
    },
    children: allSections
  }]
});

Packer.toBuffer(doc).then(buffer => {
  const outPath = '/mnt/user-data/outputs/ebook_profissional.docx';
  fs.writeFileSync(outPath, buffer);
  console.log('✅ E-book gerado com sucesso em: ' + outPath);
}).catch(err => {
  console.error('❌ Erro:', err);
  process.exit(1);
});
```

---

## Etapa 3 — Executar e personalizar

```bash
# 1. Instalar dependências
npm install -g docx

# 2. Gerar gráficos
pip install matplotlib numpy --break-system-packages
python3 /home/claude/gerar_graficos.py

# 3. Ajustar variáveis no script JS com o tema e paleta do usuário:
# TEMA, SUBTITULO, AUTOR, PRIMARY_HEX, SECONDARY_HEX, ACCENT_HEX

# 4. Rodar o gerador
node /home/claude/ebook_generator.js

# 5. Validar
python /mnt/skills/public/docx/scripts/office/validate.py /mnt/user-data/outputs/ebook_profissional.docx
```

---

## Checklist antes de entregar

- [ ] Paleta de cores aplicada consistentemente em toda a formatação
- [ ] Capa com o nome do tema, subtítulo e autor
- [ ] Sumário gerado com links funcionais
- [ ] Mínimo 7 capítulos + Introdução + Conclusão + Sobre o Autor
- [ ] Pelo menos 4 gráficos embutidos como imagens PNG
- [ ] Pelo menos 2 tabelas formatadas
- [ ] Blocos de callout/citação em cada capítulo
- [ ] Cabeçalho com nome do ebook
- [ ] Rodapé com numeração de páginas e copyright
- [ ] Arquivo validado sem erros

---

## Notas de personalização

Ao usar este skill, o Claude deve:

1. **Adaptar todo o conteúdo** para o tema específico solicitado pelo usuário
2. **Trocar os dados dos gráficos** por dados relevantes ao tema (ex: para medicina estética, mostrar crescimento de procedimentos, distribuição de especialidades, etc.)
3. **Reescrever os textos** dos capítulos com conteúdo real e aprofundado sobre o tema
4. **Personalizar as tabelas** com informações pertinentes ao assunto
5. **Ajustar os títulos dos capítulos** para refletir a estrutura ideal para o tema
6. **Usar a paleta de cores** do usuário em TODAS as variáveis de cor do script

O template acima é a estrutura base — o conteúdo real deve ser substancialmente escrito para o tema, não genérico.
