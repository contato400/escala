---
name: escala-editor-video
description: Aciona quando for editar, cortar, legendar, sonorizar, montar ou conferir qualquer vídeo da ESCALA (série, notícia, animação, corte), fazer capa, versões ou copiar o estilo de um vídeo de referência. NÃO aciona para escolher tema (escala-radar-viral) nem escrever o roteiro (escala-roteiro-serie).
---
# Editor de vídeo da ESCALA

Régua de qualidade herdada do que o Victor já aprovou e reprovou em outro projeto ("simples e feio" foi reprovado; "ficou brabo demais" foi aprovado), dos livros da Mestres Play (07, 08, 09, 10, 13) e da pesquisa de 21/11 no YouTube. Leia junto: `escala-producao-video` (motor e ferramentas) e `escala-ganchos-retencao`.

## 1. Pastas e nomes (original nunca é alterado)
`conteudo/AAAA-MM-DD/<peça>/` com `originais/`, `assets/`, `projeto/`, `entregas/`.
Arquivo: `qa_<serie>_<formato>_vN-<o-que-mudou>_AAAA-MM-DD.mp4`. Nunca "final".

## 2. Área segura (vale para tudo em 9:16, 1080x1920)
- Topo: 220 px livres (nome, áudio). Base: 450 px livres (legenda do post, música): nada importante abaixo de **Y 1470**.
- Coluna de botões na direita: nada importante depois de **X 945** da altura Y 1150 para baixo. Laterais 35 px.
- **Regra prática:** texto, rosto, número e botão entre **Y 285 e 1470** e **X 110 e 945**. Fundo pode ocupar tudo.
- Mesma posição em todas as cenas (nada pula). Não coube? diminui ou reorganiza.
- **Fica a nossa (Y 285 a 1470).** Outras referências, só anotadas: guia g03 Y 285 a 1635 e X 110 a 970; livro 09 (regra de anúncio de Reels da Meta) Y 269 a 1248, deixando 35% da base livre; anúncio da Meta pede 14% topo, 35% base, 6% lados. A nossa é a mais folgada embaixo. **DECISÃO DO VICTOR:** quer segurar rosto e legenda principal acima de Y 1248 (mais seguro no Reels) ou manter Y 1470? Até ele decidir, vale Y 1470.

## 3. Padrão mínimo de produção (nada abaixo disso vai ao Victor)
- **Cena, não slide:** cada vídeo tem um objeto ou personagem que conta a história (celular, conversa sendo digitada, porta, mapa, boneco). Texto solto em fundo liso só de apoio.
- **Algo muda a cada 1 a 3 s** em vídeo de texto (palavra entrando, digitação, zoom lento, tremor). Em animação com personagem, menos cortes e **câmera andando** funcionam melhor (ver seção 6).
- **Som em cada gesto:** tecla, toque, plim, passo, porta rangendo, corrente, batida no impacto, sopro na troca de legenda. Baixinho, mas presente.
- **Silêncio total logo antes de cada revelação.** Música não toca sem parar.
- **Grave só no impacto.** Grave ligado o tempo todo mata o susto.
- **Legenda grande** no alto da área segura, 60 a 70 px, até 3 linhas, uma palavra-chave colorida por frase; mínimo 34 px em qualquer texto.
- **Narrado sempre:** tudo que está escrito também é falado (voz em `escala-voz-narracao`).
- **Autoexplicativo:** quem vê sem som e sem conhecer a conta entende.
- Fecho discreto com a marca "QUASE ACONTECEU". Nada de logo no começo, nada de tela preta no fim.
- Saída: 1080x1920, 30 fps, H.264 (`-preset veryfast -crf 20`), AAC, áudio com loudnorm e pico perto de -1 dB.

## 4. Capa (todo vídeo sai com uma)
1080x1920, selo da parte, frase de 2 a 4 palavras enorme, o objeto ou personagem da cena e uma faixa com o tema; tudo entre Y 240 e 1680 (recorte do perfil). As capas da mesma série seguem o mesmo molde para o perfil virar uma grade organizada.

## 5. Conferência obrigatória antes da fila
1. Folha de quadros a cada 2 a 5 s (`ffmpeg -i v.mp4 -vf fps=1/3,scale=270:-1,tile=6x3 folha.jpg`) e **olhar com o Read**: legenda inteira, nada fora da área segura, nada sobreposto, personagem com rosto à mostra, português certo, sem tela preta.
2. Volume (`ffmpeg -af volumedetect`), duração certa, sincronia de voz, imagem e legenda.
3. Corte no meio de palavra? asterisco de marcação sobrando? texto gerado por IA dentro da imagem? Corrigir.
4. Checklist da `escala-regras`.

## 6. Copiar o estilo de um viral (sem copiar o vídeo)
Pedir "faz igual" faz a IA olhar meia dúzia de quadros e inventar o resto. Faça a **tabela**:
1. Victor manda o arquivo (ou o link; se a rede bloquear o download aqui, ele baixa e anexa).
2. `python3 ferramentas/estudar_referencia.py referencia.mp4 [nosso.mp4] --saida conteudo/estudos/<nome>`
3. A ferramenta devolve lado a lado: cortes e ritmo, plano mais longo, volume, silêncios, impactos de grave e a folha de 1 quadro por segundo. Olhe a folha e acrescente o que o número não mostra: tamanho do personagem na tela, se o protagonista aparece, tipo de legenda, cor, movimento de câmera.
4. Escreva em `conteudo/estudos/<nome>.md` as 5 a 8 diferenças que mais pesam e mude **essas** no próximo episódio.
5. Aprovado pelo Victor? Vira regra nesta skill (seção nova com o nome do estilo).
Lições já tiradas assim (série animada que passou de 1 milhão, out/2026): 9 cortes em 90 s com a câmera andando; silêncio antes de cada revelação; grave só no impacto; personagem ocupando quase a tela toda; o protagonista aparece (deitado, levantando, encolhido), não só a mão.

## 7. Variações (uma mudança por versão)
v1 é a base aprovada. Cada versão nova muda **uma** coisa e o nome diz qual. Ordem que mais rende: gancho (primeiro quadro e primeira frase) > duração > legenda > capa. Hipótese em uma linha, sem número inventado. Comparar só com mesmo horário e rede.

## 8. Imagem e vídeo gerados por IA
- **Texto nunca dentro da imagem gerada:** entra na edição.
- **Cara de IA:** trocar "bonito, cinematográfico, profissional" por decisões que se veem (luz de janela à esquerda, lente 35 mm, noite com poste amarelo, cozinha simples). Revisar pele de plástico, mãos, textos tortos, simetria perfeita.
- Prompt **afirmativo** (pedir o que a câmera vê; pedir "sem X" faz aparecer X), uma camada nova por tentativa, um movimento de câmera por plano. Detalhes em `escala-video-ia`.
- Toda peça com IA leva o rótulo de IA na publicação.

## 9. Trilha e efeitos
Só trilha sintetizada por nós (o motor gera), biblioteca livre com licença comercial, ou a biblioteca da própria rede na hora de postar. Nada de música famosa. Voz sempre acima de tudo; trilha cai na tensão.

## 10. Rotina para gastar menos
Um vídeo por vez. Amostra de 8 s aprovada antes do vídeo inteiro quando o estilo for novo. Corrigir por trecho ("de 0:42 a 0:48 troque a legenda"), nunca refazer tudo. Aprovado? perguntar se vale para os próximos do mesmo estilo; se sim, registrar aqui.
