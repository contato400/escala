# Pronúncia: como escrever na fala para a voz ler certo

Uso: ao montar a fala (campo `fala` do JSON), troque a palavra pela grafia da coluna "Escreva na fala". A **legenda e o título continuam com a grafia normal**. Quem usa: `escala-voz-narracao` (antes de gerar) e `escala-revisor` (ao ouvir o vídeo).
Voz de referência: Piper `pt_BR-faber-medium`. Outra voz pode precisar de outra grafia: confira de novo se trocar.
Palavra nova: confira o fonema (`PiperVoice.load(...).phonemize("palavra")`) e a transcrição com Whisper antes de gravar aqui. Nome próprio o Whisper erra mesmo com fonema certo, então confie no fonema.

| Palavra (legenda) | Escreva na fala | Situação | Onde apareceu |
|---|---|---|---|
| chip | chipe | confirmado (Whisper leu "xip" antes da troca) | s01p1-v2, 21/11 |
| PlayStation | pleisteixon | confirmado, usado no vídeo | s02p1-gta6, 21/11 |
| WhatsApp | uatsap | a confirmar: ainda não foi gerado nem transcrito; testar a voz antes de usar | sugestão (nosso) |

Regra de manutenção: só entra aqui o que foi ouvido errado ou conferido pelo fonema. Palavra que a voz já lê certo não entra.
