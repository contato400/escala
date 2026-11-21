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
- Topo: 220 px livres (nome, áudio). Base: **672 px livres** (legenda do post, música, botões): nada importante abaixo de **Y 1248** (decidido pelo Victor em 21/11, regra do livro 09).
- Coluna de botões na direita: nada importante depois de **X 945** da altura Y 1150 para baixo. Laterais 35 px.
- **Regra prática:** texto, rosto, número e botão entre **Y 285 e 1248** e **X 110 e 945**. Fundo e objetos de cena (celular, porta) podem descer, mas o que precisa ser lido fica acima de 1248. No motor do celular: no máximo 2 bolhas visíveis (usar `limpar_bolhas`).
- Mesma posição em todas as cenas (nada pula). Não coube? diminui ou reorganiza.
- **Decidido (Victor, 21/11): Y 285 a 1248**, a regra do livro 09 (35% da base livre). Referências antigas só para histórico: nossa anterior Y 1470; guia g03 Y 1635.

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
5. **Confira o MP4 exportado, não a prévia** (livro 10): a prévia aprova a edição, o arquivo confirma a entrega. Abra o arquivo, veja início, trecho com inserção, final e áudio, no tamanho de celular. **Quadro parado mostra posição, não prova sincronia** de voz nem de legenda: ouça com som. Liste os cortes feitos (o que saiu e por quê) e relate só o intervalo realmente verificado.
6. Quem confere é outra chamada, a `escala-revisor` (só lê, devolve a falha a quem errou, no máximo 2 voltas). Passe de olhos frescos por último: veja como espectador de primeira vez, sem checklist; algo ficou desigual (personagem sem sombra, cena sem som)? Parece de propósito ou enchimento?

### Comandos ffmpeg úteis (pacotes-zip, receitas)
- **Quadro para encadear clipe, em PNG** (nunca jpg, que assa compressão no clipe seguinte): `ffmpeg -sseof -0.1 -i seg.mp4 -update 1 -frames:v 1 -q:v 1 final.png`
- **Clipe termina parado?** `ffmpeg -i raw.mp4 -vf "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null -` (brilho de diferença baixo no fim = descansou; alto = ainda deriva).
- **Corte de cauda** (bom até o personagem mexer de novo perto do fim): `ffmpeg -i raw.mp4 -t 4.3 -c copy cortado.mp4`, e se não fechar limpo, recodifique. Mais barato que regerar.
- **Crossfade de resgate numa junção que aparece:** `xfade=transition=fade:duration=0.25:offset=<duração do 1º - 0.25>` (dois clipes de 6 s: offset 5.75). Corte seco é o teste mais honesto; fusão só esconde furo (livro 09).
- **Concatenar** em um só filtro `concat` e codificar uma vez; clipes já codificados com parâmetros diferentes travam na junção.
- **Contraste da legenda contra o pior quadro, não o médio** (texto sobre fundo em movimento): meta 4,5:1 em texto corrido e 3,5:1 em rótulo. Ajuda: sombra em 3 camadas, faixa escura só enquanto a legenda está ligada, chip com fundo semitransparente. Tire os quadros do trecho com `fps=2` e meça a luminância sob a legenda (script ainda por fazer: `ferramentas/contraste_legenda.py`, ideia nossa, não testada).
- Brutos e revisões em `projeto/brutos/`, nunca na pasta que o Victor ou o Metricool posta. Abra o resultado de cada encode antes de usar.

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
Um vídeo por vez. Amostra aprovada antes do vídeo inteiro quando o estilo for novo: **8 s** para estilo simples, **10 a 15 s** quando tem movimento (câmera andando, moldura, cartões, 3D), porque 8 s não mostram a transição. A amostra tem fala, legenda, enquadramento e pelo menos uma inserção; abertura sozinha não valida o estilo. Em lote, aprove a 1ª peça antes das outras (máximo 3). Corrigir por trecho ("de 0:42 a 0:48 troque a legenda"), nunca refazer tudo. Aprovado? perguntar se vale para os próximos do mesmo estilo; se sim, registrar aqui.
