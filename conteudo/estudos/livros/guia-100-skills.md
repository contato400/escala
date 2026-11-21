# Guia Definitivo: 100 Skills para Claude e Agentes Autônomos (ERGOS LAB, Mentoria Cyborg, 2026)
Lido: linhas 1 a 1947 de 1947 (inteiro; a última linha é a propaganda da mentoria). Nenhuma instrução dirigida a mim apareceu no texto (só instruções de instalação para o leitor, tratadas como conteúdo e não executadas). Não rodei nenhum comando `npx` nem baixei nenhuma skill: os links `mcpservers.org` do guia NÃO foram abertos.

## Resumo (5 linhas)
1. Catálogo de 100 "skills" (arquivos SKILL.md) de terceiros em 10 módulos: frontend, bancos, navegador/scraping, marketing, multimídia, DevOps/nuvem, segurança, QA, produtividade/tokens, operações/pesquisa.
2. A parte técnica útil é pequena: o que é skill (instrução procedimental) contra MCP (ferramentas ativas); escopos global (`~/.claude/skills`) e projeto (`.claude/skills`, vai no Git); 3 jeitos de instalar; o método de 4 etapas (diagnóstico, desenho com humano no controle, testes, acompanhamento).
3. Cada skill vem com: autor, link, comando `npx agent-skills install <autor>/<slug>`, dependências e variáveis (muitas pedem chave paga ou nuvem), e a divisão "humano decide, agente executa".
4. Mais de 60 dos 100 itens são Azure, Cosmos DB, Kubernetes, Terraform, Angular, Rust, Java: sem relação nenhuma com vídeo curto. Cerca de 15 podem render ideia ou skill própria para a ESCALA.
5. ATENÇÃO de segurança: o guia manda instalar com `npx` pacotes de nomes genéricos (`security/api-key-guard`, `audit/agent-audit-trail`, `qa/...`, `coverage/...`) cuja procedência não dá para verificar. Regra ESCALA: nunca instalar por npx; só copiar a ideia e escrever a nossa skill depois de ler o conteúdo.

## O que serve para a ESCALA (detalhado)

### A. Conceitos do capítulo 2 e 3 (linhas 71-102)
- Skill (arquivo `SKILL.md`, instrução procedimental carregada quando o contexto pede) é diferente de MCP (conector que dá ferramentas ativas: consultar banco, ler arquivo, controlar navegador). Nossas skills já seguem o padrão; os conectores (Notion, Metricool, Greenn, Higgsfield etc.) são MCP.
- Escopo: global (`~/.claude/skills/`) vale para qualquer pasta; projeto (`.claude/skills/`) acompanha o Git e todos usam as mesmas regras. A ESCALA usa escopo de projeto, certo, porque as rodadas na nuvem clonam o repositório. (O CLAUDE.md já avisa que projetos em nuvem não carregam skills do repositório sozinhos e manda ler o SKILL.md.)
- Instalação manual (Método B, linhas 94-99) é "o mais seguro": criar a pasta, salvar o SKILL.md, instalar dependências, verificar com `/skills`. O guia admite isso e é a única forma que a ESCALA aceita (ler antes de salvar).
- Diagnóstico de problema (linhas 100-102): a skill não aparece se o arquivo não for exatamente `SKILL.md` (maiúsculas) ou se a pasta não estiver dentro de `.claude/skills/`; skill local tem prioridade sobre global quando o comando de barra é o mesmo.
- Frontmatter: o guia não mostra o formato, mas as nossas skills já têm `name` + `description` com "Aciona quando... NÃO aciona para...". Manter.

### B. Os 4 pilares e o framework de 4 etapas (linhas 65-69, 1534-1539)
Pilares: 1) humano no comando estratégico, "cada ação crítica permanece sob aprovação deliberada"; 2) agentes especializados com instruções claras e acionados por contexto, em vez de um modelo genérico; 3) eliminar trabalho repetitivo; 4) grounding em fontes reais, "zero alucinação" (toda produção ancorada em base verificada).
Etapas: 1) diagnóstico: mapear tarefa repetitiva de alta fricção, "não se implementa IA onde o processo não está claro"; 2) desenho: escopo restrito de cada agente, skills necessárias, pontos de controle humano (human-in-the-loop) antes de qualquer execução irreversível; 3) testes em situação real e validação contra desvio de instrução e vazamento; 4) acompanhamento: revisar desempenho, atualizar skills, monitorar custo de tokens, ajustar gatilhos.
Aplicação ESCALA: a estrutura já bate (4 agentes enxutos, aprovação do Victor, rotina diária). Acréscimos úteis: (a) nas fichas, listar explicitamente os "pontos de controle humano" (publicar, trocar perfil, criar produto, gastar); (b) rever os gatilhos ("Aciona quando...") a cada semana junto com a métrica; (c) o pilar 4 (zero alucinação) vira regra: número de viral e métrica sempre com prova (link, print, data), nunca inventado (já está em `escala-radar-viral`: "com prova").

### C. As skills que valem para a ESCALA (marcadas com SIM ou TALVEZ na tabela abaixo)
Resumo do porquê, com a recomendação de COMO aproveitar (sempre escrevendo nossa própria skill, sem instalar o pacote):
1. **88 DBS AI Writing Fingerprint Checker (SIM, ideia)**: detectar "cara de IA" no texto. A regra fixa da ESCALA é "português simples, sem travessão, sem cara de IA". Criar uma conferência de texto (parte da `escala-roteiro-serie` ou do revisor): lista de marcas de IA (travessão, "Além disso", "é importante ressaltar", "mergulhe", frases em trio, tom de manual, abertura "Você já se perguntou"), busca por elas na legenda, roteiro e fala, e reescrita. Pode virar script `ferramentas/conferir_texto.py` com lista de padrões (sem chamar IA, custo zero).
2. **39 Copywriting Prose Creator (SIM, ideia)**: codificar o estilo de escrita em `PROSE.md` (vocabulário, ritmo, tom). Criar `memoria/voz-quase-aconteceu.md`: palavras que usamos, palavras proibidas, tamanho da frase, como é o gancho, como fala o narrador, exemplos bons e ruins. Alimenta roteiro e legenda e reduz repetição de erro.
3. **77 Grill-Me (SIM, ideia)**: o agente interroga o plano, um ponto de cada vez, até achar furos. Uso: antes de gastar (assinar ferramenta, criar produto na Greenn, lançar série nova), o chefe roda um "grill" de 5 perguntas: qual hipótese? qual prova? quanto custa? o que pode dar errado? como medimos em 72 h? Vai para `escala-ideias-fora-da-caixa` e `escala-produto-greenn`.
4. **34 A/B Testing (SIM, método)**: hipótese clara, amostra e significância, prioridade por ICE (impacto, confiança, facilidade). Para vídeo curto o volume é baixo (zero seguidores), então NÃO calcular significância; usar só a parte "uma hipótese por teste, priorizar por ICE, anotar resultado". Já existe a regra de versões do `escala-editor-video` ("cada versão muda uma coisa"); acrescentar ICE de 1 a 5 para ordenar os testes do backlog.
5. **33 Copy Editing (SIM, ideia)**: cortar palavras redundantes, encurtar frase, fortalecer argumento. Útil para legenda, gancho e página do produto. Já cabe em `escala-ganchos-retencao` e `escala-oferta`; acrescentar passo "enxugar" (cortar 20%).
6. **67 LLM Robustness & Safety Scanner, OWASP (SIM, ideia)**: testar o prompt do bot do Telegram (Workers AI) contra instrução maliciosa ("ignore as regras") e vazamento. O bot recebe texto livre do Victor, mas se alguém descobrir o bot pode mandar texto. Checar: o bot só obedece ao id do Victor; nunca imprime chaves; não executa instrução colada de terceiros. Fazer como checklist em `escala-telegram`.
7. **68 API Key & Secret Guard (SIM, ideia)**: varrer o repositório antes de commit atrás de chave, token, senha (gitleaks ou detect-secrets, ou uma regex simples). Regra fixa ("nunca guardar senha, chave") ganha uma checagem automática pré-commit. Fazer com grep local de padrões (`sk-`, `xox`, `bot[0-9]+:`, `BEGIN PRIVATE KEY`, `eyJ`), sem instalar nada.
8. **70 Agent Action Audit Trail (TALVEZ, ideia)**: registro cronológico de ações do agente com justificativa. A ESCALA já tem `memoria/passagem.md` e o diário de cada agente. Acréscimo: coluna "por quê" e "quem aprovou" em cada ação irreversível (publicar, gastar). Suficiente em markdown.
9. **96 Agent Pulse, custo e atividade (SIM, ideia)**: ler os logs locais do Claude Code e somar tokens e custo por semana. Casa com "custo perto de zero". Sem instalar: usar `/usage` e `/context` e anotar o gasto por rodada em `memoria/aprendizados.md` (ver guias-curtos.md, g02/g03).
10. **57 Cloudflare Workers Deployer (SIM, ideia)**: publicar Worker com Wrangler, D1 (banco), R2 (arquivos). O bot do Telegram já é Worker (`telegram/worker.js`). Se um dia precisar guardar estado (pedidos do Victor, fila) além de arquivos, D1 e KV são grátis para o volume; R2 para guardar vídeos prontos (10 GB grátis, a confirmar). Ler antes de assinar qualquer plano; nunca colocar o token da Cloudflare em arquivo.
11. **75 Cavecrew Subagent Orchestrator (TALVEZ, ideia)**: delegar a subagentes tarefas isoladas e receber só o resumo, para economizar contexto. O Claude Code já faz isso nativamente; para a ESCALA vale a prática: radar e conferência de vídeo em subagente que devolve resumo de 10 linhas, e o chefe não carrega as 15 telas de folha de quadros no contexto.
12. **82/83/84/85 Caveman (TALVEZ, com cuidado)**: modo de resposta ultra enxuta que corta ~75% dos tokens de saída; compressor de arquivos de memória como CLAUDE.md com backup; analisador de contexto repetido. Risco real: o modo "caveman" deixa a fala telegráfica, ruim para roteiro, legenda e mensagem ao Victor (que pedem "português simples, sem cara de IA" mas humano e claro). Só usar na conversa interna entre agentes, nunca no texto final. Compactar CLAUDE.md à mão (cortar repetição) é mais seguro que usar compressor automático: perder uma regra fixa por compressão seria grave.
13. **48 ACE Step Music Generator (TALVEZ, estudar)**: modelo de música com "pesos abertos" para trilha instrumental por texto. A ESCALA exige zero música com direito autoral, então trilha própria é valiosa. Problema: o guia liga o uso ao RunComfy (nuvem paga, chave `RUNCOMFY_API_KEY`) ou GPU local. Estudar se o ACE-Step roda grátis em alguma ferramenta e a licença do resultado para uso comercial (verificar na fonte oficial, não no guia). Alternativa que já existe no motor: trilha gerada em código (síntese simples) ou bibliotecas livres.
14. **50 MiniMax Speech & Foley (TALVEZ, estudar)**: voz e efeitos sonoros descritos em texto (chuva, passos). A skill `escala-editor-video` quer som em cada gesto (tecla, porta rangendo, passo). Efeitos gerados por IA evitam direito autoral. Exige `MINIMAX_API_KEY` paga; verificar custo. Alternativa grátis: sintetizar efeitos simples em código com ffmpeg/numpy (já parcialmente feito).
15. **41/45 AI Video/Image Generation Multi-Model (TALVEZ, só estudar o prompt)**: lista modelos que a ESCALA já conhece (Veo 3.1, Seedance, Wan, FLUX, GPT-Image, Gemini) e roteia via CLI `inference.sh` com `INFERENCE_API_KEY` (paga). Não instalar. Aproveitar: nomes dos modelos que um agente deve conhecer (confirmado também em g04).
16. **93 Deep Multi-Source Web Research (TALVEZ)**: pesquisa multi-fonte com citações; pede chaves Tavily ou Exa. O radar usa a busca do próprio Claude; vale copiar o método (cruzar 2 a 3 fontes, citar, separar fato de suposição), sem instalar.
17. **28 Playwright (JÁ TEMOS)**: o motor já usa Playwright para renderizar quadros. Nenhuma ação.
18. **81 NotebookLM Bridge (TALVEZ, baixa prioridade)**: ancorar respostas só em documentos enviados (zero alucinação). Útil se o Victor quiser consultar os livros do Drive. Precisa token do NotebookLM. A pasta `conteudo/estudos/livros/` já cumpre a função em texto.
19. **94 Amazon Product Research (TALVEZ, baixa prioridade)**: avaliar produto para afiliado (volume de busca, concorrência, margem). Para `escala-hype-e-afiliado` o método vale (checar demanda e concorrência antes de indicar acessório); a skill em si é para vender na Amazon.
20. **01 Frontend Design / 10 UI Component Builder (JÁ TEMOS)**: `ui-ux-pro-max` cobre página de venda e componentes. Nenhuma ação.

### D. O que NÃO fazer com o guia (segurança)
- Não rodar `npx agent-skills install ...` em hipótese alguma. Não consegui verificar se o pacote `agent-skills` existe, é oficial ou é cópia maliciosa (risco clássico de typosquatting). O guia afirma "autor oficial" para nomes genéricos como `security`, `audit`, `compliance`, `qa`, `coverage`, `performance`, `addie`, que não são organizações reais conhecidas.
- Skill 23 (Anti-Detect Browser, isolamento de perfis de hardware para múltiplas contas) e skill 25 (Skill Forge, engenharia reversa de chamadas de rede de um site para copiar a API interna): ambas fogem da regra "sem enganar" e podem violar os termos das plataformas. Para a ESCALA são proibidas: as contas são reais, do Victor, logadas normalmente, sem disfarçar identidade nem automatizar login em lote.
- Scraping de TikTok/Instagram/YouTube (skills 26, 29, 30): termos de uso das redes proíbem coleta automatizada fora da API oficial, e Instagram/TikTok bloqueiam. O radar deve usar busca da web, páginas públicas e as ferramentas autorizadas (TranscriptAPI para YouTube, Metricool, Windsor), com prova. Não montar scraper.
- Skill 69 (LGPD sanitizer) e 98 (Gmail): a ESCALA não guarda dado de terceiro. Não conectar o e-mail do Victor a skill de terceiros.
- Lembrete do próprio guia (e do g04): se algum dia instalar skill de fora, rodar o SkillSpector (NVIDIA) ou ler o SKILL.md e os scripts inteiros primeiro.

## Já coberto nas skills existentes (qual skill, e o que o livro acrescenta ou contradiz)
- `ui-ux-pro-max`: cobre skills 01, 03, 04, 07, 09, 10 (design, acessibilidade, performance web, Tailwind, tokens, componentes). Nada a acrescentar.
- `escala-editor-video` + `escala-producao-video`: cobrem Playwright (28) e o fluxo de edição. Possíveis acréscimos: som por texto (50), trilha original (48), ver itens 13 e 14.
- `escala-video-ia`: cobre 41, 42, 45, 46 (modelos de vídeo e imagem). O guia só confirma nomes e acrescenta o conceito de "roteador" (escolher o melhor modelo disponível por tarefa).
- `escala-memoria` e `memoria/`: cobrem 81 a 90 em parte (memória, passagem, relatório). Acréscimo: PROSE (39) e checagem de cara de IA (88).
- `omegaprompt`: cobre melhoria de prompt, relacionado a 67 (robustez).
- `escala-regras` e CLAUDE.md: cobrem 68 (chaves), 70 (auditoria), human-in-the-loop (pilar 1).
- Nenhum item contradiz as regras fixas, exceto 23 e 25 (ver D).

## Skills novas sugeridas ou melhorias
Todas escritas por nós, texto próprio, sem copiar o conteúdo do guia:
1. **`escala-voz-da-marca` (nova ou seção em `escala-roteiro-serie`)**. Aciona quando: escrever roteiro, legenda, mensagem ao Victor, texto de produto; NÃO aciona para decidir tema. Conteúdo: `memoria/voz-quase-aconteceu.md` com tom, vocabulário, tamanho de frase, proibidos; lista de "marcas de IA" a caçar (travessão, "além disso", "vale ressaltar", frases em trio, final moralista, exclamação demais); passo "enxugar 20%"; exemplos bom e ruim; script opcional `ferramentas/conferir_texto.py` que acusa as marcas por regex.
2. **`escala-guardiao-segredos` (nova, ou item do revisor)**. Aciona antes de todo commit/publicação. Conteúdo: varredura por padrões de chave/token no repositório e nos arquivos de saída, falha se achar; reforço de "nunca guardar senha, chave, telefone ou e-mail"; o que fazer se achar (apagar, pedir ao Victor para trocar a chave, registrar sem copiar o valor).
3. **`escala-questionador` (nova ou seção em `escala-ideias-fora-da-caixa`)**. Aciona quando: o Victor ou o chefe vai gastar dinheiro, criar produto, lançar série, trocar de formato. Conteúdo: modo grill de 5 a 7 perguntas, uma por vez, com prova exigida; resultado em 5 linhas: decisão recomendada, risco principal, como medir em 72 h, custo, alternativa grátis.
4. **Melhoria em `escala-analista`/`escala-chefe`**: acrescentar linha "custo da rodada" (tokens/`/usage`) e a prioridade de testes por ICE (1 a 5 cada) no backlog (`memoria/backlog.md`).
5. **Melhoria em `escala-telegram`**: checklist de robustez do prompt do bot (item C.6).
6. **Melhoria em `escala-regras`**: regra "skill ou plugin de terceiros: nunca instalar por npx; ler o SKILL.md e todos os scripts; escrever a versão nossa; Victor aprova" e a proibição das skills 23 e 25 (anti-detecção e engenharia reversa).
7. **Melhoria em `escala-editor-video`**: opção de trilha e efeitos sonoros originais (itens C.13 e C.14), com a condição de custo zero ou aprovação do Victor.

## Ferramentas citadas (nome, grátis ou preço, para que serve, tem API?)
O guia não informa preços. Quando a skill depende de chave/serviço, o guia lista a variável; não verifiquei nenhum preço. Resumo do que importa:
| Ferramenta | Variável/serviço citado | Para que serve | Observação |
|---|---|---|---|
| agent-skills (CLI npx) | `npx agent-skills install` | Instalar skills | Procedência não verificada; NÃO usar |
| inference.sh | `INFERENCE_API_KEY` | Rodar modelos de vídeo/imagem/avatar por CLI | Pago por uso |
| RunComfy | `RUNCOMFY_API_KEY` | Nuvem de modelos de imagem/vídeo/música | Pago |
| Higgsfield | `HIGGSFIELD_API_KEY` | Fotos de produto e agregador | Pago; conector já disponível no ambiente |
| ElevenLabs | `ELEVENLABS_API_KEY` | Voz e agentes de voz | Pago (ver guias-curtos g01) |
| MiniMax | `MINIMAX_API_KEY`, `MINIMAX_GROUP_ID` | Voz e efeitos sonoros | Pago |
| Firecrawl, Browserbase, Scrapegraph, Tavily, Exa | chaves próprias | Rastreio/scraping/pesquisa | Pagos; rastreio de rede social proibido pelos termos |
| Cloudflare Wrangler | `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` | Publicar Workers, D1, R2 | Tem plano grátis; nunca guardar o token em arquivo |
| gitleaks / detect-secrets | local | Achar segredos no código | Grátis, local |
| Playwright | local | Navegador automatizado | Grátis; já usado |
| NotebookLM | `NOTEBOOKLM_AUTH_TOKEN` | Respostas só com base nos documentos | Conta Google |
| Supabase, Azure, Docker, Terraform, Railway, Redis, Pinecone, Prisma | várias | Bancos e nuvem | Fora de escopo |

## Não serve para a ESCALA
Tabela completa das 100 skills. SIM = escrever versão nossa (nunca instalar o pacote); TALVEZ = só estudar, decidir depois; JÁ TEMOS = coberto por skill existente; NÃO = sem relação ou proibido.

| ID | Skill (autor/slug citado) | Vale para a ESCALA? | Motivo |
|---|---|---|---|
| 01 | Frontend Design (anthropic) | JÁ TEMOS | `ui-ux-pro-max` cobre página de venda |
| 02 | Angular Developer | NÃO | Framework que não usamos |
| 03 | Web Accessibility | NÃO | Só útil para página de venda; contraste já tratado em ui-ux |
| 04 | Web Best Practices | NÃO | Core Web Vitals de site; não temos site |
| 05 | Next.js DevTools | NÃO | Não usamos Next.js |
| 06 | Check Release Auditor | NÃO | Auditoria de release de software |
| 07 | Tailwind Styling | NÃO | Coberto por ui-ux-pro-max se um dia houver página |
| 08 | React Server Architecture | NÃO | Não usamos React |
| 09 | Figma Design Tokens | NÃO | Não usamos Figma |
| 10 | UI Component Builder | NÃO | Idem |
| 11 | Postgres Best Practices | NÃO | Sem banco de dados |
| 12 | Azure Cosmos DB Python | NÃO | Azure |
| 13 | Azure Cosmos DB TypeScript | NÃO | Azure |
| 14 | Azure Cosmos DB Rust | NÃO | Azure |
| 15 | Azure Cosmos DB Java | NÃO | Azure |
| 16 | Azure Data Tables Python | NÃO | Azure |
| 17 | Azure Postgres TypeScript | NÃO | Azure |
| 18 | Prisma Schema Optimizer | NÃO | Sem ORM |
| 19 | Redis Caching | NÃO | Sem Redis |
| 20 | Pinecone Vector Indexing | NÃO | Sem RAG vetorial |
| 21 | Agent Browser (vercel) | TALVEZ | Navegador para conferir página própria; Playwright já cobre |
| 22 | Agent Browser Inference | NÃO | Exige chave paga e grava vídeo; sem necessidade |
| 23 | Anti-Detect Browser | NÃO (PROIBIDO) | Disfarça perfis para multi-conta: contra "sem enganar" e termos das redes |
| 24 | Browser-Act | NÃO | Automação de navegador genérica; risco de automatizar contas |
| 25 | Browser-Act Skill Forge | NÃO (PROIBIDO) | Engenharia reversa de API interna de site de terceiro |
| 26 | Just-Scrape | NÃO | Scraping de rede social contra termos; chave paga |
| 27 | Website Technical Auditor | NÃO | Só para site próprio com 249 regras; não temos site |
| 28 | Playwright Automation Suite | JÁ TEMOS | O motor já usa Playwright |
| 29 | Firecrawl Web Crawler | TALVEZ (baixo) | Converter documentação de ferramenta em markdown; chave paga |
| 30 | Cloud Browser (Browserbase) | NÃO | Navegador na nuvem pago |
| 31 | Generative AI SEO | NÃO | SEO de artigo, não vídeo |
| 32 | Ad Creative Scaler | TALVEZ (futuro) | Só quando houver anúncio pago de produto; fase 1 é crescer sem pagar |
| 33 | Copy Editing | SIM (ideia) | Enxugar legenda, gancho e página de produto; item C.5 |
| 34 | A/B Testing | SIM (método) | Uma hipótese por teste, ICE; item C.4 |
| 35 | Analytics & Measurement Plan | TALVEZ | Nomear eventos e UTM do link da Greenn para o analista |
| 36 | Marketing Attribution | NÃO | Multicanal pago; irrelevante agora |
| 37 | Paid Ads Strategy | NÃO | Sem tráfego pago na fase 1 |
| 38 | App Store Optimization | NÃO | Não temos app |
| 39 | Copywriting Prose Creator | SIM (ideia) | Manual de voz da marca; item C.2 |
| 40 | RootMention SEO Audit | NÃO | SEO de site |
| 41 | AI Video Generation Engine | TALVEZ (estudar prompt) | Confirma modelos; exige chave paga |
| 42 | RunComfy AI Video Router | NÃO | Nuvem paga |
| 43 | AI Avatar Talking Head | NÃO | Avatar falando como pessoa: conflito com "enganar não" e custo |
| 44 | RunComfy Avatar Orchestrator | NÃO | Idem |
| 45 | AI Image Generation Multi-Model | TALVEZ (estudar prompt) | Já usamos FLUX; chave paga |
| 46 | RunComfy Image Router | NÃO | Nuvem paga |
| 47 | Product Photoshoot Studio (higgsfield) | NÃO | Foto de produto físico; só se vender acessório como afiliado |
| 48 | ACE Step Music Generator | TALVEZ (estudar) | Trilha original sem direito autoral; item C.13 |
| 49 | ElevenLabs Voice Agents | NÃO | Atendimento por voz |
| 50 | MiniMax Speech & Foley | TALVEZ (estudar) | Efeitos sonoros por texto; item C.14 |
| 51 | Azure AI Gateway | NÃO | Azure |
| 52 | AI Runway AKS | NÃO | Kubernetes |
| 53 | Azure Compute & GPU | NÃO | Azure |
| 54 | Enterprise Cloud Infra Planner | NÃO | Azure |
| 55 | Application Insights Telemetry | NÃO | Azure |
| 56 | Application Insights Web RUM | NÃO | Azure |
| 57 | Cloudflare Workers Deployer | SIM (ideia) | O bot já é Worker; D1/KV/R2 grátis se precisar guardar estado; item C.10 |
| 58 | Railway | NÃO | Hospedagem paga |
| 59 | Docker Orchestrator | NÃO | Sem contêiner |
| 60 | Terraform | NÃO | Sem infraestrutura como código |
| 61 | Azure Compliance | NÃO | Azure |
| 62 | Azure Identity Python | NÃO | Azure |
| 63 | Azure Identity TypeScript | NÃO | Azure |
| 64 | Azure Identity .NET | NÃO | Azure |
| 65 | Azure Identity Rust | NÃO | Azure |
| 66 | Azure Identity Java | NÃO | Azure |
| 67 | LLM Robustness & Safety Scanner (OWASP) | SIM (ideia) | Checar o prompt do bot do Telegram; item C.6 |
| 68 | API Key & Secret Guard | SIM (ideia) | Varredura de segredo antes do commit; item C.7 |
| 69 | LGPD/GDPR Sanitizer | NÃO | Não guardamos dado de terceiro |
| 70 | Agent Action Audit Trail | TALVEZ | `passagem.md` já cumpre; acrescentar "por quê" e "quem aprovou" |
| 71 | Chrome DevTools QA | NÃO | QA de site |
| 72 | Azure Pre-Deploy Validation | NÃO | Azure |
| 73 | Caveman Code Review | NÃO | Revisão de PR de software |
| 74 | Caveman Commit Generator | NÃO | Commits já são feitos sob regra do repositório |
| 75 | Cavecrew Subagent Orchestrator | TALVEZ | Delegar a subagente e receber resumo; item C.11 |
| 76 | Rigor Codebase Auditor | NÃO | Auditoria de código/ML |
| 77 | Grill-Me | SIM (ideia) | Questionar plano antes de gastar; item C.3 |
| 78 | Cucumber BDD | NÃO | Testes de software |
| 79 | k6 Load Testing | NÃO | Testes de carga |
| 80 | Stryker Mutation Testing | NÃO | Testes de software |
| 81 | NotebookLM Bridge | TALVEZ (baixo) | Consulta aos livros; pasta de estudos já cobre |
| 82 | Caveman 75% Token Compression | TALVEZ (cuidado) | Só conversa interna; arruína tom do texto final |
| 83 | Caveman Memory File Compressor | TALVEZ (cuidado) | Risco de perder regra fixa do CLAUDE.md; preferir poda manual |
| 84 | Caveman Context Learner | TALVEZ | Ideia de mover instrução repetida para memória; já fazemos |
| 85 | Caveman Quick Reference | NÃO | Cartão de ajuda |
| 86 | DBS Content Structuring | TALVEZ (baixo) | Organizar acervo de texto; temos `memoria/` e estudos |
| 87 | DBS Agent Workspace Migration | NÃO | Compatibilidade com Codex; só usamos Claude Code |
| 88 | DBS AI Writing Fingerprint Checker | SIM (ideia) | Checar cara de IA nos textos; item C.1 |
| 89 | DBS Consolidated Executive Report | NÃO | Relatório ao Victor já tem formato fixo no CLAUDE.md seção 5 |
| 90 | DBS Execution Psychology Diagnoser | NÃO | Coaching de bloqueio pessoal |
| 91 | RigorPilot AI Research Reproduction | NÃO | Pesquisa de deep learning com GPU |
| 92 | Rigor Explore AI Research | NÃO | Idem |
| 93 | Deep Multi-Source Web Research | TALVEZ | Método de cruzar fontes e citar; chaves pagas |
| 94 | Amazon Product Research | TALVEZ (baixo) | Método para avaliar acessório de afiliado |
| 95 | Agentix Multi-Agent Team CEO | NÃO | Plataforma externa; já temos escala-chefe |
| 96 | Agent Pulse (custo) | SIM (ideia) | Medir gasto de tokens por rodada; item C.9 |
| 97 | Agentspace Live URL | NÃO | Túnel público de pasta; risco de expor arquivos |
| 98 | Gmail Connector | NÃO | Não conectar e-mail do Victor a skill de terceiro |
| 99 | Lark/Feishu | NÃO | Ferramenta corporativa chinesa |
| 100 | Azure Communication Services Voice | NÃO | Telefonia |
Contagem: SIM (escrever versão nossa) = 9 (33, 34, 39, 57, 67, 68, 77, 88, 96); TALVEZ = 17 (21, 29, 32, 35, 41, 45, 48, 50, 70, 75, 81, 82, 83, 84, 86, 93, 94); JÁ TEMOS = 2 (01, 28), mais 6 cobertos por `ui-ux-pro-max` (02 a 10 só em parte); NÃO = o resto, inclusive 2 PROIBIDAS (23 e 25).
