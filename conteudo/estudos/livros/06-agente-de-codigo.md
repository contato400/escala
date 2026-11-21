# Agente de Código na Prática (Tiago Lemos de Abreu Oliveira, 1ª ed., out/2026)
Lido: linhas 1 a 7814 de 7814 (inteiro, conferido com wc -l). Nenhuma instrução embutida no texto pedindo ação ao leitor-agente: instrução no texto, ignorada (nada a registrar).

## Resumo (5 linhas)
- Livro de método para quem usa o Claude Code (app desktop, aba Code) sem programar: o humano decide, pede em português, confere na tela e aprova; o agente escreve, roda e testa.
- Parte I (cap. 1 a 3): modos de permissão, plano antes de fazer, navegador embutido, CLAUDE.md curto, Git com versões nomeadas, trava do .env, retomada no dia seguinte.
- Parte II (cap. 4 a 7): construir por especificação (função + regra com exemplo + referência), uma mudança por mensagem, varredura do "inventado", regressão e roteiro de teste aprovado ANTES, dados TESTE, prova em print.
- Partes III e IV (cap. 8 a 16): servidor próprio, banco, e-mail transacional, planilha, site de cliente com autorização, publicação com plano de volta, entrega e manutenção. Quase tudo isso é de agência de sites e não serve à ESCALA hoje; serve de exemplo de disciplina.
- O livro NÃO ensina hooks, tarefas agendadas nem subagentes (diz que skills ficam em outro livro, "Skills e Squads de Agentes de IA", linha 409). O que serve da pergunta "como o agente trabalha melhor" é o método de CLAUDE.md, plano, teste e passagem.

## O que serve para a ESCALA (detalhado)

### 1. Ciclo de trabalho do agente (aplicar em toda tarefa de código: motor, bot, ferramentas)
Passo a passo que vale como regra de operação:
1. **Primeira tarefa em pasta nova é só leitura** (cap. 1, comando 01, L.654-676): "Leia tudo, não crie/edite/apague nada. Diga em até 5 linhas: o que tem, o que dá para construir, o que falta. Termine com pergunta se faltar informação." Depois conferir que nada mudou na pasta.
2. **Plano antes de fazer** (L.694-701): "Antes de fazer, diga em linguagem simples o que vai fazer, quais arquivos cria ou muda e quais comandos roda. Espere o 'pode seguir'." Modo Plan para qualquer coisa que cria vários arquivos (L.978-984): "mudar um plano custa uma mensagem; mudar o que foi construído custa várias."
3. **Juntar todas as correções do plano numa mensagem só** (L.1037-1046) e pedir "mostre só as partes que mudaram".
4. **Uma mudança por mensagem**, com "não mude mais nada" (L.1792-1798, L.2021-2022). Cinco mudanças juntas = algo bom quebra junto. Volta-se à versão salva.
5. **Fecho de conferência em todo pedido que mexe em tela** (cap. 2, comando 04, L.1091-1099): "Abra o resultado, use cada botão como um usuário, veja na largura de computador e de celular com um print de cada, corrija, diga o que testou, o que corrigiu e o que ainda não funciona. Não diga que está pronto sem ter visto na tela." Para a ESCALA a versão é: "não diga que o vídeo está pronto sem ter conferido quadros + transcrição (Whisper)".
6. **Salvar versão nomeada no Git a cada passo que deu certo e antes de mudança grande** (L.1411-1420). A descrição da versão leva uma linha com "o que ficou por fazer".
7. **Voltar sem perder o que está bom** (comando 06, L.1475-1487): salvar o estado atual como "antes-de-voltar", mostrar quais arquivos restaura, esperar aprovação, restaurar e salvar nova versão. PROIBIDO `reset --hard` e `push --force`. (Pontos de volta internos do Claude Code não cobrem o que um comando apagou ou moveu: só o Git, L.1489-1491.)

### 2. CLAUDE.md que funciona (cap. 3, L.1242-1330; cap. 6, L.2449-2453)
- O Claude começa cada sessão sem lembrar das outras. O que ele sabe vem da pasta: arquivos, CLAUDE.md e memória automática. O que foi dito só na conversa se perde (e a conversa longa é resumida).
- CLAUDE.md = manual curto: o projeto (2 linhas), como rodar, regras que não mudam sem perguntar (frases curtas), segredos (só nomes, nunca valores), como publicar. Pedir ao agente que faça no máximo 5 perguntas antes e **mostre o texto antes de salvar** (L.1274-1289). Livro usa no máximo 40 linhas; a documentação citada recomenda menos de 200 (L.1327). Escopos: `CLAUDE.md` ou `.claude/CLAUDE.md` (projeto), `~/.claude/CLAUDE.md` (todos os projetos), `CLAUDE.local.md` (só seu, vai no .gitignore). Mudou com a sessão aberta? Vale em sessão nova ou depois de `/compact` (L.1328). `/init` cria rascunho; `/memory` mostra e edita a memória automática.
- **Erro comum: CLAUDE.md virou diário** (L.1592-1594). Sinal: cresce e o agente ignora regra. Correção: só regras e o jeito de rodar; o que mudou fica no Git. (A ESCALA já separa isso: CLAUDE.md = regras, passagem.md = histórico. Manter.)
- **Regra só na conversa não existe**: sinal = sessão nova não sabe de uma regra; correção = passar para o CLAUDE.md e abrir outra sessão (L.2733-2734).
- O CLAUDE.md orienta mas NÃO impede nada (L.1319-1321); a trava vem de `.claude/settings.json` (item 3 abaixo).
- Seção "Onde paramos" (cap. 6, comando 05, L.2709-2724): antes de abrir sessão nova, o agente reescreve no fim do CLAUDE.md, em no máximo 10 linhas: o que ficou pronto, o que está pela metade e o próximo passo, defeitos conhecidos, decisões do dono que não estão nas regras. Mostra antes de salvar; não muda outro arquivo. A sessão nova começa pelo pedido de **retomada** (cap. 3, comando 08, L.1562-1570): "Leia o CLAUDE.md e o histórico do Git. Sem mudar nada, diga em até 8 linhas qual foi a última versão, se há mudanças não salvas e o que ficou por fazer. Depois rode o projeto como o CLAUDE.md manda."
- Sinais de que a sessão passou do ponto (L.2691-2694): respostas confusas, regra combinada há pouco esquecida, arquivo pronto refeito sem pedido, anel de uso quase cheio. Não insistir: passar o bastão.
- Duas sessões mudando a mesma pasta se atropelam: uma sessão por pasta (L.1572-1573).

### 3. Segredos e permissões (cap. 2 e 3, L.785-896, L.1509-1533; cap. 12, L.5399-5404)
- `.gitignore` mínimo: `.env`, `.env.*`, `!.env.example`, `CLAUDE.local.md`, `.DS_Store`, `node_modules/` (L.1378-1388). Pedir ao agente que mostre o que entra na primeira versão e **confirme que nenhum segredo está nela**.
- `.claude/settings.json` com `{"permissions":{"deny":["Read(./.env)"]}}` (L.1519-1523). Vale em todos os modos e barra também a escrita pelo agente: quem cria e preenche o .env é o humano. Outro arquivo de segredos entra pelo nome. Não alcança programas que abrem arquivo por conta própria: a outra metade é nunca colar segredo no chat.
- `.env.example` só com os nomes (L.4214-4222). O agente gera segredos no próprio servidor e grava direto no .env sem mostrar; para conferir, só os nomes das variáveis (L.4204-4208). Se um cartão for mostrar a senha (ex.: `cat .env`), recusar; se aparecer mesmo assim, trocar.
- **Chave colada no chat, e-mail ou Git conta como vazada**: criar chave nova, apagar a antiga, colar a nova no .env, reiniciar, repetir o teste, procurar a antiga no histórico do Git sem mostrá-la (L.5399-5404). Aplicável já: a FABRICA_KEY e os 4 segredos do worker do Telegram.
- Modos: Manual (pergunta tudo; pasta nova, servidor, o que ainda não entende), Accept edits (pasta só com o projeto, depois de aprovar o plano), Plan (lê e planeja, não edita), Auto (checagem automática; tarefa longa com o dono por perto), Bypass permissions (desligado, só em máquina descartável) (L.808-875). Regra: pasta nova começa em Manual ou Plan. Nunca escrever "faça tudo sem pedir permissão".
- Ler cartão de permissão antes de aprovar: que comando é, em que pasta mexe, usa internet? Sinais de recusa: `rm -rf`, `sudo`, senha no comando, `curl ... | sh`, caminho fora da pasta (L.917-948). Pedido "Explicar um comando antes de aprovar" (L.966-976): o que faz, onde mexe, se acessa internet, se dá para desfazer e jeito mais seguro. "Aprovar sempre" só para o que se repete e se entende (ex.: ligar a prévia); se o agente parou de perguntar, listar e apagar a regra gravada (L.1149-1151).
- Esforço do modelo: padrão medium; subir (high/xhigh) quando conferir importa (corrigir defeito em projeto existente), baixar em trocas rápidas revisadas uma a uma (L.1053-1082). Anel de uso e `/usage` mostram contexto e limite; olhar antes de tarefa longa (L.1141-1146).

### 4. Especificação em vez de pedido solto (cap. 5, L.2115-2300)
Ficha de 5 partes (modelo 01, L.2118-2129): (1) o que é e para quem, uma frase; (2) funções, uma por linha, só as que vai usar; (3) **regras de comportamento, cada uma com exemplo** ("Quando eu X, acontece Y. Exemplo: Z."); (4) referência conhecida ("funciona como [app], sem copiar marca, nome nem visual"); (5) onde guarda os dados. Fecho: "Não acrescente nada que eu não pedi. Deixe rodando, abra no navegador e diga o que conferiu."
- "Eventos de vários dias" é função; "evento de 4 a 7 aparece como faixa nos dias 4, 5, 6 e 7" é regra que o agente cumpre e o humano confere (L.2132-2134).
- Salvar a especificação num arquivo (`especificacao.md`) e atualizar a cada regra nova: regra num lugar só (L.2184).
- **Toda conferência acha algo que a especificação não previa** (L.2206-2209): corrigir com UMA regra por mensagem, uma frase, com exemplo, "aplique só essa regra, não mude mais nada, acrescente ao especificacao.md, mostre o print" (comando 02, L.2237-2240).
- **Regra do livro: nada sem função na tela** (L.2246-2254). Clicar em cada item; o que não responde sai ("botão morto confunde você hoje e o cliente amanhã"). Aplicar nos vídeos: nada de cena, legenda ou selo "decorativo" sem função.
- Módulo novo no mesmo chat: pedir "mesmo visual, mesmo jeito de guardar dados, não mude o comportamento dos módulos antigos além de X" e exigir **tabela final: arquivos novos, arquivos mudados, o que mudou em cada módulo antigo**; se mudou algo não pedido, perguntar o porquê (L.2484-2524).

### 5. Teste feito pelo agente, com prova (cap. 6 e 7, L.2550-3250)
- **Conferência de regressão** (comando 03, L.2596-2613): antes de mudar uma regra antiga, listar tudo que depende dela, módulo por módulo, e esperar "pode seguir"; depois rodar de novo as conferências dos módulos antigos e devolver tabela módulo | conferência | resultado (OK/falhou). Se falhar, PARAR e avisar antes de corrigir. Exemplo do livro: mudar "semana começa na segunda" no calendário quebrou o total de horas (domingo foi para a semana seguinte). Falha na regressão = a conferência funcionando; corrigir a linha e rodar a tabela inteira de novo.
- **Teste de sincronização entre módulos** com regras escritas antes (L.2556-2570): mudar nome propaga? excluir deixa sobra? Tabela regra | o que viu | resultado, "não corrija nada ainda", no fim apagar dados de TESTE.
- **Roteiro de teste aprovado ANTES de testar** (comando 01, L.2829-2838): `roteiro-de-teste.md` com uma tabela por módulo (nº, ação, resultado esperado, largura, Resultado vazio), uma ação por linha como o usuário faria, incluindo ligações entre módulos e **casos de limite** (virada de mês, título muito longo, item sem data, horas que passam da meia-noite, excluir algo ligado). Escrito depois, o roteiro tende a confirmar o que foi construído; escrito antes e aprovado, mede contra o que o dono queria. Cada regra do especificacao.md tem uma linha.
- **Dados de teste fictícios**: 20 registros criados pelos formulários, todo título começando com `TESTE`, anotado no CLAUDE.md; nunca dado de pessoa real (L.2904-2918). Comando "Zerar dados de teste" apaga só o que começa com TESTE (L.2923-2927).
- **Rodar o roteiro**: Resultado = OK / Falhou / Não deu para testar + motivo em uma frase, print de cada falha, "não corrija ainda", lista de achados só das linhas não-OK, da mais grave para a mais leve (L.2943-2951). A prioridade fica com o humano.
- **Decisões que o agente tomou sozinho** (comando 05, L.3019-3025): "Liste as decisões que você tomou e que não estão no especificacao.md nem no CLAUDE.md: regras, formatos, arredondamentos, ordem das listas, o que acontece ao excluir. Para cada uma: onde, o que decidiu e uma alternativa." Humano responde numa mensagem ("1: sem arredondamento. 2: lista. 3: fica"); as confirmadas entram no especificacao.md e no roteiro.
- **Relato de defeito padrão** (comando 06, L.3150-3158): Onde / O que fiz / O que esperava (ou linha do roteiro) / O que aconteceu / Largura + "Antes de mudar, diga a causa provável em uma frase. Depois corrija só isso, rode de novo essa linha e as do mesmo módulo e mostre print de antes e depois." Tabela de sintomas (L.3079-3141): prévia em branco = pedir leitura dos erros do console antes de mudar; data errada = testar 23h30 e virada de mês; texto vazando = testar com o título mais longo; certo no PC e quebrado no celular = conferir nas duas larguras; registro duplicado = contar registros guardados.
- **"Peça a prova"** (comando 07, L.3199-3203): sinais de teste falso são "deve funcionar", "o código está correto", nenhuma tabela, só uma largura. Pedido: "Para cada item OK, mostre os passos, o registro de teste usado e o print. Se algum foi conferido só lendo o código, marque 'Não testado no navegador' e teste agora."
- Tudo OK na primeira rodada = suspeito: pedir mais casos de limite (L.3215-3216). O CLAUDE.md manda rodar o roteiro depois de cada mudança; versão "hub-testado" salva (L.3209-3211).

### 6. Varredura do inventado (cap. 4 e 14, L.1636-1643, L.1892-2000, L.6181-6224), casa direto com a regra "enganar não" da ESCALA
- O agente, quando falta informação, preenche com o que costuma existir: logos de clientes que nunca foram seus, depoimento com nome, "mais de 50 projetos entregues" (L.1636-1643).
- Defesa 1, no pedido: "Use só as informações do arquivo-fonte. Não invente nome, logo, depoimento, número, prazo, preço, prêmio nem certificação. Onde faltar, deixe aviso visível `[FALTA: o que falta]`" (L.1739-1743). Cada aviso é uma pergunta ao dono.
- Defesa 2, depois: **varredura** (comando 05, L.1895-1908): "Compare a página inteira, frase por frase, com o arquivo-fonte. Liste numa tabela tudo que não veio dele: nomes, empresas, logos, depoimentos, números, prazos, preços, selos, certificações, prêmios e promessas de resultado. Inclua textos alternativos e título da aba. Para cada item: onde, texto exato, sugestão (tirar ou trocar por [FALTA]). Não mude nada. Espere a decisão." Rodar de novo até voltar vazia. Humano decide item por item numa mensagem.
- Versão do cap. 14 (L.6198-6218) acrescenta serviços, planos, ofertas e "não reaproveitar/não autorizada" do inventário, e acessibilidade no mesmo pedido.
- **Prova social só verdadeira** (L.6220-6224): avaliação só se real e autorizada; com nome, a pessoa também autoriza; número só se o dono puder provar; sem isso, a seção sai.
- Ofertas que o agente "acrescenta por boa ideia" (plano de revisão mensal com preço) são oferta nova: só o dono decide (L.6120-6123). Pedir no plano uma **lista separada do que o agente acrescentaria e não está na fonte** (L.6116).
- Direito de imagem: só imagem própria ou com direito; foto de terceiro pede autorização e crédito (Lei 9.610/1998); imagem achada na internet fica de fora (L.1887-1890); referência visual descrita em palavras, nunca texto/imagem/desenho de seção alheia (L.6006-6016). Casa com "copiar o formato, nunca o vídeo".

### 7. Diagnóstico só de leitura e relatório de uma página (cap. 13, L.5629-5837)
- Frase "só olhe: não preencha formulário, não clique em envio, não crie conta, não baixe nada" é a mais importante do pedido: teste no formulário de terceiro chega de verdade ao dono (L.5633-5635, L.5852-5854). Em site de fora, a primeira ação pede aprovação por site (Allow once / Always allow / Deny); escolher Allow once, e Deny se for ação de envio.
- "Não invente números de visitas, vendas ou conversão" (L.5666-5667); só o que o print prova. Aplicar no relatório do Analista: nada de projeção sem medição.
- Relatório de uma página: uma frase do que foi avaliado e quando; tabela com no máximo 6 achados em ordem de prioridade (problema, prova em print, impacto, esforço baixo/médio/alto, o que muda); o que reaproveitar; próximo passo (L.5816-5827). Primeiro o que pesa muito e corrige fácil. Bom formato para o "relatório curto ao Victor".
- Inventário de conteúdo como **fonte única**: o que não está nele não entra (L.5729-5739). Marcar "pedir ao dono" quando a qualidade for baixa ou a info puder estar velha, e "não reaproveitar" para imagem sem licença conhecida.

### 8. Publicar com plano de volta, checagem e fonte de verdade (cap. 15, L.6385-6840)
- Antes de mudar algo irreversível (DNS), salvar print/tabela do estado atual e **escrever o plano de volta com os valores antigos** (L.6438-6451); se algo grave aparecer, não consertar com pressa: voltar (L.6714-6718). Manter o sistema antigo ligado até uma semana sem problema.
- Comando de acompanhamento pós-virada: consultar 2 DNS públicos, comparar com o estado de antes, parar se algo que não devia mudou, conferir item por item e gravar em `conferencia.md` (L.6646-6658). Depois, o humano confere no celular, fora do Wi-Fi de casa (L.6673-6708), e repete o teste no dia seguinte.
- **Seção "Como publicar" no CLAUDE.md** (comando 05, L.6784-6791): servidor/pasta de destino, o que é copiado e o que nunca vai, validação antes de recarregar, conferência depois; regras: salvar versão antes de publicar, nunca mexer no DNS, nunca alterar blocos de outros sites, se a conferência falhar voltar à versão anterior e avisar. Daí em diante todo pedido termina com: "Me mostre no painel Browser, espere a minha aprovação e publique como o CLAUDE.md manda." Isso é a regra da ESCALA "publica só com aprova", escrita como rotina.
- Prévia privada: senha + noindex (cabeçalho e páginas) + não mexer em outro site; aprovação do dono por escrito com data, guardada em `aprovacoes.md` (L.6249-6268). Erro comum: prévia aberta → testar em janela anônima. Ao ir para produção, lembrar de tirar o noindex da prévia (L.6812-6816).
- Ensaiar antes do primeiro cliente: publicar uma página de ensaio e depois executar o plano de volta (exercício, L.6817-6827).

### 9. Manutenção e monitoramento (cap. 16, L.7073-7168)
- Quatro ritmos: a cada 5 min um monitor de fora confere se o site responde; todo dia cópia fora do servidor; todo mês relatório + restauração de teste; todo ano renovação e revisão de acessos.
- Monitor: UptimeRobot grátis, 50 monitores a cada 5 min, alerta por e-mail; criar um monitor de endereço inexistente para testar o alerta e apagar (L.7098-7105). **Cópia nunca restaurada não conta** (L.4377-4378, L.4470-4472).
- Relatório mensal só leitura, em tabela item | situação | o que fazer, "não corrija nada; para cada ação proponha o passo e espere aprovação", gravado em `manutencao/AAAA-MM.md` (L.7111-7121). Erro: relatório que ninguém lê → marcar uma hora por mês.
- Contas no nome certo: o que identifica o negócio no nome do cliente, ferramenta de trabalho no seu; senha nunca por WhatsApp/e-mail, gerenciador de senhas, verificação em duas etapas em tudo (L.6958-7008). Saída do cliente: exportar tudo + LEIA-ME com nomes das variáveis sem valores + apagar depois da confirmação por escrito (L.7176-7209).

### 10. Passos concretos para a ESCALA aplicar já (sem depender de servidor)
1. Criar `.claude/settings.json` com `permissions.deny` para `Read(./.env)` e para o arquivo de segredos do worker (ex.: `.dev.vars`), e conferir `.gitignore` (hoje só 38 bytes). O repositório não tem settings.json (conferido).
2. Acrescentar ao CLAUDE.md as seções "Segredos (só nomes, nunca valores)", "Como rodar" (comando do motor, onde ficam voz e cache) e "Onde paramos" (10 linhas, reescrita antes de cada passagem de bastão). Manter abaixo de 200 linhas (hoje 61).
3. Pedido-padrão de início de rodada da fábrica: "Leia CLAUDE.md, estado, última passagem; sem mudar nada, diga em até 8 linhas o que ficou por fazer; depois siga". Já é quase isso na skill escala-memoria; falta o limite de linhas e o "mostre antes de salvar".
4. Criar `conteudo/roteiro-de-teste-video.md` (ver skill sugerida): lista de checagens aprovadas ANTES de produzir cada vídeo, com casos de limite (palavra com til, número por extenso, 1ª palavra mascarada pelo som de clique, duração > 60 s, legenda cortada pela interface do TikTok, cor sobre o fundo).
5. Varredura do inventado em todo roteiro/legenda de afiliado ou de produto: tabela do que não veio da fonte (número, preço, prazo, "comprovado", depoimento) antes de ir à fila.

## Já coberto nas skills existentes
- `escala-memoria` (Começo/Fim de etapa, passagem.md, aprendizados): já tem o equivalente de "Onde paramos" e de registrar decisões. O livro acrescenta: limite de 10 linhas, "mostre antes de salvar", sinais de sessão que passou do ponto, "regra só na conversa não existe" e o pedido de retomada em até 8 linhas.
- `escala-regras` e CLAUDE.md seção 2 (regras fixas, "enganar não", aprovação do Victor, nunca guardar senha): o livro reforça com mecanismos (deny no settings.json, varredura do inventado, aprovação por escrito guardada com data). Não contradiz nada.
- `escala-editor-video` (conferência por transcrição Whisper e quadros, cf. aprendizados 21/11): é a mesma ideia de "prova em print" do cap. 7; o livro acrescenta roteiro aprovado antes, casos de limite e a tabela OK/Falhou/Não deu para testar.
- `escala-telegram` (aprovação pelo botão vale como "aprova"): coerente com "toda publicação passa pela aprovação" e com o fecho "espere a minha aprovação e publique como o CLAUDE.md manda". O livro acrescenta: permissão se confere no servidor (no worker, validar chat do Victor em toda ação, não só esconder botão) e trocar chave vazada.
- `escala-producao-video` / motor: sem nada do livro sobre vídeo. Só o método de regressão serve (mudar o motor sem quebrar o que funcionava).
- `ui-ux-pro-max` e `omegaprompt`: o livro recomenda a skill `frontend-design` da Anthropic (anthropics/skills, Apache 2.0) e manda **ler o SKILL.md antes de usar** porque a skill pode mandar rodar comandos com as suas permissões (L.6018-6040, L.6056-6063). Regra útil para skills de terceiros que a ESCALA já importou (carrossel, ebook, prompt, ui-ux).

## Skills novas sugeridas ou melhorias

### Nova: `escala-codigo-pratica` (como o agente de código trabalha na ESCALA)
Aciona quando for criar ou mudar código da ESCALA (motor/, telegram/worker.js, ferramentas/), quando uma sessão do Claude Code for passada para outra, quando um teste de vídeo ou do bot for combinado, ou quando algo deu errado depois de uma mudança. NÃO aciona para roteiro, radar ou publicação.
Conteúdo em tópicos:
- Ciclo: ler → plano → "pode seguir" (no caso da fábrica automática, plano curto escrito na passagem) → uma mudança por vez → conferir com prova → salvar versão nomeada → registrar.
- Regra "uma regra por mensagem/commit": cada mudança no motor com `não mude mais nada` e commit próprio com mensagem curta.
- Regressão do motor: antes de mudar voz, legenda, ritmo ou formato, listar o que depende; depois rodar o **vídeo de referência** (parte 1 v2) e comparar tabela item | antes | depois (duração, palavras mascaradas, legenda cortada, volume). Se falhar, parar e avisar.
- Prova obrigatória: "pronto" só com print de quadros + transcrição; quem disser "deve funcionar" refaz.
- Decisões tomadas sozinhas: toda rodada lista no fim as decisões não pedidas (arredondar duração, trocar voz, cortar cena) com alternativa; Victor confirma e entram na skill.
- Segredos: nunca em chat/commit/log; deny no settings.json; trocar se vazar; conferir `git diff --staged` antes de commitar (nenhum token, nenhum e-mail).
- Sessão longa: sinais de que passou do ponto, `/compact`, passar o bastão com "Onde paramos".
- Skill de terceiros: ler antes de usar; perguntar autor, licença, se manda rodar comando ou acessar a internet.

### Nova: `escala-teste-video` (roteiro de teste antes de produzir)
Aciona antes de renderizar qualquer vídeo novo e quando um vídeo flopou por defeito técnico. Conteúdo:
- Modelo de tabela do cap. 7 adaptado: nº | checagem | esperado | onde (celular/TikTok/Reels/Shorts) | Resultado (OK / Falhou / Não deu para testar + motivo).
- Linhas fixas: gancho nos 3 primeiros segundos; 1ª palavra audível (não mascarada por clique); palavras com til e numerais lidos certo; legenda dentro da área segura de cada rede; duração mínima de 60 s se for TikTok pago; etiqueta de IA ligada; aviso de publicidade se afiliado; nada ligado ao Wesley ou ao Victor; nenhum trecho de terceiros com direito autoral.
- Casos de limite: nome muito longo na tela, valor em reais por extenso, fim de parte cortado, cor sobre fundo claro.
- Dados "TESTE": rascunhos e arquivos de teste com prefixo `TESTE-` e apagados antes de ir à fila.
- Prova: transcrição + lista de quadros; "não corrija ainda", achados em ordem de gravidade, o Produtor corrige um por vez.

### Melhorias em skills existentes
- `escala-regras` (seção do checklist): acrescentar item "Varredura do inventado: tabela do que está na legenda/roteiro/página e não veio da fonte (número, preço, prazo, selo, depoimento, promessa). Rodar até voltar vazia. Sem fonte, sai ou vira [FALTA]". Texto sugerido: "Antes de entrar na fila, todo roteiro, legenda, página de venda e post de afiliado passa pela varredura do inventado. O que não vem da fonte registrada sai ou vira [FALTA: ...]."
- `escala-memoria` (seção Fim de etapa): acrescentar "Onde paramos (máx. 10 linhas, no fim de memoria/passagem.md): pronto, pela metade + próximo passo, defeitos conhecidos, decisões do Victor ainda não nas regras. Mostrar antes de salvar." E, no começo: "resumo de retomada em até 8 linhas antes de agir".
- `escala-telegram` (seção do Worker): "Permissão se confere no servidor: o worker valida o chat do Victor em toda ação (aprovar, recusar, produzir), não só esconde botão. Teste com papéis: chat do Victor, chat desconhecido, sem chat. Chave vazada é trocada na hora (FABRICA_KEY)."
- `escala-produto-greenn` e `escala-oferta`: ver livro 14. Do 06 só se aproveita a ficha "Escopo: incluído / não incluído / o que muda o escopo" e a "tabela de acessos" quando houver suporte a cliente de produto.
- CLAUDE.md: seção 5 já pede passagem.md; sugiro incluir ali "Onde paramos".
- Criar `.claude/settings.json` (não existe) com deny de leitura do .env e arquivos de token.

### Não existe no livro (lacuna a preencher noutro estudo)
- **Hooks** (rodar script antes/depois de ferramenta, ex.: bloquear commit com segredo), **tarefas agendadas** (fábrica 7h/12h/17h), **subagentes**/squads e **criação de skills**: o livro remete a "Skills e Squads de Agentes de IA" (L.409). Se esse livro estiver no Drive, vale um leitor dedicado para a fábrica. Registrado aqui para não procurar de novo neste texto.

## Ferramentas citadas (nome, grátis ou preço, para que serve, tem API?)
| Ferramenta | Preço (out/2026, do livro) | Para que serve | API |
|---|---|---|---|
| Claude Code (app, aba Code) | planos pagos: Pro US$ 20/mês (US$ 17 anual), Max a partir de US$ 100; grátis não tem Code | agente de código local, nuvem ou SSH | sim (Claude Console, chave em API keys; Max 5x/20x trazem US$ 100/200 de crédito de API/mês que não cobre uso interativo do Code, L.5387-5397) |
| Comandos `/init`, `/memory`, `/compact`, `/usage`, `/voice` (terminal), `/reload-plugins` | incluídos | rascunho do CLAUDE.md, memória automática, resumir contexto, ver limite, ditado, recarregar plugin | não se aplica |
| Painel Browser com Auto-verify changes | incluído | navegador embutido, prints, cliques, confere sozinho | não |
| Skill `frontend-design` (anthropics/skills, Apache 2.0; plugin `claude-plugins-official`) | grátis | critérios de tipografia, cor, composição | não |
| Git / GitHub Free | grátis (privados ilimitados) | versões nomeadas e cópia do histórico | sim (GitHub) |
| PageSpeed Insights / Lighthouse | grátis | notas Performance, Accessibility, Best Practices, SEO (90+ bom); LCP até 2,5 s, INP até 200 ms, CLS até 0,1 | sim (PSI API, Google) |
| Google Search Console | grátis | propriedade de domínio, sitemap, bloqueios | sim |
| Google Sheets API (conta de serviço) | uso normal sem custo; cota 300 gravações/min/projeto | o sistema escreve em planilha do dono | sim |
| Resend | grátis 3.000 e-mails/mês, 100/dia, 3 domínios; depois US$ 20/mês | e-mail transacional (SPF, DKIM, DMARC) | sim |
| Brevo | grátis até 300/dia com conta aprovada; depois R$ 40/mês | idem, alternativa | sim |
| UptimeRobot | grátis 50 monitores a cada 5 min; depois US$ 10/mês | avisa por e-mail quando o endereço cai | sim |
| Bitwarden | grátis (compartilha com 1 pessoa); Families US$ 47,88/ano | senhas compartilhadas | sim |
| Cloudflare R2 | grátis até 10 GB/mês | cópia fora do servidor | sim (S3) |
| Backblaze B2 | US$ 6,95/TB/mês; 10 GB grátis | idem | sim (S3) |
| Supabase | grátis 2 projetos de 500 MB, pausa em 1 semana sem uso, sem cópia automática; Pro US$ 25/mês | banco + login prontos | sim |
| Neon | grátis até 100 projetos de 1 GB; suspende após 5 min sem uso | Postgres gerenciado | sim |
| PostgreSQL, Caddy (HTTPS automático), Ubuntu LTS | grátis | banco, porteiro HTTPS, sistema | não se aplica |
| Servidor Akamai/Linode SP 2 GB US$ 16,80/mês, 4 GB US$ 33,60; Hetzner 2 GB € 11,99 | pago | VPS | sim |
| Registro.br | ~R$ 40/ano .com.br, DNS grátis | domínio e zona DNS | não |

## Não serve para a ESCALA
- Servidor próprio, SSH, firewall, Caddy, PostgreSQL, cópia diária, túnel SSH (cap. 9 e 10): a ESCALA roda em Cloudflare Workers grátis e tarefas na nuvem; custo perto de zero (regra do CLAUDE.md). Só as ideias de plano de volta e restauração testada interessam.
- Sistema de ordens de serviço com portal, perfis e isolamento (cap. 8 e 11), LGPD de cliente da oficina, controlador/operador: sem clientes de serviço. Reaproveitável só se a ESCALA vender sistema a terceiros (não é a missão).
- E-mail transacional e planilha do dono (cap. 12): só quando houver produto com área de membros e entrega por e-mail; Greenn já entrega.
- Diagnóstico de site de cliente, redesign, publicação em domínio de cliente, termo de autorização, redirecionamentos 301 (cap. 13 a 15): serviço de agência, fora da missão. O termo (L.7392-7451) só inspira se a ESCALA algum dia usar conteúdo de terceiro com permissão.
- Preço, proposta e contrato (livro "Gestor de IA"): não está neste livro.
- Passos de Mac/Windows (instalar app, Finder, Pré-Visualização, Terminal): operação roda em nuvem.
- Hooks, tarefas agendadas, subagentes: não tratados (ver lacuna acima).
