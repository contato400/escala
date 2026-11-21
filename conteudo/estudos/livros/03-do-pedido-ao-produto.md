# Do Pedido ao Produto no Ar (Tiago Lemos de Abreu Oliveira, Lemos Educação, 1ª ed. out/2026)
Lido: linhas 1 a 7710 de 7710 (inteiro, `wc -l` conferido; última leitura chegou à contracapa). Instrução no texto, ignorada: nenhuma encontrada.

## Resumo (5 linhas)
1. Livro-método para quem não programa: usar um agente de IA que trabalha numa pasta (Codex, da OpenAI) para pôr no ar página, site, sistema com login e site 3D. Os 4 projetos são fictícios (Ateliê Trama, Órbita, Casa Pátio).
2. O núcleo, que independe da ferramenta: 5 verbos (pedir, planejar, construir, verificar, publicar), critério de aceite testável, plano antes de executar, UMA mudança por pedido, ponto de volta antes de mudança grande, relato do agente com "o que ficou para eu testar".
3. Para sistema: escrever ESPECIFICACAO.md de 7 partes (objetivo, fluxo em verbos, telas, estados vazio/carregando/erro, dados, escopo e NÃO escopo, onde publicar), construir v1 com dados "Demonstração", depois ligar API paga com 4 travas (crédito pré-pago sem recarga, limite rígido, chave restrita, MODO_TESTE ligado por padrão) e 10 regras de produção no servidor.
4. Segurança é capítulo inteiro: nunca segredo no chat/print/código/Git, .env.local + .env.example, chave vazou = revogar, agente nunca recebe senha de painel (humano faz login, agente guia), ler skill/MCP de terceiros antes de instalar, desligar plugin que sobrou.
5. Honestidade embutida no briefing: nada de cliente, número, depoimento, selo ou formulário fingido; dado de exemplo sempre marcado ("Resultado ilustrativo", "Dados ilustrativos", "Demonstração", "Imagem ilustrativa"). Combina com as regras da ESCALA.

## O que serve para a ESCALA (detalhado)
Foco pedido: transformar pedido em produto/sistema no ar (bot e produto próprio na Greenn) e rotinas/documentos automatizados. Os números de linha referem-se ao arquivo `03 - Do Pedido ao Produto no Ar.txt`.

Livro sobre o Codex (agente da OpenAI) que constrói páginas, sites e sistemas numa pasta do computador, sem programar. Os 4 projetos: página interativa, site institucional (GitHub+Vercel+domínio), banco de criativos com login (Supabase+API de imagem com teto de gasto), site 3D em hospedagem cPanel. O método é independente de ferramenta; o que serve é o PROCESSO de pedido, critério de aceite, segurança e rotinas.

### Cap 1 (l.412-760): método e critério de aceite
- Método em 5 verbos (l.280): pedir (objetivo + referências + critério), planejar (agente propõe, você corta o que não pediu), construir, verificar (você mesmo clica/testa), publicar (com caminho de volta).
- Divisão: humano define objetivo, referências, critério de aceite, aprova plano/permissões e dá palavra final; agente planeja, executa, confere o que dá e RELATA o que mudou, como testou e o que sobrou para o humano (l.471-478).
- MODELO 01 "Pedido com critério de aceite" (l.541-555): Objetivo / Referências / Está pronto quando (1. ação de teste -> o que tem de acontecer; 2. idem; 3. no celular; 4. Não pode) / Fora desta etapa / "Antes de executar, mostre um plano curto e espere aprovação. Ao terminar, relate o que mudou, como conferiu cada item e o que ficou para eu testar."
- Critério vago vs verificável (l.503-522): "fica bonito no celular" vira "título e botão principal aparecem sem rolar a tela". Regra: mínimo 4 itens testáveis sim/não (um de clique, um de conteúdo, um no celular, um do que NÃO pode acontecer).
- "Bonito não é pronto" (l.593-610): agente erra e às vezes dá por testado o que não testou. Verificação final é do humano: formulário com dado de teste, clicar todo botão/link, abrir no celular de verdade, ler cada texto e número; dado de exemplo marcado como ilustrativo.
- Ao falhar: dizer QUAL item falhou e o que viu; "não ficou bom" não corrige (l.616).
- Ajustar: uma correção por vez e dizer o que preservar (l.569-572).

### Cap 2 (l.769-1190): ambiente (Git, Node, Python, GitHub, Vercel, Supabase)
- Conferência pedida ao agente em tabela "item | o que encontrou | pronto sim/não | próximo passo", sem instalar nada e esperando autorização (l.1062-1081). Padrão reaproveitável: auditoria só-leitura antes de mexer.
- Pasta do livro com uma subpasta por projeto, cada uma com LEIA-ME de 3 linhas (nome, o que publica, capítulo) (l.1128-1135).
- Contas: GitHub com verificação em 2 etapas, repositório privado, Vercel/Supabase entrando por "Continue with GitHub". Limites (out/2026): Vercel Hobby só uso pessoal NÃO comercial (Pro US$20/mês); Supabase Free até 2 projetos e pausa após 1 semana sem atividade (l.1035-1043). ATENÇÃO para a ESCALA: se um dia usarmos Vercel para página de venda comercial, Hobby não vale; Cloudflare Pages/Workers (que já usamos) é grátis e permite uso comercial.

### Cap 3 (l.1192-1540): AGENTS.md, ANDAMENTO.md, retomada, tarefa agendada
- Chat comum NÃO cria arquivos; agente de pasta cria. Um projeto = uma pasta; nunca abrir pasta pessoal inteira (l.1280-1283). Um chat por frente de trabalho, com nome (l.1309-1315).
- AGENTS.md na raiz (equivalente ao nosso CLAUDE.md), até 40 linhas, 8 regras (l.1381-1401): projeto em 1 frase; responder em português simples e explicar termo técnico em 1 frase; plano curto antes de mudança grande e esperar "pode seguir"; preservar arquivos do dono (trabalhar em cópia); não instalar sem dizer para quê; não publicar nem enviar ao GitHub/Vercel sem pedido explícito; nunca abrir/mostrar .env, só nome da variável; ao fim de cada tarefa atualizar ANDAMENTO.md (data, feito, falta, próximo passo).
- COMANDO 02 "Retomar projeto" (l.1447-1453): ler AGENTS e ANDAMENTO, ver Git (últimos registros e alterações não salvas), listar arquivos principais; NÃO instalar nem reconstruir; responder em até 10 linhas: onde paramos, o que falta, se algo diverge do ANDAMENTO, próximo passo; esperar confirmação. (Equivale ao nosso memoria/passagem.md.)
- Tarefa agendada: roda sem supervisão com permissões padrão; começar por tarefas SÓ LEITURA que escrevem relatório (l.1461). Exemplo COMANDO 03 (l.1483-1487): abrir o site, conferir todos os links e imagens, criar relatorios/links-AAAA-MM-DD.md com cada link quebrado (endereço, página, erro) ou "Nenhum link quebrado"; se não abrir, escrever o motivo e parar. Frequência semanal.

### Cap 4 (l.1541-1900): modelo, esforço, limite
- Classificar o pedido: mudança ESTRUTURAL (seção nova, integração, 3D) vai para o modelo mais capaz com modo plano; AJUSTE FINO (cor, borda, frase) vai para o modelo mais barato (l.1629-1640). Subir esforço um nível por vez só quando a resposta esquecer parte do pedido, quebrar o que funcionava ou for raso (l.1625-1628).
- Pedido de ajuste fino delimitado (l.1663-1665): "Em [ARQUIVO], mude só [O QUE] para [COMO]. Não altere o que eu não citei, não instale nada, não crie arquivos. Ao terminar, liste arquivos alterados e onde vejo."
- Pedido de plano (l.1690-1695): o que muda em até 5 passos + arquivos; o que pode quebrar e como evita; o que fica de fora; a menor primeira etapa aprovável. "Não instale nem crie arquivos até eu aprovar." Aprovar só a primeira etapa.
- Modo rápido gasta 2,5x mais limite; ligar só com prazo. Medir tarefa pela % do painel antes e depois (l.1733-1737).
- Limite baixo (COMANDO 03, l.1796-1802): pedir 3 partes sem executar: menor mudança que mantém funcionando; o que preparo sozinho até renovar; pedido completo para depois. Ideia para nós: quando a cota da fábrica estiver baixa, só ajuste fino/planejamento.
- Assinatura x API têm cobranças separadas; sistema publicado gasta API mesmo com o agente fechado (l.1804-1830). Vale para nós: Workers AI grátis vs Higgsfield pago.
- Preços out/2026: ChatGPT Plus R$99,90; Go R$39,99; Pro desde R$525. Codex no Plus: 5 a 45 mensagens locais por janela de 5h no modelo topo, 350 a 3000 no leve (l.1755-1760).

### Cap 5 (l.1907-2270): permissões e segredos (MUITO ÚTIL)
- Quatro hábitos: limitar alcance, ler antes de aprovar, salvar pontos de volta (commit), segredo no lugar certo (l.1929-1931).
- Tabela de decisão de comando (l.1992-2010): npm install = aprovar só desta vez; git push = aprovar se pediu; sudo/rm -rf/caminho fora da pasta = negar e perguntar. Preferir o escopo mais estreito ("só desta vez").
- Seção Segurança do AGENTS.md (l.2020-2050), 7 regras: trabalhar só na pasta; explicar em 1 frase o que o comando faz e se desfaz antes de pedir aprovação; nunca pedir senha/chave/token/código no chat (dizer nome da variável e onde digitar); não ler/mostrar .env; chave secreta só em código de servidor; pedir confirmação antes de publicar/enviar ao GitHub/apagar/instalar; criar ponto de volta antes de mudança grande.
- Ponto de volta (l.2069-2072): commit com .gitignore conferido (.env, .env.local, .env*.local, node_modules, builds), listar arquivos que entram, descrição "[o que está funcionando agora]", não enviar nada ao remoto. Voltar (l.2093-2096): sem mudar nada, mostrar o que mudou, listar os 5 últimos pontos, esperar escolha, dizer o que se perde, voltar SEM apagar histórico e sem tocar em arquivos ignorados.
- Segredos: chave pública (pode ir ao navegador) x secreta (só servidor). Código lê variável de ambiente (OPENAI_API_KEY); valores só no .env.local; .env.example com nomes sem valor vai ao Git; no servidor, nas variáveis do serviço de deploy (l.2119-2128). Comando 04 (l.2156-2163): criar .env.local sem valor, .env.example com um comentário por linha (serviço e se é pública/secreta), .gitignore correto; "depois que eu preencher, não abra nem mostre". O humano digita o valor e escreve só "Preenchi o .env.local".
- Entrar nas contas você mesmo; nunca arquivo com senha do painel para o agente publicar sozinho (l.2172-2177). Revogar apps autorizados que não usa.
- Chave vazou (l.2199-2220): apagar mensagem não adianta, Git guarda histórico; só REVOGAR. Ordem: revogar, criar outra com menor permissão, trocar nos lugares (.env.local, variáveis do servidor), publicar de novo (na Vercel variável nova só vale para deploy novo), conferir uso/gasto nos dias seguintes. Crédito pré-pago baixo e sem recarga automática limita estrago.
- Print com chave: o chat lê imagens; conferir captura antes de enviar.

### Cap 6 (l.2275-2690): primeira página por voz
- Ditado com 5 blocos nesta ordem: o que explica, para quem, identidade visual, tom, o que o visitante pode fazer; fechar com "o que NÃO pode ter" e "mostre um plano antes de qualquer arquivo; não crie arquivos ainda" (l.2341-2348, 2385-2387). Ler a transcrição antes de enviar: nomes próprios, números e negações erram ("não" perdido inverte regra) (l.2393-2396).
- Corrigir o plano: dizer só o que muda e aprovar o resto; conferir 4 pontos: seções e ordem, lista de imagens, lógica do simulador, o que ficou de fora (l.2418-2424).
- IMAGENS COM PEDIDO GUARDADO (l.2458-2487): cada PNG tem um .txt do mesmo nome com o prompt COMPLETO palavra por palavra, data e ferramenta; serve para refazer uma imagem, manter o mesmo estilo na próxima e saber a origem. "Estilo comum" declarado uma vez para todas as imagens do lote; "sem texto, sem logotipo, sem rosto reconhecível". Conferir cada imagem grande: letras inventadas, mãos com dedos a mais, luz diferente. Refazer só uma: "Refaça X a partir do X.txt com [mudança]. Atualize o .txt."
- Lista de avaliação da v1 (l.2553-2620): mensagem (5 segundos dizem o que oferece), hierarquia (título, subtítulo, uma ação principal), legibilidade, celular (360 px), botões e simulador, números com "Resultado ilustrativo". Revisão pedida ao agente SEM alterar arquivo, tabela item | ok/problema | onde | como conferiu, e no fim "o que só eu posso julgar" (l.2631-2636). Contraste mínimo 4,5:1. Máximo 3 correções por rodada.
- Regra de conteúdo: não inventar preço, depoimento, número de alunos (l.2385). (Combina com nossa regra "enganar não".)

### Cap 7 (l.2691-3070): evoluir sem recomeçar
- Ponto de volta antes de cada mudança estrutural; UMA mudança por pedido; se quebrar, volta ao ponto (l.2720-2724, 3043-3044).
- Pedido de recurso novo com 5 regras de proteção (l.2792-2807): versão leve no celular; respeitar "reduzir movimento"; carregar só quando a seção chega perto da tela e pausar fora; se falhar, imagem estática com texto alternativo; não mudar o resto. Sempre: plano curto primeiro, e "diga como conferir cada regra".
- Gráfico (l.2839-2852): dado de exemplo leva "Dados ilustrativos" abaixo; valor escrito em cada barra; contraste 3:1; animação roda uma vez em menos de 2 s.
- Ajuste pelo "Annotate": clicar no elemento na prévia e escrever o pedido (l.2881-2883).
- Três níveis de visibilidade: prévia local (só você), link de teste (conforme compartilhamento), página publicada (qualquer um) (l.2906-2937). Antes de mandar link, conferir com quem está compartilhado.
- Pedido "deixar leve e conferir no celular" (l.2984-2993): converter imagens para WebP/AVIF no tamanho exibido guardando originais; 3D só perto da tela; erros no console; relatório com peso antes e depois. Teste no celular real: rolar, tocar, reduzir movimento, Tab com contorno visível.

### Cap 8 (l.3074-3465): skills
- Skill = pasta com SKILL.md (nome + descrição no topo) + referências (lidas só quando preciso) + scripts. O agente lê só nome e descrição de todas e abre o resto ao decidir usar; "a descrição manda": vaga, chama na hora errada ou nunca (l.3123-3136). Reforça nossa regra: descrição com "Aciona quando... NÃO aciona para...". Correção de skill na hora errada: pedir descrição nova com "Use quando..." (l.3440).
- 5 PERGUNTAS ANTES DE INSTALAR SKILL DE TERCEIRO (l.3204-3233): quem fez (autor/histórico)? o que lê (pastas)? o que executa (scripts um a um)? envia dados para fora (URLs, upload, pedido de chave)? licença permite o uso? Instalações não provam segurança. Comando 02 (l.3254-3261) manda ler a skill inteira sem executar e responder esses 5 pontos + riscos.
- Skill gravada/criada deve ter: nome, descrição com "Use quando", passos, pasta de origem e prefixo INFORMADOS A CADA USO (sem caminho fixo), nunca apagar/alterar original, parar e perguntar se o arquivo já existe, nada sai do computador, no fim listar arquivos criados com tamanho antes/depois (l.3329-3342). Testar a skill em chat novo, com cópias, depois de criar (l.3352).
- Skill de publicação cPanel: login do humano digitado no painel; nenhuma senha em chat/arquivo; raiz do domínio conferida antes do envio; backup antes de substituir; publicação só confirmada depois de aberta por HTTPS (l.3415-3418).

### Cap 9 início (l.3469-3600): plugins/MCP
- Plugin = pacote com servidor MCP (+ skills). Cada plugin é também um acesso: fim do capítulo manda desligar o que sobrou. Tabela acesso/cuidado/capítulos (l.3565-3600). Cada servidor MCP ligado pesa no limite de uso (l.1733).

### Cap 9 (cont., l.3600-3890): plugins/MCP na prática
- Conectar só o necessário agora; cada servidor MCP ligado soma contexto e gasta limite (l.3616-3618). Ao autorizar, ler a conta, o que poderá fazer e o alcance; escolher o menor alcance (l.3620-3624).
- Pedido de animar imagem (l.3669-3676): arquivo de entrada nomeado, duração, resolução, "autorizo enviar só esse arquivo", movimento descrito, "câmera parada, luz igual, sem texto, pessoas ou objetos novos", "ANTES de gerar diga o modelo e quantos créditos custa e espere meu ok", salvar em videos/x.mp4 com x.txt (prompt, modelo, data), "não altere a página". Assistir até o fim procurando dedos a mais, peça mudando de forma, luz piscando; refazer mudando UMA coisa. Útil para nós no Higgsfield/Kling: sempre pedir custo antes e guardar o prompt.
- Higgsfield por plugin/MCP exige assinatura paga; grátis ilimitado só no site (l.3683-3685). (Nós já temos o MCP do Higgsfield; regra: só gastar quando houver lucro.)
- Catálogo de produto (l.3712-3721): âncora na foto de referência ("mantenha forma, proporção, cor, esmalte e detalhes exatamente como na foto"), "sem texto, logotipo, pessoas ou objetos de marca", e NÃO reescrever descrição para driblar filtro do gerador: troque produto/cena (l.3704-3706). Alinha com nossa regra de não enganar (produto real igual à foto).
- Publicar na Vercel (l.3757-3762): primeiro prévia; enviar só arquivos usados; lista do que NÃO sobe (referências, catálogo, vídeos, testes, .git, AGENTS.md, ANDAMENTO.md, .txt de pedidos, originais, segredos); "liste o que vai subir e espere meu ok". Teste: abrir no celular fora do Wi-Fi e sem login; se pedir login, ainda não é público. Produção só quando pede.
- Adicionar MCP por endereço (l.3795-3801): copiar o endereço SÓ da documentação oficial (servidor desconhecido recebe o que o agente manda e pode devolver instruções escondidas). Tipos: Streamable HTTP (endereço) e STDIO (programa local). Se pedir chave, não colar no chat.
- COMANDO 04 "Listar plugins conectados e o que cada um acessa" (l.3835-3837): serviço, conta, o que consegue fazer, se este projeto usou, quais posso desligar; não desligar nada. Rodar ao fim de cada projeto ou mensal. Fechar também o lado do serviço (apps autorizados).

### Cap 10 (l.3892-4310): briefing de site em 6 blocos + honestidade (MUITO ÚTIL para produto/página de venda)
- Agente preenche lacunas com o que sites costumam ter: "+200 empresas", depoimentos falsos, formulário que agradece sem enviar (l.3902-3906). O briefing fecha as lacunas.
- Seis blocos (l.3956-4026): Objetivo (UMA ação principal; "levar o visitante a pedir diagnóstico"), Público (específico), Conteúdo (seções nomeadas na ordem), Estilo visual (decisões concretas: "azul profundo, branco, detalhe em verde"; "moderno e bonito" deixa o agente escolher), Requisitos (360 px, todo botão com destino, contraste 4,5:1, foco visível, alt text), Plano curto (mostrar e esperar aprovação).
- REGRAS DE HONESTIDADE (l.4030-4040, 4094-4099): não inventar clientes, depoimentos, números, logotipos, prêmios, selos; não criar formulário que finge enviar; sem canal de contato real, o botão avisa que está em configuração e o agente explica o que falta conectar. Rosto gerado por IA no lugar do dono também é invenção; foto só do dono ou licenciada.
- Ao ler o plano: conferir seções/ordem, procurar número ou promessa que você não deu, botão principal, uso da foto, o que ficou fora. Corrigir tudo numa mensagem e aprovar o resto (l.4134-4136).
- Avaliar v1 como visitante, 4 itens (l.4163-4220): proposta de valor em 5 segundos (sem "soluções inovadoras"), ação principal (nenhum botão concorrente), honestidade (procurar números/nomes/selos/"mensagem enviada" sem canal), acessibilidade básica (contraste sobre foto, Tab). Comando 02: comparar com o briefing bloco a bloco, tabela, e "aponte as 3 partes que mais parecem modelo pronto".
- Lista de até 5 pontos genéricos, cada um: problema, efeito desejado, onde (l.4259-4261). Ponto de volta "v1 do site".
- Correções prontas: "Remova todo número, cliente e depoimento que eu não forneci"; "Remova o formulário; sem canal, o botão só avisa" (l.4265-4272).

### Cap 11 (l.4313-4680): refino em cadeia, GitHub, Vercel, domínio
- Refino em cadeia (l.4366-4394): para problemas de CONJUNTO, um pedido só listando pontos "[SEÇÃO]: [PROBLEMA]. Quero [EFEITO]", com regras de manter textos/cores/honestidade e plano antes. (Ajuste fino = um por pedido; conjunto = em cadeia.)
- Refazer foto mantendo reconhecível (l.4419-4431): gerar 2 opções lado a lado, esperar escolha, original fora do Git (dado pessoal). Para nós: personagens fictícios, não rosto do Victor.
- Fluxo de publicação (l.4435-4527): repositório privado; ponto de volta; só o branch main é produção; mudanças vão num branch com prévia de endereço próprio; aprovação antes de ir ao main. COMANDO 04 "Publicar a próxima alteração" (4 passos: branch novo sem tocar no main; passar a prévia e esperar aprovação; aprovada, leva ao main e confirma produção; se a prévia falhar, explicar e não tocar no main). É o mesmo princípio da nossa fila de aprovação, aplicado a deploy.
- Rollback (l.4550-4557): voltar primeiro, investigar depois; rollback troca o que está no ar mas o código ruim continua no repositório; corrigir antes do próximo envio; depois do rollback o deploy automático pode parar.
- Domínio (l.4560-4572, 4595-4599): registrar no nome do dono com renovação automática; Vercel mostra registros A (raiz) e CNAME (www); .com.br R$40/ano no Registro.br; DNS demora; HTTPS vem depois do DNS bater. COMANDO 05 conferir domínio: ambos abrem por HTTPS, redirecionam, e nenhum link canônico/imagem de compartilhamento ainda usa .vercel.app.
- Erro: envio ao GitHub que não publica = projeto Vercel não ligado ao repo; domínio sem cadeado = registro CAA ou DNS ainda espalhando.

### Cap 12 (l.4683-5050): ESPECIFICAR o sistema antes de construir (MUITO ÚTIL: "pedido vira sistema")
- Pedido vago ("um sistema para gerar criativos") faz o agente decidir equipe, pagamento, editor sozinho e esquecer estados (l.4697-4701). Solução: escrever um arquivo de especificação de 7 partes que o agente lê antes de cada mudança.
- Problema em 1 frase + fluxo principal em VERBOS ("entrar -> preencher ficha -> escrever pedido -> gerar -> ver ampliado -> aprovar/descartar -> baixar -> consultar galeria -> ver uso do mês"). Cada verbo vira uma tela/botão; verbo que não resolve o problema fica fora (l.4750-4761).
- COMANDO 01 Entrevista (l.4784-4794), com /plan: "me entreviste até 10 perguntas, UMA POR VEZ, cada uma com sugestão de resposta e motivo; cubra quem usa, telas, estados (carregando, vazio, erro), dados, o que fica de fora, onde publicar, ferramenta de referência. No fim entregue a especificação em 7 partes e liste o que ficou indefinido. Não crie arquivos nem escolha tecnologia." Referência: citar ferramenta ou anexar prints seus sem dados de clientes (organiza telas; estilo vem da ficha da marca).
- MODELO ESPECIFICACAO.md, 7 partes (l.4858-4879): 1 Objetivo e quem usa; 2 Fluxo; 3 Telas; 4 Estados (carregando, vazio, erro, com mensagens); 5 Dados (campos de cada entidade); 6 Escopo da v1 + NÃO escopo (mínimo 3 itens); 7 Onde publicar (parte do servidor separada da tela para nenhuma chave chegar ao navegador).
- COMANDO 02 gravar e revisar (l.4888-4891): gravar o texto sem mudar; revisar apontando contradições, passos do fluxo sem tela, telas sem uso no fluxo e perguntas a responder antes da v1. Só construir quando a revisão não apontar nada que mude uma tela.
- Demonstração SEMPRE marcada com selo "Demonstração"; entrada sem senha; Gerar devolve imagem desenhada em código sem chamar serviço (l.4909-4913). Depois vira o "modo de teste".
- COMANDO 03 construir v1 só interface (l.4926-4936): telas com os 3 estados; dados de demonstração num único arquivo; aviso "Acesso de demonstração: login não ligado"; seletor de estado só na demo para ver vazio/carregando/erro; estrutura com lugar separado para servidor; "não conecte banco nem API, não crie chaves, não instale serviço pago"; funcionar em 360 px.
- COMANDO 04 conferir telas e estados (l.4969-4972): tabela tela/estado | existe | como chego | o que falta; selo em todo dado demo; nenhuma tela pede senha ou chama serviço externo; algo do não escopo apareceu?; correções por importância, esperar escolha.
- COMANDO 05 registrar decisões no AGENTS.md (l.4997-5003): antes de qualquer mudança ler a especificação e dizer que parte afeta; pedido no não escopo = avisar e esperar; se aprovado, atualizar a especificação ANTES do código; "nunca simule login ou geração como se fossem reais". AGENTS é lido em todo chat; a especificação só quando mandam: liga os dois.
- Erros: v1 parece pronta demais (aceita qualquer senha), escopo cresceu, estado ausente (tela em branco com galeria vazia) (l.5006-5014).

### Cap 13 (l.5053-5400+): API paga sem conta surpresa
- QUATRO TRAVAS ANTES DA PRIMEIRA IMAGEM PAGA (l.5081-5083): (1) crédito pré-pago SEM recarga automática (o saldo é o teto da conta; com recarga, erro ou chave vazada compra crédito novo no cartão); (2) projeto separado com limite mensal rígido ("Enforce hard limit") + alerta na metade; corte não é instantâneo, então manter crédito baixo e as duas travas juntas; (3) chave restrita (só o recurso de imagem, nome descritivo, validade se houver), digitada pelo humano no .env.local; (4) MODO_TESTE ligado por padrão.
- Números (out/2026): compra mínima US$5 (padrão US$10), crédito vence em 1 ano; recarga automática vem ligada, desligar; saldo zero devolve erro credit_balance_exhausted, limite do projeto project_spend_limit_exceeded (l.5135-5142). Custo de imagem (quadrado): ~US$0,006 low, ~US$0,013 medium, ~US$0,053 high (l.5324-5326). Modelos citados: gpt-image-2.5-flare e gpt-image-2.5-sunburst. (Comparar com FLUX grátis do Cloudflare Workers AI.)
- COMANDO 01 ligar API com modo de teste (l.5217-5234): conferir documentação oficial antes de programar; rota de servidor; qualidade rascunho=mais baixa, final=intermediária; servidor junta o pedido à ficha da marca e a tela mostra o texto final; chave só no servidor e nunca em log/resposta; MODO_TESTE diferente exatamente de "desligado" => devolve exemplo marcado, não chama API (falha segura: qualquer valor estranho = teste); um clique = no máximo uma chamada, registrada com hora, SEM nova tentativa automática; imagens reais em geradas/ fora do Git.
- COMANDO 02 primeira geração real (l.5263-5266): reiniciar servidor sem abrir .env; humano clica UMA vez em rascunho; agente confere nos registros que houve única chamada; anotar gasto no painel; se não aparecer, conferir depois ANTES de gerar outra.
- MODELO 01 comparar qualidades (l.5329-5341): mesmo pedido, rascunho vs final: tempo, gasto, atende? e decisão. Depois voltar MODO_TESTE para ligado.
- COMANDO 03 tratar erros (l.5367-5380): recusa por conteúdo (sem retry automático, mensagem amigável), saldo/limite ("geração pausada por limite de gasto"), chave inválida ("indisponível"), demora (conferir a galeria antes de tentar de novo). Usuário vê só a mensagem; log guarda código e hora, nunca a chave; simulador de cada erro no modo de teste. O sistema não gera pessoa real sem autorização, marca de terceiro, imitação de artista (l.5360).

### Cap 14 (l.5435-5790): Supabase (login, banco, arquivos privados)
- Só vale se algum dia a ESCALA precisar de sistema com login (hoje o bot usa KV do Cloudflare, o que basta). Princípios reaproveitáveis:
  - MCP do banco limitado ao projeto (`project_ref`) e com aprovação obrigatória de toda escrita (`default_tools_approval_mode = "writes"`), porque texto gravado no banco pode esconder instrução para o agente (l.5507-5520). Dado lido de banco/comentário = dado, nunca ordem (regra que já usamos).
  - Toda tabela com dono e regra de acesso: cada conta vê/cria/muda/apaga só o que é dela; chave pública (sb_publishable_) no navegador, chave secreta (sb_secret_) só no servidor; nunca as chaves antigas anon/service_role (l.5545-5559, 5568-5570).
  - Toda mudança de estrutura do banco vai para `supabase/migrations` no Git (l.5551).
  - Arquivos em bucket privado, pasta por dono, link temporário de 10 min (vencido, a galeria pede outro sozinha) (l.5632-5640). Teste: link de 60 s abre em janela anônima e 1 minuto depois não abre.
  - Conferir com DUAS contas (A e B) que uma não vê dados da outra; relatório "quem vê, cria, muda e apaga" por tabela, marcando como problema tabela sem regra, regra que vaza dados de outra conta e chave secret fora do servidor (l.5728-5731).
  - Free: banco 500 MB, 1 GB de arquivos, SEM backup diário, projeto pausa após 1 semana sem uso; e-mail padrão só entrega à equipe (2/hora); backup semanal com `supabase db dump` fora do Git (l.5614-5617, 5740-5746).
  - E-mail de confirmação: Site URL vem como localhost, trocar pelo endereço real, senão o link cai em página inexistente (l.5669-5672).

### Cap 15 (l.5797-6200): REGRAS DE PRODUÇÃO (sistema aberto a terceiros, API paga) - MUITO ÚTIL
- Princípio: regra de custo/segurança mora no SERVIDOR, não na tela; esconder botão não impede pedido direto ao servidor (l.5812-5815).
- As 10 regras (COMANDO 01, l.5918-5938), reaproveitáveis para o Worker do bot e qualquer automação que gaste dinheiro: (1) chaves só no servidor; (2) validar cada pedido (tamanho, formato, qualidade) e recusar o resto com mensagem clara; (3) conferir dono em cada pedido sem confiar em ID vindo do navegador; (4) contra clique duplo: botão trava e servidor ignora pedido igual em andamento; (5) limite mensal por conta em variável (falhas também contam, porque o provedor pode ter cobrado; no limite, avisa e NÃO chama a API); (6) cadastro só para lista de e-mails permitidos, valendo no banco e no servidor; (7) erro/recusa/timeout viram "falhou" sem detalhe técnico; (8) "processando" há mais de 10 min vira "falhou"; (9) ao recarregar, status volta do banco; (10) fora da produção o modo de teste fica ligado. Entregar tabela "regra | onde está no código | como conferir sem gastar crédito".
- Variáveis por ambiente: Production x Preview; chave paga SÓ em Production; Preview com modo de teste ligado (nada cobrado); chave de produção diferente da local (troca uma sem parar a outra); tipo Secret (ninguém lê depois) (l.5958-6060). Variável nova só vale em deploy novo (Redeploy).
- Roteiro de teste em produção SEM gerar nada (COMANDO 03, l.6102-6110): rotas recusam pedido sem login; nenhuma chave secreta nos arquivos baixados pelo navegador; e-mail fora da lista não cria conta nem direto no banco; lista de itens com resultado esperado e coluna para marcar. Limite de teste = 1 para provar o bloqueio com uma geração só. Escolher limite: limite x contas x custo por imagem cabe no teto de gasto.
- Rotina semanal depois do lançamento (l.6125-6131): gasto do projeto (gasto sem criativo na galeria = investigar), banco/arquivos perto do limite do plano + cópia semanal, itens em "falhou". Trocar chaves de tempos em tempos, com validade.
- Geração de vídeo passa do tempo da função: iniciar a geração, guardar status, buscar resultado depois (assíncrono) (l.6147-6149).
- Se abrir para outras pessoas (l.6150-6157): termos de uso curtos + página de privacidade (dados guardados, para quê, por quanto tempo, quem recebe, como pedir acesso/correção/exclusão), citar tratamento fora do Brasil, canal de contato (LGPD arts. 9, 18, 33; Resolução CD/ANPD 2/2022). Importante se a Greenn/página de venda coletar e-mail. Não é orientação jurídica.
- Exercício "tente furar as regras" (l.6186-6191): e-mail fora da lista, 3 cliques rápidos (deve virar 1 criativo), passar do limite.

### Cap 16 (l.6211-6630): site 3D por rolagem com Blender via MCP
- Ficha de cômodos a partir da planta: antes de modelar, o agente transforma a referência em tabela e lista "o que a referência NÃO diz" com sugestão para cada item; o humano decide; o agente marca "suposto" o que deduziu (l.6308-6312). Padrão para qualquer referência (vídeo viral, planta): extrair ficha + lacunas, humano decide, só então produzir.
- Pedido de 3D em 6 partes (l.6432-6453): resultado, exigência central (fachada e interior = mesma cena), acabamento, câmera (altura de pessoa, só por portas, pausa em cada ambiente, parar de rolar para a câmera), ferramenta (salvar .blend antes de cada etapa, mostrar vista de cima nomeada e esperar aprovação), site só DEPOIS do 3D aprovado.
- Corrigir erro de modelagem: UM por pedido, "Em [cômodo], [o que está errado]. Deve ficar [como], como na planta. Salve antes. Não mexa em outros cômodos. Mostre antes e depois." (l.6480-6482).
- Exportar leve: .glb com Draco/Meshopt, texturas WebP, sem objetos que a câmera não vê, modelo simples no celular, fallback se o 3D falhar; "não existe número oficial de peso para o celular: teste num aparelho comum" (l.6491-6518).
- Panorâmicas 360 (2:1) renderizadas no Blender (Cycles) e melhoradas por IA preservando geometria, marcadas "Imagem ilustrativa"; refazer só a faixa com emenda (l.6523-6564).
- Blender 5.2.2 LTS grátis; MCP for Blender (ahujasid/mcp-for-blender, terceiros, código aberto, telemetria ligada por padrão: `DISABLE_TELEMETRY=true`) executa código dentro do Blender: instalar só pela página oficial e salvar antes de cada pedido (l.6352-6367). Instalação: `uvx mcp-for-blender install-addon`; Codex: servidor STDIO `uvx mcp-for-blender`.

### Cap 17 + Apêndices (l.6634-7710): hospedagem cPanel, skill publicar-cpanel, listas
- Vercel x cPanel (l.6704-6741): Vercel publica a cada push e tem rollback; cPanel é ZIP + backup antes de cada troca, serve vários sites e e-mail. Hospedagem compartilhada NÃO roda Node.js; site estático e 3D rodam no navegador do visitante (l.6762-6771).
- Não presumir `public_html`: a raiz de cada domínio é a coluna Document Root; subdomínio por registro A ao IP da hospedagem; NÃO trocar nameservers (derrubaria o site principal); só ligar "Force HTTPS" depois do certificado válido (l.6778-6792).
- Entrega ao agente de tarefa que exige login: humano entra, agente guia "um passo por vez, espere eu dizer feito"; nunca senha/token/código no chat nem em arquivo; FTPS só com conta limitada à pasta e senha digitada em campo oculto (getpass) (l.6866-6903, 7250-7260).
- Ordem fixa: pacote -> acesso -> publicar -> conferir. "Publicado" só depois de abrir o endereço final por HTTPS; ZIP no computador não é site publicado; conferência de que nenhum ZIP, backup, inventário ou .env abre pelo endereço público; registro local publicacoes.md (data, versão, domínio, pasta remota, SHA256 do ZIP, backup, resultado, sem credencial) (l.7219-7224).
- Script `empacotar.py` (l.7304-7396): recusa pacote sem index.html, com ZIP dentro do build, nome repetido, `.env`, node_modules, tipo de arquivo que site estático não usa (.blend) ou padrão de chave (`sk-...`, `sb_secret_`, PRIVATE KEY); gera inventário .json com SHA256 por arquivo. A ideia (varredura de segredos antes de empacotar/publicar) vale como `ferramentas/` na ESCALA antes de qualquer commit/publicação. Não rodei o código.
- Skill escrita como exemplo de boa estrutura (l.7162-7224): descrição com "Use quando... Não serve para..."; seção "Regras que nunca mudam" numeradas; "Modos" (só pacote / guiada / conferência / atualização); passos numerados; seção "Quando faltar algo: entregue o pacote e diga o que falta"; referências em arquivos separados lidos só na etapa que precisa.
- Apêndice C, listas de conferência (l.7437-7471): Segredos e chaves; Antes de publicar um site (todo botão/link com destino real, nenhum dado que você não forneceu, exemplos marcados, ponto de volta, lista do que vai subir revisada); Antes de abrir sistema a outros (regras no servidor com conferência sem custo, convite, limite por conta, 2 contas testadas, crédito baixo sem recarga, limite rígido, privacidade); Antes de substituir site na hospedagem (raiz do Document Root, backup fora do servidor, ZIP com versão e lista do que muda/entra/sai).
- Apêndice D solução de problemas: formato "sintoma. causa provável (onde está a correção)" (l.7478-7525). Bom formato para um futuro `memoria/problemas.md`.

## ADAPTAÇÃO PARA A ESCALA: do pedido do Victor ao produto no ar
O fluxo do livro, traduzido para o bot do Telegram e para o produto próprio na Greenn (fase 2):
1. PEDIDO: o Victor manda no Telegram (voz ou texto) uma ideia ("quero um e-book sobre golpes"). O chefe responde com o MODELO 01: objetivo, referências, "está pronto quando" (mínimo 4 itens sim/não: um de clique, um de conteúdo, um no celular, um do que NÃO pode acontecer), fora desta etapa. O Victor só corrige o que sair errado.
2. ENTREVISTA (ideia vaga): até 10 perguntas, UMA por vez, cada uma com sugestão e motivo, no Telegram com botões Sim/Não/Outro (l.4786). Fecha com ESPECIFICACAO de 7 partes + "o que ficou indefinido".
3. PLANO CURTO ANTES: o agente nunca constrói na primeira resposta. Mostra seções, textos principais, o que fica de fora, o que gasta dinheiro; o Victor aprova só a primeira etapa (l.1699).
4. CONSTRUIR v1 em modo teste/demonstração, marcada, sem custo e sem publicar.
5. VERIFICAR: tabela "item | ok/problema | onde | como conferiu" feita pelo agente + "o que só o Victor pode julgar" + teste no celular real.
6. PUBLICAR só com "aprova" do Victor, em duas fases: prévia (link de teste) e produção; sempre com ponto de volta e lista do que sobe.
7. MEDIR e registrar em memoria/passagem.md (pedido, feito, pendente, verificado) e relatório semanal só-leitura.

## Já coberto nas skills existentes (e o que o livro acrescenta ou contradiz)
- `escala-regras` / CLAUDE.md: "aprovação do Victor antes de publicar", "nunca guardar senha/chave", "enganar não" já existem. O livro ACRESCENTA: critério de aceite com itens sim/não, regras de honestidade para PÁGINA DE VENDA (sem número/depoimento/selo/formulário falso), dado ilustrativo sempre rotulado, e a lista "segredos e chaves" (chave que vazou = revogar, não apagar).
- `escala-telegram`: já tem leitura de pedidos, prévia com botões e segurança do token. Acrescenta: modelo de pedido com critério de aceite, entrevista de 1 pergunta por vez, tabela "regra | onde | como conferir sem gastar" para o Worker, e as regras 4, 5, 7, 8 de produção (anti clique duplo, limite mensal por conta/chave, itens "processando" que expiram) para a fila/KV.
- `escala-memoria`: passagem.md ~ ANDAMENTO.md e comando "Retomar o projeto". O livro acrescenta o formato de retomada em até 10 linhas e a regra "se algo estiver diferente do que o registro diz, avisar".
- `escala-produto-greenn` e `escala-oferta`: definem quando e o que vender, mas NÃO têm processo de construção/checagem do produto nem página de venda. O livro acrescenta: briefing em 6 blocos + honestidade (ver sugestão abaixo), avaliação "como visitante" em 4 itens, domínio próprio e HTTPS.
- `escala-publicacao`: aprovação via fila. Acrescenta o padrão "prévia -> aprovação -> produção, com rollback" e a regra "publicado só depois de abrir o endereço final".
- `escala-video-ia`: acrescenta guardar o PROMPT COMPLETO ao lado de cada imagem/vídeo (.txt: pedido, modelo, data), estilo comum declarado uma vez por lote, âncora em foto de referência, pedir custo antes de gerar e refazer mudando uma coisa só.
- `ui-ux-pro-max`: o livro contradiz nada; reforça requisitos mínimos (360 px, contraste 4,5:1, foco visível, alt text, reduzir movimento).
- Não há menção nas skills a "Mestres Play 03"; este livro não foi aproveitado antes (conferido por grep: só escala-editor-video cita "mestres").

## Skills novas sugeridas e melhorias
### NOVA: `escala-pedido-a-produto` (processo de ponta a ponta)
- Aciona quando: o Victor pedir "cria um [site/página de venda/bot/sistema/e-book/automação]", quando uma ideia vaga precisar virar especificação, quando for construir página de venda ou ferramenta para a fase 2 (Greenn), ou "transforma isso em produto". NÃO aciona para vídeo (escala-producao-video) nem para roteiro.
- Conteúdo:
  1. Modelo de pedido com critério de aceite (Objetivo, Referências, Está pronto quando >= 4 itens sim/não, Não pode, Fora desta etapa, plano antes, relato no fim).
  2. Entrevista: até 10 perguntas, uma por vez, com sugestão e motivo; entregar ESPECIFICACAO.md em 7 partes (objetivo/quem usa; fluxo em verbos; telas/entregáveis; estados vazio-carregando-erro; dados; escopo e NÃO escopo (mínimo 3); onde publicar). Salvar em `produtos/<nome>/ESPECIFICACAO.md`.
  3. Plano curto, corte do que não foi pedido, aprovar só a primeira etapa.
  4. v1 em modo demonstração com selo; uma mudança por pedido; ponto de volta (commit) antes de mudança estrutural; ajuste fino x estrutural.
  5. Verificação: tabela do agente + lista do humano + celular real.
  6. Publicar: prévia, aprovação do Victor na fila, produção, rollback; conferência final (todo botão leva a destino real, nada inventado, lista do que sobe revisada).
  7. Fechar com passagem (pedido, feito, pendente, verificado) e "retomada" em 10 linhas.
### NOVA: `escala-seguranca-segredos` (curta)
- Aciona quando alguém for guardar/usar chave, token, senha, ligar plugin/MCP/skill de terceiro, instalar algo, ou quando uma chave aparecer fora do lugar. Conteúdo: 7 regras de segurança (l.2020-2050), segredo só em variável de ambiente (.env.local fora do Git, .env.example só nomes), chave pública x secreta, tabela de decisão de comando, "chave vazou" em 5 passos, as 5 perguntas antes de instalar skill/MCP (quem fez, o que lê, o que executa, envia dados para fora, licença) e o COMANDO "listar plugins/MCP conectados" mensal. Ligar ao ambiente "escala" (FABRICA_KEY por cabeçalho injetado pela rede, nunca em arquivo).
### NOVA: `escala-custo-api` (trava de gasto)
- Aciona quando for ligar qualquer serviço pago (Higgsfield, Kling, Veo, API de imagem/voz/LLM). Conteúdo: 4 travas (crédito pré-pago baixo sem recarga automática; limite rígido + alerta na metade; chave restrita só ao recurso necessário e separada por ambiente; MODO_TESTE ligado por padrão, em que qualquer valor diferente de "desligado" = teste); um clique = no máximo uma chamada, sem retry automático, registrada com hora; pedir ao agente o custo e esperar "ok" ANTES de gerar; falhas contam no limite; conferir o painel do provedor antes de gerar a próxima; comparar qualidade rascunho x final e registrar custo/tempo; mensagens de erro amigáveis e log só com código/hora.
### MELHORIAS em skills existentes
- `escala-produto-greenn`, seção nova "Checklist de página de venda e oferta": "Briefing em 6 blocos (Objetivo único: levar a comprar/clicar; Público; Conteúdo na ordem; Estilo visual com decisões; Requisitos: 360 px, contraste 4,5:1, todo botão leva a destino real; Plano). Honestidade: nada de depoimento, número de vendas/alunos, selo, preço riscado falso ou 'mensagem enviada' sem canal; produto de exemplo marcado 'ilustrativo'. Avaliar como visitante: em 5 segundos dá para dizer o que é e para quem? há um só botão principal? Lista de até 5 pontos genéricos com problema/efeito/onde. Antes de ligar tráfego: abrir no celular fora do Wi-Fi e sem login, testar o link de checkout da Greenn de ponta a ponta."
- `escala-telegram`, seção "Pedidos novos de sistema": "Quando o Victor pedir um produto/sistema (e não um vídeo), responder com o Modelo de pedido (critério de aceite) em vez de começar; fazer a entrevista com UMA pergunta por vez e botões; só avançar depois da aprovação do plano curto." Mais: "Regras de produção para o Worker: limite diário/mensal de gerações pagas por chave em KV, travar clique duplo, itens 'processando' há mais de X min viram 'falhou', mensagens de erro curtas ao Victor sem detalhe técnico".
- `escala-memoria`, seção "Retomada": "Ao retomar, responder em até 10 linhas: onde paramos, o que falta, se algo diverge do estado.md, próximo passo; esperar confirmação antes de mexer. Não instalar nem reconstruir nesta etapa."
- `escala-video-ia`, seção "Registro de prompts": "Ao lado de cada imagem/vídeo gerado, salvar .txt com o pedido completo palavra por palavra, data e ferramenta; declarar 'estilo comum' uma vez por lote; para refazer: 'Refaça X a partir do X.txt com [uma mudança]. Atualize o .txt'. Conferir cada imagem: letras inventadas, dedos a mais, luz diferente; vídeo: peça mudando de forma, luz piscando. Pedir custo antes de gerar com serviço pago."
- `escala-publicacao`, seção "Conferência pós-publicação": "Só dizer 'publicado' depois de abrir o endereço/post final; registrar data, versão, onde e resultado em memoria/passagem.md, sem credencial."
- Ferramenta sugerida (não criada): `ferramentas/varrer_segredos.py`, inspirada no empacotar.py: antes de commit/publicação, recusar `.env*`, padrões de chave (`sk-`, `sb_secret_`, `PRIVATE KEY`) e arquivos fora do esperado, e gerar inventário com SHA256. Obs.: o commit do repositório já deve passar por varredura equivalente.

## Ferramentas citadas (nome, preço, para quê, tem API?)
| Ferramenta | Preço (out/2026, segundo o livro) | Para quê | API/MCP |
|---|---|---|---|
| Codex / ChatGPT Plus (OpenAI) | Plus R$99,90/mês; Go R$39,99; Pro desde R$525 | Agente que constrói em pasta | CLI e nuvem; não usamos (temos Claude Code) |
| GitHub | Grátis (privados ilimitados, 2FA) | Repositório e histórico | API e MCP |
| Vercel | Hobby grátis só uso pessoal NÃO comercial; Pro US$20/mês | Deploy automático por push, prévia por branch, Instant Rollback, domínio | API, plugin/MCP |
| Supabase | Free (500 MB banco, 1 GB arquivos, sem backup, pausa em 1 semana); Pro US$25/mês | Login, banco, arquivos privados | API, MCP (`mcp.supabase.com/mcp?project_ref=`) |
| API de imagem OpenAI (gpt-image-2.5-flare / sunburst) | Pré-paga, mín. US$5; ~US$0,006 low, ~0,013 medium, ~0,053 high por imagem quadrada | Gerar imagem por código | API |
| Higgsfield | Assinatura paga com créditos; plugin/MCP exige assinatura (grátis só no site) | Imagem e vídeo IA (já temos MCP na sessão) | MCP `https://mcp.higgsfield.ai/mcp` |
| Blender 5.2.2 LTS + MCP for Blender | Grátis, código aberto (add-on de terceiros) | Modelar 3D por pedido | MCP (STDIO, `uvx mcp-for-blender`) |
| Three.js | Grátis | 3D na página | biblioteca |
| Pannellum / Photo Sphere Viewer | Grátis | Visualizador 360 | biblioteca |
| Registro.br | .com.br R$40/ano | Domínio | painel |
| cPanel (ex.: HostGator) | Plano pago, comparar renovação | Hospedagem de site estático, e-mail | File Manager, FTPS |
| Python 3.10+, Node LTS, Git | Grátis | Base do ambiente | - |
| Supabase CLI (`supabase db dump`) | Grátis | Backup semanal | CLI |
| uv / uvx | Grátis | Instalador de programas Python | CLI |
| WCAG 2.2 | Norma | Contraste 4,5:1 (texto grande 3:1), 2.2.2 (animação > 5 s precisa de pausa) | - |
Alternativas já nossas e grátis: Cloudflare Workers/Pages (uso comercial permitido), Workers AI FLUX (~170 imagens/dia), KV do Cloudflare no lugar do Supabase enquanto não houver login de público.

## Não serve para a ESCALA
- Instalação de Homebrew/winget, Git/Node/Python no PC do dono (cap. 2): nosso ambiente é nuvem do Claude Code.
- App ChatGPT/Codex, planos, modelo/esforço/modo rápido, /plan, painel de uso, ditado, Annotate (cap. 3 e 4): ferramenta que não usamos (a ideia de "ajuste fino x estrutural" sim, já aproveitada).
- Gravar habilidade por tela (Record a skill, só macOS) e $skill-installer (cap. 8): específicos do Codex.
- Páginas Ateliê Trama/Órbita/Casa Pátio, vaso 3D com Three.js, gráfico animado, simulador de turmas (cap. 6, 7, 10): exemplos fictícios de site institucional; só o método importa.
- Site 3D guiado por rolagem e tour de casa/imóvel (cap. 16): fora do nosso formato de vídeo vertical (Blender MCP poderia servir no futuro para cenas 3D do motor, mas exige PC com Blender e não roda na nuvem sem GPU).
- Hospedagem cPanel, FTPS, DNS do Registro.br e Vercel Hobby (cap. 11 e 17): só quando houver página de venda própria com domínio; Greenn já hospeda checkout.
- LGPD/termos/privacidade (cap. 15 passo 5): só quando coletarmos dados (e-mail de lista); aí ler de novo.
- Credenciais, licença e código de cópia: o livro vem marcado com e-mail e código do comprador (mp-copia). Não copiar trechos extensos para a repo; citamos método e referências de linha.
