---
name: escala-produto-greenn
description: Aciona quando for criar, precificar ou vender produto próprio da ESCALA (e-book, guia, checklist, minicurso feito com IA) na Greenn, ou montar link de venda na bio e oferta para a audiência das contas. NÃO aciona antes de um tema provar audiência (fase 1 é crescer).
---
# Produto próprio (fase 2)

## Quando começar
Só quando um tema tiver provado audiência (série com 100 mil views ou mais, ou 1.000 seguidores somados) e os comentários mostrarem uma dor ou pergunta repetida.

## O que criar
Produto barato, rápido de consumir, ligado ao tema que viralizou: e-book ou guia de R$ 9,90 a R$ 27 (ex.: "Os golpes mais comuns de 2026 e como fugir de cada um"), checklist, minicurso curto. Conteúdo verdadeiro e útil, conferido em fontes; feito com IA mas revisado. Nunca prometer resultado garantido nem dinheiro fácil.

## Na Greenn (com aprovação do Victor)
Produto, oferta, página simples (o que é, para quem é, o que tem dentro, preço, garantia de 7 dias) e checkout. Nome do produtor = marca da ESCALA, não Wesley nem Victor. Toda criação ou mudança na Greenn passa pela fila de aprovação.

## Venda nas contas
Link na bio; menção natural no fim de parte de série ("o guia completo está no link do perfil"); aviso de publicidade quando for indicação de produto de terceiro. Medir vendas por origem com UTM (utm_source=escala, utm_medium=tiktok/instagram/youtube, utm_content=serie-parte).

## Lições dos livros (nosso, curtas)
Origem: livros 11, 14, 15, 16, 03 e 06, notas em conteudo/estudos/livros/. Só vale depois do tema provar audiência.
- **Sem rosto vende menos** (livro 11): produto próprio é a terceira fonte. Não esperar venda alta. Montar com o que o canal já tem (roteiros, fichas, imagens), conferindo a licença das imagens e da voz. O afiliado paga primeiro (`escala-hype-e-afiliado`).
- **Seguidor não é lead** (livro 07): entretenimento cresce rápido e raramente compra; assunto de aprender cresce devagar e paga melhor. Contar leads (pediu o link, comentou a palavra), não só seguidor.
- **Acervo gerado uma vez** (livro 15): pacote de 100 a 300 itens (desenho, cartaz, ficha, checklist) criado em lote com um estilo fixo, curado e entregue em PDF ou ZIP. Começar com 24 para testar. O valor é a curadoria, nunca a exclusividade das imagens. Versão limpa e gabarito como bônus. Nada gerado por IA a cada clique do cliente.
- **Ficha do produto antes de fazer** (livros 14 e 03): finalidade, quem usa, entregáveis, regras que se conferem, fora desta etapa e pelo menos 4 itens sim/não de aceite. Ver `escala-pedir-a-ia`.
- **Antes de ligar tráfego:** abrir o link de checkout fora do Wi-Fi e sem login, testar de ponta a ponta. Página sem depoimento, número de vendas, selo ou preço riscado que não existam. Exemplo marcado "ilustrativo". Termos, privacidade e reembolso como "rascunho para revisão jurídica", sem nome nem marca do Wesley ou do Victor, avisando que o texto de apoio pode ter sido feito com IA.
- **Lista de espera:** formulário que só grava; só nome e e-mail; frase "usamos seu e-mail só para avisar do lançamento e apagamos depois de [prazo]"; apagar depois; nenhum dado de menor. Link de entrega com código longo e aleatório, nunca número em sequência.
- **Conta antes de produzir** (`escala-custos`): ponto de equilíbrio = custo ÷ margem por venda, em vendas por mês, com cenário fraco de metade das vendas.

## Assinatura (fase 2, para depois)
Origem: livro 14. **DECISÃO DO VICTOR:** se e quando vender algo recorrente (clube, pacote mensal de ideias ou checklists). Só com produto único já vendido. Se aprovar:
1. Grátis = o conteúdo e uma isca simples sem custo recorrente para nós. Pago = o que dá trabalho recorrente ou valor repetido. O limite do plano vale no servidor, não só escondendo botão.
2. O acesso muda só por evento de venda confirmado. Conferir na Greenn se há assinatura recorrente e como chega o aviso (webhook assinado ou consulta). Se não for assinado, validar cada aviso com `get_sale` antes de liberar.
3. Renovação recusada: manter o acesso e avisar para atualizar o cartão, sem cortar na hora. Cancelamento vale até o fim do período pago, depois volta ao grátis sem apagar o que o cliente já recebeu. Desistência em 7 dias devolve o valor (CDC art. 49).
4. Testar com cliente de mentira: compra, recusa, renovação, renovação recusada, cancelamento. Nota fiscal combinada com o contador.
5. Cópia dos dados fora do código, cifrada se tiver dado pessoal. Nunca segredo em arquivo.

