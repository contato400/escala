# OmegaPrompt — Templates de Documento

> Templates prontos para uso. Copie e adapte conforme o caso de uso.

---

## Template 1: Conversa de Conselho — Agente com Ferramentas

```python
messages = [
    {
        "role": "system",
        "content": """Você é [NOME_DO_AGENTE], [DESCRIÇÃO_DO_PAPEL].

Ao responder:
- [REGRA 1]
- [REGRA 2]
- [REGRA 3]

Ferramentas disponíveis para você usar quando necessário."""
    },
    {
        "role": "user", 
        "content": "{pergunta_do_usuario}"
    }
]
```

---

## Template 2: Relatório Analítico — Análise com CoT

```markdown
# [TÍTULO DA ANÁLISE]

## Escopo
Esta análise abrange [DOMÍNIO], excluindo [EXCLUSÕES].

## Contexto
{contexto_dinamico}

## Dados
{dados_especificos}

## Análise
(desenvolva o raciocínio aqui antes de concluir)

## Conclusão
```

---

## Template 3: Documento Estruturado — Extração de Dados

```xml
<instructions>
  Extraia as informações do documento abaixo e preencha o XML de saída.
  Preencha com "N/A" quando a informação não estiver presente.
</instructions>

<document>
{texto_para_extrair}
</document>

<output>
  <field_1></field_1>
  <field_2></field_2>
  <field_3></field_3>
</output>
```

---

## Template 4: Classificação com Few-Shot

```
Classifique o texto abaixo como [CLASSE_A], [CLASSE_B] ou [CLASSE_C].
Responda apenas com a classificação.

Exemplos:
"{exemplo_classe_a_1}" → [CLASSE_A]
"{exemplo_classe_a_2}" → [CLASSE_A]
"{exemplo_classe_b_1}" → [CLASSE_B]
"{exemplo_classe_b_2}" → [CLASSE_B]
"{exemplo_classe_c_1}" → [CLASSE_C]

Texto: "{texto_a_classificar}" →
```

---

## Template 5: ReAct — Agente com Raciocínio

```
Responda à pergunta usando os passos Thought, Action e Observation.

Ferramentas disponíveis:
- {ferramenta_1}: {descricao_1}
- {ferramenta_2}: {descricao_2}
- Finish[resposta]: use quando tiver a resposta final

[Inclua 1-2 exemplos de thought/action/observe aqui]

Pergunta: {pergunta}
Thought:
```

---

## Template 6: Summarização com Controle de Tamanho

```
Você é um assistente especializado em síntese de conteúdo.

Resuma o texto abaixo em exatamente {N} parágrafos.
Mantenha: pontos principais, dados numéricos relevantes, conclusões.
Omita: exemplos redundantes, repetições, detalhes de suporte.
Linguagem: [FORMAL/INFORMAL], [PT-BR/EN]

Texto:
"""
{texto_longo}
"""

Resumo em {N} parágrafos:
```

---

## Template 7: Geração de Conteúdo com Persona

```
Você é [NOME], [CARGO] na [EMPRESA].
Seu tom é [DESCRIÇÃO DO TOM].
Seu público é [DESCRIÇÃO DO PÚBLICO].

[TAREFA ESPECÍFICA]

Contexto adicional:
{contexto_dinamico}

[REFOCO DA TAREFA]

[TRANSIÇÃO/INÍCIO DA RESPOSTA]
```

---

## Template 8: Pipeline RAG — Prompt com Contexto Recuperado

```
Responda à pergunta do usuário com base APENAS nas informações fornecidas abaixo.
Se a informação necessária não estiver no contexto, diga "Não encontrei essa informação na base."
Não invente ou suponha dados além do que está no contexto.

Contexto relevante:
---
{trecho_1}
---
{trecho_2}
---
{trecho_3}
---

Pergunta: {pergunta_do_usuario}

Resposta:
```
