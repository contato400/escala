---
name: escala-radar-viral
description: Aciona quando for descobrir o que está viralizando no TikTok, Instagram Reels ou YouTube Shorts, escolher temas e formatos do dia, montar o banco de temas ou estudar um vídeo viral para adaptar na ESCALA. NÃO aciona para escrever o roteiro (escala-roteiro-serie) nem produzir o vídeo (escala-producao-video).
---
# Radar viral

## Onde olhar (todo dia, 20 a 30 min)
- **TikTok**: aba "Novelas" (populares), "Creator Search Insights" (pesquisar no app; filtrar Brasil; ver tópicos em alta dos últimos 7 dias e o gráfico), página Explorar/For You do nicho.
- **YouTube Shorts**: busca por tema com filtro "esta semana" e ordenar por visualizações; qualquer assunto que estiver subindo (jogo, polêmica, desenho, animal, música, história, humor, notícia), sem filtro de nicho. Use a TranscriptAPI (`search_youtube` com `upload_date: week`, `sort: views`; `get_youtube_transcript` para ler o roteiro e mapear a estrutura).
- **Instagram Reels**: aba Reels e Explorar; os Reels e perfis que mais estão crescendo, de qualquer assunto.
- **Notícia do dia**: o assunto que todo mundo está comentando (lançamento, polêmica, caso famoso), sem explorar vítima.

## Buscas que já trouxeram ouro (21/11)
- "como criar curtas de animação virais", "stickman animated shorts", "novelinha com IA", "você decide o fim série", "e se" + tema; filtro do último mês, ordenar por views.
- Achados: séries animadas narradas em segunda pessoa com voto do público (perfil de 0 a 24 mil seguidores em 6 dias, relato do criador); bonecos 2D sobre fundo 3D contando "e se..." (canal com centenas de milhões de views em um mês, relato); novelinhas com personagem consistente. Formatos em `escala-ganchos-retencao`.
- Para estudar o estilo de um viral com números: `ferramentas/estudar_referencia.py`.

## O que anotar de cada viral (modelo)
| Campo | Exemplo |
|---|---|
| Link e rede | tiktok.com/... |
| Views, data, duração | 3,2 mi, 18/11, 1:10 |
| Views por dia e inscritos do canal | 800 mil por dia, canal com 4 mil (nosso) |
| Tipo de gancho (0 a 2 s) | erro comum, resultado primeiro, contraste... (o TIPO, nunca a frase) |
| Estrutura | cena chocante → contexto rápido → 2 viradas → gancho |
| Por que prende | curiosidade, injustiça, medo, identificação |
| Como adaptar (nossa versão) | personagem, cenário e virada nossos |
Nunca copiar falas, imagens ou personagens; extrair só o esqueleto. Guardar o tipo de gancho e o molde em 1 linha, sem a frase original (origem: livro 07, notas em conteudo/estudos/livros/).
Visualização de terceiro não prova nada sozinha: retenção e envios do vídeo dos outros a gente não vê. Ao olhar um post de referência, ver também a data e o tamanho do perfil (sucesso de 3 anos atrás pode não repetir; perfil enorme alcança muito com qualquer coisa).

## Perfil laboratório (uma conta de pesquisa por rede)
Conta separada, que NÃO publica, em TikTok, Instagram e YouTube. Regra única: nada fora do que se pesquisa (um vídeo de humor visto até o fim já puxa o feed errado). Passo a passo:
1. Escrever 10 termos em 3 grupos: tema, dúvida do público, assunto de nicho pequeno.
2. Buscar um termo por vez, abrir a aba de vídeos curtos, assistir até o fim, curtir e salvar o que serve, pular na hora o que não serve. Depois de cada termo, rolar o feed 5 min do mesmo jeito.
3. Fechar e abrir o app. Se o feed ainda não é do alvo, repetir. Anotar quantas sessões foram precisas.
4. Seguir só 3 a 5 perfis: 2 grandes (o que funciona há tempo) e 2 ou 3 pequenos que crescem rápido (o que funciona agora).
5. Duas coleções salvas: **Tema** (vídeos de um assunto) e **Formato** (vídeos de QUALQUER assunto cuja estrutura queremos usar). Como a conta não tem nicho, a coleção Formato é a que mais importa.
6. Colecionar ganchos ouvindo só os 5 primeiros segundos, 10 min por semana; anotar o tipo e o molde, sem copiar a frase.

## Planilha de 15 referências (`conteudo/estudos/referencias.md`)
Meta inicial: 15 linhas, pelo menos 5 de assuntos diferentes dos que já fizemos. Colunas: link | criador | rede | coleção (Tema ou Formato) | TIPO de gancho | promessa | estrutura em 3 a 5 passos | duração | recurso visual | hipótese do porquê funcionou (separada do que foi observado) | como adaptamos. "Salvar sozinho vira gaveta": cada salvo ganha linha na mesma semana.
- Descrever o vídeo com palavras nossas, escrever o molde em 1 linha sem citar o assunto original e propor 3 peças nossas com outro exemplo, outra voz e outra prova.
- **Regra das 3**: só vira série ou formato nosso o molde que aparece em 3 referências de criadores DIFERENTES. Com 1 referência a chance de sair cópia é grande. Crédito, borda, marca d'água e legenda não transformam um vídeo em nosso.
- **Lacuna de idioma**: formato que já funciona em outro idioma ou assunto e ainda não aparece em português. Nunca afirmar que "não existe": marcar [CONFERIR NA BUSCA] e buscar de verdade em português antes de decidir.
- **Sinal de recomendação** (YouTube): na busca com filtro de recentes, olhar canais PEQUENOS (menos inscritos do que views do vídeo) com muita view em poucos dias. Para comparar idades diferentes, views divididas pelos dias desde a publicação. Dá para automatizar com a TranscriptAPI (`list_channel_videos` e metadados).
- Moda ou demanda: no Google Trends (Brasil, 5 anos) curva estável ou subindo é demanda; "montanha que sumiu" é moda.

## Filtros antes de um tema entrar no banco (nosso, a partir do livro 07)
"E daí?" (muda algo para quem assiste?) e teste do envio (mandaria a um amigo?). Desconfiar da variação cosmética ("3 dicas" x "3 segredos" é o mesmo tema; variação real muda o problema, a prova ou o contexto). Notícia: fonte original (quem publicou primeiro), data conferida na própria página e prazo de validade. Se a resposta ao "E daí?" for nada, descarta.
Leia junto: `escala-medicao-e-teste` (número de cada referência quando virar peça nossa).

## Entrega diária
3 temas, cada um com: prova (views e data), esqueleto, ideia da nossa versão e título da série. Salvar em `conteudo/AAAA-MM-DD/radar.md` e manter `conteudo/banco-de-temas.md` (temas que funcionaram sobem; os que floparam saem).

## Sinais de tema bom
Funciona para muita gente (amplo), tem tensão que sobe e desce, dá para virar série de 3 a 7 partes, tem prova de view recente, e cabe num produto barato depois (fase 2).
