# Modelos de pedido (copiar e preencher)

Origem: livros 01 (ficha P.R.O.M.P.T.), 03 e 14 (critério de aceite, correção), 06 e 15 (especificação). Adaptado (nosso).

## 1. Pedido de roteiro de uma parte de série
```
Tarefa: escrever a parte [N] da série [NOME].
Quem assiste: [público e rede]. Função: roteirista de vídeo vertical de 60 a 90 s.
Objetivo: 70% ou mais não arrastam em 2 s; 65% ou mais até o fim; [seguir para ver a parte N+1].
Fatos (um por linha): <biblia> ... </biblia>; o que aconteceu na parte anterior; regras fixas do CLAUDE.md.
Esqueleto do viral de referência (só estrutura, nunca fala nem imagem): <esqueleto> ... </esqueleto>
Exemplo do jeito (2 a 3 linhas NOSSAS já aprovadas): ...
Formato: JSON do motor, 16 a 19 trechos, gancho de até 6 palavras na tela, legenda de 1 linha + "Parte N" + 3 a 5 hashtags. Terminar com "Trechos: N".
Evitar: Wesley, Krav Magá, Victor, "oi gente", trecho protegido, promessa de dinheiro, vítima real, travessão.
Está pronto quando: (1) 16 a 19 trechos; (2) gancho de até 6 palavras; (3) etiqueta de IA na legenda; (4) nenhum fato fora da bíblia; (5) sem [CONFIRMAR] sobrando.
Use só os fatos acima. Onde faltar, escreva [CONFIRMAR: o que falta]. Mostre o plano antes de escrever e espere.
Quando eu pedir ajuste: mantenha o aprovado, mude só o apontado, mostre só o trecho alterado e a lista "o que mudou".
```

## 2. Melhorar o pedido antes de produzir
```
Antes de produzir, leia o pedido abaixo. Faça até 5 perguntas do que falta, cada uma com "Sugestão:" tirada do que já está decidido. Depois reescreva o pedido com mais detalhe, com limites que se medem e 4 ou mais itens de aceite sim/não. Não produza nada. Onde não houver resposta, escreva [CONFIRMAR].
```

## 3. Correção em três partes
```
Sintoma: na [tela, cena ou trecho X], quando [Y], aconteceu [Z]. [erro colado inteiro]
Esperado: [o que deveria aparecer, com exemplo]. Antes funcionava até [versão ou commit].
Restrição: mude só [X]. Não mude [Y]. Se precisar mexer em mais coisas, pergunte antes.
Antes de mudar, diga a causa provável em uma frase. Ao terminar, diga o que mudou e como eu confiro.
```

## 4. Depois de duas correções sem melhora
```
Voltei para a versão anterior. Duas tentativas não resolveram: [sintoma]. As duas [o que mudaram]. Não repita esse caminho. Proponha outro em até cinco linhas e diga como vou testá-lo.
```

## 5. Investigar sem mudar nada
```
Não altere nada. Diga se o problema está no roteiro, na voz, no motor ou na publicação; liste o sinal que confirma ou descarta cada um; proponha duas formas de corrigir com o risco de cada uma e os testes que confirmam. Confira se a causa explica TODOS os casos que anotei.
```

## 6. Conferência por tabela, em tarefa nova e sem alterar nada
Tabela: item | situação (feito, em parte, não feito) | onde eu confiro (tempo do vídeo ou arquivo) | o que falta. A lista que o produtor escreve é a versão dele; a conferência é a prova. "Pronto" só com prova (quadros e transcrição), nunca "deve funcionar".

## 7. Contestar o plano
```
Para cada item do critério de aceite, cite o trecho do plano que o cumpre ou escreva "faltou". Liste o que você decidiu sozinho sem eu pedir. Calcule pelo plano, valor por valor, este caso: [caso]. Atualize o plano e espere a minha aprovação.
```

## 8. Instrução fixa para IA que gera texto (bot e Workers AI)
Só o que está escrito; se não trata do assunto, "não encontrado"; nunca deduza; responda só neste formato; fora do formato, tentar de novo uma vez e depois registrar "erro de formato". A saída é rascunho: só o Victor aprova.

## 9. Resumo de passagem para sessão nova (até 250 palavras)
1 Objetivo. 2 Decidido (nomes e números exatos). 3 Cortado (o que saiu e por quê, para não voltar). 4 Regras (tom, limites, palavras proibidas). 5 Próximo passo. `[CONFERIR]` onde não houver certeza. Ler linha a linha antes de seguir.
