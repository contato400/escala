---
name: omegaprompt
description: >
  Framework completo de engenharia de prompt baseado em ciência — use sempre que o usuário pedir
  para criar, melhorar, auditar, revisar ou otimizar um prompt para LLMs. Também ative quando o usuário
  quiser construir uma aplicação com LLM, montar um agente, criar pipelines de IA, ou quando disser
  frases como "me ajuda com esse prompt", "como faço o modelo fazer X", "meu prompt não está funcionando",
  "quero que o GPT/Claude faça Y", "como estruturar essa instrução", ou qualquer variação. 
  Esse skill aplica os 12 frameworks do livro Prompt Engineering for LLMs (O'Reilly) de forma prática e sistemática.
---

# OmegaPrompt — Framework de Engenharia de Prompt

## Princípio Central

> **LLMs são motores de completar texto que imitam os padrões do treinamento.**

Tudo que você faz no prompt deve parecer com documentos bem escritos que o modelo já viu. Clareza, estrutura e padrões familiares sempre vencem criatividade rebuscada.

---

## Fluxo de Trabalho ao Receber uma Tarefa de Prompt

### Passo 1 — Diagnóstico (sempre faça antes de escrever)

Responda mentalmente:
- **Qual é o objetivo real?** (classificar, gerar, extrair, raciocinar, transformar, agir?)
- **Qual tipo de saída?** (texto livre, JSON estruturado, código, decisão binária, lista?)
- **A tarefa exige raciocínio multi-etapas?** → use Chain-of-Thought
- **Precisa de dados externos/privados?** → use RAG ou Tool Usage
- **É tarefa recorrente em volume?** → pense em Workflow em vez de agente

---

### Passo 2 — Escolha o Tipo de Documento

| Tipo | Melhor para | Formato recomendado |
|------|-------------|-------------------|
| **Conversa de Conselho** | Interação direta com usuário, multiround, ferramentas | ChatML / system+user+assistant |
| **Relatório Analítico** | Análise objetiva, chain-of-thought, sumários | Markdown com cabeçalhos |
| **Documento Estruturado** | Saída que será parseada por código | XML ou YAML |

---

### Passo 3 — Monte o Prompt com a Anatomia Correta

```
[INTRODUÇÃO]      → Define o contexto e orienta o modelo desde o início
[CONTEÚDO/CONTEXTO] → Informação dinâmica (dados do usuário) + estática (regras/exemplos)  
[REFOCO]          → Relembra a tarefa principal (obrigatório em prompts longos)
[TRANSIÇÃO]       → Inicia a resposta para o modelo não desviar
```

**Regra do Vale do Meh:** Informação no meio do prompt é menos lembrada. Coloque o mais crítico no início ou no final.

**Técnica Sanduíche:** Para prompts longos, declare o objetivo no início E repita no fim antes da transição.

---

### Passo 4 — Defina o Conteúdo (Estático vs. Dinâmico)

**Estático** (hardcoded, sempre igual):
- Persona/papel do modelo
- Regras e restrições
- Exemplos (few-shot)
- Formato de saída

**Dinâmico** (variável por requisição):
- Dados do usuário
- Resultados de APIs
- Histórico de conversa
- Trechos recuperados via RAG

---

### Passo 5 — Escolha a Forma de Instrução

**Zero-Shot (instrução explícita):**
- Use afirmações positivas: "Responda em JSON" (não "Não responda em texto")
- Adicione razões: "Use linguagem formal, pois o público é executivo C-level"
- Evite absolutos; prefira condicionais

**Few-Shot (exemplos implícitos):**
- Melhor para ensinar **formato e estilo** de saída
- Respeite a distribuição dos exemplos (evite viés de ancoragem)
- Use poucos exemplos para formato; zero-shot para lógica complexa

---

## Técnicas Avançadas

### Chain-of-Thought (CoT)

Use quando a tarefa exigir raciocínio, lógica ou matemática.

**Versão Zero-Shot:** Adicione ao final do prompt:
> *"Pense passo a passo antes de responder."*

**Versão Few-Shot:** Inclua exemplos onde o raciocínio precede a resposta:
```
P: A densidade da pera é ~0.6g/cm³. A água tem 1g/cm³. A pera afunda?
R: Objetos menos densos que a água flutuam. 0.6 < 1, portanto a pera flutua. Resposta: Não.
```

**Versão Relatório (scratchpad):** Em Markdown, inclua seção `## Análise` antes de `## Conclusão` para o modelo "pensar em voz alta".

---

### ReAct — Raciocínio + Ação Iterativa

Para tarefas que precisam de pesquisa ou múltiplas etapas com ferramentas.

Loop padrão:
```
Thought → o que preciso fazer?
Action  → [ferramenta]([parâmetro])
Observe → resultado da ação
... repete ...
Action  → Finish[resposta final]
```

Instrução de ativação no prompt:
```
Resolva a tarefa usando passos de Thought, Action e Observation.
Pense antes de cada ação. Quando tiver a resposta, use Finish[resposta].
```

---

### Tool Usage

Para dar ao LLM acesso a APIs, dados privados ou ações no mundo real.

**Checklist de design de ferramentas:**
- [ ] Nome claro e autoexplicativo (ex: `buscar_cliente_por_cpf`)
- [ ] Descrição em linguagem natural do que a ferramenta faz e quando usar
- [ ] Cada parâmetro documentado com tipo e propósito
- [ ] Número mínimo de ferramentas (mais ferramentas = mais confusão)
- [ ] Evite sobreposição entre ferramentas

---

### RAG — Retrieval-Augmented Generation

Para contextualizar com dados recentes, privados ou extensos demais para o prompt.

**Pipeline:**
```
Query → Retrieval → Ranking → Inserção no prompt → LLM
```

**Tipos de retrieval:**
- **Lexical (BM25):** rápido, baseado em palavras-chave
- **Semântico (embeddings):** mais preciso, detecta sinônimos e contexto
- **Híbrido:** recomendado para produção

**Cuidado com Chekhov's Gun:** Todo trecho inserido no prompt será usado pelo modelo. Insira apenas o que for genuinamente relevante — trechos irrelevantes confundem mais do que ajudam.

---

### LLM Workflows (Pipelines)

Para tarefas complexas onde um agente conversacional não é confiável o suficiente.

**Quando usar Workflow em vez de Agente:**
- Múltiplas etapas bem definidas e previsíveis
- Alto volume de processamento em lote
- Necessidade de auditoria e rastreabilidade por etapa
- Falhas precisam ser isoladas e retentadas

**Estrutura básica:**
```
1. Definir objetivo → o que precisa ser produzido?
2. Quebrar em tarefas atômicas → cada uma com input/output claro
3. Implementar cada tarefa → pode usar LLM com prompt especializado
4. Orquestrar → processo supervisor distribui e coleta resultados
5. Monitorar → avaliar qualidade e erros por etapa
```

---

## Controle de Saída

### Anatomia da Completion Ideal

```
[PREÂMBULO]    → boilerplate, raciocínio (valioso!) ou fluff (custoso)
[RESPOSTA]     → conteúdo principal
[PÓS-ESCRITO] → comentários extras (mova para depois da resposta principal)
```

**Para eliminar fluff:** Peça a resposta direta primeiro, comentários depois:
> *"Responda diretamente. Se quiser adicionar contexto extra, faça depois da resposta principal."*

**Stop Sequences:** Configure sequências de parada (`\n#`, `</answer>`, etc.) para encerrar a geração no ponto certo e economizar tokens.

**Inception Trick:** Para modelos de completion, comece a escrever a resposta no prompt para forçar o tom e formato:
> `"A recomendação é: [Claude completa daqui]"`

---

## Checklist de Auditoria de Prompt

Use para revisar qualquer prompt antes de finalizar:

**Estrutura**
- [ ] Introdução clara define o tipo de tarefa logo no início?
- [ ] Conteúdo crítico está fora do "Vale do Meh" (não apenas no meio)?
- [ ] Há refoco antes da transição (em prompts longos)?
- [ ] A transição sinaliza claramente onde começa a resposta?

**Conteúdo**
- [ ] Instruções usam afirmações positivas (não negações)?
- [ ] Informação irrelevante foi removida (Chekhov's Gun)?
- [ ] Exemplos few-shot representam a distribuição real esperada?
- [ ] Conteúdo dinâmico está separado do estático?

**Saída**
- [ ] O formato de saída está especificado (JSON, Markdown, texto livre)?
- [ ] Há stop sequence ou sinal claro de fim?
- [ ] Tarefas complexas têm Chain-of-Thought ativado?
- [ ] A saída pode ser parseada programaticamente se necessário?

---

## Referências Detalhadas

Para cada framework com exemplos aprofundados, consulte:
- `references/frameworks.md` — os 12 frameworks completos com exemplos
- `references/document_types.md` — templates de Conversa, Relatório e Documento Estruturado

---

## Tabela Rápida de Decisão

| Situação | Framework | Técnica |
|----------|-----------|---------|
| Precisa de raciocínio/math | Chain-of-Thought | "Pense passo a passo" |
| Precisa buscar informação | ReAct | Loop Thought→Action→Observe |
| Dados privados/recentes | RAG | Retrieval + inserção no prompt |
| Ações externas | Tool Usage | JSON Schema + loop de ferramenta |
| Tarefa complexa em volume | LLM Workflow | Pipeline com etapas atômicas |
| Formato rígido parseável | Documento Estruturado | XML/YAML com stop sequence |
| Análise/sumário | Relatório Analítico | Markdown com scratchpad |
| Interação com usuário | Conversa de Conselho | ChatML / system+user+assistant |
