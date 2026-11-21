# Acessos e segredos (só NOMES e onde moram; nunca o valor)
| Nome | Onde mora | Para que | Como revogar |
|---|---|---|---|
| TELEGRAM_TOKEN | Cloudflare, Worker chefe, segredo | bot falar no Telegram | @BotFather > /mybots > API Token > Revoke |
| DONO_ID | Cloudflare, Worker chefe, segredo | bot só responder ao Victor | trocar o valor no Cloudflare |
| WEBHOOK_SECRET | Cloudflare, Worker chefe, segredo | Telegram provar que é ele | gerar novo e rodar /configurar |
| FABRICA_KEY (e FABRICA_KEY_NOVA na troca) | Cloudflare, Worker chefe + segredo de rede do ambiente "escala" | fábrica falar com o chefe | trocar no Cloudflare e no formulário da nuvem |
| Metricool | conta nova da ESCALA (e-mail Victor Augusto) | agendar TikTok e YouTube | painel do Metricool |
