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
| Gancho (0 a 2 s) | "Ela abriu a porta e..." |
| Estrutura | cena chocante → contexto rápido → 2 viradas → gancho |
| Por que prende | curiosidade, injustiça, medo, identificação |
| Como adaptar (nossa versão) | personagem, cenário e virada nossos |
Nunca copiar falas, imagens ou personagens; extrair só o esqueleto.

## Entrega diária
3 temas, cada um com: prova (views e data), esqueleto, ideia da nossa versão e título da série. Salvar em `conteudo/AAAA-MM-DD/radar.md` e manter `conteudo/banco-de-temas.md` (temas que funcionaram sobem; os que floparam saem).

## Sinais de tema bom
Funciona para muita gente (amplo), tem tensão que sobe e desce, dá para virar série de 3 a 7 partes, tem prova de view recente, e cabe num produto barato depois (fase 2).
