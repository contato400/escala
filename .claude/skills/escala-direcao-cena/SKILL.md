---
name: escala-direcao-cena
description: Aciona quando for transformar uma história em planos antes de gerar ou animar qualquer coisa: premissa, gancho, roteiro em duas colunas, lista de planos, storyboard por imagem, movimento de câmera, continuidade entre planos, personagem que volta em várias cenas, ou decidir o que vai em código, imagem grátis ou vídeo pago. NÃO aciona para escolher o tema (escala-radar-viral), escrever a legenda ou o texto falado do episódio (escala-roteiro-serie) nem para montar e conferir o MP4 (escala-editor-video).
---
# Direção de cena: da história aos planos

Origem: livros 08, 09, 10, 12 e 13, notas em `conteudo/estudos/livros/`. Adaptação nossa marcada "(nosso)".
Leia junto: `escala-roteiro-serie` (texto), `escala-biblia-serie` (continuidade da série), `escala-video-ia` (prompt e gerador), `escala-animacao-personagens` (boneco em código), `escala-editor-video` (montagem), `escala-voz-narracao`.

Regra de ouro: **erre no papel, depois na imagem, só por último no vídeo.** Uma linha de roteiro custa nada, uma imagem custa pouco, um clipe custa caro. O gerador não lembra do pedido anterior: quem segura a história é o papel.

## Ordem de trabalho (3 portões)
1. Premissa, roteiro e lista de planos. Nada gasto. **Portão A:** soma dos planos bate com a duração; custo previsto escrito; Victor vê a prévia na fila.
2. Fichas (personagem, lugar) e storyboard, uma imagem por plano. **Portão B:** todas lado a lado, na ordem, conferidas.
3. Piloto: o plano mais arriscado primeiro. **Portão C:** piloto visto, custo real ao lado do previsto. Só então o resto.
Pular portão é o erro mais caro: o livro 09 gastou 2.800 créditos num clipe repetindo um defeito que já estava na imagem aprovada.

## 1. Premissa em uma frase
"[Personagem com um traço que se vê] quer [desejo concreto], mas [obstáculo]; até que [virada], e [nova realidade numa imagem]."
- Mais uma linha de **mensagem central** (o que a história prova). Plano que não serve à mensagem nem a uma batida sai.
- Testes: alguém quer, algo atrapalha, algo muda. O desejo tem fim visível. A virada nasce de ajuda, descoberta, decisão ou revelação (sorte não vale). O obstáculo piora antes de melhorar. A última imagem responde à primeira.
- Teste da Story Spine: troque "por causa disso" por "e depois". Se ainda faz sentido, os fatos estão só em fila.
- **Um impossível por vídeo, com função** (mostra o desejo, a virada ou a mensagem). Tire: se nada se perde, era enfeite.
- Sem nicho (decisão do Victor): a premissa vem do que viralizou, de qualquer assunto.
- Estrutura: 15 s = problema já rolando 0-4, virada 4-11, nova realidade 11-15. 30 s = situação 0-7, conflito e virada 7-23, resolução 23-30. 60 s = mundo 0-12, desejo e problema 12-24, tentativa e obstáculo 24-36, virada 36-46, nova realidade 46-60.

## 2. Gancho = o melhor quadro nos 3 primeiros segundos
- Pegue o quadro mais forte da história (o que estava no meio) e leve para o começo, corte seco para o início real. O quadro volta mais tarde e responde à pergunta. Testa no editor, sem gastar nada.
- Segura quando: funciona sem som e sem letreiro; já está em movimento no 1º quadro (sem tela preta, logo, fade); abre uma pergunta; vem da própria história.
- Quatro formas: ação no meio, detalhe que o olho não vê, rosto reagindo a algo fora do quadro, o fim primeiro.
- Aprove o gancho como imagem antes de animar. Mais ganchos: `escala-ganchos-retencao`.

## 3. Roteiro em duas colunas: IMAGEM | SOM
- Uma linha por mudança que o público precisa ver. Imagem com verbo de gesto ("o sorriso desmancha devagar" se filma; "ela fica decepcionada" não).
- Som com dono: quem fala (entre aspas), ambiente, efeito, música ou **silêncio planejado**. Letreiro, preço e cartela vão para a edição.
- Rodapé CONTA: soma dos tempos, palavras faladas (2 a 2,5 por segundo, com 0,5 s livre antes e depois), segundos de voz. 15 s ~35 palavras e 3 a 5 planos; 30 s ~75 e 6 a 9; 60 s ~150 e 10 a 14.
- Plano de 4 a 6 s quando há o que olhar, 2 a 3 s quando a cena corre. Plano com fala = fala cronometrada + 1 s.
- Teste "e se tirar?" em cada efeito e inserção: se o público entende igual sem ele, corta.
- Copiar o ritmo de um viral: anote o segundo de cada corte e use como ponto de partida. As imagens são nossas.

## 4. Lista de planos e ficha de plano
Colunas da lista: Nº | batida | tempo | duração | plano | UM movimento | ação | lado na tela | som e fala | porta/ferramenta | entradas | quadro do storyboard | status. Modelos completos em `references/fichas.md`.
- Ficha de plano em 10 eixos: sujeito, ação, ambiente, estética, luz, enquadramento (os 6 da imagem) + movimento do sujeito, movimento de câmera, ritmo e som (os 4 do tempo).
- Ordem do pedido de vídeo: **câmera: cena. detalhes.** Câmera primeiro (plano, altura, UM movimento com velocidade e alvo), depois quem faz o quê onde, depois estética e som.
- Reserve por cena um **plano de reação** e um **inserto** (curtos, baratos, salvam a montagem quando um gesto entorta).
- Plano que o aviso do assistente deve pegar: menos de 2 s, mais de 8 s, fala que não cabe, dois falantes com boca no mesmo plano.

## 5. Storyboard: uma imagem por plano
- Uma imagem por **plano**, nunca por batida (com uma por batida a manga mudou e a luz saltou). Duas variações por quadro. Nome `pNN-sb.png`.
- A imagem mostra o **começo da ação**, no estado de antes (amarra: solto; acende: apagado; enche: vazio). Tudo que o pedido cita está no quadro ou na referência, senão o gerador inventa.
- Confira lado a lado, na ordem do filme: rosto, roupa, luz, objetos, lado da tela. Corrija na imagem; só depois gere vídeo.
- Câmera e luz de uma imagem passam para a seguinte: alinhe as cenas-mestras numa tela e leia a luz de uma para a outra antes de qualquer clipe.

## 6. Câmera com significado
Escolha o movimento pela pergunta do plano, depois pelo efeito.
| Pergunta do plano | Movimento |
|---|---|
| O que acontece aqui? | câmera parada (a mais difícil de obter: escreva "no tripé, não se move" e o que se mexe no cenário) |
| O que está ao lado? | pan, tilt, whip pan |
| Onde eu entro? | push-in, dolly, travelling, arco, grua |
| O que devo reparar? | zoom, crash zoom (parado, golpe, parada seca) |
| Onde estamos? | aéreo, top shot (peça a imagem de chegada) |
| Com quem estou? | câmera na mão, acompanhamento, por cima do ombro |
| O que estava escondido? | revelação, troca de foco |
- Pedido de câmera tem 5 peças: tipo (nome em inglês entre parênteses), velocidade e duração, alvo (onde para, pelo corte no corpo: "até cortar no peito"), o que o sujeito continua fazendo, trava ("só esse movimento").
- **Um movimento por plano.** Nomear equipamento ("drone") faz o objeto aparecer: descreva o ponto de vista. Órbita de 360 graus inventa o verso. Perto de rosto, pouco e devagar.
- Tamanho do plano pelo corte no corpo: geral, conjunto, inteiro, americano (joelhos), médio (cintura), primeiro plano (peito), close (ombros), detalhe. Ângulo pelo poder: de baixo engrandece, de cima fragiliza, rente ao chão dá escala. Lente: número e efeito (24 situa, 50 perto do olho, 85 retrato).
- No motor em código (nosso): push-in = zoom lento no centro; pan e tilt = deslocamento; parallax = camadas em velocidades diferentes; câmera na mão = jitter de poucos pixels.

## 7. Continuidade
- **Raccord:** objeto, roupa, luz, direção de quem anda e olhar não pulam. Cortar no meio de um gesto esconde o corte.
- **Ficha do set** por cena, com o campo ESTADO (molhado, rasgado, aceso, mordido, objeto em qual mão). Repita o estado em todo pedido depois que ele muda. A frase de luz e a roupa usam as MESMAS palavras em todo pedido.
- **Eixo de 180 graus:** todas as câmeras do mesmo lado da linha entre os personagens. O modelo não sabe onde ela passa: escreva o lado de cada um em todo pedido.
- **Cena-mestra com inventário:** para o mesmo lugar em vários planos, aprove um plano aberto e escreva o inventário (personagens e roupa, objetos, luz, cores, hora, clima). Cada vista parte da cena-mestra, nunca da vista anterior: "Mesma cena e mesmo instante da imagem 1. Só a câmera muda: [...]. A luz vem de [...] vista do novo lugar." A luz não gira com a câmera. Peça só o que o inventário tem.
- Corte por semelhança: a forma na mesma posição do quadro nos dois pedidos. J-cut e L-cut: a voz chega antes da imagem ou continua sobre o corte.
- Cadeia de clipes: o último quadro (exportado com `ffmpeg -ss T -i v.mp4 -frames:v 1 q.png`, nunca print) abre o próximo. Depois de 3 ou 4 elos, volte à imagem aprovada.

## 8. Personagem fixo
- Ficha em texto (idade, rosto, cabelo, roupa com cor e tecido, 2 ou 3 traços que se leem pequenos) colada IGUAL em todo pedido. Cada personagem com um traço que o separa dos outros.
- **Âncora aprovada:** frente, expressão neutra, fundo liso, luz uniforme, uma pessoa, sem texto. Gere 3 ou 4, aprove 1, salve `<nome>-ancora`. O defeito dela vai para todas as cenas; trocar no meio da série = salvar `-2` e refazer as dependentes.
- **Folha em 3 vistas** (frente, três quartos, perfil), pedida como "três fotografias da mesma pessoa lado a lado", nunca como "folha de personagem". Em estilo desenhado, o estilo da âncora é o estilo da série.
- Série sempre parte da âncora, nunca da última imagem boa (cópia da cópia vira outra pessoa). Frase no fim do pedido: "Mantenha rosto, cabelo e roupa da referência."
- Uma pessoa por imagem; lugar vazio na referência (o modelo copia pose); mapa "Imagem 1 é..., Imagem 2 é..." na ordem do envio; trava "exatamente 3 pessoas, cada uma uma vez". Se o rosto não volta em 2 tentativas, simplifique a cena.
- Referências do mundo real: nunca rosto de pessoa real, famoso, Wesley ou Victor.

## 9. Uma ação por clipe
- Um gesto e um movimento de câmera por clipe. Duas ações viram transição inventada. Clipe com rosto: 5 s, câmera parada ou lenta, gesto pequeno.
- Transição entre dois quadros muda UMA coisa (lugar, distância ou assunto, não os três).
- Fala em quadro só com boca sincronizada; sem isso, narração fora de quadro (já é o nosso padrão).
- Gere longo e acelere queda lenta na montagem (`setpts`). A duração pedida não é garantida: monte pelo segundo real.

## 10. Onde cada plano é feito (custo perto de zero)
| Plano | Como |
|---|---|
| Cena fixa, texto, gráfico, boneco | motor em código (`motor/`, `escala-animacao-personagens`) |
| Cenário, storyboard, cena sem personagem que volta | imagem grátis (FLUX schnell pelo Worker, uns 170 por dia), animada por câmera em código |
| Gancho, virada, final | vídeo pago, só com OK do Victor e custo lido antes (no Higgsfield, `estimate_video_cost`) |
- Corte seco é grátis, não deforma e todo mundo entende. Monte primeiro só com cortes e gere clipe só onde a história pede continuidade.
- FLUX schnell gera só por texto (nosso, confirmar antes de prometer): consistência vem de ficha igual, bloco de estilo igual e seed fixa se houver. Personagem idêntico em muitos planos = boneco em código ou gerador com imagem de referência.
- DECISÃO DO VICTOR: qual gerador com imagem de referência (Gemini/Nano Banana, ChatGPT) fixa as âncoras; e quando liberar Flow, Veo ou Kling para os planos pagos.
- Rascunho (1 saída, resolução baixa, mesmo modelo do final) > piloto > final. Nunca "gerar de novo com o mesmo pedido" para corrigir: se o erro volta igual, está na imagem ou no texto; se muda, é sorteio.

## Checklist antes de entregar ao Victor
- [ ] Premissa de uma frase e mensagem central escritas.
- [ ] Melhor quadro nos 3 s, funcionando sem som.
- [ ] Roteiro IMAGEM | SOM com a CONTA fechando.
- [ ] Lista de planos com UM movimento cada, reação e inserto previstos.
- [ ] Storyboard lado a lado, uma imagem por plano, estado de antes.
- [ ] Ficha do set com ESTADO; lado da tela escrito; luz igual.
- [ ] Âncora e folha dos personagens aprovadas.
- [ ] Custo previsto por plano, ferramenta grátis antes da paga.
- [ ] Rótulo de IA, sem rosto real, sem texto dentro da imagem.
