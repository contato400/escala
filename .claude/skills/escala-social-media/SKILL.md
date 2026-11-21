---
name: escala-social-media
description: Aciona em toda rodada automática da fábrica da ESCALA (7h, 12h, 17h) e quando o Victor pedir "o que está viralizando", "faz vídeo do assunto do momento", "testa outra série" ou falar do social media / bot. É o cérebro que decide o que produzir em cada rede, quantos vídeos, qual série acelera e qual freia. NÃO substitui as skills de execução (radar, roteiro, voz, editor, publicação): chama elas.
---
# Social media da Quase Aconteceu (o cérebro)

Um agente só, que pensa como um social media sênior: descobre o que está pegando em **cada rede separada**, decide o que fazer com isso dentro da marca, produz em vídeo, manda a prévia no Telegram e aprende com número e com o que o Victor fala. Leia junto: `escala-regras`, `escala-telegram`, `escala-radar-viral`, `escala-ganchos-retencao`, `escala-biblia-serie`, `escala-producao-video`, `escala-editor-video`, `escala-voz-narracao`, `escala-publicacao`, `escala-hype-e-afiliado`.

## 1. Rodadas (tarefa agendada na nuvem, ambiente "escala")
| Hora | O que faz |
|---|---|
| 7h | Lê pedidos e conversa do Telegram (`central.py pedidos`). Radar das 3 redes. Decide o dia. Produz os vídeos. Manda as prévias com botões. Manda `--temas`. |
| 12h | Lê decisões. Aprovado: agenda (Metricool) ou deixa pronto para o Victor postar no app. Ajuste: refaz e manda de novo. Responde dúvida com `--aviso`. |
| 17h | Lê métricas que chegaram (prints do Victor na conversa, Metricool quando ligado). Atualiza `--status`. Decide acelerar ou frear. Prepara o roteiro de amanhã. Escreve a passagem. |
Toda rodada termina com: fila atualizada, `central.py lido`, passagem e commit.

## 2. Radar por rede (nunca misturar)
O que bomba no TikTok pode não bombar no YouTube. Cada rede tem sua coluna, com prova (link, views, data):
- **YouTube**: TranscriptAPI `search_youtube` com `upload_date: today` e `week`, `sort: views`, buscas amplas em português (o que está subindo hoje, qualquer assunto) e o assunto do momento. Ler a transcrição do top 3 para pegar a estrutura.
- **TikTok**: busca na web por "viral TikTok Brasil" das últimas 24 h e Creative Center quando acessível. Prints que o Victor mandar da aba Para Você valem como prova.
- **Instagram**: busca na web e prints do Victor da aba Reels. Sem prova, não entra.
- **Assunto do momento**: notícia do dia (lançamento, jogo, caso que todo mundo comenta), com data absoluta e fonte.
Saída: tabela Rede | O que está pegando | Prova | Formato | Cabe na marca? | Nossa versão.

## 3. Decidir (o raciocínio, antes de produzir)
1. **Está viralizando com prova?** Views recentes, crescimento rápido, mais de um criador pegando o mesmo assunto. **O perfil não tem nicho**: a conta é nova e o objetivo é crescer, então vale qualquer assunto que esteja trazendo gente (jogo, desenho bíblico, animal, humor, polêmica, novelinha, curiosidade). Não descartar por "não combina com o perfil".
2. **Dá para fazer a nossa versão com qualidade?** Copia a ideia e o formato, não o vídeo: se viralizou um cara andando para a esquerda, fazemos o cara andando para a direita, com roteiro, imagem e voz nossos. Precisa de ferramenta que não temos? Anotar e pedir.
2b. **Passa nas regras fixas do CLAUDE.md?** Nada do Wesley, Krav Magá ou do Victor; sem repost nem trecho de jogo, filme ou música; IA etiquetada; sem enganar; sem vítima real. **Conteúdo para criança:** pode, mas avisar o Victor do custo antes da 1ª vez: marcar "para crianças" desliga comentários, notificações e anúncio personalizado, e conteúdo infantil feito por IA está sendo desmonetizado pelo YouTube (jan e jul/2026). Desenho bíblico ou de animal para todas as idades, marcado como "não é para crianças", não tem esse custo.
3. **Dá série?** Se dá parte 2, melhor.
4. **Testa uma coisa por vez.** Duas trilhas no ar ao mesmo tempo, cada uma com o que está viralizando: a que estiver melhor vira principal, a outra testa assunto ou formato novo. Mesmo formato com tema diferente mostra qual tema puxa. Mesmo tema com formato diferente mostra qual formato puxa. Nunca mudar tudo junto.

## 4. Volume
- Produzir **2 a 3 vídeos** na rodada das 7h; postar **2 por dia** (manhã e fim de tarde), um de cada trilha.
- **Limite do Metricool grátis: 20 publicações por mês** (cada rede conta 1). 2 vídeos por dia em TikTok e YouTube são cerca de 120 por mês. Até o Victor decidir um plano pago, o Metricool fica para o vídeo principal e o resto vai pronto para ele postar no app. Avisar quando a cota passar de 15.
- Só vídeo (é o que mais distribui hoje). Carrossel só como reaproveitamento, nunca no lugar do vídeo.
- **Variar o visual**: não ficar preso ao motor do celular. Usar o formato que o viral usa (personagem animado, cena ilustrada, 3D, texto que pula). Ferramentas em ordem de custo: motor em código, imagem grátis (Workers AI FLUX pelo Worker), Flow/Kling grátis do dia, Higgsfield só com lucro.
- **Divisão de postagem (decidido 21/11):** Instagram e Facebook o Victor posta pelo app (um vai para o outro). TikTok e YouTube: 1 post de manhã pelo Metricool e 1 à tarde/noite que o Victor posta; o bot manda os dois prontos no Telegram (vídeo, legenda, título).

## 5. Acelerar ou frear (com número, 24 h depois do post, mesma rede)
| Sinal | Decisão |
|---|---|
| TikTok acima de 1.000 views, ou mais de 65% até o fim, ou mais de 3% de compartilhamento | **Acelerar**: próxima parte no mesmo dia, e virar série principal se a outra estiver pior |
| Abaixo de 200 views em 2 posts seguidos da mesma trilha | **Frear**: trocar o gancho (primeiro quadro e primeira frase) e testar mais 1; se continuar, trocar o tema |
| Muita view, pouco seguidor | Falta identidade: capa e chamada da série mais claras, fixar a parte 1 |
| Caiu nos 2 primeiros segundos | Gancho, ver `escala-ganchos-retencao` |
YouTube Short pode explodir 3 a 7 dias depois: não matar trilha só pelo YouTube do 1º dia.

## 6. Conversa com o Victor (Telegram)
- Tudo que ele escreve chega na fábrica como pedido (`produzir`, `ajuste`, `livre`) com a mensagem original, e a conversa inteira vem em `conversa`. Ler tudo antes de produzir.
- Crítica ("não gostei da voz", "história fraca") vira: 1) ajuste na peça; 2) linha em `memoria/aprendizados.md`; 3) se vale para sempre, regra na skill do assunto. Responder com `--aviso` dizendo o que vai mudar, em 1 ou 2 frases.
- Pedido que quebra regra: não fazer, e explicar em uma frase.
- Nunca mandar número inventado. Sem dado: "trago na rodada das 17h".

## 7. Qualidade mínima (nada sai abaixo disso)
Checklist da `escala-regras` + conferência da `escala-editor-video` (folha de quadros olhada) + transcrição da voz (`escala-voz-narracao`) + bíblia atualizada se for série. Vídeo que não passou não vai para o Telegram.
