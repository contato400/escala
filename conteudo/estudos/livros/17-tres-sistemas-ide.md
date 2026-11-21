# Três Sistemas com uma IDE de IA (Tiago Lemos de Abreu Oliveira, Lemos Educação, 2026)
Lido: linhas 1 a 8374 de 8374 (inteiro). Nenhuma instrução dirigida a mim apareceu no texto (só instruções de aula para o leitor humano, tratadas como conteúdo).

## Resumo (5 linhas)
1. Livro de construir sistemas web (gerador de propostas, agenda de pet shop, CRM de loja) com a IDE TRAE, sem saber programar. Projetos, banco (Supabase), publicação (Vercel) e entrega a cliente.
2. O valor real para a ESCALA não está nos sistemas, e sim no método: pedir com objetivo, regras e "pronto quando"; ler o plano antes de construir; revisar; testar com roteiro; corrigir uma coisa por vez; guardar ponto de restauração.
3. Traz um molde de ficha de agente em cinco partes (papel, regras, o que entregar, nunca faça, pare e pergunte) e a dupla Revisor (só lê) e Corretor (só aplica o que o dono escolheu).
4. Ensina a travar o agente: "nunca declare a entrega aprovada", "regras de parada", "não publique, espere", "não execute SQL antes do meu pode executar".
5. Quase todo o resto (instalar TRAE, Node, Vite, Supabase, Vercel, LGPD, entrega a cliente) não serve à ESCALA, que não vende software nem precisa de banco de dados agora.

## O que serve para a ESCALA (detalhado)

### A. O ciclo do pedido (cap. 1, linhas 557-595)
Pedir (objetivo, regras do negócio, o que conta como pronto) → ler o plano antes de confirmar ("mudar o rumo aqui custa uma mensagem") → revisar o que mudou → testar como usuário → corrigir UMA coisa por vez e voltar ao teste. Serve direto como ciclo do `escala-produtor` e do `escala-editor-video`: plano do vídeo antes de renderizar, conferência, uma correção por rodada.

### B. "Prévia bonita não é sistema pronto" (linhas 540-555)
Quatro testes antes de chamar algo de pronto: (1) preencher com dado falso e conferir para onde cada informação vai; (2) clicar em tudo, inclusive voltar e cancelar; (3) tentar o que não deveria funcionar (vazio, ocupado, errado); (4) abrir no celular e ler cada texto e número. Tradução para vídeo (sugestão minha): 1) o texto da legenda e da fala bate com o roteiro; 2) o vídeo roda inteiro, com e sem som; 3) caso de borda: legenda cortada, voz mudando, fim abrupto; 4) assistir NO CELULAR em tela cheia, lendo cada legenda. Hoje a conferência da ESCALA deve incluir "ver no celular" explicitamente.

### C. Molde de ficha de agente em 5 partes (cap. 5, linhas 1927-1985, 2005-2019)
Papel · Regras de trabalho · O que entregar · Nunca faça · Pare e pergunte quando. Citação útil: "as duas últimas impedem o agente de decidir sozinho o que é seu". Exemplos de "nunca faça" que valem para a ESCALA:
- "dizer que a entrega está aprovada ou pronta para publicar (quem aprova é o Victor, depois de testar)";
- "apagar arquivos; mudar o que não foi pedido".
Exemplos de "pare e pergunte": "houver mais de um caminho razoável, ou a mudança apagar dados, instalar algo grande ou mexer em login e permissões".
Aplicação: conferir se cada ficha em `.claude/agents/` tem as cinco partes; hoje as regras fixas do CLAUDE.md cobrem "nunca", mas "pare e pergunte" pode estar fraco.

### D. Dupla Revisor + Corretor (linhas 2068-2133)
- Revisor: só LÊ (sem editar, sem rodar). Procura, nesta ordem: erro que quebra função; risco de segurança; regra do negócio desrespeitada; código repetido; problema no celular. Entrega tabela numerada: problema, arquivo, gravidade (alta/média/baixa), como reproduzir, correção em uma linha.
- Corretor: aplica só os números que o dono escolheu, menor mudança que resolve, confere o resto. "Gravidade baixa pode esperar, segurança não."
Aplicação para a ESCALA: um `escala-revisor` read-only que confere vídeo/roteiro/legenda contra as regras fixas (zero ligação Wesley, direito autoral, IA etiquetada, sem enganar, sem promessa de dinheiro) e devolve tabela numerada com gravidade. Quem corrige é o produtor, só nos itens aprovados. Combina com a regra "toda publicação passa pelo Victor".

### E. Regras de parada para tarefa grande (cap. 9, linhas 3765-3786) e plano antes de gastar (cap. 5, linhas 1911-1925; cap. 4, linhas 1589-1601)
Texto pronto, adaptável para o chefe/produtor numa tarefa longa (ex.: lote de 6 vídeos):
- "Antes de construir, mostre o plano e espere eu escrever plano aprovado."
- "Construa uma etapa por vez; ao fim de cada etapa diga o que fez, os arquivos, como eu testo e o que falta."
- "Se disser que testou, mostre o que testou e o resultado."
- "Não publique. Se a oferta de publicação aparecer, avise e espere."
Pedido de plano sem escrever nada: objetivo, quem usa, regras que não podem falhar, "pronto quando"; resposta com partes, arquivos, dúvidas numeradas e o que fica de fora. Pedido de custo antes de tarefa grande: etapas, arquivos lidos/criados/mudados, que parte tende a gastar mais, se dá para dividir.

### F. Pedido de correção específico (cap. 10, Modelo 01, linhas 4241-4253)
Campos: Defeito (nome curto) · Onde · O que eu fiz (passos) · O que aconteceu (texto exato) · O que deveria acontecer (a regra) · Como repetir · Não mude (o que já passou). Fecha com "diga o que mudou e repita o passo que falhou". "Um defeito por pedido. Refaça a linha que falhou e as vizinhas." É o molde ideal para o Victor reclamar de um vídeo pelo Telegram e o bot transformar em pedido de ajuste ("o Ajusta" do botão). Sugestão: o `escala-telegram` guardar a crítica do Victor nesse formato (vídeo, momento do vídeo em segundos, o que viu, o que esperava, não mexer em X).

### G. "O que ficou fora e o que você supôs" (cap. 10, Comando 02, linhas 4036-4053)
Antes de construir: (1) o que do pedido ficou fora/mudou; (2) o que supôs sem eu ter dito; (3) o que vai testar sozinho e como mostra. Excelente para o produtor antes de renderizar: listar suposições (duração, tom, quem fala, final) e o Victor/chefe corrige pelo número.

### H. Roteiro de validação por papel e tabela "Faça / Deve acontecer" (linhas 4081-4196, 7945-7966)
Escrever o roteiro de teste ANTES de construir, depois ele vira lista de aceite. Linhas de borda que "pegam defeito frequente" (data que volta um dia por fuso; confirmação que promete e-mail que o sistema não envia). Equivalente na ESCALA: lista de aceite do vídeo escrita antes (gancho nos 3 primeiros segundos, legenda legível, selo de IA, aviso de publicidade se houver, nada de promessa) e depois marcada OK/Falhou. Lição transversal: "o 'testei tudo' do resumo do agente não vale; o roteiro é sempre seu" (linhas 4295-4296, 3807-3809). Para a ESCALA: o relatório "conferido" do produtor deve mostrar o que foi conferido e o resultado, e o Victor/chefe amostra.

### I. Referência visual sem copiar (cap. 11 e 12, linhas 4387-4423, 4537-4543, 4829-4871, 4909-4954)
Muito alinhado à regra "copiar o formato, nunca o vídeo":
- Quatro perguntas para qualquer imagem de referência: é uma tela só e inteira? dá para ler? está livre de dados reais? combina com as outras? (tabela, linhas 4387-4427).
- Regra de ouro: usar de um site SÓ a disposição (ordem e peso dos blocos). "Cole no chat o esboço, nunca a captura. Assim marca, textos, imagens e cores do site ficam de fora desde o começo." Para a ESCALA: ao estudar vídeo viral, o produtor escreve um ESBOÇO do formato (ordem dos blocos, tempos, tipo de corte) e passa só esse esboço ao motor/gerador de imagem, nunca o frame/trecho do original.
- Pedido de recriar: "Use o frame só como referência de estrutura. Troque tudo o que identifica o original: marca, textos, imagens, cores. Textos novos, nada traduzido do original." Depois "procure qualquer palavra, nome ou foto vinda do original e peça a troca".
- Ficha da referência (Modelo 01, linhas 4861-4871): arquivo, criador, endereço, gratuito/pago, licença, frame usado, usado em, o que foi trocado. Para a ESCALA: ficha de referência do radar (rede, link do vídeo, criador, o que foi copiado = só formato, o que foi trocado = tudo o resto). Dá prova de "copiamos o formato, não o vídeo" caso a plataforma questione. Observação: crédito ao criador só vale para licença livre (CC BY); em vídeo viral de terceiros não há licença, então a ficha é interna, sem crédito público, e o conteúdo precisa ser 100% novo.
- "A imagem manda mais que o pedido" é erro comum: manter a linha "textos, nomes e dados vêm deste pedido, não da imagem".

### J. Contexto e custo de IA (cap. 3 e 4, linhas 1346-1362, 1562-1590, 1779-1787)
- Uma conversa por tarefa: conversa longa gasta mais e mistura assuntos; abrir chat novo e dizer em duas linhas onde parou (casa com `memoria/passagem.md`).
- Ficar no mesmo modelo e só trocar quando o agente falhou 2 ou 3 vezes no mesmo problema; anotar a troca em uma linha (data · tarefa · modelo A → B · motivo). Sugestão: arquivo `memoria/notas-modelos.md` ou seção em `aprendizados.md`.
- Laboratório de modelos: mesmo pedido, pastas separadas, mesma tabela (funções que passaram /N, erros, visual 1 a 5, tempo, consumo). Útil para comparar FLUX schnell vs. outro gerador de imagem na ESCALA: mesmo prompt de personagem, nota de consistência 1 a 5, tempo, custo.
- Medir antes e depois: saldo antes e depois da tarefa mostra o custo real do lote.

### K. Segurança de chaves (cap. 13, 17; linhas 5266-5301, 5398-5412, 6894-6933)
Regras diretas para o repositório da ESCALA (token do bot, Cloudflare, Metricool): chave só em variável de ambiente fora do Git; ver o `.gitignore`; "se o agente pedir a chave secreta, recuse"; "mostrar só o começo de cada valor"; procurar no projeto qualquer chave escrita no código antes de publicar; se vazou, apagar e trocar. Lista de checagem de SQL antes de executar (não aplica agora, mas a ideia "mostre e explique antes de executar; não execute sem eu escrever pode executar" vale para qualquer comando destrutivo do agente).

### L. Ponto de restauração com Git (cap. 8, linhas 3053-3083, 3336-3372)
Só criar ponto DEPOIS de testar, assim o último ponto é sempre bom. Pedido de volta seguro: rodar `git status` e `git log --oneline -5`, listar arquivos alterados em linguagem simples, esperar confirmação, só então `git restore .`, nunca `git reset`, `git clean` ou `git push`, não apagar arquivos novos, listar para decidir. Casa com o hábito de commit por etapa na ESCALA: um commit por vídeo/rodada aprovada.

### M. Privacidade ao usar ferramenta de IA (linhas 1013-1051, 7483-7490)
Ligar o "modo privacidade"/desligar uso para treino onde existir; não colocar dados reais de pessoas em projeto aberto em ferramenta de IA. Reforça a regra "nunca guardar senha, chave, telefone ou e-mail" (inclusive: o arquivo do livro vem com e-mail do comprador carimbado; não copiei).

### N. Dados de teste "visivelmente falsos" (linhas 408-417)
Telefone (11) 90000-0000, e-mail example.com, sem CPF. Útil para qualquer exemplo de roteiro de golpe/celular no motor (a ESCALA já faz formato celular e Pix): usar sempre número e chave Pix inventados e claramente falsos, nunca de pessoa real.

## Já coberto nas skills existentes (qual skill, e o que o livro acrescenta ou contradiz)
- `escala-regras` e CLAUDE.md: "agente prepara, publica só com aprova" já cobre o "nunca se declarar aprovado". O livro acrescenta a frase de bloqueio dentro de CADA ficha de agente e a seção "pare e pergunte".
- `escala-editor-video` (conferência): já tem conferência. O livro acrescenta o roteiro "Faça / Deve acontecer" escrito antes e o teste "no celular, lendo tudo", mais "o testei do agente não vale".
- `escala-memoria`: já faz passagem. O livro acrescenta "um chat por tarefa" e a nota de troca de modelo.
- `escala-radar-viral` e `escala-editor-video` (copiar estilo de referência): o livro acrescenta a técnica do esboço (passar só a estrutura) e a ficha da referência.
- `omegaprompt`: o livro NÃO contradiz; usa pedido com objetivo, regras, pronto quando. Complementa com exemplos de "nunca faça" e "pare e pergunte".
- Não encontrei conflito com nenhuma regra fixa do CLAUDE.md. Única atenção: o livro usa travessão e jargão técnico; qualquer texto trazido daqui para skills deve seguir "português simples, sem travessão".

## Skills novas sugeridas ou melhorias

### Skill nova: `escala-revisor` (read-only)
Aciona quando: um roteiro, vídeo (frames/legenda/áudio), legenda de post, prévia do Telegram ou página de produto está pronto e vai para a fila do Victor; também quando o Victor reclama de algo e é preciso achar a causa. NÃO aciona para criar nem corrigir.
Conteúdo:
- Papel: só lê e confere; não edita, não renderiza, não publica, não se declara aprovado.
- Ordem de busca: (1) quebra a regra fixa (ligação Wesley/Victor, direito autoral, IA sem etiqueta, enganar, promessa de dinheiro, afiliado sem aviso, dado pessoal); (2) falha técnica (áudio, legenda cortada, formato 9:16, duração); (3) retenção (gancho nos 3 s, final de parte); (4) repetição de vídeos anteriores; (5) leitura no celular.
- Saída: tabela numerada Problema | Onde (arquivo/segundo) | Gravidade (alta/média/baixa) | Como reproduzir | Correção em uma linha. Gravidade alta e regra fixa bloqueiam a fila.
- Corretor: o produtor aplica só os números que o chefe/Victor escolher, menor mudança, e reconfere os vizinhos.

### Melhoria: fichas em `.claude/agents/` (todas)
Seção sugerida ao fim de cada ficha, em 5 linhas: "Papel / Regras de trabalho / O que entregar / Nunca faça (aprovar a própria entrega; publicar; apagar arquivo; mudar o que não foi pedido) / Pare e pergunte quando (mais de um caminho razoável; gasto novo; mudar conta, perfil, login; apagar)".

### Melhoria: `escala-editor-video`, seção "Conferência"
Acrescentar: "Antes de render, escreva a lista de aceite (5 a 8 linhas, cada uma com ação e resultado esperado, que outra pessoa marcaria sim/não). Depois do render, marque OK/Falhou e mostre ao chefe o que foi conferido, não só 'conferido'. Sempre assistir no tamanho de celular. Cada falha vira pedido de correção no molde: Defeito, Onde (segundo), O que vi, O que deveria acontecer, Não mude. Um defeito por vez; depois repita a linha que falhou e as vizinhas."

### Melhoria: `escala-radar-viral`, seção "Estudar um vídeo viral"
Acrescentar a "Ficha da referência" interna (rede, link, criador, data, números de prova, o que copiamos = só formato e ordem dos blocos, o que trocamos = tema específico, texto, imagem, voz, trilha, cores) e a regra "passe ao produtor o ESBOÇO do formato, nunca o vídeo, a transcrição literal ou os frames".

### Melhoria: `escala-telegram` (botão Ajusta)
Guardar a crítica do Victor no molde de pedido de correção específico (Defeito, Onde, O que aconteceu, Deve acontecer, Não mude). Se a crítica vier vaga ("tá ruim"), o bot pergunta uma coisa por vez: onde (segundo), o que viu, o que esperava.

### Melhoria: `escala-memoria`
Regra: um chat/rodada por tarefa; ao abrir novo, ler a passagem e dizer em duas linhas onde parou. Registrar troca de modelo/ferramenta de IA em `memoria/aprendizados.md` numa linha (data · tarefa · de → para · motivo).

### Melhoria: `escala-video-ia` (laboratório de geração)
Tabela de comparação para testar dois geradores (ou duas versões do prompt) com o mesmo pedido: personagem igual entre cenas (1 a 5), erros visíveis (mãos, texto), estilo (1 a 5), tempo, custo/créditos. Anotar a escolha com o motivo.

## Ferramentas citadas (nome, grátis ou preço, para que serve, tem API?)
| Ferramenta | Preço (out/2026, segundo o livro) | Para que serve | API |
|---|---|---|---|
| TRAE (IDE com agente, ByteDance) | Free US$ 0 (só modo automático, sem SOLO); Lite US$ 8, Pro US$ 20, Pro+ US$ 60, Ultra US$ 200 por mês | Construir sistemas com agente de IA numa pasta | Não é o foco; aceita modelos externos por chave |
| OpenRouter | Créditos em dólar, taxa 5,5% na compra com cartão (mín. US$ 0,80) | Acessar modelos de várias empresas com uma chave e limite de gasto por chave | Sim |
| Supabase | Grátis: 2 projetos ativos, 500 MB banco, 1 GB arquivos, pausa em 1 semana sem uso; Pro a partir de US$ 25/mês | Banco de dados, login e arquivos | Sim |
| Vercel | Hobby grátis (só uso pessoal e não comercial); Pro US$ 20/mês por pessoa que publica | Publicar site na internet | Sim |
| Figma / Figma Community | Starter grátis; arquivos gratuitos da Community em licença CC BY 4.0 | Layouts e referência de estrutura | Sim |
| Google Stitch | Entra com conta Google; limites e preço não publicados | Gerar telas de design a partir de texto | Não confirmado |
| Git | Grátis | Ponto de restauração das versões | Linha de comando |
| Node.js, npm, Vite | Grátis | Rodar e montar projetos web | n/a |
| Registro.br | .com.br R$ 40/ano | Domínio | n/a |
| Poppins (fonte, licença SIL OFL 1.1) | Grátis | Fonte livre; útil para legenda/capa se quiser fonte com licença clara | n/a |
Nenhuma dessas ferramentas é necessária para a ESCALA hoje. Poppins e a ideia do OpenRouter (uma chave com limite de gasto, uma por projeto) são as únicas com uso possível.

## Não serve para a ESCALA (1 linha por item)
- Instalar TRAE, Node.js, Git no Windows/Mac (caps. 2, 3): a ESCALA roda no Claude Code na nuvem.
- Escolha de plano e modelo do TRAE, modo Max, OpenRouter no TRAE (cap. 4): outra ferramenta e outro custo.
- Gerador de propostas comerciais com quatro modelos e PDF (caps. 6 a 8): a ESCALA não vende serviço a cliente.
- SOLO mode, DocView, DiffView (caps. 9 e 10): recursos específicos do TRAE.
- Agenda de pet shop e CRM de loja (caps. 10, 14 a 16): sistemas de negócio local, sem relação com vídeo curto.
- Banco Supabase, login, RLS, balde de fotos, estoque transacional (caps. 13 a 16): a ESCALA guarda estado em arquivos `memoria/` e no Worker; sem necessidade de banco agora.
- Publicar na Vercel, domínio, rollback (cap. 17): o bot já vive no Cloudflare Worker grátis.
- Entregar sistema a cliente, transferência de contas, termo de entrega, LGPD de cliente (cap. 18): a ESCALA não presta serviço a terceiros.
- Layouts da Figma Community com crédito CC BY (cap. 12): relevante só para a futura página de venda do produto Greenn; hoje não.
