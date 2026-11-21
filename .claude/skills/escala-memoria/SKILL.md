---
name: escala-memoria
description: Aciona SEMPRE no começo e no fim de qualquer tarefa da ESCALA, e quando o Victor perguntar "já fizemos isso?", "o que está pendente?" ou pedir para registrar ou lembrar algo. NÃO aciona para guardar senha, chave, telefone ou e-mail.
---
# Memória da ESCALA (nada se perde)

## Começo
Ler `memoria/estado.md`, a última entrada de `memoria/passagem.md`, `memoria/aprendizados.md` e a ficha do agente em `.claude/agents/`. Conferir se a tarefa já foi feita.

## Fim de cada etapa
1. `memoria/passagem.md`: data, pedido, feito, decisões, pendente, verificado.
2. `memoria/estado.md`: o que mudou no estado das contas (seguidores, séries no ar, produtos).
3. `memoria/aprendizados.md`: o que deu certo ou errado, com evidência (link, números).
4. Regra que vale para o próximo trabalho do mesmo tipo vai para a **skill** do assunto. O que vale só para esta peça não é registrado.
5. Ficha do agente responsável (seção "Diário"): o que fez, o que funcionou, o que melhora amanhã.
6. Commit e push no GitHub com mensagem curta.

## Nunca guardar
Senha, chave de API, código de verificação, telefone, e-mail, dado de seguidor.
