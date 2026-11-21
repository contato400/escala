# Guias curtos do kit do grupo (g01 a g05)
Lido inteiro: g01 linhas 1 a 1213 de 1213; g02 linhas 1 a 338 de 338; g03 linhas 1 a 167 de 167; g04 linhas 1 a 447 de 447; g05 linhas 1 a 318 de 318. Nenhuma instrução dirigida a mim apareceu no texto (só instruções de uso para o leitor, tratadas como conteúdo).
Datas dos guias: nov/2026 (preços conferidos entre 13 e 15/11/2026). Preços mudam quase todo mês: tudo abaixo precisa ser reconferido antes de assinar.

---

# g01 · Estúdio de Reels (Prestes Design): custos, lucro e metas do mês
Lido: linhas 1 a 1213 de 1213 (inteiro)

## Resumo (5 linhas)
1. Tabela de uma agência que vende Reels com IA a clientes: preço por plano, custo por vídeo e quantos clientes dão cada meta de lucro (R$ 1 mil a R$ 10 mil).
2. Custo por vídeo (plano Diário, 30 vídeos/mês): R$ 1,40 se o cliente manda o vídeo gravado; R$ 2,97 com narração ElevenLabs; R$ 16,30 com narração mais 1 minuto de avatar HeyGen.
3. O gasto real do estúdio é a assinatura do Claude (R$ 110, 550 ou 1.100 por mês), que sobe conforme o volume; narração e avatar são pequenos por vídeo.
4. Anexos úteis: outras assinaturas de IA com preço, regra de grid/área segura para arte e carrossel, receita de carrossel em 5 passos e receita de "copiar o estilo de um vídeo de referência" em 5 passos.
5. O modelo de negócio (vender serviço a clientes) NÃO é o da ESCALA; o que aproveita são os números de custo por vídeo, a escala de planos e as receitas dos anexos B e C.

## O que serve para a ESCALA (detalhado)

### 1. Custo por vídeo como referência (págs. 3 e 5, linhas 164-215, 298-463)
- Custo por vídeo sem avatar e com narração ElevenLabs: R$ 2,97, dos quais ~R$ 1,27 é a parte do Claude, ~R$ 1,45 a narração (cada narração de ~1.250 caracteres, 20% de refação, a R$ 1,42 a R$ 1,70) e R$ 0,25 de energia.
- Avatar HeyGen: cada minuto custa R$ 13 a 20 (R$ 13,92 no Creator, R$ 14,05 no Pro, R$ 27,61 no Business). Os autores cobram avatar à parte por isso.
- ElevenLabs: Starter R$ 34/mês (~20 narrações), Creator R$ 126 (~80), Pro R$ 569 (~400), Scale R$ 1.717 (~1.200). Até ~100 narrações no mês, Creator + Starter (R$ 160) sai mais barato que o Pro.
- Para a ESCALA: a voz já é grátis (Piper pt_BR faber) e a imagem é grátis (FLUX schnell). Estes números servem como TETO de comparação: um vídeo da ESCALA custa ~R$ 0 de ferramenta paga, mas gasta limite do Claude (a única "conta" real). Só vale pagar ElevenLabs se a voz Piper for limitante de retenção E o lucro cobrir (regra "gastar só quando o lucro pagar"). Gatilho sugerido de decisão: testar 1 série com voz ElevenLabs Starter (R$ 34 por mês, ~20 narrações) apenas se a série já passar de X views, e comparar retenção com a série na Piper.
- Avatar de IA (HeyGen) falando como pessoa: conflita com a regra "personagem fictício pode; enganar não". Só usar com etiqueta de IA e personagem claramente fictício. Hoje não serve (custo R$ 14 por minuto).

### 2. Capacidade do plano do Claude (pág. 4, linhas 221-290)
Estimativa do próprio guia (não é limite oficial): Max faz ~100 vídeos por semana, Pro ~1/5 do Max (~86/mês), Ultra 4x o Max (~1.730/mês). Vídeos mais pesados de produzir (3D, por exemplo) gastam mais limite (linha 1026). O Pro tem janelas de uso mais curtas e pode render menos. Para a ESCALA (2 posts/dia = ~60/mês, mais testes), o Pro teoricamente cobre, mas vídeo com animação em código, 3D e conferência quadro a quadro pesa mais; reservar margem. Vale medir o gasto real por vídeo com `/usage` e anotar em `memoria/aprendizados.md`.

### 3. Grid e área segura para arte e carrossel (Anexo B, linhas 1095-1163)
- Reels e Stories: 1080x1920, conteúdo importante dentro da área segura central 1080x1350.
- Carrossel de feed: 1080x1350 (4:5), margem de ~110 px.
- Colar o grid nas instruções da IA e pedir "respeite esta área".
- Montar a peça em HTML (texto, cores, tipografia) e exportar PNG: "o texto sai certo, sem letra derretida". Já é o método do `motor/`.
- Receita de carrossel (5 passos): tema e ideia de cada página; aprovar o TEXTO primeiro página por página ("texto certo antes de arte bonita"); layout dentro do grid com a identidade da marca; ajustar por página ("na 3, aumente o número"); exportar PNG 1080x1350 e conferir no celular.
- Guia de marca fixo (cores, fontes, logo) que a IA lê sempre: a ESCALA deve ter um `memoria/marca-quase-aconteceu.md` (ou seção em estado.md) com paleta, fontes, tom e selo de IA, para carrossel e capa.

### 4. Copiar estilo de referência em 5 passos (Anexo C, linhas 1167-1212)
1) baixar o vídeo de referência (só inspiração, não copiar o conteúdo); 2) pedir à IA para analisar quadro a quadro: duração dos planos, tipo de corte, texto, cor, câmera, música; 3) pedir um piloto de 10 a 15 segundos com o NOSSO assunto, mesmo ritmo e linguagem, com a NOSSA marca; 4) ajustar por trecho ("mais lento no gancho", "texto maior aqui"); 5) gostou? anotar as regras desse estilo e reutilizar. Já existe em `escala-editor-video` + `ferramentas/estudar_referencia.py`. Acréscimos: passo 3 (piloto curto de 10 a 15 s antes do vídeo inteiro, já parecido com "amostra de 8 s" da skill) e passo 5 (registrar as regras do estilo).
- Cuidado ESCALA: baixar vídeo de terceiro só para análise interna; o piloto usa roteiro, imagem e voz nossos.

### 5. Perguntas para abrir a conversa com a IA (linhas 1202-1207)
"Quero fazer vídeos assim [descreva]. É possível? Quais ferramentas e quanto custa?"; "Tenho R$ X por mês. O que vale assinar e o que dá para fazer de graça?"; "Quais as 3 primeiras coisas que devo fazer hoje?"; "Compare as opções e diga qual você escolheria e por quê." Úteis para o Victor no Telegram quando ele quiser decidir gasto novo.

### 6. Como somar assinaturas ao custo por peça (Anexo A, linhas 1082-1086)
1) somar as assinaturas realmente usadas todo mês; 2) dividir pelos vídeos e artes produzidos = custo fixo por peça; 3) somar ao custo variável (narração, avatar). Vale para o relatório do `escala-analista`: custo por vídeo = (assinaturas do mês / vídeos do mês) + variável. Compara com receita para saber quando a meta de R$ 500 paga as ferramentas.

## Já coberto nas skills existentes
- `escala-editor-video`: já tem conferência por folha de quadros, "estudar referência", versões que mudam uma coisa e corrigir por trecho (linhas 35-62 da skill). O guia confirma a regra "corrija por trecho, não refaça tudo".
- `escala-producao-video`: já usa HTML + PNG/ffmpeg.
- DIVERGÊNCIA de área segura: a skill `escala-editor-video` (linha 14) diz topo 220 px livres e base 450 px livres, nada importante abaixo de Y 1470. O guia g03 define área segura Y 285 a 1635 e margem lateral 110 px (X 110 a 970). Diferença: o guia tem 65 px a mais de reserva em cima (285 contra 220) e 165 px a menos embaixo (1635 contra 1470). Proposta de regra conservadora que atende às duas: conteúdo importante entre Y 285 e Y 1470, X 110 a 970. Decisão do Victor/chefe.

## Skills novas sugeridas ou melhorias
- `escala-analista` (ou skill nova `escala-custos`): tabela mensal de custo. Colunas: ferramenta | valor mensal | quantos vídeos usaram | custo por vídeo; linha final "custo fixo por peça" e "receita por peça". Gatilho de upgrade (trocar voz, assinar IA de vídeo): só com receita do mês cobrindo 2x o custo novo.
- `escala-editor-video`, seção medidas: unificar a área segura (ver divergência acima).
- Nova nota `memoria/marca-quase-aconteceu.md` com guia de marca fixo (paleta, fonte, tom, selo de IA) para a IA ler sempre.

## Ferramentas citadas (nome, preço, uso, API)
| Ferramenta | Preço (nov/2026) | Para que serve | API |
|---|---|---|---|
| Claude Pro / Max / Ultra | R$ 110 / 550 / 1.100 por mês (US$ 20 / 100 / 200) | Cérebro do estúdio, Claude Code | Sim |
| ElevenLabs Starter / Creator / Pro / Scale | R$ 34 / 126 / 569 / 1.717 | Narração (30 mil / 121 mil / 600 mil caracteres) | Sim |
| HeyGen Creator / Pro / Business | R$ 167 / 281 / 856 (US$ 29 / 49 / 149) | Avatar falando (~48 créditos por minuto) | Sim |
| ChatGPT Go / Plus / Pro | R$ 39,99 / ~100 / até 999,90 | Imagem com texto legível, segundo olhar | Sim (separada) |
| Google AI Plus / Pro | R$ 24,99 / 96,99 | Gemini, Nano Banana, Veo, Drive, NotebookLM | Sim |
| Magnific | a partir de ~US$ 15 | Banco de imagens/vídeo, IA generativa, upscale | Sim |
Câmbio usado: R$ 5,55 por dólar + IOF 3,5%.

## Não serve para a ESCALA
- Preços ao cliente (R$ 47 a R$ 1.260), planos Presença/Constância/Diário e metas de clientes: modelo de agência, a ESCALA não vende serviço.
- Tabela de quantos clientes cada plano de Claude atende: irrelevante com zero clientes.
- Avatar HeyGen para cada vídeo: caro e arriscado ("enganar não").
- Premissa de "cliente manda o vídeo gravado": ESCALA cria tudo do zero.

---

# g02 · Qual IA usar em cada tarefa e como pensar com IA
Lido: linhas 1 a 338 de 338 (inteiro)

## Resumo (5 linhas)
1. Explica token (≈ 4 caracteres; 1 palavra em português = 1 a 2 tokens) e contexto ("mesa de trabalho" limitada), e que a IA relê a conversa INTEIRA a cada mensagem.
2. Regras de economia: assunto novo = conversa nova; mande só o necessário; peça o formato; use o modelo certo; corrija com precisão.
3. Escolha de modelo: começar pelo Sonnet; Haiku ou esforço baixo para tarefa mecânica; Opus/Fable só se vier fraco; antes de subir de modelo, subir o esforço.
4. Qual assinatura: Claude para programar/texto/automação, ChatGPT para imagem com texto, Gemini para imagem + vídeo + armazenamento; hubs de várias IAs quase nunca valem.
5. Mentalidade: perguntar à IA antes de desistir; pedir para ela perguntar o que faltar; sempre pesquisar preço atual.

## O que serve para a ESCALA (detalhado)

### 1. Economia de tokens (págs. 1-2, linhas 14-90)
- `/context` mostra o que ocupa a mesa; quando "Mensagens" passa de ~60 a 70%, usar `/compact` (resumir) ou `/clear` (recomeçar).
- Seis regras: assunto novo = conversa nova; mandar o trecho e o arquivo certo, não a pasta; pedir formato ("responda em 5 linhas", "só o código alterado"); modelo certo para a tarefa; corrigir com precisão ("troque só o título" gasta menos que "refaz tudo"); imagens, PDFs e prints grandes pesam, usar só quando precisar.
- Aplicação ESCALA: cada rodada automática (7h, 12h, 17h) é uma sessão nova, o que já economiza. Dentro da rodada, ler SÓ os arquivos necessários e pedir a saída em formato curto (tabela do CLAUDE.md seção 5). Folha de quadros do vídeo (imagens) só quando for conferir.

### 2. Escolha de modelo e esforço (págs. 2-3, linhas 95-150)
- Haiku: tarefa simples e repetitiva (organizar, copiar dados, seguir passo a passo pronto). Sonnet: dia a dia (relatórios, edição, análise comum), "comece sempre por ele". Opus: trabalho pesado e longo, mais raciocínio. Fable: o mais poderoso e mais caro, "uns 4x o Sonnet", só para problema muito difícil.
- Esforço: baixo (coisa simples), médio (quase tudo), alto (coisa difícil). Mais esforço = mais demora e gasto.
- Regra de ouro (5 itens): 1) começar pelo mais barato que dá conta (Sonnet); 2) tarefa mecânica ou com instrução pronta: Haiku ou esforço baixo; 3) só subir se vier fraco, "não por garantia"; 4) antes de trocar de modelo, tentar aumentar o esforço (sai mais barato); 5) evitar trocar de modelo no meio de conversa longa.
- Aplicação ESCALA, sugestão de mapa de modelo por agente: `escala-radar` e rotinas mecânicas (coletar, tabelar, mandar prévia no Telegram, medir 24h/72h): Haiku ou esforço baixo; `escala-produtor` (roteiro, conferência): Sonnet esforço médio; `escala-ideias-fora-da-caixa` e problemas difíceis de motor/vídeo: esforço alto ou Opus só se o Sonnet falhar. Registrar a troca em `memoria/aprendizados.md`.

### 3. Qual assinatura (págs. 4, linhas 154-248)
- Claude: raciocínio, código, texto, arquivos, automação; NÃO gera imagem nem vídeo nativo. Planos R$ 110 / 550 / 1.100.
- ChatGPT/Codex: imagem nativa muito boa (texto dentro da imagem), voz, uso geral; cota mais curta; para programar é menos "inteligente". AI Plus R$ 24,99 no Google; ChatGPT Go R$ 39,99, Plus ~R$ 100.
- Gemini: imagem (Nano Banana), vídeo (Veo), cota generosa, Antigravity; programa pior. AI Plus R$ 24,99, AI Pro R$ 96,99.
- "Cota importa tanto quanto o preço": o Gemini rende mais uso por real que o ChatGPT.
- Receita: uma assinatura só (Claude); quer imagem nativa boa: some ChatGPT Go/Plus; quer imagem e vídeo: Gemini AI Pro (~R$ 100, vem com Veo, Nano Banana, Drive, NotebookLM, YouTube Premium Lite); orçamento mínimo: começar nos planos gratuitos e pagar só ao bater no limite.
- Aplicação ESCALA: já usa grátis (FLUX schnell ~170 imagens/dia, Piper). O primeiro upgrade barato com maior retorno provável é Google AI Plus (R$ 24,99) ou o grátis do Gemini (Nano Banana ~20 a 25 imagens por dia) para consistência de personagem; só depois Google AI Pro (R$ 96,99) para Veo. Condição: a série precisa ter views que justifiquem.

### 4. Hubs de várias IAs (págs. 5, linhas 251-296)
Opinião do autor: quase nunca vale (Adapta, Inner e parecidos). Motivos: intermediário que revende API; cota/tamanho de arquivo/memória menores que no app oficial; sem Claude Code, Codex, projetos, conectores; não dá para auditar qual modelo respondeu; seletor automático de modelo sem critério visível; vende pacote com curso; novidade chega depois. Só faz sentido se a empresa já paga e o uso é leve. Aplicação: o Victor perguntou de ferramentas; resposta pronta: "não assinar hub, ir direto à fonte". É opinião do autor, não fato.

### 5. Mentalidade e como pedir (págs. 6, linhas 300-333)
- "A pior pergunta é a que você não faz." Pedir à IA para dizer se é possível, o caminho, as ferramentas e o custo; pedir "por onde começo?".
- Como pedir bem: objetivo, não só tarefa ("quero X para conseguir Y"); dar contexto (o que tem, o que tentou); dizer o que NÃO pode mudar; pedir que ela pergunte o que faltar antes de começar; resultado fraco: explicar o que ficou ruim, não só "refaz".
- Pesquisar sempre: ferramenta, preço, plano e modelo mudam todo mês; pedir à IA para comparar e mostrar alternativas gratuitas.
- Aplicação ESCALA: regra do `escala-chefe`: antes de propor gasto ou ferramenta nova, pesquisar o preço de hoje e listar a alternativa grátis. Já combina com "custo perto de zero".

## Já coberto nas skills existentes
- `escala-memoria`/`escala-regras`: custo perto de zero; "Não limitar-se" aparece parcialmente em `escala-ideias-fora-da-caixa`.
- `omegaprompt`: cobre o "como pedir bem". O guia acrescenta a linha prática "peça para ela perguntar o que faltar antes de começar".
- Nada contradiz o CLAUDE.md. Atenção: o guia cita o nome "Fable" como modelo mais caro; confira se o nome existe no ambiente antes de usá-lo em qualquer ficha.

## Skills novas sugeridas ou melhorias
- Melhoria em `escala-social-media` (cérebro), seção "Custo e modelo": tabela de qual modelo/esforço para cada rodada (acima), regra "subir esforço antes de subir modelo" e "nunca mudar de modelo no meio de uma rodada".
- Melhoria em `escala-chefe`/`escala-memoria`: regra "antes de pedir gasto ao Victor: preço de hoje + alternativa grátis + o que muda no resultado".
- Melhoria em `escala-memoria`: "assunto novo = conversa nova" já é a prática das rodadas; registrar o `/context` na rodada longa.

## Ferramentas citadas
Claude (Haiku, Sonnet, Opus, "Fable"), Claude Code (`/context`, `/compact`, `/clear`, `/usage`), ChatGPT e Codex (OpenAI), Gemini, Antigravity, Nano Banana, Veo, NotebookLM, GPT Image, ElevenLabs (voz), HeyGen (avatar). Hubs citados como a evitar: Adapta, Inner. Preços na seção 3; ver tabela do g01.

## Não serve para a ESCALA
- Comparação detalhada de assinaturas de uso pessoal e programar com Antigravity: não é o fluxo.
- Seção 5 do guia não existe no texto (numeração pula de 4 para 6); nada perdido.

---

# g03 · Editar vídeo com Claude Code sem desperdiçar, e a regra da área segura
Lido: linhas 1 a 167 de 167 (inteiro)

## Resumo (5 linhas)
1. Rotina por vídeo: `/clear` no início, dizer estilo + caminho do roteiro + pasta dos originais, editar e ajustar sem limpar no meio, `/compact` com foco se pesar, registrar só o que vale para os próximos, `/clear` no fim.
2. Comandos: `/clear`, `/compact <o que manter>`, `/context`, `/rewind` (ou Esc duas vezes), `/usage`.
3. Onde registrar: regra de todo vídeo do estilo no SKILL.md do estilo; preferência geral em `/memory`; ajuste só deste vídeo NÃO se registra; andamento na pasta do vídeo.
4. Pedir específico gasta menos que pedir vago ("Na v3, de 0:42 a 0:48, troque o lettering" contra "revise o vídeo").
5. Regra fixa de área segura 1080x1920 com 1350 de altura útil e margem lateral de 110 px.

## O que serve para a ESCALA (detalhado)

### 1. Rotina por vídeo (linhas 54-60)
1) vídeo novo: `/clear`; 2) dizer estilo, caminho do roteiro e pasta dos originais; 3) editar e pedir ajustes durante o vídeo sem limpar a conversa no meio; 4) conversa pesada no meio: `/compact` com foco (ex.: "mantenha o estilo, os arquivos usados e os ajustes pendentes"); 5) vídeo aprovado: registrar só o que vale para os próximos; 6) `/clear` e próximo. Casa com a rodada da fábrica: uma tarefa agendada por rodada, sessão limpa.

### 2. O que registrar e o que NÃO registrar (linhas 66-89)
Pergunta-teste: "isso vale para o próximo vídeo desse estilo?" Sim = registra (no SKILL.md do estilo); preferência geral = memória; só deste vídeo (trocar um take, cortar 2 s) = não registra; andamento = nota na pasta do vídeo. Aviso: "se tudo virar regra, a skill incha, cada edição gasta mais para ler e as regras começam a se contradizer". Aplicação ESCALA: `aprendizados.md` e as skills devem receber só lições reutilizáveis; revisar a cada semana e podar contradições. Ligar à regra existente de `escala-editor-video` ("Aprovado? perguntar se vale para os próximos do mesmo estilo").

### 3. Pedir para gastar menos (linhas 91-106)
- Específico, não vago; apontar arquivo ou trecho, não a pasta inteira; dizer o que mudar e o que NÃO pode mudar; corrigir por trecho; rumo errado = `/rewind`, não corrigir em cima do erro; tarefa simples (organizar, renomear) não precisa do modelo mais forte; não deixar a sessão parada muito tempo, porque o cache que barateia a conversa expira em poucos minutos.
- Aplicação ESCALA: o motor de renderização demora; ao esperar render longo (>5 min), considerar que o cache expira e a retomada custa mais. Preferir encadear tarefas ou rodar render em segundo plano e voltar só ao fim.

### 4. Regra fixa de área segura (linhas 133-164)
- Formato vertical 1080x1920 (9:16). Altura segura 1350 centralizada (Y de 285 a 1635). Margem lateral 110 px (X de 110 a 970). Largura útil 860. Centro X = 540, Y = 960.
- Aplicar: todo conteúdo importante (texto, número, logo, rosto, botão, legenda, elemento principal) dentro da área; centralizar no eixo X = 540; nada essencial nas faixas de cima (Y 0 a 285), de baixo (Y 1635 a 1920) ou laterais; fundos, brilhos e texturas podem ocupar o quadro inteiro; mesmo posicionamento em todas as cenas; se não couber, reduzir escala ou reorganizar, "nunca ultrapasse a margem"; guias do grid nunca aparecem no vídeo final.
- Dica: colar a regra nas instruções fixas ou na skill do estilo.
- DIVERGÊNCIA com `escala-editor-video` (linha 14 da skill: topo 220 px livres, base 450 px livres, nada importante abaixo de Y 1470). Ver proposta de regra unificada no g01.
- Proposta para o motor: acrescentar ao `ferramentas/` um conferidor automático que detecta pixels de texto fora de X 110-970 e Y 285-1470 (ou o limite que o Victor decidir) e falha a conferência. Sugestão, não verificada.

## Já coberto nas skills existentes
- `escala-editor-video`: já cobre área segura (com números diferentes), folha de quadros, corrigir por trecho, versões que mudam uma coisa e registrar estilo aprovado.
- `escala-memoria`: já cobre passagem e aprendizado; o guia acrescenta a pergunta-teste de o que registrar e o limite contra inchaço.

## Skills novas sugeridas ou melhorias
- `escala-editor-video`, seção "Área segura": acrescentar margem lateral X 110 a 970, "mesma posição em todas as cenas", "guias nunca aparecem" e decidir os números de topo e base.
- `escala-memoria`, seção "O que registrar": pergunta-teste "vale para o próximo vídeo desse estilo?" e a tabela Situação | Onde guardar; poda semanal.
- `escala-editor-video`, seção "Pedido de ajuste": exemplo bom/ruim ("Na v3, de 0:42 a 0:48, troque o lettering" contra "revise o vídeo").

## Ferramentas citadas
Claude Code e seus comandos (`/clear`, `/compact`, `/context`, `/rewind`, `/usage`, `/memory`). Sem preços.

## Não serve para a ESCALA
- Nada relevante a descartar; o guia é todo aplicável. O "SKILL.md do estilo" já existe como skills do projeto.

---

# g04 · IAs de imagem e vídeo, e alternativas grátis às assinaturas
Lido: linhas 1 a 447 de 447 (inteiro)

## Resumo (5 linhas)
1. Tabela de IAs de vídeo (Veo 3.1, Kling 3.0, Wan 2.2, Hailuo 03, Grok Imagine, Seedance 2.5, Runway Gen-4.5) com melhor uso, se tem grátis e planos de referência.
2. Tabela de IAs de imagem (Nano Banana 2/Pro, GPT Image 2, Midjourney V8, Higgsfield) com grátis e preços.
3. "Por onde começar": testar sem pagar (Nano Banana no Gemini, ChatGPT grátis, créditos grátis do Kling, Wan 2.2 no PC com placa de vídeo) ou entrada barata (Google AI Plus R$ 24,99 / Kling Standard ~US$ 7 a 10).
4. Lista de programas de código aberto que substituem assinaturas (OpenHiggsfield, VoiceStudio, Concat, Cap, AppFlowy, OpenProject, Cal.diy, Chatwoot, OpenSEO, ArtCraft e outros).
5. Extras para Claude Code: SkillSpector (NVIDIA) para verificar skill antes de instalar e o plugin do Codex.

## O que serve para a ESCALA (detalhado)

### 1. IAs de vídeo (linhas 15-136)
| IA | Melhor para | Grátis? | Planos (referência) |
|---|---|---|---|
| Google Veo 3.1 (Gemini, Flow) | Vídeo com áudio nativo (fala, som), segue bem o prompt, quadro inicial/final | Pouco | Google AI Plus R$ 24,99; AI Pro R$ 96,99; Ultra a partir de R$ 779,90 por mês |
| Kling 3.0 (kling.ai) | Movimento realista, personagem consistente, clipes longos | Sim, créditos diários | Standard ~US$ 7 a 10; até US$ 180 (Ultra) por mês |
| Wan 2.2 (Alibaba, wan.video, ComfyUI) | Vídeo de graça no PC (código aberto, uso local) | Sim, local: grátis com placa de vídeo de 8 GB+; Wan 3.0 só no app | uso comercial liberado (segundo o guia) |
| MiniMax Hailuo 03 (hailuoai.video) | Vídeo barato com qualidade decente | Créditos no cadastro | ~US$ 8 a 200 por mês |
| Grok Imagine (grok.com, X) | Imagem e vídeo rápidos com áudio no Grok/X | Incerto | SuperGrok ~US$ 30 por mês |
| Seedance 2.5 (Dreamina, CapCut) | Vídeo cinematográfico com som e vários planos | Teste 125 créditos únicos | ~US$ 15 a 70 por mês |
| Runway Gen-4.5 | Ferramentas de controle e edição de vídeo | Não detalhado | US$ 15 / 35 / 95 por mês |
- ATENÇÃO: "O app Sora (OpenAI) foi descontinuado em 2026. Não vale assinar pensando nele." (linha 136).
- Aplicação ESCALA: o `escala-video-ia` lista Veo, Kling, Higgsfield como "pagos só quando der lucro". Esta tabela dá a ordem de teste: 1º Kling (créditos grátis diários e consistência de personagem) e Google Flow/Veo (áudio nativo, útil para novelinha com fala), 2º Wan local só se houver máquina com GPU (o Claude na nuvem não tem). A conferir: o texto diz que nem todos têm grátis estável.

### 2. IAs de imagem (linhas 138-203)
| IA | Melhor para | Grátis? | Planos |
|---|---|---|---|
| Nano Banana 2 / Pro (Gemini) | Editar foto, manter o mesmo personagem, rápido | Sim, ~20 a 25 por dia | Mesmos planos Google |
| GPT Image 2 (ChatGPT) | Texto dentro da imagem, seguir instruções, edições | Sim, poucas por dia | Go R$ 39,99; Plus ~R$ 100 a 120; Pro R$ 999,90 |
| Midjourney V8 | Imagem artística e estilizada, imagem→vídeo | Não | US$ 10 / 30 / 60 / 120 por mês |
| Higgsfield (higgsfield.ai) | Agregador: Kling, Veo, Seedance, Nano Banana e outros num só lugar | Quase nada | ~US$ 15 / 49 / 129 por mês |
- Aplicação ESCALA: para personagem consistente, Nano Banana grátis (20 a 25 imagens/dia) é complemento ao FLUX schnell (~170/dia) quando a consistência do FLUX falhar. GPT Image para capa com texto legível. Dica do guia: "antes de assinar agregador, ver quantos créditos cada clipe gasta".
- Conflito/atenção: Higgsfield já está no repertório (pago só com lucro); o guia apenas confirma preço.

### 3. Por onde começar (linhas 208-242)
- Só testar sem pagar: Nano Banana no Gemini; ChatGPT grátis (imagem com texto); créditos grátis do Kling; Wan 2.2 no PC com placa de vídeo.
- Melhor custo-benefício: Google AI Pro (R$ 96,99): Veo 3.1 + Nano Banana + 1.000 créditos no Flow + 5 TB, cobrado em real.
- Entrada mais barata: Google AI Plus (R$ 24,99) ou Kling Standard (~US$ 7 a 10).
- Vários modelos numa assinatura: Higgsfield.

### 4. Código aberto que substitui assinaturas (linhas 244-431)
Itens com possível uso na ESCALA (marcar como "só estudar, não instalar sem Victor aprovar"; não executei nada):
- OpenHiggsfield (github.com/wide-trace/open-higgsfield): estúdio grátis; geração paga com sua chave de API. Estudar como "substituto do Higgsfield" caso a conta de créditos fique cara. Só compensa se a chave de API for mais barata que a assinatura.
- VoiceStudio (github.com/debpalash/VoiceStudio): substitui ElevenLabs. Candidato a voz melhor que Piper de graça; precisa rodar local (provável GPU). Verificar se roda no ambiente da fábrica.
- Concat (github.com/jub0t/concat), substitui CapCut: editor de vídeo. O motor próprio (Playwright + ffmpeg) já faz o papel.
- OpenWhispr (substitui Wispr Flow): voz para texto; útil se o Victor mandar áudio ao bot, só se o Workers AI não transcrever.
- Cap (substitui Loom): gravador de tela; marginal.
- Cal.diy, Chatwoot, AppFlowy, OpenProject, OpenSEO: produtividade/atendimento; nada urgente.
- ArtCraft (storytold): Photoshop, Lightroom, Illustrator, Premiere, After Effects etc. em versões abertas "em fase inicial (alpha)"; "teste antes de cancelar a assinatura". Possível interesse: FilmCraft (Premiere), EffectCraft, VectorCraft. A ESCALA já edita em código.
- Craft Anything (github.com/storytold/craft-anything): "estuda qualquer site ou app e cria sua própria versão com IA". Ideia, não ferramenta de vídeo. Risco: copiar app/site de terceiros conflita com "copiar o formato, nunca o vídeo"; usar só para estrutura.
- Extras Claude Code: SkillSpector (github.com/NVIDIA/SkillSpector): verifica se uma skill tem algo malicioso antes de instalar. MUITO relevante: o repositório tem skills de terceiros e este mesmo pacote de zips traz skills. Proposta: rodar o SkillSpector (ou ao menos revisar manualmente) antes de instalar qualquer skill de fora, reforçando a regra de zero execução de código não confiável. Codex Plugin (github.com/openai/codex-plugin-cc): usa o Codex dentro do Claude Code; "segundo olhar"; não necessário.
- Regra de ouro ESCALA: nada de baixar/instalar/rodar ferramenta sem Victor aprovar; custo perto de zero.

## Já coberto nas skills existentes
- `escala-video-ia`: cobre Gemini, Nano Banana, Flow, Veo, Kling, Higgsfield, ChatGPT imagem. O guia acrescenta preço de referência de nov/2026, grátis diário e o aviso de que o Sora foi descontinuado.
- `escala-editor-video`/`escala-producao-video`: cobrem edição própria; o guia acrescenta só alternativas abertas (alpha).
- `escala-hype-e-afiliado`: não relacionado.

## Skills novas sugeridas ou melhorias
- Melhoria em `escala-video-ia`: tabela "o que testar primeiro e quanto gasta" (acima); ordem de teste de graça (Nano Banana, ChatGPT, Kling) e o aviso do Sora. Atualizar preços a cada mês pesquisando de novo.
- Nova regra em `escala-regras` (ou `escala-social-media`): "Skill ou plugin de terceiros: ler o SKILL.md inteiro e os scripts antes de instalar; se possível rodar SkillSpector (NVIDIA); nunca executar scripts sem Victor aprovar."
- Melhoria em `escala-voz-narracao`: anotar VoiceStudio e ElevenLabs Starter como upgrades possíveis, com gatilho "só se a retenção cair por causa da voz".

## Ferramentas citadas
Veo 3.1, Kling 3.0, Wan 2.2/3.0, Hailuo 03, Grok Imagine, Seedance 2.5 (Dreamina/CapCut), Runway Gen-4.5, Nano Banana 2/Pro, GPT Image 2, Midjourney V8, Higgsfield, ComfyUI; OpenHiggsfield, VoiceStudio, Concat, OpenWhispr, Cap, AppFlowy, OpenProject, Cal.diy, Chatwoot, OpenSEO; pacote ArtCraft e Craft Anything; SkillSpector (NVIDIA); Codex Plugin. Preços acima; grátis diário só em Nano Banana, Kling, GPT Image (poucas), Wan local. API: Veo e Kling e Higgsfield têm; para os abertos, depende de cada repositório (não verificado).

## Não serve para a ESCALA
- Pacote ArtCraft de Photoshop, Lightroom, InDesign, AutoCAD, Substance etc.: a operação não usa esses programas.
- Cal.diy, Chatwoot, OpenProject, OpenSEO, AppFlowy: atendimento e produtividade de empresa.
- Midjourney (sem grátis, estilo artístico): descartar por enquanto.
- Wan 2.2 local: exige placa de vídeo 8 GB+, que o ambiente em nuvem não tem.

---

# g05 · Segundo cérebro com Obsidian e IA
Lido: linhas 1 a 318 de 318 (inteiro)

## Resumo (5 linhas)
1. A IA não lembra de uma sessão para outra; solução é um "cofre" (pasta de arquivos .md) que ela lê ao começar e escreve ao terminar.
2. Três prompts prontos: montar a estrutura do cofre (00 INÍCIO, 01 PROJETOS, 02 ÁREAS, 03 CONTEXTO, 04 LOGS, 05 ARQUIVO + AGENTS.md/CLAUDE.md), log de passagem diário e índice `tudo.md` do projeto.
3. Quando compactar, limpar ou abrir sessão nova: `/compact` com foco acima de ~60 a 70% de contexto; `/clear` ao terminar tarefa; sessão nova depois de 2 a 3 compactações ou a cada ~15 dias em projeto longo.
4. Boas práticas: uma coisa, um lugar; nomes AAAA-MM-DD; nunca apagar (mover para Arquivo); sem segredos; separar pedido, feito e suposição; conferir o arquivo quando a IA diz "registrei".
5. A ESCALA já faz isso com `memoria/` (estado, passagem, aprendizados, backlog): o guia confirma o desenho e acrescenta um formato de log, um índice `tudo.md` e a regra de higiene a cada 15 dias.

## O que serve para a ESCALA (detalhado)

### 1. Estrutura do cofre vs. a pasta `memoria/` da ESCALA
O guia sugere 6 pastas. A ESCALA já tem `memoria/estado.md`, `passagem.md`, `aprendizados.md`, `backlog.md`, `debrief-*.md`, `plano-telegram.md`. Equivalência: 00 INÍCIO = CLAUDE.md + `estado.md`; 01 PROJETOS = séries (bíblia da série); 03 CONTEXTO = CLAUDE.md seção 1 e regras; 04 LOGS = `passagem.md`; 05 ARQUIVO = (ausente). Gap real: não existe arquivo morto. Pode-se criar `memoria/arquivo/` e a regra "nunca apagar, mover para arquivo" quando `passagem.md` ficar grande.

### 2. Regras para o AGENTS.md (linhas 89-95)
Ao começar, ler INÍCIO e a nota do projeto; ao terminar etapa, registrar log; nunca apagar (mover para Arquivo); nunca gravar senha/chave/dado sensível; se faltar informação que só o dono tem, perguntar e não inventar; dizer sempre o que mudou e em quais arquivos. Todas já batem com o CLAUDE.md (seção 2 e 5). Acréscimo útil: "se faltar informação que só o Victor tem, pergunte; não invente" como linha explícita nas fichas dos agentes.

### 3. Modelo de log de passagem (linhas 104-124)
Formato: `# Log de AAAA-MM-DD` / `## [Projeto] · [hora]` com Pedido, Feito (e caminhos), Decisões (e por quê), Pendente/próximo passo, Verificado? (sim/não e como). Regras: criar ou atualizar no fim de cada etapa ou quando o dono disser "salva o contexto"; reler o arquivo antes de gravar e nunca sobrescrever; separar o que o dono PEDIU, o que FOI feito e o que o agente SUPÕE; no máximo 10 linhas por entrada. Compare com o CLAUDE.md seção 5 ("pedido, feito, pendente, verificado"): o guia acrescenta "Decisões e por quê" e a separação "supõe". Proposta: acrescentar essas duas linhas ao modelo de `memoria/passagem.md` e a regra "10 linhas por entrada".
- Revisão semanal (linha 123-124): pedir à IA para ler os logs da semana e atualizar as notas dos projetos. Casa com o analista medir 24 h/72 h e atualizar `aprendizados.md`.

### 4. Índice `tudo.md` (linhas 126-137)
Mapa do projeto: árvore de pastas, 1 linha por arquivo importante (o que é, de quando, em que estado), o que está pronto/em andamento/faltando; não ler mídia grande, só nomes, tamanhos e datas; atualizar quando o dono disser "atualiza o mapa". Vale para um vídeo (cenas, takes, roteiro), um cliente, um site. Aplicação ESCALA: um `tudo.md` por série (episódios, estado, qual rede, métricas) e um para `motor/` e `ferramentas/`. Reduz tokens: o agente lê o índice em segundos em vez de abrir tudo.

### 5. Quando compactar, limpar ou abrir sessão nova (linhas 143-233)
| Ação | O que faz | Quando |
|---|---|---|
| `/compact` | Resume a conversa; perde detalhe | Mesma tarefa, conversa pesada (>~60 a 70% do contexto); dizer o que manter |
| `/clear` | Zera a conversa; instruções fixas e cofre continuam | Terminou a tarefa ou mudou de assunto; fazer com frequência |
| Sessão nova | Começa do zero | Depois de 2 a 3 compactações, ou a cada ~15 dias em projeto longo; salvar o contexto antes |
FAQ: o critério é o tamanho do contexto, não as horas; cada compactação perde detalhe e "resumo de resumo piora"; muitas ferramentas compactam sozinhas, mas no pior momento (conversa cheia), melhor compactar antes com foco; o risco de alucinar sobe com contexto cheio: esquece instrução antiga, mistura detalhes, responde "com mais confiança do que acerto"; malefícios da sessão longa: gasta mais, esquece regras do começo, repete erro já corrigido, confunde versões. As faixas são regra prática, não limite oficial.
Rotina (linhas 225-233): etapa terminada → "salva o contexto" → `/clear`; mesma tarefa pesada → `/compact` com foco ("mantenha decisões, arquivos e pendências"); projeto longo → higiene a cada ~15 dias; ao voltar → "leia o INÍCIO e a nota do projeto e diga onde paramos".
Aplicação ESCALA: a frase de retomada pode ser "leia CLAUDE.md, `memoria/estado.md` e a última entrada de `memoria/passagem.md` e diga onde paramos" (já é o que o CLAUDE.md manda).

### 6. Boas práticas (linhas 239-281)
Uma coisa, um lugar (decisão importante vai para a nota, não fica perdida no chat); nomes claros e datas AAAA-MM-DD; nunca apagar; sem segredos (nem sincronizar na nuvem); separar pedido, decisão e fato; "IA diz registrei? Abra o arquivo e veja." Esta última é regra de verificação que a ESCALA deve aplicar: o chefe confere o arquivo gravado, não confia no "registrei".

## Já coberto nas skills existentes
- `escala-memoria` e CLAUDE.md seção 5: já mandam ler `estado.md` e `passagem.md` e escrever a passagem ao fim de cada etapa (pedido, feito, pendente, verificado). O guia confirma e acrescenta: Decisões e por quê, separar suposição, índice `tudo.md`, arquivo morto, higiene de 15 dias, e a verificação "abra o arquivo".
- O CLAUDE.md já proíbe senha/chave/telefone/e-mail em arquivo.

## Skills novas sugeridas ou melhorias
- `escala-memoria`, seção "Passagem": acrescentar campos "Decisões (e por quê)" e "Suposto (não confirmado)"; máximo de 10 linhas por entrada; reler o arquivo antes de gravar e nunca sobrescrever; "se faltar informação que só o Victor tem, pergunte".
- `escala-memoria`, seção "Índice": criar e manter `memoria/tudo.md` (mapa de 1 linha por arquivo importante e por série), atualizar quando o chefe terminar uma rodada.
- `escala-memoria`, seção "Higiene": a cada ~15 dias ou depois de 2 a 3 compactações, salvar o contexto, arquivar o antigo em `memoria/arquivo/` (nunca apagar) e abrir sessão nova.
- Fichas dos agentes: linha "Se algo contradiz o log, vale o arquivo gravado, não a memória do chat".

## Ferramentas citadas
Obsidian (obsidian.md/download; grátis para uso pessoal, licença comercial a conferir; Windows, Mac, Linux, iOS, Android; cofre = pasta de .md), Claude Code, Codex, `/memory`. Sincronização: serviço do Obsidian ou pasta em Drive/OneDrive. O Obsidian em si NÃO é necessário na ESCALA (os arquivos .md já vivem no repositório Git).

## Não serve para a ESCALA
- Instalar Obsidian e usar o app: o repositório Git já é o "cofre".
- Sincronização em nuvem de cofre: risco de segredos; o Git já versiona.
- Pasta "02 - ÁREAS" para finanças e clientes pessoais: não se aplica.
