---
name: escala-biblia-serie
description: Aciona quando for começar uma série nova, escrever o próximo episódio, conferir continuidade, criar personagem fixo ou montar série em que o público vota na ESCALA. NÃO aciona para vídeo avulso de notícia ou alerta sem continuação.
---
# Bíblia da série (o público lembra de tudo)

Se no episódio 3 a corrente ficou por dentro da porta, no 10 ninguém pode tirar pelo lado de fora: alguém comenta, e o comentário de furo derruba a série. Toda série tem um arquivo `conteudo/series/<serie>/biblia.md`, lido inteiro **antes** de escrever cada episódio.

## Modelo do arquivo
```
# <Nome da série>
Premissa (1 frase):
Narração: (segunda pessoa "você" / terceira pessoa) · voz:
Formato: duração, 1 episódio = 1 dia da história? termina em escolha?
Tom e limites: (o que a série nunca mostra)

## Personagens fixos
| Nome | Papel | Aparência (cabelo, roupa, cor fixa) | Jeito de falar | Voz | Bordão ou mania | Nunca faz |

## Lugares
| Lugar | Como é (o que tem dentro, onde fica cada coisa) |

## Regras do mundo (numeradas, uma nova por episódio quando fizer sentido)
1. ...

## Linha do tempo
| Ep | Dia da história | O que aconteceu | Onde cada personagem terminou | Objetos e estado (porta trancada? luz?) | Escolha do público e resultado |

## Ganchos abertos (perguntas que o público quer ver respondidas)
## Ideias para próximos episódios
```

## Antes de escrever o episódio
1. Ler a bíblia inteira e os 2 últimos roteiros.
2. Procurar furo: personagem num lugar impossível, objeto que mudou de estado, regra quebrada.
3. Escrever, depois **atualizar a linha do tempo** e os ganchos abertos.

## Série com voto ("você decide")
- Fechar cada episódio em **duas** opções claras e curtas.
- Contar os votos dos comentários em 12 a 24 h (mais curtidos contam como apoio) e registrar o resultado na linha do tempo.
- As duas opções precisam render história; nunca uma opção "certa" óbvia.
- Responder comentários dizendo a opção que está ganhando (puxa mais comentários).

## Personagem consistente na imagem
Cada personagem fixo tem uma **ficha visual aprovada** (frente, perfil, 3/4 e 3 expressões) em `conteudo/series/<serie>/personagens/`. Toda imagem nova parte da ficha como referência, nunca só do texto. Em animação desenhada em código (`escala-animacao-personagens`), a ficha é o próprio componente com as cores fixas.
