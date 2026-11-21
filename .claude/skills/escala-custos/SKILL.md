---
name: escala-custos
description: Aciona quando for gastar ou pensar em gastar com gerador de vídeo ou imagem, voz, API ou assinatura (Higgsfield, Kling, Veo, Flow, Seedance, ElevenLabs, Nano Banana, plano do Claude), antes de clicar em gerar, ao fechar o custo de um vídeo ou série, ao medir o limite do Claude por rodada, ou quando o Victor perguntar "vale pagar?". NÃO aciona para escolher o que gerar (escala-video-ia) nem para decidir tema (escala-radar-viral).
---
# Custos: gastar só quando o lucro pagar

Origem: livros 09, 11, 12, 13, 15, 16 e guias curtos (g01, g02, g04), notas em conteudo/estudos/livros/. Preços datados de out e nov/2026: **conferir o preço de hoje** antes de decidir (tabela em `references/precos-referencia.md`). Leia junto: `escala-video-ia`, `escala-conformidade-plataformas`, `escala-regras`.

## 1. A regra
Custo perto de zero. Gerador pago só com lucro no caixa e "DECISÃO DO VICTOR" escrita. Sem teto e sem custo previsto, nada pago roda.
Conta de grandeza (livro 09): vídeo de 60 s feito só de clipes gerados custa R$ 100 a R$ 250 contando refações. Com 2 posts por dia isso não fecha. Gerar clipe só nos 2 ou 3 planos que mais valem (gancho, virada, final); o resto com imagem grátis, movimento de câmera no motor, corte seco e som bom (nosso).

## 2. Custo por segundo aprovado
`custo por segundo aprovado = créditos gastos em TODAS as versões do plano ÷ segundos que entraram no corte`.
- Preço de tabela mente: no caso do livro 09, modelo de 100 por segundo virou 250 por segundo aprovado, e plano com 4 versões para 3 s virou 667 por segundo.
- Custo da entrega aprovada (livro 12): `custo por tentativa × tentativas até aprovar + horas`. Quase nunca se aprova na primeira.
- Gravar em `projeto/tentativas.md` (colunas acrescentadas: unidade de cobrança, seed, aprovada sim/não). Ao fechar o episódio, uma linha: custo do vídeo aprovado.
- Custo fixo por peça = assinaturas usadas no mês ÷ vídeos do mês; somar o variável (livro g01).

## 3. Antes de cada geração paga (checklist)
1. Ler o custo no botão de gerar, que não gasta nada. Se não aparecer, escrever "teste" no pedido e olhar de novo. Com o Higgsfield MCP, rodar `estimate_video_cost` ou `estimate_image_cost` antes de `generate_*` e mostrar o número.
2. Previsto = créditos por segundo × segundos × tentativas (3 por plano como partida: simples 2 rascunhos + 1 final; elenco 3 + 1; fala e ação 4 + 2).
3. Pedir UMA saída por vez. Cada saída extra é geração paga e as versões saem parecidas.
4. Mudar um campo por vez e anotar. Duração é linear: 15 s não sai mais barato que 3 de 5 s.
5. Agente que escolhe modelo sozinho gasta sem avisar: marcar 1 modelo de imagem e 1 de vídeo, dizer o formato em cada pedido e pedir estimativa antes (livro 13).
6. Um clique = no máximo uma chamada, sem nova tentativa automática, registrada com hora (livro 03). Falha também conta como gasto.
7. Baixar o resultado no mesmo dia (a API do Google guarda 2 dias). Salvar prompt, ficha e vídeo fora da ferramenta com modelo e data: o Sora foi desligado em 2026.

## 4. Fases e regras de parada
| Fase | Para que serve | Como |
|---|---|---|
| Rascunho | o pedido se entende? | modo barato, 1 saída, baixa resolução |
| Piloto | o plano completo funciona? | MESMO modelo do final, elenco, fala e duração definitivos, resolução baixa. Primeiro piloto é a sequência mais arriscada (2 ou 3 personagens, fala em quadro) |
| Final | só do aprovado | resolução que o destino pede e só ela: 1080x1920 basta; 4K custa 4 a 5 vezes |
Rascunhar em outro modelo não aprova nada. Refazer o final: mesma seed e parâmetros, ou o piloto como referência. Nunca "gerar de novo com o mesmo pedido": sorteia tudo.
Paradas:
- **Por plano:** passou das tentativas do tipo, muda uma coisa grande (a porta, o quadro ou o plano). Mantém "3 tentativas sem melhora" da `escala-video-ia`.
- **Por fase:** não abrir a seguinte sem refazer a conta com números reais.
- **Por projeto:** aos 80% do teto, parar planos novos e montar com o que existe.
- **Teto** = previsto + folga (50% no primeiro projeto, depois o desvio do último; nunca menos que refazer a sequência mais cara).
- **Ordem de corte** se apertar: plano que outro já cobre; segundos de planos calmos; resolução do final sem rosto; só no fim fala ou personagem.

## 5. Travas de gasto (antes da primeira chamada paga)
1. Crédito **pré-pago sem recarga automática** (o saldo é o teto; com recarga, erro ou chave vazada compra crédito no cartão). Assinar mensal antes de anual, só anual depois de 3 meses medidos. Cartão virtual com limite próprio.
2. **Limite rígido** por projeto ("hard limit") e alerta na metade. O corte não é instantâneo (pode passar uns 10 min): manter saldo baixo e as duas travas juntas.
3. **Chave restrita** a um recurso, uma por uso, digitada pelo Victor; nunca no chat, arquivo ou log. Vazou: revogar primeiro, criar outra depois. Nunca guardar chave em arquivo (CLAUDE.md).
4. **Modo teste ligado por padrão**: qualquer valor diferente de "desligado" não chama a API e devolve exemplo marcado.
5. Plano "ilimitado" cobre poucos modelos, entra em fila e NÃO vale por conector (MCP) nem API: cobra crédito. Anual libera o saldo do ano no 1º dia: dividir por 12 como teto mensal.
6. Conta em dólar: multiplicar pelo câmbio e por 1,035 (IOF). Anotar serviço, plano e data de renovação para cancelar no dia certo.

## 6. O que é grátis hoje e o que custa
| Item | Situação (conferir licença em `escala-conformidade-plataformas`) |
|---|---|
| Piper (voz pt_BR), motor em código (Playwright + ffmpeg), trilha gerada pelo motor | grátis |
| Cloudflare Workers AI, FLUX schnell | cerca de 170 imagens por dia grátis |
| Cloudflare Workers (bot) | grátis, 100 mil pedidos por dia |
| Metricool | 20 posts por mês grátis (cada rede conta 1); avisar passando de 15 |
| Nano Banana no Gemini, ChatGPT imagem, créditos diários do Kling | grátis em cota pequena, **uso pessoal ou com marca d'água: conferir antes de monetizar** |
| Nano Banana pela API do Google | NÃO tem nível grátis (pré-pago mínimo US$ 5) |
| Higgsfield, Kling pago, Veo/Flow nos créditos, Seedance, ElevenLabs, HeyGen, Magnific | pago: só com lucro e DECISÃO DO VICTOR |
Tabela de custo por vídeo (nosso): etapa | ferramenta | chamadas | preço unitário | total. Preencher antes de aprovar série nova.

## 7. Medir o limite do Claude por rodada
O limite do plano é a conta real da fábrica. Por rodada (7h, 12h, 17h): rodar `/usage` antes e depois, anotar o gasto por tipo de tarefa em `memoria/aprendizados.md` (rodada, tarefa, % usada). Vídeo com animação, 3D e conferência quadro a quadro pesa mais.
Para gastar menos: rodada é sessão nova; ler só os arquivos necessários; pedir saída em formato curto; corrigir por trecho; comece pelo modelo mais barato que dá conta e **suba o esforço antes de subir o modelo**; tarefa mecânica em esforço baixo; nunca trocar de modelo no meio da rodada. Se o cache expirou (espera longa de render), encadear tarefas.

## 8. Quando vale pagar
Só com receita real e "DECISÃO DO VICTOR". Antes de pedir gasto ao Victor, entregar:
1. Preço de HOJE (conferido) e a alternativa grátis.
2. O que muda no resultado, com número da série: se a retenção cair por causa da voz, vale testar voz paga; se não, não.
3. Conta: custo novo por mês, receita do mês (fato) ou estimativa (suposição), ponto de equilíbrio e cenário fraco com METADE da receita estimada.
4. "Se..., então...": o dado que mudaria a conclusão. Sem "você deve", sem porcentagem de chance.
Gatilho sugerido (nosso): receita do mês cobrindo 2 vezes o custo novo, mês fechado. Hub de várias IAs: não assinar, ir direto à fonte (opinião do guia g02).
