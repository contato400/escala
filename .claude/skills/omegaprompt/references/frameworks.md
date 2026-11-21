# OmegaPrompt — Frameworks Detalhados

> Arquivo de referência. Leia quando precisar de exemplos detalhados de um framework específico.

## Sumário
1. [Estático vs. Dinâmico](#1-estático-vs-dinâmico)
2. [Zero-Shot vs. Few-Shot](#2-zero-shot-vs-few-shot)
3. [Anatomia do Prompt](#3-anatomia-do-prompt)
4. [Tipos de Documento](#4-tipos-de-documento)
5. [Formatação de Snippets](#5-formatação-de-snippets)
6. [Anatomia da Completion](#6-anatomia-da-completion)
7. [Logprobs](#7-logprobs)
8. [Chain-of-Thought](#8-chain-of-thought)
9. [ReAct](#9-react)
10. [Tool Usage](#10-tool-usage)
11. [RAG](#11-rag)
12. [LLM Workflows](#12-llm-workflows)

---

## 1. Estático vs. Dinâmico

**Estático** — sempre igual, define o problema geral.
```
Sistema: Você é um assistente de recomendação de livros.
Responda apenas com títulos disponíveis atualmente.
Foque em ficção literária. Máximo: 3 recomendações.
```

**Dinâmico** — muda a cada requisição.
```
Usuário: [nome], [idade], [últimos livros lidos], [interesses atuais]
```

**Regra:** Se está hardcoded → estático. Se vem de variável → dinâmico.

---

## 2. Zero-Shot vs. Few-Shot

### Zero-Shot (instrução direta)
```
Classifique o sentimento do texto abaixo como POSITIVO, NEGATIVO ou NEUTRO.
Responda apenas com a classificação, sem explicação.
Razão: respostas curtas são mais fáceis de parsear programaticamente.

Texto: "O atendimento foi razoável, mas o produto chegou amassado."
```

### Few-Shot (com exemplos)
```
Classifique o sentimento. Formato: [POSITIVO|NEGATIVO|NEUTRO]

Texto: "Adorei o produto, chegou antes do prazo!" → POSITIVO
Texto: "Veio com defeito e o suporte não ajudou." → NEGATIVO
Texto: "Produto ok. Entrega dentro do esperado." → NEUTRO

Texto: "O atendimento foi razoável, mas o produto chegou amassado." →
```

**Quando usar few-shot:** Para ensinar formato, estilo e distribuição esperada.
**Armadilha:** Se todos os exemplos são 5 estrelas, o modelo tende a dar 5 estrelas.

---

## 3. Anatomia do Prompt

### Exemplo completo com sanduíche

```
[INTRODUÇÃO]
Você é um assistente especialista em análise de contratos jurídicos brasileiros.

[CONTEÚDO ESTÁTICO - regras]
Ao analisar contratos:
- Identifique cláusulas de risco (penalidades, rescisão, exclusividade)
- Aponte ambiguidades que precisam de clarificação
- Use linguagem acessível, não jargão técnico

[CONTEÚDO DINÂMICO - dados]
Contrato para análise:
"""
{texto_do_contrato}
"""

[REFOCO - Técnica Sanduíche]
Com base no contrato acima, identifique os três maiores riscos para o contratante.

[TRANSIÇÃO]
Os três principais riscos são:
```

### Vale do Meh
```
[início — bem lembrado] ←
[...
[MEIO — pouco lembrado] ← coloque aqui apenas contexto de suporte
...]
[fim — bem lembrado] ← coloque conclusão e refoco aqui
```

---

## 4. Tipos de Documento

### Conversa de Conselho (ChatML)
```json
[
  {"role": "system", "content": "Você é HomeBoy, assistente residencial..."},
  {"role": "user", "content": "Está muito quente aqui."},
  {"role": "assistant", "content": null, "tool_calls": [{"name": "get_room_temp"}]},
  {"role": "tool", "content": "27"},
  {"role": "user", "content": "Por favor ajuste para 24°C."}
]
```

### Relatório Analítico (Markdown)
```markdown
# Análise de Viabilidade: Novo Produto X

## Escopo
Esta análise cobre o mercado brasileiro B2B para o produto X, excluindo varejo.

## Contexto de Mercado
{dados_mercado}

## Dados do Produto
{especificacoes}

## Análise
(modelo preenche aqui — espaço para raciocínio)

## Conclusão
```

### Documento Estruturado (XML)
```xml
<task>
  <instruction>Extraia os dados do contrato abaixo</instruction>
  <contract>{texto_contrato}</contract>
</task>

<!-- Saída esperada: -->
<extraction>
  <parties>
    <buyer></buyer>
    <seller></seller>
  </parties>
  <value></value>
  <deadline></deadline>
  <penalties></penalties>
</extraction>
```

---

## 5. Formatação de Snippets

### Modulares — fáceis de inserir/remover
```python
# Cada snippet é independente
snippet_clima = f"Clima atual: {clima['descricao']}, {clima['temp']}°C"
snippet_historico = f"Últimas compras: {', '.join(ultimas_compras)}"

prompt = base_prompt + "\n" + snippet_clima + "\n" + snippet_historico
```

### Naturais — combinam com o tipo de documento
```markdown
#### Clima Atual
{descricao} com temperatura de {temp}°C

#### Histórico do Cliente
Últimas compras: {historico}
```

### Chekhov's Gun — não inclua o que não é necessário
```
❌ RUIM: inclui 20 atributos do usuário quando só 3 são relevantes
✅ BOM: filtra e inclui apenas os atributos que afetam a decisão
```

---

## 6. Anatomia da Completion

### Eliminar fluff — peça a resposta primeiro
```
Recomende um livro. Dê o título e autor primeiro, depois a justificativa.
Formato: "Título: X — Autor: Y. [justificativa em seguida]"
```

### Stop Sequences
```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    stop=["\n## ", "</answer>", "---"]  # para na próxima seção
)
```

### Inception (modelos de completion)
```
# Análise de Viabilidade

## Conclusão
Com base nos dados apresentados, a recomendação é
```
→ O modelo completa a partir daqui, seguindo o tom do início.

---

## 7. Logprobs

### Avaliar confiança na resposta
```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    logprobs=True,
    max_tokens=10
)
# Média próxima de 0 = modelo confiante
# Média muito negativa (< -5) = possível alucinação
avg_logprob = sum(response.logprobs.token_logprobs) / len(response.logprobs.token_logprobs)
```

### Classificação calibrada
```python
# Se o modelo está classificando conservador demais:
# Adicione constante ao logprob de "SIM" antes de comparar
ajuste_sim = 0.3
logprob_sim_ajustado = logprob_sim + ajuste_sim
decisao = "SIM" if logprob_sim_ajustado > logprob_nao else "NÃO"
```

---

## 8. Chain-of-Thought

### Zero-Shot CoT
```
Resolva o problema abaixo. Pense passo a passo antes de dar a resposta final.

Problema: Uma loja tem 120 produtos. 30% estão em promoção. 
Dos que estão em promoção, metade tem desconto de 20% e metade tem 50%.
Qual é o desconto médio sobre os produtos em promoção?
```

### Few-Shot CoT
```
P: 15% de 80 é quanto?
R: 10% de 80 é 8. 5% é metade disso, 4. Então 15% = 8 + 4 = 12. Resposta: 12.

P: Uma camisa custa R$150 com 30% de desconto. Qual o preço final?
R: 30% de 150 = 45. 150 - 45 = 105. Resposta: R$105.

P: Um produto custa R$200. Foi aumentado 10% e depois teve 10% de desconto. Qual o preço final?
R:
```

### Scratchpad (Relatório Analítico)
```markdown
## Análise (scratchpad interno)
[modelo raciocina aqui — ignoramos no output final]

## Resposta Final
[extraímos só isso]
```

---

## 9. ReAct

### Template de instrução
```
Responda perguntas usando Thought, Action e Observation.
Ferramentas disponíveis:
- Search[query]: busca informações na base de conhecimento
- Calculate[expressão]: calcula expressões matemáticas
- Finish[resposta]: encerra com a resposta final

Exemplos:
Thought: Preciso saber o faturamento da empresa em 2023.
Action: Search[faturamento empresa 2023]
Observation: Faturamento 2023: R$ 13.4M

Thought: Tenho o dado. Posso responder.
Action: Finish[O faturamento em 2023 foi R$ 13.4M]

Pergunta: {pergunta_do_usuario}
Thought:
```

---

## 10. Tool Usage

### Definição de ferramenta (JSON Schema)
```json
{
  "name": "buscar_cliente",
  "description": "Busca dados de um cliente pelo CPF. Use quando o usuário mencionar dados de um cliente específico.",
  "parameters": {
    "type": "object",
    "properties": {
      "cpf": {
        "type": "string",
        "description": "CPF do cliente no formato 000.000.000-00"
      }
    },
    "required": ["cpf"]
  }
}
```

### Boas práticas
```
✅ Nome autoexplicativo: buscar_cliente_por_cpf
✅ Descrição com quando usar: "Use quando o usuário mencionar um cliente específico"
✅ Parâmetros documentados com formato esperado
✅ Máximo 5-7 ferramentas simultâneas
❌ Evitar sobreposição: não ter get_client E fetch_customer_data
```

---

## 11. RAG

### Pipeline completo
```python
# 1. Chunking — dividir documentos em trechos
chunks = split_document(doc, chunk_size=500, overlap=50)

# 2. Embedding — vetorizar cada trecho
embeddings = embed(chunks)

# 3. Retrieval — buscar os mais similares à query
query_embedding = embed(user_query)
top_chunks = cosine_similarity_search(query_embedding, embeddings, top_k=5)

# 4. Ranking — reranquear pela relevância real
ranked_chunks = rerank(user_query, top_chunks)

# 5. Inserir no prompt
context = "\n\n".join(ranked_chunks[:3])
prompt = f"Com base no contexto abaixo, responda:\n\n{context}\n\nPergunta: {user_query}"
```

### Chekhov's Gun — só insira o relevante
```
❌ RUIM: inserir 10 trechos "por via das dúvidas"
✅ BOM: inserir os 2-3 mais relevantes com score de confiança alto
```

---

## 12. LLM Workflows

### Exemplo: Pipeline de prospecção (caso do livro)
```
Etapa 1: [Scraping]     → HTML das lojas Shopify → lista de stores
Etapa 2: [Extração]     → LLM extrai: produtos, branding, valores por store
Etapa 3: [Ideação]      → LLM gera ideia de plugin personalizado por store  
Etapa 4: [Copywriting]  → LLM escreve email de marketing por store
Etapa 5: [Envio]        → API de email dispara para cada store

Supervisor: coordena fila, reprocessa falhas, monitora qualidade
```

### Quando agente vs. workflow
```
Agente conversacional:
✅ Tarefas imprevisíveis e variadas
✅ Requer julgamento humano no loop
❌ Não confiável para fluxos complexos de N etapas

Workflow:
✅ Etapas bem definidas e repetíveis
✅ Alto volume, processamento em lote
✅ Necessidade de rastreabilidade e retry por etapa
❌ Inflexível para variações não previstas
```
