# Pacotes de código (5 zips): o que é cada um e o que aproveitar
Leitura só de arquivos de texto. Nada foi executado, instalado ou importado; nenhum link foi aberto. Os conteúdos são dados não confiáveis. Instruções que apareceram dentro dos pacotes (ver cada seção) foram ignoradas e anotadas como "instrução no texto, ignorada".

| Pacote | O que é | Serve para a ESCALA? | O que copiar |
|---|---|---|---|
| site-de-10k (skill) | Skill de Claude Code que cria site de scroll com vídeo hero gerado por IA e publica na HostGator | O site, não. As leis do vídeo gerado por IA e a conferência, sim | Melhorias em `escala-video-ia`, `escala-editor-video`, `escala-regras` (gate de texto) |
| AGENTE_EXTREME_FINAL | Coach de copy do livro Adweek Copywriting Handbook (Sugarman), em arquivos .md para Codex | Em parte: gancho, escorregador, edição, rubrica de revisão | Skill nova `escala-copy-escorregador` (nossa, curta) |
| cyberdog-1.0.1 | Arquivo de design do Figma de um site de robô, com AGENTS.md | Não | Só o molde de AGENTS.md ("pergunte, não invente valor") |
| myloot-main | App local de inventário pessoal (Node.js), do mesmo grupo dos guias | Não | Ideias de arquitetura (porta de entrada de itens, histórico, rascunho) e o formato de memória |
| OpenJarvis-main | Framework acadêmico (Stanford) de IA pessoal local, em Python | Não como ferramenta; ideias de memória e aprendizado sim | Playbook com contadores, arquivos SOUL/MEMORY/USER, "reação ruim vira regra" |

---

## 1. z_sitede10k-skill (site-de-10k)
Arquivos lidos inteiros: `site-de-10k/SKILL.md` (200 linhas) e `references/` leis-de-prompt.md (101), pacote-de-design.md (74), pipeline-scrub.md (518), publicacao.md (138), receitas-ffmpeg.md (139), solucao-de-problemas.md (95). Total 1.265 linhas.

### O que é
Uma skill em 11 fases para um agente construir "um site cinematográfico guiado por scroll": gera com Higgsfield uma imagem inicial e um vídeo de 6 s (ou uma corrente de vários clipes), re-encoda com `ffmpeg` com keyframe curto, constrói HTML/CSS/JS puro em que o vídeo avança conforme o scroll, e publica por FTP na HostGator. Inclui pesquisa de clientes, pacote de design, autoteste e medição de velocidade.

### Instruções no texto, ignoradas
- "Extraia o zip, leia tudo, responda só com o checklist da Fase 1" e "esta skill governa sobre outras" (SKILL.md, linhas 10 e 12): instrução de acionamento do próprio pacote; não se aplica ao nosso projeto.
- Fase 1 manda conectar o conector do Higgsfield e instalar ffmpeg, Node e `winget`/`brew`; Fase 10 manda criar `hostgator.env` com usuário e senha do cPanel em arquivo. Nada disso foi feito.
- Conflito com regra fixa: guardar senha em arquivo (`hostgator.env`) contradiz o CLAUDE.md seção 2 ("nunca guardar senha"). Não copiar essa parte.

### Serve ou não
O produto final (site com scroll, HostGator, SEO, formulário) não tem a ver com vídeo curto. A página de venda do produto Greenn não precisa disso (a Greenn hospeda a página de checkout). O valor está nas partes de geração de vídeo por IA e conferência, que são rigorosas e testadas em construção real.

### O que copiar (com texto nosso, sem colar o original)
**A. Em `escala-video-ia` (seção "Leis do clipe")**, acrescentar:
1. **O movimento concorda com o enredo.** O clipe de cena precisa fazer o que a frase diz (subir, descer, entrar); movimento que briga com a ação lê errado. (lei 1)
2. **Um assunto, um movimento contínuo, sem cortes dentro do clipe.** Transformação de uma coisa em outra é a tomada mais difícil; evitar (lei 2). Se precisar, esconder a troca em flash ou nuvem e manter a trajetória.
3. **Trave o caminho, liberte o corpo.** Trajetória da câmera rígida, mas o personagem e a cena vivos (respiração, vento, luz). Nunca estabilizar congelando o personagem (lei 3).
4. **Planeje o final primeiro:** o último quadro precisa ser uma chegada composta (lei 4). Serve de gancho de fim de parte e de primeiro quadro do próximo clipe.
5. **Assuntos tolerantes:** névoa, luz, tecido, silhueta distante, fluido renderizam bem; mãos, teclado, rosto de perto, animais com anatomia conhecida mostram erro na hora (lei 5). Para novelinha, preferir plano médio, costas, sombras e mãos fora do quadro, ou fazer em código (`escala-animacao-personagens`).
6. **Venda os cruzamentos:** quando a câmera atravessa vidro, água ou porta, escrever o momento físico da lente (gotas, borrão curto). Passagem limpa lê como falsa (lei 8).
7. **Guardas permanentes no prompt:** "no text, no logos, no lettering anywhere" em todo prompt de imagem e de vídeo, e inspecionar o resultado contra marca registrada "contrabandeada" (a IA adora inserir logo real) antes de animar (lei 12, Fase 6 passo 3). Reforça "nunca pedir texto na imagem" que já existe na skill.
8. **Frase de espaço vazio:** nunca escrever "escuridão vazia à esquerda e à direita"; o modelo pinta painéis pretos. Descrever o mundo contínuo de borda a borda, com a região calma como parte dele (leis de prompt, linhas 48 a 50). Útil para deixar espaço para legenda.
9. **Prompts de gerador em inglês** (modelos rendem melhor), conversa e legenda em português. Verificar se vale para Veo/Kling antes de adotar como regra.
10. **Regra do quadro barato primeiro:** gerar e aprovar o quadro inicial (imagem, barato) antes de gastar no clipe (caro); consultar o preço exato antes de gerar e dizer ao Victor (Fase 6, passo 1 e 4). Nosso `escala-video-ia` já pede "custo lido na tela" e "3 tentativas sem melhora"; o pacote acrescenta o degrau do quadro inicial aprovado e a regra "três clipes falhos no mesmo conceito = problema de conceito, trocar o conceito, não o prompt" (Fase 6, passo 7). O conector Higgsfield deste ambiente tem tools de estimativa de custo (`estimate_image_cost`, `estimate_video_cost`): usar antes de gerar.
11. **Falso positivo de conteúdo sensível:** quando o job volta marcado como nsfw em cena inocente, o filtro leu errado; jobs marcados não são cobrados; reescrever o prompt em palavras simples de fotografia de produto, nomeando o objeto cedo (solução de problemas, linha 19). Verificar o saldo antes.
12. **Inspeção de coerência de marca:** listar antes os detalhes assinatura (cor, material, logo) e conferir cada imagem contra a lista, não só contra "parece bonita" (Fase 6). Para a ESCALA: roupa, cor de cabelo, cicatriz, objeto do personagem fixo (já na ficha de personagem; falta o passo de conferir cada imagem contra a ficha).
13. **A inspeção corre nos dois sentidos:** às vezes o modelo melhora o storyboard; se o resultado for melhor que o plano, flexionar o roteiro em vez de forçar o plano.

**B. Em `escala-editor-video` (seção "Conferência" e "Encadear clipes")**, acrescentar os comandos de `receitas-ffmpeg.md`, que são exatos e baratos:
- **Quadro de encadeamento em PNG de qualidade cheia, nunca jpg de revisão:** `ffmpeg -sseof -0.1 -i seg.mp4 -update 1 -frames:v 1 -q:v 1 final.png` (jpg assa compressão em cada clipe seguinte).
- **Checagem objetiva de repouso do final:** `ffmpeg -i raw.mp4 -vf "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null -`. A curva de brilho de diferença cai se o clipe termina parado e fica alta se continua derivando. Substitui o olho para saber se o clipe "descansa".
- **Corte de cauda:** se o clipe é bom até o personagem voltar a se mexer perto do fim, cortar no último quadro estável em vez de refazer: `ffmpeg -i raw.mp4 -t 4.3 ...`. Barato e resolve muito re-roll (gera clipe de 8 s, aproveita 4,3 s).
- **Crossfade curto de resgate numa junção que aparece:** `xfade=transition=fade:duration=0.25:offset=<comprimento do primeiro menos 0,25>`. Para dois clipes de 6 s: offset 5,75. Para três: encadear xfade, segundo offset 11,5.
- **Lei da costura:** identidade de textura fina não atravessa clipes (trama, grão, pele); posição atravessa. Então cada junção entre clipes deve cair dentro de movimento ou de um momento que justifique renovar a textura (varredura de lente, batida de desfoque, escuro curto, virada de luz). Nunca encostar dois "repousos" sobre textura específica (leis de prompt, linhas 87 a 89). Dica de corte para novelinha: cortar na ação, não no repouso.
- **Mundos abstratos encadeiam com confiança:** luz, partículas, atmosfera quase não erram na continuação. Bom para vinheta de abertura da série e transições de cenário.
- **Concat sem divergência:** juntar os clipes brutos num único filtro `concat` e codificar uma só vez; se só há arquivos já codificados, usar o mesmo comando em todos e o demuxer `concat`. Parâmetros diferentes travam em cada junção.
- **Pasta de revisão fora da pasta de publicação:** brutos e revisões nunca vão para a pasta que sobe. Na ESCALA: `projeto/brutos/` fora do que o Metricool/Victor posta.
- **Verificar depois de cada encode:** abrir o resultado e extrair um quadro antes de usar (falha silenciosa pega agora é grátis).

**C. Em `escala-editor-video` (legenda sobre vídeo): sistema de legibilidade**, adaptado de `pipeline-scrub.md` (linhas 242 a 311). Texto sobre filmagem viva é fundo em movimento que não se controla quadro a quadro:
1. Escurecimento suave global sob a legenda (scrim) e, melhor, um scrim local que só aparece enquanto aquela legenda está ligada.
2. Sombra de texto em três camadas (borda justa, brilho médio, queda larga).
3. Para texto pequeno (rótulos, "Parte 2"), chip com fundo semitransparente e blur.
4. **Auditoria do pior quadro:** medir contraste contra o pior quadro do trecho, não o médio. Meta: 3,5 para 1 de contraste de pior pixel sob a legenda; 4,5 para 1 em texto corrido. "O quadro médio mente; o pior quadro é o que o espectador vai estar lendo." Um script pequeno em Python (Pillow) com a mesma conta de luminância relativa resolve e roda no motor sem custo (pode virar `ferramentas/contraste_legenda.py`, ideia nossa, não testada).
5. Posicionar a legenda na região mais calma dos quadros.
Aplicável a Reels/Shorts, onde o texto fica sobre imagem em movimento.

**D. Em `escala-regras` ou `escala-editor-video`: gate de revisão de texto** (Fase 9). Antes de mostrar qualquer coisa ao Victor, rodar `grep` no texto final (roteiro, legendas, mensagem) por travessão e por palavras de estoque de IA, reescrever e rodar de novo até retornar zero. Lista do pacote em português: alavancar, robusto, empoderar, destravar, acionável, orientado a dados, soluções, sinergia, escalável. Acréscimos para nós: "além disso", "vale ressaltar", "mergulhar", "panorama", "testamento", "elevar", "não é só X, é Y", "o futuro é promissor", finais de moral, atribuição vaga ("muitos especialistas dizem"), faixa falsa ("de X a Y" que é só lista). **Exceção importante e correta:** dispositivo de marca deliberado (um trio desenhado "Colher. Coar. Servir.", um staccato planejado) é ofício, não sinal; a diferença é intenção. Casa com a regra fixa "sem travessão, sem cara de IA" e pode virar o `ferramentas/conferir_texto.py` sugerido em `guia-100-skills.md`.

**E. Em `escala-editor-video`: passe de olhos frescos, por último** (autoteste item 12): largar o checklist e olhar o vídeo como espectador de primeira vez, com zero contexto: cada elemento tem seu lugar? Algum elemento paralelo ficou desigual (um personagem sem sombra, uma cena sem som)? Lê como feito de propósito ou como enchimento? Conserta antes de o Victor ver. Se o ambiente permitir, mandar um subagente revisor (read-only) olhar a folha de quadros sem o roteiro.

**F. Em `escala-social-media` ou `escala-chefe`: regra dos dois travamentos** (solução de problemas, linha 95): se uma ferramenta ou serviço trava duas vezes seguidas sem resposta, está fora do ar: parar, nomear em voz alta, reiniciar, nunca fazer uma terceira chamada. Diferente de render lento (job com progresso está trabalhando). Para a rodada automática: se Higgsfield, Metricool ou Telegram não responde 2 vezes, registrar na passagem e seguir com o que dá em vez de insistir.

**G. Aviso de espera (Fase 6):** render leva minutos; avisar uma linha ao começar e usar o tempo para outra tarefa (na rodada: mandar a prévia da parte 1 enquanto a parte 2 renderiza).

**H. Direção para variar os vídeos (pipeline-scrub, linhas 472 a 483):** "duas seções vizinhas nunca dividem o mesmo esqueleto de layout" vira "dois vídeos seguidos da mesma série não usam o mesmo molde de composição"; e evitar os visuais que gritam "IA fez isso" (creme com serifa e terracota, quase-preto com verde-ácido, quase-preto com âmbar). Para a ESCALA: variar paleta e composição entre séries, sempre amostrando a paleta do próprio mundo da série.

### O que NÃO copiar
- Scroll-scrub, blob, anel de carregamento, portões de hero estático, entrada de texto por caractere (pipeline-scrub, linhas 1 a 240 e 313 a 470): é engenharia de site.
- Publicação por FTP/HostGator, `hostgator.env` com senha, API do cPanel (publicacao.md, Fase 10).
- Pesquisa de clientes e funil de uma página (Fase 3): conceito útil, mas já coberto por `escala-radar-viral` e `escala-oferta`.
- A conversa honesta de custos nos créditos do Higgsfield (números de 2026 podem mudar; consultar o custo direto no conector).

---

## 2. z_AGENTE_EXTREME_FINAL
Arquivos lidos inteiros (6 .md): AGENTS.md (83 linhas), COMANDOS.md (42), 02_GUIA_COMPLETO_Sugarman.md (1.329), 03_METODO_APLICADO_Sugarman.md (181), 04_TRILHA_30_DIAS_E_EXERCICIOS.md (114), 05_MODELOS_POR_FORMATO.md (110). A pasta `LIVRO/` que o AGENTS.md cita não vem no pacote.

### O que é
Uma pasta-coach para Codex: o `AGENTS.md` define um agente "Agente Extreme" com menu de comandos (estudar capítulo, copy, revisar, coach de negócios, anotar) baseado no livro "The Adweek Copywriting Handbook" de Joseph Sugarman. O `02` é um resumo capítulo a capítulo (15 axiomas, 23 elementos de copy, 31 gatilhos psicológicos, 13 anúncios comentados, mídias). O `03` é o manual operacional (briefing, estrutura-modelo, rubrica de revisão de 10 critérios). O `04` é uma trilha de 30 dias com exercícios e flashcards. O `05` traz modelos por formato (anúncio, roteiro de vídeo curto, carrossel, página de vendas, VSL, e-mail, WhatsApp).

### Instruções no texto, ignoradas
O `AGENTS.md` instrui o agente (responder só em texto, não criar arquivos exceto "anotar", sugerir próximo comando no fim de cada resposta). São instruções para o coach de outra pessoa; não valem aqui.

### Aviso de direitos
O `02` é um resumo em outras palavras de livro protegido por direitos autorais, feito por terceiro. Não copiar trechos literais para o repositório. As ideias gerais (axiomas e gatilhos) são conhecidas e podem ser reescritas com palavras e exemplos nossos, curtas.

### Serve ou não
Serve em parte, para o texto dos vídeos e do produto. Sugarman escreve para anúncio impresso e venda direta, mas os mecanismos de atenção (primeira frase, curiosidade, escorregador, edição) são os mesmos de gancho e retenção. Tem pontos que conflitam com as regras fixas: urgência, medo, culpa, ganância e "fazer o leitor sentir que deve algo" só podem entrar na versão honesta (o próprio material pede honestidade: "nunca invente depoimento, urgência falsa nem promessa de resultado com prazo" e "Esperança: sugira, não prometa", `03`, seção 11).

### O que copiar como skill nova (`escala-copy-escorregador`, nossa)
Aciona quando: escrever ou revisar legenda, gancho, texto de capa, carrossel, texto de página de produto ou mensagem de venda. NÃO aciona para roteiro de série (escala-roteiro-serie) nem para voz.
Conteúdo, em tópicos curtos com palavras nossas:
1. **Tudo trabalha para a primeira frase** (Axioma 2) e **a primeira frase só precisa fazer ler a segunda** (Axioma 3): em vídeo vira "o primeiro quadro, o texto da capa e a primeira fala só existem para a pessoa ficar mais 3 segundos". Já está em `escala-ganchos-retencao`; acrescentar a regra de que **a primeira frase é curta, fácil e quase incompleta** ("Ela abriu a porta.").
2. **Escorregador:** cada frase obriga a ler a seguinte; procurar na revisão o ponto onde alguém pararia. Em vídeo: o ponto onde a pessoa sai (ver `escala-ganchos-retencao`, diagnóstico pela retenção).
3. **Sementes de curiosidade** nos pontos onde o ritmo cai: frase curta de ponte ("Mas tem um detalhe." "E foi aí que..."). Sem exagero (Axioma 8, cap. 10). Já parcialmente em `escala-roteiro-serie`; acrescentar na lista de ganchos de fim de parte.
4. **Venda o conceito, não o produto** (Axioma 9): em vez de "vídeo sobre golpe do Pix", o conceito "o golpe que parece o banco te ligando". Dez conceitos diferentes para o mesmo assunto antes de escolher um (trilha, dia 12). Combina com `escala-ideias-fora-da-caixa`.
5. **Cura vende mais que prevenção** (Axioma 15): posicionar o vídeo como solução de uma dor que a pessoa já sente ("o que fazer agora que você caiu no golpe") em vez de "como evitar". Para afiliado: acessório que resolve um problema atual, não "para o caso de".
6. **Sintonia / dizer sim:** abrir com afirmações verdadeiras que o público reconhece ("Você já recebeu uma mensagem de número desconhecido.") antes de levar à virada (Axioma 5). Útil em vídeo informativo.
7. **Emoção primeiro, lógica para justificar** (3 princípios da emoção). Palavras com carga emocional escolhidas com cuidado (caso do "fix" contra "repair" que aumentou resposta em 20%, cap. 11; é dado do livro, sem verificação nossa).
8. **Honestidade é o gatilho principal** (Gatilho 2): admitir o defeito logo e explicar por que não importa aumenta a resposta. Para a ESCALA: "o vídeo é feito com IA" dito de forma natural, nunca escondido, pode virar traço da marca.
9. **Especificidade** (Gatilho 29): número exato, nome de lugar, hora ("às 3h12") soa como pesquisa e prende mais que "muitos", "um dia". Só com dado verdadeiro.
10. **Contar histórias** (Gatilho 26) e **engajamento mental** (27): deixar a pessoa concluir sozinha o final; não explicar a moral.
11. **Edição: cortar 30 a 50%** (Axioma 14, cap. 17), cinco princípios: caçar "que" e conectivos, variar o ritmo da frase, juntar frases, cortar palavras sem função, reordenar para a emoção vir antes da explicação. Deixar descansar até o dia seguinte quando der. **Não dizer demais:** "é o erro mais comum; cortar de 50% a 80%".
12. **Ritmo:** frases curtas, longas, médias, curtas; tríades ("Abriu. Olhou. Fugiu."). Não repetir o mesmo molde em todo vídeo (senão vira previsível).
13. **Legibilidade (cap. 21):** média de 8 a 15 palavras por frase no início; em português, apenas o espírito da regra. Já coberto pela voz natural de `escala-voz-narracao`.
14. **Rubrica de revisão de 10 critérios** (03, seção 8) adaptada para vídeo curto e legenda: (1) o primeiro quadro e a primeira frase fazem ficar? (2) o clima combina com o tema? (3) existe ponto de abandono? (4) conceito claro e diferente? (5) emoção antes da explicação? (6) a sequência responde cada dúvida na hora? (7) a objeção foi levantada? (8) prova específica? (9) pedido único e claro no fim? (10) enxuto, pessoal, sem clichê? Nota de 0 a 10 por critério e 3 maiores problemas; reescrever; dizer o que testar.
15. **Pedido único e explícito no fim** (elemento 23) e **P.S. é a linha mais lida** (cap. 36): em legenda, a última linha traz o pedido único (seguir, comentar, link na bio com aviso de publicidade se for afiliado). Uma chamada por vídeo.
16. **Modelos prontos úteis** (`05`, seções 2 e 3): roteiro de vídeo curto de 0 a 60 s e carrossel de 7 a 10 slides, ambos com função de cada bloco. A estrutura do roteiro curto do pacote: 0 a 3 s gancho; 3 a 10 s sintonia; 10 a 25 s história; 25 a 40 s demonstração com especificidade; 40 a 50 s objeção; 50 a 60 s pedido único. Compatível com GPEC de `escala-ganchos-retencao`. Para carrossel, `reels-para-carrossel` já traz o método; a ideia nova é "cada slide termina com uma frase que obriga a passar ao próximo".
17. **Uma oferta, uma decisão (simplicidade):** teste real do livro, um único modelo de relógio vendeu 3 vezes mais que nove (Gatilho 24). Para o produto Greenn: uma oferta só, sem muitas opções, no início.
18. **Garantia forte:** trocar só a garantia dobrou a resposta no caso Consumers Hero (Gatilho 9); período de teste de 30 a 60 dias reduz devolução (elemento 16). Para a Greenn, a garantia de 7 dias do CDC já é obrigatória; considerar mais (a decidir pelo Victor).

### Gatilhos: usar só a versão honesta
Mapa para o `escala-regras`:
| Gatilho do pacote | Pode, de forma honesta | Não pode (regra fixa) |
|---|---|---|
| Urgência (20) | Prazo real do bônus ou da oferta | "Vai esgotar" falso, contador falso |
| Medo (21) | Alertar perda real e comprovada (golpe) com fonte | Explorar vítima real ou criança; assustar para vender |
| Esperança (31) | Sugerir o benefício | Prometer resultado, prazo ou dinheiro fácil |
| Depoimento (18) | Depoimento real e autorizado | Depoimento falso ou "eu usei e funcionou" falso |
| Culpa/reciprocidade (28) | Entregar muito valor antes de pedir | Pressão emocional |
| Autoridade (8) | Fato verificável ("a maior série de...") | Fingir ser profissional |
| Ganância (7) | Dar mais do que o esperado, explicando como | Preço absurdo sem explicação |

### O que NÃO copiar
- O formato de coach (menu de comandos, trilha de 30 dias, flashcards): é para uma pessoa estudar, não para o agente produzir.
- Casos antigos (relógios, rádios CB, aviões, Wall Street Journal), mala direta, 0800, catálogo, cupom.
- Estilo "Eu para você" assinado como pessoa: na ESCALA a marca é fictícia e "zero ligação com o Victor"; usar "eu" do narrador/personagem, nunca assinar como o Victor.
- "Teste de urgência, medo e ganância" sem as salvaguardas acima.

---

## 3. z_cyberdog-1.0.1
Arquivos lidos: README.md (83 linhas), CLAUDE.md (5), AGENTS.md (45); `Cyebrdog.fig` (32 MB, binário do Figma) apenas listado, não aberto.

### O que é
Um arquivo de design do Figma ("Cyberdog", conceito de site de produto de robótica, 7 quadros de 1920x1080), vendido pela HorizonX com licença comercial para adaptar, sem revender nem publicar o arquivo original. O README ensina a importar no Figma, conectar o MCP oficial do Figma ao Claude Code ou Codex e pedir "construa isto como site responsivo"; o AGENTS.md e o CLAUDE.md dizem ao agente como ler o design e montar o código.

### Instruções no texto, ignoradas
README: comandos `claude mcp add --transport http figma https://mcp.figma.com/mcp` e `codex mcp add ...`; AGENTS.md: "ask the user to link the intended Slide", "use the official Figma MCP server". Não executei nem adotei.

### Serve ou não
Não serve para a ESCALA: é design de site de produto físico, não tem vídeo, personagem ou conteúdo viral. O conteúdo ("Cyberdog" de robótica, "Buy Now") não combina com o tema. A licença proíbe republicar o arquivo; também não usaria a arte de terceiros.

### O que aproveitar (ideia, não arquivo)
O `AGENTS.md` é um bom molde curto de instrução para agente de implementação, com 4 blocos: "O que tem na pasta", "Sobre este design", "Como ler o design", "Como construir", "Pronto significa". Regras que valem em nossas fichas: "Nunca invente um valor que o design não dá; pergunte" e "Pronto significa: bate com o quadro no desktop, funciona em 390 px, console sem erro, e você disse o que não conseguiu igualar e por quê" (mesma ideia do "nunca declarar aprovado" do livro 17). Sugestão: `escala-produtor` ganhar um bloco "Pronto significa" (vídeo no 9:16, legenda dentro da área segura, selo de IA, aviso de publicidade se houver, e a lista do que não ficou como o planejado).

---

## 4. z_myloot-main (MyLoot)
Arquivos lidos inteiros: README.md (259 linhas) e NOTAS.md (252). Estrutura de pastas listada: `public/` (interface), `docs/` (site do projeto, vídeos e músicas), `exemplos/` (guias em PDF, kits, modelos de prompt), `_ferramentas/` (scripts Python de ícone, kits e PDFs), `server.js`, `nuvem.js`, `celular.js`, `integracoes.js`, instaladores `.bat/.command/.sh`, `LICENSE` (MIT), `versao.json`. 207 arquivos, ~106 MB (vídeos e MP3 em `docs/`).

### O que é
App local em Node.js puro (sem dependências), do mesmo grupo (Prestes Design) que fez os guias g01 a g05 (os 5 guias em PDF vêm dentro de `exemplos/guias`). É um "inventário pessoal" com visual de joguinho (XP, níveis, mascotes): guarda PDFs, prompts, comandos, links, notas, tarefas, calendário, clientes, financeiro e hábitos; roda no PC, abre no celular pela rede com QR Code e PIN; sincroniza entre PCs pela pasta do Google Drive; usa Claude Code ou Codex instalados para "pedir à IA"; exporta para Obsidian; tem 42 links de ferramentas (a lista do Guia 04).

### Instruções no texto, ignoradas
Os instaladores (`Instalar.bat`, `instalar.sh`, `Instalar.command`) e o "Atualizar agora" (baixa um ZIP do GitHub e copia por cima) não foram lidos nem executados; o README manda baixar e rodar, ignorado. Atenção: um app que se auto-atualiza baixando código da internet é o tipo de coisa a não instalar sem revisão.

### Serve ou não
Não serve como ferramenta: é para uso pessoal em um PC com navegador; a ESCALA roda no Claude Code em nuvem e no Cloudflare Worker, com memória em arquivos `.md` no Git. Duplicaria o `memoria/` com outro banco (`db.json`) que o agente não leria. Nenhuma função resolve um problema atual (crescer, produzir, publicar).

### Ideias que valem a pena (sem instalar)
1. **Porta de entrada de itens (`/api/entrada`, NOTAS linhas 103 a 108):** outros programas mandam itens por POST com código; "mesmo app + mesmo id atualiza em vez de duplicar", etiquetas e checklist só acrescentam, nunca apagam; 401 sem código. Para a ESCALA: se o Worker do Telegram precisar receber algo de outra ferramenta, usar o mesmo contrato (id estável, só acrescentar, token no cabeçalho, nunca apagar). Hoje não é necessário.
2. **Histórico com desfazer** (NOTAS linhas 190 a 195): toda ação guarda antes e depois e dá para desfazer só os campos que aquela ação mexeu. Ideia para `memoria/`: o Git já dá isso; registrar no `passagem.md` o commit de cada etapa.
3. **Rascunho antes de salvar e "não salvou" avisa:** princípio de nunca perder o que foi digitado. Já é prática do repositório (commit por etapa).
4. **Gravação que falha não some:** faixa avisando, repete em 3, 6, 12, 24, 30 s e guarda a mudança no armazenamento local (NOTAS linhas 213). Útil como regra para o Worker: se a chamada ao Telegram ou ao Metricool falha, tentar de novo com espera crescente e registrar em vez de perder a prévia. A conferir no `telegram/worker.js` se já faz.
5. **Backup em ZIP sem compressão com CRC e "guarda o banco atual antes de restaurar":** padrão de restaurar sem destruir.
6. **Lixeira em vez de apagar:** regra "nunca apagar, mover" (também no guia g05). Para `memoria/`: criar `memoria/arquivo/`.
7. **Segredos separados do banco e do backup** (`data/segredos.json` fora do Git, do backup e do Drive; NOTAS linha 31): confirma a regra fixa e a prática de variável de ambiente do Worker.
8. **Instruções prontas** (`exemplos/instrucoes-prontas.json`) com "sempre mostrando o plano antes e sem apagar nada": reforça o padrão "plano antes, nunca apagar".
9. **Ideias para próximas versões** (NOTAS linha 247): "Agendar e publicar posts no Instagram, TikTok, Facebook e YouTube (estilo Metricool), avaliar se vale" e, na `versao.json`, parceiro "SortHub: referências do Instagram e do TikTok. Salve posts, veja as métricas, transcreva vídeos e mande tudo para o MyLoot". É um serviço externo (SortHub) para guardar referências de vídeos virais e transcrever; pode ser útil ao radar, mas não verifiquei o serviço nem preço. Anotar como pesquisa futura, com a ressalva de que baixar e transcrever vídeo de terceiros só serve para estudo interno.
10. **Voz local com Whisper no navegador** (`onnx-community/whisper-base` com Transformers.js, NOTAS linha 98): transcrição sem enviar áudio para fora e sem custo. Útil para transcrever áudios que o Victor mande ao bot, se o Workers AI não resolver; precisa rodar no navegador ou em Node, não no Worker. Anotar.
11. **Músicas:** `docs/site/musica/` tem 7 MP3 (arcade-rush, boss-battle-groove etc.) sem informação de licença. NÃO usar como trilha dos vídeos (regra fixa: nada com direito autoral; origem desconhecida conta como risco).

### O que NÃO copiar
- O app inteiro, os vídeos e as músicas, mascotes, XP, financeiro, clientes, Notion/Trello.
- A skill externa `design-taste-frontend` que as NOTAS dizem ter sido instalada (linha 154): não verifiquei; não instalar.

---

## 5. z_OpenJarvis-main
Arquivos lidos: README.md (184 linhas) inteiro; docs/architecture/overview.md (242 linhas) inteiro; design-principles.md (linhas 1 a 160 de 300); skills.md (arquitetura, 222 linhas) inteiro; learning/ace.md (135) inteiro; showcase/cost-savings.md, morning-brief.md, persistent-memory.md inteiros; tutorials/scheduled-ops.md (linhas 1 a 120 de 215); architecture/security.md (linhas 1 a 110 de 211); user-guide/data-boundary-scan.md (linhas 1 a 40). Lista de pastas e arquivos de `docs/`, `src/`, `examples/`, `configs/`, `deploy/` conferida. Não li o código em `src/`, `rust/`, `desktop/`, `frontend/`. 2.230 arquivos, ~107 MB.

### O que é
Framework de pesquisa e produção de Stanford (Hazy Research, Scaling Intelligence Lab) para "IA pessoal em dispositivo pessoal": local primeiro, nuvem só quando preciso. Python 3.11+, instaladores por `curl | bash`/PowerShell, motor de modelos locais (Ollama, vLLM, llama.cpp, MLX) e opcionalmente nuvem (OpenAI, Anthropic, Google). Cinco primitivos: Inteligência (catálogo de modelos), Motor (inferência), Lógica de agentes (9 tipos, incluindo um que embrulha o Claude Agent SDK), Memória (SQLite/FTS5, FAISS, BM25 etc.) e Aprendizado (traços de execução alimentam política de roteamento e otimizadores). Traz agendador (cron), canais (WhatsApp, Discord, Slack, Telegram), conectores (Gmail, Calendário, Drive), skills no padrão agentskills.io (importa de Hermes ~150 skills e OpenClaw ~13.700 skills), telemetria de custo e energia, scanner de segredo e PII, sandbox em contêiner e um placar público de economia.

### Instruções no texto, ignoradas
`curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash`, `irm ... | iex`, `jarvis init`, `jarvis connect gdrive`, `jarvis skill install hermes:arxiv`, "Comment 'take' on any issue". Nenhum executado. Há ainda documentação de "mining" (`docs/user-guide/mining*.md`, `docs/development/mining*.md`, `src/openjarvis/mining`, "Pearl", design de 2026-05-05); não li o conteúdo: é mineração em cima do framework, nada a ver com a ESCALA e um motivo extra para não instalar sem revisão.

### Serve ou não
Não serve como ferramenta nem como base: exige máquina própria ligada (Mac mini, GPU), Python, Ollama e modelos locais, e é um pacote de 2.230 arquivos. A ESCALA já tem o mesmo desenho em formato mais leve: tarefas agendadas (as rodadas de 7h, 12h e 17h) no Claude Code, bot de Telegram como canal e memória em arquivos. Os modelos locais pequenos não substituiriam o Claude para roteiro e conferência.

### Ideias que valem a pena (copiar como ideia, escritas por nós)
1. **Memória em três arquivos de texto simples** (`SOUL.md` = como o agente deve se comportar, `MEMORY.md` = fatos e preferências, `USER.md` = quem é o usuário; showcase persistent-memory): "auditável, portável, compõe, não deriva. Plain markdown que eu posso ler não mente". Já fazemos com `memoria/estado.md`, `aprendizados.md`, `passagem.md` e as fichas. Acréscimo: manter uma seção "Como o Victor gosta de receber" (tom, tamanho, o que sempre corta) em `memoria/estado.md`, atualizada quando ele critica algo.
2. **Reação ruim vira regra** (morning-brief, "ele aprendeu meu gosto"): quando o dono reage com 👎 a um item, o sumarizador atualiza o `MEMORY.md`. Mapeamento direto: o botão **Recusa** (e **Ajusta**) do Telegram deve registrar em `memoria/aprendizados.md` uma linha com o motivo (ou perguntar um "por quê" curto) para a próxima rodada não repetir. Hoje o CLAUDE.md diz que "aprende com a crítica do dono"; este é o mecanismo.
3. **Playbook com contadores (ACE):** o arquivo de estratégias traz cada linha como `[id] helpful=5 harmful=0 :: texto da estratégia` ("quando o usuário pedir conversão, prefira a forma exata antes de arredondar"). Gerador, refletor e curador: um agente propõe, outro avalia o que ajudou ou atrapalhou, outro poda. Aplicação: `memoria/aprendizados.md` em formato de lista numerada com `ajudou=N` e `atrapalhou=N`, atualizada pelo analista em 24 h e 72 h (quando um padrão de gancho se repetir com bom resultado, soma 1; se flopar, soma em `atrapalhou`). O que atinge `atrapalhou` maior que `ajudou` com pelo menos 3 usos vira "evitar". Torna o aprendizado mensurável e podável, em vez de só crescer. Pode ser feito em markdown, sem código.
4. **Mínimo de amostras antes de aprender** (`min_traces = 20` no ACE; "Skips skills below min_traces_per_skill"): só otimizar uma regra depois de uma amostra mínima. Para a ESCALA: no começo (zero seguidores), 3 a 5 vídeos por formato antes de concluir "esse formato funciona"; mais coerente com a regra "sem número inventado" de `escala-editor-video` seção 7.
5. **Telemetria de custo por chamada e "o que teria custado na nuvem"** (cost-savings): registrar, por rodada e por vídeo, tokens, tempo e gasto (`/usage`), para o analista mostrar "o custo da operação do mês". Já sugerido em `guias-curtos.md` (g01 e g02) e em `guia-100-skills.md` (item C.9).
6. **Scanner de segredo/PII antes de enviar ao modelo** (security.md: `SecretScanner`, `PIIScanner`, modos WARN, REDACT, BLOCK; "auditoria por padrão"): padrão para o pré-commit da ESCALA (varredura local; avisar, redigir ou bloquear). Mesmo desenho do item "guardião de segredos" em `guia-100-skills.md`.
7. **Skills com origem registrada (`.source` com commit e data), parser estrito e tolerante, "scripts só com flag explícita":** ao importar skill de terceiro, copiar só SKILL.md e referências, não rodar scripts sem aprovação, e guardar de onde veio. Exatamente a regra proposta para `escala-regras` (ler antes, nunca instalar por `npx`). Acrescentar o arquivo `.origem` (de onde, quando, quem aprovou).
8. **Skill como catálogo leve:** o agente recebe só o nome e a descrição de cada skill no prompt e carrega o corpo quando precisa (`<available_skills>`); o mesmo que o CLAUDE.md já pede (descrição com "Aciona quando... NÃO aciona para..."). Confirma que a descrição precisa ser curta e precisa.
9. **Agente agendado "operativo" com estado persistente e compressão de memória:** o modelo de uma tarefa de rodada que lê o estado da anterior e atualiza. É o que `memoria/estado.md` + `passagem.md` fazem; o OpenJarvis confirma o desenho (estado + traço + política).
10. **Sandbox/montagem segura e política de arquivos sensíveis** (`file_policy.py`, `mount_security`): lista de padrões de arquivo sensível (.env, chaves) que o agente nunca lê nem envia. Reforçar no `.gitignore` e nas fichas.
11. **Preset "morning digest":** briefing de 5 bullets às 7h (2 min de leitura). Mapeia para a mensagem curta do chefe ao Victor (CLAUDE.md seção 5: tabela e decisões numeradas): manter 5 bullets e no máximo 2 min de leitura.

### O que NÃO copiar
- Qualquer instalação (`install.sh`, Ollama, Rust, desktop), o módulo de mineração, os canais WhatsApp (Baileys é protocolo não oficial: risco de bloqueio de conta), o Twitter bot de exemplo (publicação automática sem aprovação conflita com a regra "toda publicação passa pelo Victor").
- Importar milhares de skills de Hermes/OpenClaw: qualidade e segurança desconhecidas.
- Telemetria para o placar público e `posthog` em `deploy/`: envio de dados a terceiro.

---

## Resumo de ações sugeridas (para o chefe decidir; nada foi alterado fora deste arquivo)
1. `escala-video-ia`: acrescentar "Leis do clipe" (itens 1 a 13 da seção 1.A) e a regra "3 clipes falhos no mesmo conceito = trocar o conceito".
2. `escala-editor-video`: acrescentar os comandos ffmpeg exatos (PNG de encadeamento, checagem de repouso, corte de cauda, xfade, costura), o sistema de legibilidade de legenda com auditoria do pior quadro e o passe de olhos frescos.
3. `escala-regras` + ferramenta `ferramentas/conferir_texto.py`: gate de revisão de texto (travessão, palavras de estoque de IA, sinais quietos), com a exceção do dispositivo de marca deliberado.
4. Nova skill `escala-copy-escorregador` (curta, texto próprio), com o mapa de gatilhos honestos.
5. `memoria/aprendizados.md`: formato com `ajudou` e `atrapalhou`, amostra mínima antes de concluir, e o botão Recusa/Ajusta do Telegram escrevendo a razão lá.
6. `escala-regras`: skill/plugin de terceiro nunca por `npx` nem script; ler tudo, escrever a nossa, registrar `.origem`.
7. Nada de instalar myloot, OpenJarvis, cyberdog nem rodar o site-de-10k.
