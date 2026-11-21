---
name: escala-medicao-e-teste
description: Aciona quando for ler os números de vídeos já postados (3 h, 24 h, 72 h, semana), comparar com a média da conta, decidir o que repetir ou cortar, montar um teste (gancho, formato, horário), tratar um flop, ler um print de métrica que o Victor mandou pelo Telegram (pedido tipo "print"), escrever o relatório ao Victor ou fechar o mês. NÃO aciona para produzir o vídeo (escala-producao-video), nem para como cada rede entrega (escala-crescimento-plataformas).
---
# Medição e teste

Origem: livros 07, 01, 02, 20 e 11, notas em conteudo/estudos/livros/. Itens marcados (nosso) são adaptação da ESCALA, não estão no livro.
Leia junto: `escala-crescimento-plataformas` (como a rede entrega), `escala-ganchos-retencao` (diagnóstico pela retenção), `escala-memoria` (onde registrar), `escala-social-media` (acelerar ou frear).

Regra de base: não existe número mágico. Todo vídeo é comparado com a **própria média da conta**, nunca com número de terceiro. Estudo de 2026 diz 8,5 s de tempo médio em Reels: NÃO é meta.

## 1. Linha de base
- Uma por rede e por formato. Pegar os últimos 10 vídeos de duração parecida e tirar a média de: tempo médio assistido (ou % até o fim), % que não arrastou em 2 s e envios por mil alcançados.
- Com menos de 5 posts do formato, o primeiro número é só base. Não decide nada. Anotar em `relatorios/indicadores.md` com a data.
- Marcar os vídeos acima da média e perguntar: "o que esse vídeo fez nos primeiros segundos que os outros não fizeram?" (gancho, assunto ou formato).
- Uma métrica por função: vídeo = tempo médio e envios; carrossel = salvamentos; oferta = cliques e conversas. Para comparar post pequeno com grande, dividir pelo alcance.

## 2. Leitura em quatro tempos
| Quando | O que fazer | O que NÃO fazer |
|---|---|---|
| 3 h | Ver se começou a ser entregue; responder comentário (com aprovação do Victor) | Decidir qualquer coisa; mexer no post |
| 24 h | Acelerar ou frear a série (limiares da `escala-social-media`) | Julgar gancho ou tema |
| 72 h | Julgar gancho e formato contra a média do mesmo formato, mesma duração, mesma faixa de horário, sem impulsionamento | Julgar tema com 1 vídeo |
| 2 a 4 semanas | Olhar o conjunto: que assunto, gancho e formato se repetem nos melhores; mexer no calendário | Mudar duas coisas ao mesmo tempo |
- Conta pequena pode demorar mais para ser entregue. YouTube Short pode subir de 3 a 7 dias depois: não apagar nem esconder só porque foi mal no 1º dia.
- Dar 60 dias de ritmo constante ao método antes de julgar o método. Quem posta um mês e para não junta dado.
- Se a leitura pega o dia ainda em andamento, marcar "período incompleto".

## 3. Teste de uma variável
Escrever ANTES de produzir (em `memoria/aprendizados.md`, seção "Testes em andamento"):
1. Hipótese: "Se eu [mudança], então [métrica] vai [subir ou cair], porque [motivo]."
2. Uma única mudança. Formato, duração, assunto, horário e rede ficam iguais.
3. Número de partida (a base da seção 1) e o número que indicaria melhora.
4. Mínimo de 3 peças. Série nova entra como piloto de 5 partes e só se julga a trilha depois das 5.
5. **Data de decisão** (ex.: 15 dias) e as três saídas decididas antes: mantém, ajusta, abandona.
6. Escolher o teste mais barato. Nunca repetir teste que já está no diário, nem hipótese descartada com outro nome.
Nada novo vai ao ar na sexta à noite ou no fim de semana, e o piloto sai primeiro em 1 rede, em horário em que o Victor está olhando (nosso, de livro 20).
Horário: não existe horário mágico. Testar duas faixas (manhã e noite) por 2 semanas cada, com peças parecidas; Instagram só mostra horários de maior atividade a partir de 100 seguidores.

## 4. Ciclo do flop
Quando 2 vídeos seguidos da mesma trilha ficam abaixo da base (ou 3 posts entre 0 e 200 views), parar e abrir a ficha. Gerar de novo UMA vez antes de culpar a skill.
**Ficha do flop** (com número, sem palpite; se faltar número, anotar por uma semana antes):
- Problema em uma linha, sem a solução imaginada ("preciso trocar a voz" já escolheu a resposta).
- Fatos: views, % até o fim, % que não arrastou em 2 s, horário, e QUANDO NÃO acontece (a série vizinha do mesmo dia foi bem).
- O que já tentamos e o resultado com número.
- Resolvido quando: o limiar de "acelerar" da `escala-social-media`, por 3 dias.
**Três soluções** por caminhos diferentes (quem, o que ou como muda), cada uma com ação, responsável e quando. Avaliar contra os mesmos critérios (custo, esforço, impacto, risco de regra fixa). Solução que fere regra fixa sai com a regra citada. Não escrever "% de chance": a nota só ordena a rodada.
**Teste de 1 semana** da vencedora, com regra de decisão (mantém, ajusta, abandona) escrita antes. O resultado volta para "já tentamos" e o ciclo recomeça com um fato a mais.
Diagnóstico em ordem, parar no primeiro sim: 1) gancho (tempo médio baixo, muita gente sai no começo); 2) produção (voz, legenda, cena); 3) clareza (assistem mas não enviam: mostrar o resultado antes). Pergunta final: "eu assistiria até o fim se fosse de outra pessoa?". Se o diagnóstico for claro e a resposta for não, republicar como peça nova, em vez de mexer na antiga.

## 5. Contadores em `memoria/aprendizados.md`
Uma linha por elemento testado (tipo de gancho, formato, duração, horário, voz, série):
`elemento | ajudou=N | atrapalhou=N | neutro=N | última atualização`
- Cada peça soma 1 em UM contador, comparada com a base da seção 1 (acima da base = ajudou; abaixo = atrapalhou; dentro de 10% = neutro).
- **Mínimo de 5 amostras** no elemento antes de virar regra. Com menos, escrever "sem amostra" e não mudar skill.
- Virou regra (5 ou mais amostras com 80% ou mais para um lado)? Vira linha de comportamento na skill do assunto, escrita como "num teste, X aconteceu; faça Y", nunca como frase pronta.
- Resultado que NÃO funcionou entra com número também.

## 6. Print de métrica que o Victor manda
1. Pedido tipo "print": baixar com `python3 ferramentas/central.py arquivo <ref> print.jpg` e abrir com o Read.
2. Responder em duas listas: **Lido** e **Suposto**. Número ilegível vira "ilegível no print N", nunca palpite. Nunca arredondar.
3. Tabela linha por linha na ordem do print, nomes e unidades como aparecem, com a contagem de linhas e * nas duvidosas. Print é "uma leitura do número", não o número.
4. Esperar o Victor responder "conferido" (ou corrigir) antes de gravar em `relatorios/metricas.md`. Conferir o total e 3 valores ao acaso.
5. Para decidir acelerar ou frear, pedir o número digitado ou o export do painel. Pedir vários prints em ordem, com recorte legível, PNG ou JPEG.
6. Sem @ nem nome de seguidor em arquivo. Comentários: categorias aprovadas antes de contar, 2 exemplos copiados ao pé da letra, quantas linhas lidas.

## 7. Indicadores com definição congelada
Escrever em `relatorios/indicadores.md` na primeira semana e NUNCA mudar a definição (senão a comparação entre meses perde o valor). Mudou a regra de contagem? Abrir um indicador novo e manter o velho. Proposta (a validar com o Victor):
1. Vídeos produzidos e quantos passaram na conferência de primeira.
2. Aprovados sem ajuste, com ajuste e recusados.
3. Publicados por rede e por trilha.
4. Objetivo da trilha: % até o fim em 24 h, views em 72 h, seguidores ganhos.
5. Tempo do pedido do Victor até a prévia no Telegram.
6. Falhas de regra: pegas na conferência x escapadas para o ar (escapada é incidente).
7. Custo do mês contra o orçado.
Cada indicador tem: definição, de onde sai o número, base e meta. Seguidor ou view não é venda; na fase 2 contar também leads (pediu o link, comentou a palavra).

## 8. Relatório ao Victor (semanal e mensal): 4 blocos, uma página
1. **Números ao lado da base** em tabela curta (a tabela Tarefa | Status | Evidência | Próxima ação do CLAUDE.md segue para a rodada diária).
2. **O que mudou e por quê** (versão de skill, teste fechado).
3. **O que vem** no próximo período.
4. **Uma decisão**, com 2 ou 3 opções, a consequência de cada uma e o prazo ("responda até sexta").
Regras: só número que está em arquivo; se um número piorou, dizer o que vai ser feito; não creditar à série o que pode ter outra causa; amostra pequena = "ainda não dá para saber"; em uma linha, o que os dados não permitem afirmar; sem jargão. Se o Victor responder, registrar a decisão em `memoria/passagem.md`.

## 9. Revisão mensal (dia 1)
Painel em `relatorios/painel-AAAA-MM.md`: peças por formato; média por formato e do mês anterior; melhor peça e por quê; pior peça e diagnóstico; contadores da seção 5; diário de testes (data, hipótese, mudança, resultado, decisão); custo contra orçado; próximo teste e data. Antes, escrever em 3 linhas o que mudou no mês, para a revisão não virar faxina sem critério. Procurar a mesma regra escrita de dois jeitos em skills diferentes e apagar a velha.

## Checklist antes de fechar uma leitura
[ ] Comparei com a base do mesmo formato e duração? [ ] Tempo certo (3 h não decide)? [ ] Mexi em uma variável só? [ ] Hipótese e data de decisão estavam escritas antes? [ ] Amostra mínima respeitada? [ ] Atualizei os contadores e a passagem?
