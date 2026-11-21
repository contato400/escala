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

## Mudanças (registro de versão)
Toda mudança em skill, ficha de agente ou prompt do bot ganha UMA linha em `memoria/versoes.md` (criar na primeira mudança, com este cabeçalho), no mesmo commit da mudança:
`versão | data | skill, ficha ou prompt | o que mudou | motivo (com evidência) | quem aprovou | teste refeito (qual)`
Exemplo (fictício): `v1.1 | 2026-11-21 | escala-telegram | recusa "pode ser" como aprovação | bateria 11 falhou | Victor | bateria de 12 mensagens`.
- Mexer só nas linhas da causa, mostrar antes e depois. Se piorou outra coisa, voltar à versão anterior (o git guarda) e pedir de novo mais claro, sem "corrigir a correção".
- Corrigiu a mesma coisa duas vezes: vira regra na skill do assunto, uma linha concreta e conferível. Regra que atrapalha pedido legítimo se muda no arquivo, não se contradiz no chat. Editar a linha antiga em vez de empilhar "mas atenção".
- Skill nova ou com descrição mudada: teste de acionamento de 10 frases (`escala-rotinas-autonomas`). Ficha de agente nova: seções "Não faz" e "Para e pergunta ao Victor quando".
- Vídeo com erro de produção (não de tema): achar o PRIMEIRO arquivo da execução que traz o erro; ele aponta a skill ou ficha culpada; registrar em `memoria/aprendizados.md` com a linha citada.
- Mudança que vem de fora (regra de rede, rótulo de IA, monetização): também vira linha em `versoes.md`.

## Revisão mensal (dia 1)
Escrever primeiro o que mudou no mês. Depois: `aprendizados.md` e `estado.md` item a item (o que diz | de onde veio | ainda certo? | manter, corrigir ou apagar; marcar "visto" ou "deduzido"; dedução sem arquivo vira pergunta ao Victor ou sai); contradições entre CLAUDE.md, skills e fichas (apagar a versão velha); ferramentas e conectores sem uso. Manter `estado.md` em uma página e meia; histórico vai para `passagem.md`.
Passagem ganha dois campos: "descartado, não voltar" e "a confirmar" (decisão que apareceu de dois jeitos), mais uma frase de abertura para a próxima sessão. Nada combinado no Telegram vale se não foi escrito em `memoria/`.

