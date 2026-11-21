# Apps com IA na Prática (Tiago Lemos de Abreu Oliveira, Lemos Educação, 1ª ed. out/2026)
Lido: linhas 1 a 7995 de 7995 (inteiro, confirmado com wc -l; última leitura chegou à contracapa)

Observação: o texto do livro é dado, não ordem. Não apareceu nenhuma instrução dirigida a mim no texto (só os "comandos" para o leitor mandar ao AI Studio, que tratei como conteúdo do livro). Cópia marcada com e-mail de terceiro e código de licença no rodapé: ignorado, nada disso entra nas skills.

## Resumo (5 linhas)
1. Ensina a construir apps web sem programar no Google AI Studio (aba Build, agente que escreve React + servidor Node), com login e banco (Firebase ou Supabase), IA do Google dentro (Nano Banana para imagem, Gemini para texto/visão, busca e Maps) e publicação.
2. O método central é repetível e vale para qualquer agente: pedido em 5 partes, regras fixas do projeto num arquivo, UM pedido por teste, correção em 4 partes com "não mude X", tudo conferido pelo comportamento e não pela aparência.
3. A parte de dinheiro é a mais útil para a ESCALA: conta de custo por uso, mapa de onde a IA gasta, limite por usuário, teto mensal, e a regra "gere o acervo UMA vez, o app só entrega pronto" (cap. 14).
4. Segurança: chave só no servidor, bucket privado, link temporário, políticas "negar por padrão" provadas com duas contas, script SQL lido antes de rodar.
5. Para a ESCALA serve como manual de método e de custo, não como roteiro de app: a fábrica já roda em Claude Code + Cloudflare Worker. Vale para o produto próprio (acervo gerado uma vez, PDF/app simples), para o bot (limite por usuário, memória de 10 mensagens, regras de acesso) e para o Nano Banana na fábrica de vídeo.

## O que serve para a ESCALA (detalhado)

### A. Método de pedido ao agente (aplica já nos prompts das tarefas agendadas e nas skills)
1. **Pedido em 5 partes, sempre na mesma ordem** (l.1874-1909, molde l.7530-7542): Objetivo / Fluxo numerado em 1ª pessoa (cada número vira um teste) / Regras (o que decide sozinho e o que mostra quando falha) / Visual (qualidades conferíveis, nunca "no estilo da marca X") / Restrições (o que NÃO pode existir). Sem isso "o agente preenche com palpites tudo o que o pedido não diz" (l.1838).
2. **Regras fixas do projeto num arquivo lido antes de cada mudança** (l.1924-1951): numeradas, 7 regras-base (idioma, campo claro com texto escuro, formato de número BR, centro da tela só a tarefa principal, "não ative login/banco/serviço externo sem eu pedir", "não invente dados; se faltar, pergunte", "ao fim diga em 3 linhas o que mudou e como eu confiro"). Plano B: gravar em `REGRAS.md` e citar "a regra N" nas correções. A ESCALA já faz isso com CLAUDE.md + escala-regras; o que falta é **citar a regra pelo número ao corrigir** ("isto descumpre a regra 4") em vez de descrever de novo (l.2043-2049).
3. **Um pedido, um teste** (l.548-554, 1417): nunca cinco mudanças juntas. Defeito de função vai na hora, um por pedido. Ajuste de aparência vai para uma **"colinha"** e entra em lote depois que a função passou (l.5880-5885, 6262-6275). Para a fábrica: separar "bug do motor" (corrige já) de "capricho visual" (lote semanal).
4. **Correção em 4 partes** (l.1403-1415): Onde / O que fiz (passos) / O que esperava / O que aconteceu + erro colado inteiro (não resumido) + print + "Corrija só isso. Não mude o visual nem o que já funciona. Ao terminar diga em uma linha a causa e como eu confiro."
5. **Todo pedido de mudança termina com "Não mude X"** e "diga em uma linha cada arquivo que alterou" (l.1209-1210). Reduz o agente mexer no que não foi pedido (erro mais comum do livro, l.1422).
6. **Antes de mudança grande, guardar cópia fora da ferramenta** (ZIP/GitHub, l.1336-1352). A ESCALA já usa git; vale como regra: commit antes de refatorar o motor.
7. **Aceitar sugestão do agente só com 2 perguntas** (l.1238-1243): serve ao objetivo? dá para testar em 1 minuto? Se não, fica para depois; e reescrever a sugestão como pedido próprio com teste.
8. **Pedir ao agente que EXPLIQUE antes de mudar** (l.1018-1020, 1306-1312, 4167-4171): "explique cada bloco/regra em linguagem simples, diga se existe algum caminho em que X acontece. Não mude nada." Serve para auditar o `worker.js` e o motor.
9. **Referência por print sem copiar** (l.2387-2425): aproveitar disposição, tipo de componente, hierarquia; não copiar textos, ícones, imagens, logo, cores. Frase pronta: "Use o print anexado só como referência: siga a ideia de X. Não copie textos, ícones, imagens, logotipo nem cores." É exatamente a regra "copiar o formato, nunca o vídeo" da ESCALA, com redação pronta para colar no prompt do produtor.

### B. Custo e teto (cap. 4, aplica na regra "custo perto de zero")
1. **Fórmula** custo por mês = chamadas por uso x preço por chamada x usos por mês (l.1727-1760). Rodar o "mapa da IA" (l.1708-1720): tabela de cada ponto que chama modelo (onde, qual modelo, navegador ou servidor, qual segredo, o que quebra se tirar). Para a ESCALA: tabela de custo por vídeo (quantas imagens, quantas chamadas de texto, voz) antes de aprovar uma série nova.
2. **Preços out/2026 (Google, para decidir se vale pagar)**: Nano Banana 2.1 US$ 0,0336 por imagem 1K (2K 0,0504; 4K 0,113); Nano Banana Pro US$ 0,134; Gemini 3.8 Flash US$ 0,75/3,75 por milhão de tokens (entrada/saída) até 31/12/2026, dobra em 01/01/2027 (l.1763-1766, 7812-7815). Conta de exemplo: 3 imagens por uso x 200 usos = ~US$ 20/mês (l.1754-1757). Um vídeo com 10 imagens 1K custaria ~US$ 0,34 só de imagem.
3. **Imagem pela API do Gemini NÃO tem nível gratuito** (l.1543-1545, 2574): exige pré-pago (mínimo US$ 5, crédito vence em 12 meses, sem Pix, cartão; l.1613-1615). Isso confirma que o grátis para a ESCALA continua sendo FLUX no Cloudflare; Nano Banana só quando houver caixa.
4. **Pré-pago com recarga automática DESLIGADA e teto mensal** (US$ 5 no teste) (l.1587-1650). Saldo zero = todas as chaves do projeto param com erro 402. O teto pode ser ultrapassado por ~10 min (atraso de cobrança).
5. **Quem paga**: link compartilhado e app publicado gastam a SUA chave (l.1663-1691). Regra geral: nunca publicar nem compartilhar app com IA paga sem limite por usuário.
6. **Limite por usuário** (l.4280-4289, 7231-7238): contador no banco, conferido no servidor ANTES de chamar o modelo; mensagem fixa "Você chegou ao limite de hoje. Volte amanhã."; testar com limite 3 e depois subir para o real. Cada mensagem = 3 gravações (pergunta, resposta, contador) (l.4275). Aplica no bot do Telegram se o dono abrir o bot a mais gente (hoje só aceita o Id do Victor).
7. **Memória do assistente = instrução + só as últimas 10 mensagens** (l.4122-4124, 4227-4240): segura o custo (a entrada cresce com o histórico). Aplica na conversa livre do bot (Workers AI).
8. **A regra de ouro do produto** (l.5155-5173): pedir IA a cada clique do usuário "funciona na prévia e quebra no primeiro mês de vendas". Conta: 1.000 usuários x 3 desenhos x 30 dias = 90.000 imagens = mais de US$ 3.000/mês. Solução: **gerar o acervo uma vez** (300 desenhos ~US$ 10) e o app só entrega arquivo pronto, sem chamar IA durante o uso.

### C. Geração de imagem com consistência (aplica em escala-video-ia e no pipeline de vídeo)
1. **Atribuir papel numerado a cada imagem de referência** (l.3086-3093): "A imagem 1 é a pessoa. A imagem 2 é a peça de cima... Vista a pessoa com as peças, respeitando corte, cor, estampa e tecido. Mantenha rosto, cabelo, corpo, pose, fundo e luz da imagem 1. Das imagens 2 e 3, ignore fundo, cabide, manequim e etiqueta." Padrão para personagem fixo: "imagem 1 = ficha do personagem, imagem 2 = cenário; mantenha rosto/roupa da 1, fundo/luz da 2".
2. **Limites de referência no Nano Banana 2.1**: até 14 imagens por pedido, até 10 de objeto e 4 de personagem (l.3051-3052). Sem proporção indicada sai no formato da foto enviada ou quadrado (l.3052): sempre mandar a proporção (9:16 para vídeo).
3. **Aceita 1:1, 4:5, 9:16 e 16:9** (l.2593).
4. **Predefinição de estilo travada** (l.2762-2776, 5206-5212): um texto fixo anexado a toda descrição + proporção e resolução travadas. Exemplo "Giz Azul": "Ilustração para folha de atividade impressa. Só contorno preto, grosso e uniforme, como de canetão, sobre fundo branco puro. Formas arredondadas, personagem alegre. Áreas fechadas, sem linhas soltas. Cenário mínimo, com no máximo três objetos. Sem cinza, sombra, textura, texto ou moldura." Para a ESCALA: uma predefinição por série (a "bíblia visual" em uma frase colável), junto com o texto sempre no editor (já regra em escala-video-ia: nunca pedir texto na imagem).
5. **Descartar** toda imagem com área aberta, cinza, texto ou semelhança com personagem conhecido (l.5214-5216): checklist de curadoria do lote.
6. **Teste de modelos com critérios fixos** (l.2833-2877): mesma descrição, mesma proporção, 1K, nos 3 modelos, lado a lado com nome e tempo; critérios: fidelidade (marcar item a item o que apareceu), texto (a palavra saiu certa?), edição (dois retoques seguidos mantêm o objeto?), custo. Escolher o MAIS BARATO que passa nos critérios que importam; depois remover o botão de comparar para ninguém disparar 3 cobranças.
7. **Edição seguida preserva o objeto**: teste "mesmo frasco, mesma tampa" após editar para noite (l.2683-2706). Texto em imagem: encurtar se sair letra trocada (l.2776).
8. **SynthID**: toda imagem da API leva marca d'água invisível; o Google não reivindica a propriedade mas pode gerar imagens parecidas para outros; "a proteção de imagens geradas por IA não está garantida: o valor do produto está na curadoria e no app, não na exclusividade de cada desenho" (l.2919-2924, 5238-5246). A política do Google proíbe apresentar conteúdo gerado como feito só por humanos para enganar. Reforça a regra "IA sempre etiquetada".
9. **Rotular tudo que passa por foto real**: arquivo baixado "gerada-por-ia-<data>", etiqueta "Imagem ilustrativa gerada por IA", "Simulação" gravada no canto (l.2642, 3096-3099, 3452).
10. **Foto de pessoa real, autorização por escrito, maiores de 18, nunca criança; não guardar a foto** (l.3267-3276, 7685-7688). Coerente com regra ESCALA de não explorar vítima real nem criança.

### D. Cadeia de IAs com conferência (aplica no roteiro -> vídeo e na checagem de fatos)
1. **Cadeia visão -> lista -> texto -> imagem** (l.3402-3412): cada etapa devolve um formato fixo (JSON, não parágrafo) para a próxima; um erro no começo passa até o fim; por isso **dois pontos de conferência**: a lista (humano corrige) e a receita (o próprio app confere antes de mostrar).
2. **Segunda leitura de conferência no servidor** (l.3607-3621): antes de mostrar, comparar a saída com a lista de entrada; se aparecer algo fora, refazer UMA vez sem o item; se falhar de novo, descartar e mostrar "Não deu para montar...". Mostrar "Conferida com a sua lista" / "Refeita sem: X". Equivale ao checklist de conferência do produtor: o roteiro só cita fatos da lista de fatos do radar; segunda leitura procura fato novo/inventado ("tempere a gosto" escondido no passo mesmo com ingredientes limpos).
3. **Regra repetida 3 vezes** (abertura, seção própria, proibição nominal listando os itens) porque "uma regra dita uma vez se perde no meio do pedido" (l.3426-3430). Aplica em prompts longos: repetir a regra de ouro (ex.: "sem trecho com direito autoral") no começo, no meio e nas proibições.
4. **Gerar a imagem só quando o usuário abre** (l.3496-3499): controla custo. Na fábrica: gerar imagens/vídeo só do roteiro aprovado, rascunho barato antes.
5. **Fundamentação (grounding)** (l.3720-3935): o modelo consulta busca/Maps antes de responder; regra "sugira só o que apareça nas fontes consultadas, nunca de memória"; mostrar a fonte com link; **item sem fonte não aparece, e o app avisa quantos foram descartados** (l.3929-3935). Para o radar viral: cada tema só entra com prova (link/print), sem prova é descartado e o relatório diz quantos. Teste de sanidade: pedir algo que não existe (praia em cidade sem mar) e conferir que a lista vem menor, sem inventar (l.3956-3957).
6. **Termos de dados do Google**: não guardar resultados de busca/Maps; guardar só o que o usuário escreveu (l.3960-3978). Busca: 5.000 consultas grátis/mês por ferramenta, depois US$ 14 por mil (l.3742). Em nível gratuito da API a busca aparece indisponível (l.2013).

### E. Produto próprio (fase 2 da ESCALA; ligar a escala-produto-greenn)
1. **Produto com acervo gerado uma vez** (cap. 14): o tema que viralizou vira um acervo de 100 a 300 itens (desenhos para colorir, cartazes, fichas, checklists) criado em lote com a predefinição de estilo, curado, e entregue como PDF/ZIP na Greenn. Custo único (~US$ 10 por 300 imagens no Nano Banana, ou grátis no FLUX com triagem maior). Começar com 24 itens para testar (l.5217-5218).
2. **O valor está na curadoria**, não na exclusividade (l.5243-5246): vender pacote organizado, nomeado, por tema.
3. **Modelo "app só para o adulto"**: a criança recebe a folha impressa e não acessa o app (l.5154-5156); termos da API do Gemini (desde 23/03/2026) proíbem app dirigido a menores de 18 ou de acesso provável por eles (l.5171-5172, 7843). Cuidado se o produto virar app para criança: tem de ficar fora, vender para pais/professores.
4. **Dois entregáveis por produto**: versão limpa (para a turma) e gabarito (l.5163-5164): ideia de bônus em e-book (versão aluno + versão professor).
5. **Valor mínimo guardado de dados**: nome/e-mail, aceite de 18+ com data e texto, nenhum dado de criança (l.5361-5372, 5475-5480).
6. **Documento de manutenção** (l.7390-7406) e **rotina mensal** (l.7359-7363): compara gasto com teto, exporta cópia, repete testes, confere preços datados, registra mudanças. Aplicar na revisão mensal do analista.
7. **Aviso de privacidade modelo** (l.7340-7350): responsável/contato, dados guardados, para quê, onde ficam, por quanto tempo, direitos (confirmar, corrigir, cópia, apagar). Necessário se a ESCALA coletar e-mail para a Greenn/lista.
8. **Termos do Google Nível inicial/profissional**: os termos do AI Studio e da API valem para uso profissional ou comercial, não pessoal (l.7185-7186): vender um app feito no AI Studio é permitido, sob os termos.

### F. Bot e segurança (aplica no `telegram/worker.js` e nas chaves da fábrica)
1. **Chave só no cofre/servidor, nunca em pedido, chat, print ou arquivo do projeto** (l.492-503, 7583-7584). Se vazar, ordem de troca sem parar o app: criar chave nova, colocar no cofre, TESTAR, só então apagar a antiga (l.1563-1567). Verificação: buscar os primeiros caracteres da chave no código/ZIP e não achar nada (l.5021-5026, 7693).
2. **Negar por padrão**; desconfiar de 3 sinais em regras de acesso: "qualquer usuário logado pode ler", data de validade nas regras, bloco que vale para o banco inteiro (l.4179-4181). Provar com 2 contas, inclusive colando o endereço da tela do outro (l.4196-4205).
3. **Mensagem de erro humana + "digitando..."** no lugar de balão vazio; nunca gravar mensagem vazia (l.4312-4313).
4. **Cotas do Firebase** (grátis): 1 GiB, 40.000 gravações e 50.000 leituras por dia; estourou, todos os bancos criados pelo agente param até ~meia-noite do Pacífico (l.4268-4270). Referência se algum dia a ESCALA guardar estado por usuário.
5. **Supabase grátis** (l.4448-4451): 2 projetos ativos, 500 MB de banco, 1 GB de arquivos, 50.000 usuários ativos/mês; projeto parado 1 semana é pausado (Resume project). Chaves `sb_publishable_` (pode ir ao navegador) e `sb_secret_` (só servidor). Tabela nova exige GRANT (erro 42501) (l.4499-4505). Região São Paulo (sa-east-1). Sem backup automático no grátis; exportar tabelas em CSV e baixar fotos mensalmente (l.7380-7383).
6. **Script SQL: pedir ao agente transcrever INTEIRO no chat e conferir 4 itens antes de rodar** (RLS em cada tabela; "public" só no bucket de catálogo aberto; nenhum insert com e-mail/senha; nenhuma tabela que não deveria existir) (l.4585-4600, 6857-6863). Script idempotente (pode rodar de novo).
7. **Bucket privado + caminho `{id do usuário}/...` + link temporário de 3600 s + banco guarda caminho, nunca link** (l.4555-4559, 4636-4638). Link temporário não se cancela antes de vencer: por isso a validade curta (l.4681-4682).
8. **Primeira administradora sem senha no código** (l.6881-6901): cadastra-se como todo mundo, entra como `sem_acesso`, e um comando SQL só de quem tem o painel a promove.
9. **Antes de divulgar**: rodar a revisão de segurança (l.7196-7211) em tabela item / ok ou problema / onde no código / correção, "Não corrija nada ainda. Diga quais problemas impedem a publicação"; testar em janela anônima, celular e 2 contas (l.7296-7308); religar confirmação de e-mail (exige SMTP próprio, serviço de e-mail transacional) (l.7313-7321).
10. **Nunca testar com dados de cliente real**; no nível gratuito o Google pode usar o conteúdo e revisores podem ler (l.399-400, 574-576).

### G. Ferramentas de design e protótipo (aplica em página de venda/produto)
1. **Google Stitch** (stitch.withgoogle.com, grátis, Google Labs): desenha telas por pedido e exporta para o AI Studio; limites não publicados; se acabar volta no dia seguinte (l.2224-2233). Desenho cuida do visual, pedido cuida do funcionamento (l.2335-2343). Ajustes numa versão nova ao lado para comparar (l.2294-2306). Útil para a página de venda/capa do e-book e protótipo do site da bio; não para vídeo.
2. **Leaflet 1.9.4 + OpenStreetMap**: mapa grátis com crédito "© OpenStreetMap contributors"; uso leve (l.5041-5046). Não usado na ESCALA hoje.
3. **Foursquare Places API**: faixa grátis, depois US$ 15 por mil; só guardar o fsq_place_id; "Powered by Foursquare" obrigatório (l.4834-4846). Não serve à ESCALA (ver fim).

### H. Lições de processo para uma "fábrica" confiável
1. **Plano do sistema inteiro antes da 1ª tela** (cap. 15): mapa das telas, ordem de construção pela dependência ("uma tela só nasce depois das telas de que precisa para ser testada", l.5585), regras da casa decididas antes (regra no meio da obra obriga a refazer, l.5693). Pedido de contexto que apresenta o sistema inteiro e pede só a primeira tarefa (l.5784-5825). Linha "Telas futuras: não as crie; deixe só o ponto de ligação" evita dois erros opostos (l.5877-5878). Aplica ao construir a fábrica em fases (radar -> roteiro -> vídeo -> prévia -> métricas): um módulo por pedido.
2. **Teste de amarração**: criar numa tela e conferir na outra (l.5946-5948, 6062-6063). Para a fábrica: depois de mexer no motor, rodar o exemplo completo de ponta a ponta.
3. **Regras de negócio declaradas com fórmula à vista**: indicador sem fórmula escrita não se confere (l.6542-6544). Exemplo: ocupação = noites vendidas / (quartos ativos x noites do período); roteiro de validação com números que fecham (R$ 903, saldo R$ 703, 23,8%) (l.6586-6624, 7014). Para o analista: toda métrica da ESCALA com fórmula escrita embaixo (retenção, taxa de seguidor por view, RPM) e um caso de teste feito à mão.
4. **Regra de falta de dado**: todo cartão mostra um número, mesmo zero; bloco vazio mostra "Nada por aqui hoje" (l.6516-6517) - "cartão em branco esconde defeito". Aplicar nos relatórios do analista/chefe.
5. **Nada se exclui, se inativa; estorno é lançamento negativo** (l.6031, 6466-6467): auditoria. Aplica na fila `aprovacao/fila.md` e no diário: não apagar linha, só marcar status.
6. **Recomeço limpo antes de teste de ciclo inteiro** (l.6570-6574).
7. **Bloquear duplo clique** (botão desativado enquanto processa; "funciona uma vez só por reserva, mesmo com dois cliques", l.2597-2599, 6426-6427). Aplica nos botões Aprova/Ajusta/Recusa do Telegram: idempotência (aprovar duas vezes não pode publicar duas vezes).
8. **Trava de duplicidade**: "no máximo uma tarefa aberta do mesmo tipo por quarto" (l.6385): evita duas peças iguais na fila.

## Já coberto nas skills existentes (qual skill, e o que o livro acrescenta ou contradiz)
- **escala-video-ia** já cobre: ficha de personagem, imagem-ficha, encadear último quadro, "nunca pedir texto na imagem", custo lido na tela e `projeto/tentativas.md`, "3 tentativas sem melhora muda a abordagem". O livro ACRESCENTA: (a) instrução com papéis numerados por imagem; (b) limite 14 referências/10 objeto/4 personagem do Nano Banana 2.1; (c) predefinição de estilo travada; (d) teste de modelos com 4 critérios; (e) preços oficiais; (f) imagem do Gemini só com pré-pago (não tem grátis). Não contradiz.
- **escala-regras / CLAUDE.md** (IA etiquetada, não enganar, não copiar): o livro reforça com SynthID e a política do Google contra apresentar IA como humano. Não contradiz.
- **escala-producao-video / escala-editor-video** (conferência antes da fila, folha de quadros): o livro acrescenta "segunda leitura de conferência" automática antes de mostrar e o padrão "refaz uma vez, depois descarta".
- **escala-telegram** (Worker, botões, Workers AI): acrescenta limite por usuário, memória de 10 mensagens, idempotência do botão, troca de chave sem parar. O bot atual só aceita o Id do Victor, então o limite por usuário é futuro.
- **escala-produto-greenn / escala-oferta**: já definem quando começar e preço de R$ 9,90 a R$ 27; o livro acrescenta o modelo "acervo gerado uma vez + curadoria" e as regras de dados mínimos/aviso de privacidade. Não contradiz.
- **ui-ux-pro-max**: cobre o visual; o livro só acrescenta o fluxo Stitch -> pedido de regras e a regra "descreva qualidades, não a marca".
- **omegaprompt**: cobre engenharia de prompt; o livro traz os moldes de pedido de sistema (5 partes) e correção (4 partes), que são complementares e mais curtos.
- Livros 07-13 da Mestres Play: não houve sobreposição real; o livro 15 não trata de viral, ganchos, retenção nem edição.

## Skills novas sugeridas ou melhorias

### Melhorias em skills existentes (texto sugerido)
1. **escala-video-ia, seção "Personagem consistente"** acrescentar:
   - "Na instrução ao modelo de imagem, dar um papel numerado a cada referência: 'A imagem 1 é a ficha do personagem. A imagem 2 é o cenário. Mantenha rosto, cabelo, roupa e pose da imagem 1; fundo e luz da imagem 2. Das demais, ignore fundo e texto.' Limite do Nano Banana 2.1: 14 imagens por pedido (até 10 de objeto e 4 de personagem). Sempre informar a proporção (9:16); sem ela sai no formato da foto enviada ou quadrado."
   - "Cada série tem uma predefinição de estilo de UMA frase (técnica, traço, paleta, fundo, o que não pode ter) que é colada em todo prompt da série e guardada na bíblia visual."
   - "Descartar na triagem: área aberta no traço, texto, mão/dente deformado, semelhança com personagem famoso."
   - "Teste de modelos antes de fixar o modelo da série: mesma descrição, mesma proporção, 3 modelos lado a lado; critérios fidelidade, texto, edição seguida, custo; fica o mais barato que passa."
   - "Nano Banana pela API não tem nível grátis (precisa de pré-pago, mínimo US$ 5, recarga automática desligada, teto mensal): grátis continua sendo Cloudflare FLUX."
2. **escala-regras (checklist) ou escala-memoria**: acrescentar "Ao corrigir, citar a regra pelo número ('isto descumpre a regra 4 do CLAUDE.md') e pedir que o agente procure o mesmo erro no resto (Capítulo 5, Comando 04)". Acrescentar "Todo pedido de ajuste termina com 'Não mude X. Diga em uma linha o que alterou e como conferir.'"
3. **escala-producao-video, seção "Conferência antes da fila"**: acrescentar item 5 "Segunda leitura automática: comparar o roteiro final com a lista de fatos do radar; qualquer número, nome, data ou afirmação fora da lista volta uma vez para refazer sem ela; se falhar de novo, cortar o trecho. Registrar em `conteudo/.../conferencia.md` 'Conferido com os fatos' ou 'Refeito sem: X'."
4. **escala-radar-viral**: acrescentar "Tema sem prova (link ou print com data e métrica) não entra no relatório; o relatório diz quantos foram descartados por falta de prova. Teste de sanidade: perguntar por tema que não existe e conferir que a lista vem menor, sem inventar."
5. **escala-telegram, seção "Segurança"**: acrescentar "Botões Aprova/Ajusta/Recusa são idempotentes (segundo clique não repete a ação). Troca de chave sem parar: criar a nova, colocar no ambiente, testar, só então apagar a antiga. Se o bot for aberto a mais gente: limite diário por usuário conferido no servidor antes de chamar o modelo, e só as últimas 10 mensagens vão ao modelo."
6. **escala-produto-greenn**: acrescentar seção "Acervo gerado uma vez": "Produto digital baseado em imagens (desenhos para colorir, cartazes, fichas) = lote de 24 para testar, 100 a 300 para vender, gerados com a predefinição de estilo da série, curados e nomeados por tema, entregues em PDF/ZIP. Nunca prometer exclusividade das imagens (o valor é a curadoria). Dois arquivos por item quando fizer sentido (versão limpa e gabarito). Se coletar e-mail: aviso de privacidade (responsável, dados, finalidade, onde ficam, prazo, direitos) e guardar o mínimo; nunca dado de criança."
7. **escala-crescimento-plataformas ou analista (ficha)**: "Toda métrica do relatório tem a fórmula escrita embaixo e um caso de teste feito à mão. Cartão sem dado mostra 0, nunca fica em branco. Revisão mensal: gasto vs teto, cópia do estado, conferir preços/limites datados das ferramentas e registrar mudanças."

### Skill nova sugerida: `escala-custo-ia` (opcional, pequena)
- Aciona quando for aprovar série nova, escolher modelo de imagem/voz/texto, ou o gasto passar de zero.
- Conteúdo: (1) tabela "mapa de custo por vídeo" (etapa, ferramenta, chamadas, preço unitário, total) para preencher antes de aprovar uma série; (2) preços de referência datados (out/2026, com aviso para reconferir); (3) regra de pré-pago com recarga desligada e teto; (4) regra "gerar em lote uma vez e reutilizar"; (5) rotina mensal de conferência.

### Skill nova sugerida (só se um dia virar app próprio): `escala-app-ia-no-ar`
- Aciona quando o produto próprio virar um app/site com login (hoje não precisa).
- Conteúdo: pedido em 5 partes, regras de projeto, 1 pedido 1 teste, chave no cofre, Supabase grátis com RLS e teste de 2 contas, bucket privado e link de 3600 s, revisão de segurança antes de publicar, aviso de privacidade, documento de manutenção. Fonte: capítulos 5, 11, 12, 18 e 19 deste livro.

## Ferramentas citadas (nome, grátis ou preço, para que serve, tem API?)
| Ferramenta | Preço (out/2026, conforme o livro) | Para que serve | API? |
|---|---|---|---|
| Google AI Studio (aistudio.google.com) | Grátis para construir; Brasil atendido | Construir apps por pedido (agente), conversa com Gemini | Sim (API do Gemini, ai.google.dev) |
| API do Gemini texto (Gemini 3.8 Flash) | Nível grátis só para alguns modelos de texto e para testes seus; pago US$ 0,75/3,75 por milhão de tokens (dobra 01/01/2027) | Texto, visão (ler foto), resumos | Sim |
| Nano Banana 2.1 / 2 Lite / Pro | Sem nível grátis; US$ 0,0336 (1K), 0,0504 (2K), 0,113 (4K); Pro US$ 0,134 | Gerar, editar e unir imagens; 14 referências; 1:1, 4:5, 9:16, 16:9; SynthID | Sim |
| Busca do Google / Google Maps (grounding) | 5.000 consultas grátis/mês cada; depois US$ 14 por mil; Maps oficial só em inglês | Resposta com fonte e lugares reais | Sim (via Gemini) |
| Google Stitch (stitch.withgoogle.com) | Grátis (Labs), limites não publicados | Desenhar telas e exportar para AI Studio | Não informado |
| Firebase (Auth + Firestore) | Cota grátis: 1 GiB, 40 mil gravações e 50 mil leituras/dia; acima disso plano Blaze | Login Google e banco de texto | Sim |
| Supabase | Grátis: 2 projetos ativos, 500 MB, 1 GB arquivos, 50 mil usuários ativos; pausa após 1 semana parado; Pro tem backup | Login, banco Postgres, arquivos, RLS | Sim |
| Cloud Run / publicação do AI Studio | Nível inicial grátis (até 2 apps, conta pessoal sem faturamento pago); publicação padrão cobra pela tabela do Google Cloud | Pôr o app no ar em subdomínio ai.studio | Não |
| GitHub | Grátis (repositório privado) | Cópia e histórico do app | Sim |
| Foursquare Places API | Faixa grátis; depois US$ 15 por mil | Lista de negócios locais | Sim |
| Leaflet 1.9.4 + OpenStreetMap | Grátis, uso leve, com crédito | Mapa na tela | Sim (tiles) |
| Dribbble, Figma Community | Dribbble sem licença de uso; Figma CC BY 4.0 permite adaptar com crédito | Referência de design | Não |
| Veo (vídeo no AI Studio) | Prévias com saída da API marcada para 22/10/2026; Google indicava Gemini Omni Flash | Vídeo gerado | Sim |
| Antigravity | Citado como o agente da tela de construção | Escreve o código do app | Não |
| Lovable, Cursor, Codex, Vercel | Citados como assuntos de outros livros, sem preço | Outros construtores/hospedagem | - |
| SMTP / e-mail transacional (qualquer) | Não detalhado | Necessário para confirmar e-mail no Supabase | Sim |

## Não serve para a ESCALA (1 linha por item)
- Caps. 2 e 3 (calculadora, versões do AI Studio, ZIP/GitHub): treino de ferramenta que não usamos; só o método de pedido aproveita.
- Cap. 5 projetos A e B (conversor de moedas, checklist da padaria): exemplos de app sem relação com vídeo.
- Cap. 6 montador de treino: serve só o método Stitch + print de referência.
- Cap. 8 provador de roupa e configurador de carro: depende de foto de pessoa real e de cliente enviando foto; fora do escopo (só o padrão de papéis numerados aproveita).
- Cap. 9 receitas pela câmera: app de celular com câmera; só a ideia de cadeia com conferência aproveita.
- Cap. 10 planejador de viagem com Maps: Maps oficial só em inglês e termos proíbem guardar resultados; sem uso em vídeo curto.
- Cap. 13 Radar do Bairro, Foursquare, Leaflet: prospecção de negócios locais, nada a ver com viral.
- Caps. 15 a 18 (sistema da pousada, 16 telas, reservas, financeiro, FNRH, diárias, governança): sistema de gestão hoteleira; só os padrões de plano, regras com fórmula e teste com números que fecham aproveitam.
- Película/Contran, FNRH Digital e demais normas: setores sem relação.
- Publicação no Cloud Run com subdomínio ai.studio: só importa se o produto virar app; hoje o produto é PDF/e-book na Greenn.
- Exercícios e "Confira antes de avançar" de cada capítulo: treino de leitor, não regra.
