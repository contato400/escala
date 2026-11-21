# Como funciona a Central da Quase Aconteceu

## Os 3 pedaços (em 1 frase cada)
1. **O bot** (@quaseaconteceu_central_bot, "Central Quase Aconteceu"): é a portaria. Fica no Telegram, conversa com você, guarda seus pedidos e mostra os vídeos com botões. Mora no Cloudflare (grátis, sempre ligado, não depende do seu computador).
2. **A IA do bot**: um modelo grátis do próprio Cloudflare (Llama 3.3 70B, pelo "Workers AI"). Ela só **entende e responde** o que você escreve. Ela não faz vídeo, não pesquisa e não posta.
3. **A fábrica**: sou eu (Claude Code) rodando na nuvem, no ambiente "escala", com todas as skills. É quem pesquisa o que viraliza, escreve, faz o vídeo, confere e manda a prévia no bot. Hoje eu rodo quando você me chama aqui; o próximo passo é deixar agendado (7h, 12h e 17h) para rodar sozinho.

```
Você (Telegram)  ⇄  BOT no Cloudflare (guarda tudo, responde, botões)
                          ⇅  (chave da fábrica)
                    FÁBRICA = Claude Code na nuvem (pesquisa, vídeo, prévia)
```

## O que você pode fazer no bot
| Você manda | O que acontece |
|---|---|
| Qualquer frase ("não gostei da voz", "faz vídeo de GTA 6", "como estamos?") | A IA responde na hora e o texto vira **pedido** para a fábrica (ela classifica: produzir, ajuste ou conversa) |
| `/produzir <o que quer>` | Pedido de produção direto |
| **Foto/print** (ex.: estatística do vídeo) | Vira pedido tipo "print"; a fábrica baixa e lê os números |
| `/fila` | Lista o que está esperando sua aprovação |
| `/temas` | Mostra os temas que o radar achou hoje |
| `/status` | Mostra os números que o analista mandou |
| `/pausa` e `/retomar` | Freio de emergência da fábrica |
| Botões **Aprova / Ajusta / Recusa** na prévia | Aprova vira ordem de publicar; Ajusta pede que você escreva o que mudar (a próxima mensagem vira o ajuste); Recusa tira da fila |

## O que a fábrica faz em cada rodada
1. Lê tudo que você mandou desde a última vez (pedidos, prints, conversa, botões).
2. Se você mandou `/pausa`, só avisa "pausado" e para.
3. Pesquisa o que está viralizando em cada rede (com prova: link, views, data).
4. Decide o que produzir (skill `escala-social-media`), faz o vídeo, confere (revisor, transcrição da voz, área segura).
5. Manda a prévia no bot com vídeo, legenda e botões.
6. Manda um aviso curto ("fiz isso, falta aquilo") e o **sinal de vida**. Se passar 7 horas sem sinal, o próprio bot te avisa que a fábrica parou.

## Segurança
- O bot só responde ao seu Telegram (seu Id). Qualquer outra pessoa é ignorada.
- O token do Telegram fica só no Cloudflare. A fábrica usa outra chave (FABRICA_KEY) só para falar com o bot.
- Nada é publicado sem você apertar **Aprova** (ou mandar "aprova" aqui).

## Limites de hoje (o que dá para melhorar)
| Limite | Por quê | Como melhorar |
|---|---|---|
| A fábrica ainda não roda sozinha | Falta criar a tarefa agendada | Próximo passo: rodada manual 2 e agendar 7h/12h/17h |
| A IA do bot é simples | É o modelo grátis do Cloudflare | Trocar pela API do Gemini (você já assina) ou do Claude com teto baixo, se quiser respostas melhores |
| O bot não gera vídeo na hora | Vídeo é feito pela fábrica nas rodadas | Pedido urgente: me chamar aqui, ou rodada extra agendada |
| Vídeo realista (Flow/Veo) | Não há conector do Flow; o Higgsfield está no plano grátis (10 créditos) | A fábrica entrega os pedidos prontos cena por cena; você cola no Flow e manda os clipes no bot; a fábrica monta, legenda e confere |
| Publicação | Metricool grátis tem 20 posts/mês; Instagram pelo app | Plano pago do Metricool quando der lucro |
