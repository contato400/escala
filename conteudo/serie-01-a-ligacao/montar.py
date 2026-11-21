# Gera os JSON das 5 partes da série 1 para o motor (motor/gerar_serie.py).
import json, os
D = os.path.dirname(os.path.abspath(__file__))
R = "<span style='color:#ff3341'>"
def cta(n): return f"Segue para ver <span class=k>a parte {n}</span><small>sai amanhã</small>"
CENTRAL = {"nome": "Central de Segurança", "icone": "bank"}
POLICIA = {"nome": "Delegacia de Polícia", "icone": "police"}
NETO = {"nome": "Caio (neto)", "icone": "user"}

P = {}
P[1] = dict(selo="PARTE 1", trechos=[
 dict(fala="Nove da noite. O celular da Dona Neide tocou. Era o banco.", legenda="21h. O ^banco ligou.", telefone="on", chamada=CENTRAL),
 dict(fala="Boa noite, dona Neide. Aqui é o Rodrigo, da central de segurança do seu banco.", voz="tel", bolha="Boa noite, dona Neide. Aqui é o Rodrigo, da segurança do banco."),
 dict(fala="Tem uma compra de quatro mil, oitocentos e noventa reais no seu cartão, em Manaus. Foi a senhora?", voz="tel", bolha="Compra de R$ 4.890 em Manaus. Foi a senhora?", tensao=True),
 dict(fala="Ela nunca tinha ido pra Manaus.", legenda="Ela nunca foi pra *Manaus."),
 dict(fala="E o pior: ele sabia o nome completo dela, o CPF e o final do cartão.", legenda="Ele sabia o ^nome, o ^CPF e o ^final do cartão."),
 dict(fala="Fica tranquila, a gente vai bloquear agora. Só confirma a sua senha no teclado.", voz="tel", limpar_bolhas=True, bolha="Vamos bloquear. Só confirma a sua senha no teclado."),
 dict(fala="Ela digitou os quatro números, com o dedo tremendo.", legenda="Ela digitou a *senha.", dedo=True),
 dict(fala="Pausa aqui: banco nenhum pede a sua senha por telefone. Nunca.", regra="Banco NUNCA pede senha por telefone."),
 dict(fala="Perfeito. Agora presta atenção, que é muito importante.", voz="tel", limpar_bolhas=True, bolha="Perfeito. Agora presta atenção."),
 dict(fala="Pega uma tesoura e corta o cartão ao meio. Mas não estraga o chip.", voz="tel", bolha="Corta o cartão ao meio. Mas não estraga o chip.", tensao=True),
 dict(fala="Por que ele queria o chip inteiro?", legenda="Por que ele queria o ^chip inteiro?"),
 dict(fala="Um funcionário nosso já está indo buscar o cartão na sua casa.", voz="tel", bolha="Um funcionário já está indo buscar na sua casa.", tensao=True),
 dict(fala="Ela olhou pro relógio. Nove e quinze da noite, e ela estava sozinha em casa.", legenda="E ela estava *sozinha em casa."),
 dict(fala="A Dona Neide abriu a gaveta da cozinha, e pegou a tesoura.", legenda="Ela pegou a *tesoura.", escurecer=True),
 dict(fala="E você? Entregaria esse cartão?", final=dict(selo="FIM DA PARTE 1", pergunta="E você? Entregaria o cartão?", chamada=cta(2))),
 dict(fala="Segue pra ver a parte dois amanhã.", mostrar_chamada=True)],
 capa=dict(selo="PARTE 1", titulo=f"O BANCO<br>{R}LIGOU</span>", faixa="Ele sabia até o CPF dela", quadro=6.0))

P[2] = dict(selo="PARTE 2", trechos=[
 dict(fala="Ontem, um falso funcionário do banco mandou a Dona Neide cortar o cartão ao meio.", legenda="Ontem: o falso banco pediu o *cartão.", telefone="on", chamada=CENTRAL),
 dict(fala="Ela cortou. O chip ficou inteiro.", legenda="Ela cortou. O ^chip ficou inteiro."),
 dict(fala="Muito bem, dona Neide. Agora não desliga, tá? A linha fica protegida.", voz="tel", bolha="Muito bem. Não desliga, tá? A linha fica protegida."),
 dict(fala="Linha protegida não existe. Ele só queria que ela não falasse com mais ninguém.", legenda="Ele não queria que ela falasse com *ninguém."),
 dict(fala="Ela pensou no neto, o Caio. Ele sempre sabia o que fazer.", legenda="Ela pensou no neto, o ^Caio."),
 dict(fala="E bem nessa hora chegou uma mensagem dele: vó, tá acordada?", limpar_bolhas=True, bolha="Vó, tá acordada?", rotulo="MENSAGEM DO CAIO:"),
 dict(fala="Dona Neide, por segurança a senhora não pode avisar ninguém. Nem a família.", voz="tel", bolha="Por segurança, a senhora não pode avisar ninguém. Nem a família.", tensao=True),
 dict(fala="Guarda isso: quem pede segredo é golpista. Banco de verdade nunca pede.", regra="Pediu segredo? É golpe."),
 dict(fala="Ela deixou a mensagem do neto sem resposta.", legenda="Ela deixou o neto *sem resposta."),
 dict(fala="O motoboy já está chegando. Coloca o cartão num envelope fechado.", voz="tel", limpar_bolhas=True, bolha="O motoboy está chegando. Coloca o cartão num envelope."),
 dict(fala="Cartão cortado, senha entregue, envelope fechado. Tudo pronto.", legenda="Cartão, senha e *envelope prontos."),
 dict(fala="Aí alguém bateu na porta.", legenda="Alguém bateu na *porta.", telefone="off", porta="on", batida=True),
 dict(fala="Boa noite! Vim buscar o cartão do banco.", voz="porta", voz_porta="Boa noite! Vim buscar o cartão do banco."),
 dict(fala="Ela olhou o envelope na mão. Ali dentro estava tudo.", legenda="Ali dentro estava ^tudo."),
 dict(fala="Ela pegou o envelope e foi abrir.", legenda="Ela pegou o envelope e foi ^abrir.", tensao=True),
 dict(fala="E agora? Ela devia abrir essa porta?", final=dict(selo="FIM DA PARTE 2", pergunta="Ela devia abrir a porta?", chamada=cta(3))),
 dict(fala="Segue pra ver a parte três amanhã.", mostrar_chamada=True)],
 capa=dict(selo="PARTE 2", titulo=f"NÃO CONTA<br>{R}PRA NINGUÉM</span>", faixa="E bateram na porta", quadro=4.0))

P[3] = dict(selo="PARTE 3", trechos=[
 dict(fala="Ontem, um motoboy bateu na porta da Dona Neide pra buscar o cartão que ela tinha cortado.", legenda="Ontem: o *motoboy chegou.", porta="on", batida=True),
 dict(fala="Ela olhou pelo olho mágico. Capacete preto, mochila de entrega, celular na mão.", legenda="Capacete, mochila e ^celular na mão."),
 dict(fala="Pode abrir, senhora. É rapidinho, só assinar.", voz="porta", voz_porta="Pode abrir, senhora. É rapidinho, só assinar."),
 dict(fala="A mão dela já estava na maçaneta.", legenda="A mão já estava na *maçaneta.", tensao=True),
 dict(fala="Foi aí que ela lembrou do almoço de domingo, quando o Caio falou uma coisa.", legenda="Ela lembrou do ^Caio."),
 dict(fala="Vó, banco nenhum manda ninguém buscar cartão na casa da gente.", voz="neto", regra="Banco NUNCA manda buscar cartão.", regra_titulo="O CAIO TINHA FALADO"),
 dict(fala="Ela tirou a mão da porta.", legenda="Ela tirou a +mão da porta."),
 dict(fala="E falou alto: o senhor espera aí, que eu vou ligar pro meu banco.", legenda="\"Espera aí. Vou ligar pro ^meu banco.\""),
 dict(fala="Do outro lado, silêncio. Depois, passos descendo a escada, bem rápido.", legenda="Silêncio. Depois, *passos.", porta="off"),
 dict(fala="Ele fugiu. E funcionário de banco de verdade não foge.", legenda="Banco de verdade não *foge."),
 dict(fala="Mas o celular não parou de tocar.", legenda="Mas o celular ^tocou.", telefone="on", chamada=CENTRAL),
 dict(fala="Dona Neide, por que a senhora não entregou? Agora a sua conta está em risco.", voz="tel", bolha="Por que a senhora não entregou? Sua conta está em risco.", tensao=True),
 dict(fala="Se a gente não resolver em dez minutos, a senhora perde tudo.", voz="tel", bolha="Em 10 minutos a senhora perde tudo.", tensao=True),
 dict(fala="Pressa e medo. São as duas armas de todo golpista.", legenda="^Pressa e ^medo: as armas do golpe."),
 dict(fala="Então vamos fazer de outro jeito. A senhora vai passar o seu saldo pra uma conta segura.", voz="tel", limpar_bolhas=True, bolha="Vamos fazer de outro jeito. Passa o saldo pra uma conta segura."),
 dict(fala="Conta segura.", legenda="Conta *segura.", escurecer=True),
 dict(fala="Você sabe o que é a tal conta segura? Comenta aí.", final=dict(selo="FIM DA PARTE 3", pergunta="Você sabe o que é a tal conta segura?", chamada=cta(4))),
 dict(fala="Segue pra ver a parte quatro amanhã.", mostrar_chamada=True)],
 capa=dict(selo="PARTE 3", titulo=f"O OLHO<br>{R}MÁGICO</span>", faixa="A mão já estava na maçaneta", quadro=6.0))

P[4] = dict(selo="PARTE 4", pix_tela=dict(para="Para: R. SILVA SERVIÇOS<br><span style='font-size:32px;color:#666'>\"conta segura\"</span>", valor="R$ 12.300,00"), trechos=[
 dict(fala="Ontem, o falso banco mandou a Dona Neide passar todo o dinheiro pra uma conta segura.", legenda="Ontem: \"passa tudo pra conta ^segura\".", telefone="on", chamada=CENTRAL),
 dict(fala="É uma conta no seu nome, senhora. Só pra proteger o dinheiro até amanhã.", voz="tel", bolha="É uma conta no seu nome. Só até amanhã."),
 dict(fala="Ela abriu o aplicativo e foi no Pix. Doze mil e trezentos reais. A economia de uma vida.", legenda="R$ 12.300. A economia de uma *vida.", pix="on"),
 dict(fala="Mas o nome na tela não era o dela.", legenda="Mas o nome não era o ^dela."),
 dict(fala="Era de um tal de R. Silva Serviços. Um desconhecido.", legenda="Era de um *desconhecido."),
 dict(fala="Pode confirmar, dona Neide. Rápido, antes que bloqueiem tudo.", voz="tel", legenda="\"Confirma. *Rápido.\"", dedo=True, tensao=True),
 dict(fala="O dedo dela foi pro botão verde.", legenda="O dedo foi pro *botão.", tensao=True),
 dict(fala="E aí o celular vibrou. Outra ligação. Era o Caio.", legenda="Outra ligação: ^Caio.", pix="off", chamada=NETO),
 dict(fala="Vó, a senhora não respondeu a minha mensagem. Tá tudo bem?", voz="neto", bolha="Vó, a senhora não respondeu. Tá tudo bem?", rotulo="CAIO DISSE:"),
 dict(fala="Ela contou tudo, chorando.", legenda="Ela contou ^tudo."),
 dict(fala="Vó, desliga agora e não faz nada! Isso é golpe!", voz="neto", bolha="Desliga agora e não faz nada! É golpe!", rotulo="CAIO DISSE:", tensao=True),
 dict(fala="Guarda isso: conta segura não existe. Nenhum banco pede pra você mudar o seu dinheiro de lugar.", regra="Conta segura NÃO existe."),
 dict(fala="Ela desligou tudo. O dinheiro ficou onde estava.", legenda="Ela desligou. Dinheiro +salvo.", encerrar=True),
 dict(fala="Só que, dois minutos depois, o celular tocou de novo.", legenda="2 minutos depois...", chamada=POLICIA),
 dict(fala="Dona Neide, aqui é o delegado Moura. Sabemos do golpe. Precisamos da sua ajuda pra prender essa quadrilha.", voz="tel", bolha="Aqui é o delegado Moura. Precisamos da sua ajuda pra prender a quadrilha.", tensao=True),
 dict(fala="E a ajuda era um Pix.", legenda="E a ajuda era um *Pix.", escurecer=True),
 dict(fala="Polícia pede Pix? Responde aí.", final=dict(selo="FIM DA PARTE 4", pergunta="Polícia pede Pix?", chamada="Segue para ver <span class=k>o final</span><small>sai amanhã</small>")),
 dict(fala="Segue pra ver o final amanhã.", mostrar_chamada=True)],
 capa=dict(selo="PARTE 4", titulo=f"A CONTA<br>{R}SEGURA</span>", faixa="R$ 12.300 a um clique", quadro=12.0))

P[5] = dict(selo="FINAL", pix_tela=dict(para="Para: OPERAÇÃO SIGILOSA<br><span style='font-size:32px;color:#666'>\"da polícia\"</span>", valor="R$ 5.000,00"), trechos=[
 dict(fala="Ontem, um falso delegado ligou pra Dona Neide pedindo um Pix pra pegar os golpistas.", legenda="Ontem: o falso ^delegado ligou.", telefone="on", chamada=POLICIA),
 dict(fala="É uma operação sigilosa. Faça um Pix de cinco mil reais pra gente rastrear a quadrilha.", voz="tel", bolha="Operação sigilosa. Faça um Pix de R$ 5 mil pra rastrear a quadrilha."),
 dict(fala="Ela abriu o Pix. Cinco mil reais.", legenda="Ela abriu o *Pix.", pix="on"),
 dict(fala="Mas dessa vez ela já sabia.", legenda="Mas dessa vez ela já ^sabia."),
 dict(fala="Polícia não pede Pix. Nunca.", pix="cancelar", regra="Polícia NUNCA pede Pix."),
 dict(fala="E ela respondeu: vou desligar e ir na delegacia, com o meu neto.", legenda="\"Vou na delegacia com meu ^neto.\"", encerrar=True),
 dict(fala="Meia hora depois, bateram na porta.", legenda="Bateram na *porta.", telefone="off", pix="off", porta="on", batida=True),
 dict(fala="Vó, sou eu! O Caio!", voz="porta", voz_porta="Vó, sou eu! O Caio!"),
 dict(fala="Ela não abriu na hora. Primeiro ligou pro celular dele, e ouviu tocar do lado de fora.", legenda="Primeiro ela ^ligou pra conferir."),
 dict(fala="Era ele. Ela abriu a porta e chorou no abraço do neto.", legenda="Era ele. +Abraço.", porta="off"),
 dict(fala="No dia seguinte, os dois foram ao banco. Cartão novo, senha nova e boletim de ocorrência feito.", legenda="Cartão novo, senha nova e +boletim."),
 dict(fala="E o Caio deixou o limite do Pix bem baixo no período da noite, no celular dela.", legenda="Limite do Pix +baixo à noite."),
 dict(fala="Grava essas regras.", legenda="Grava essas ^regras:", lista="on", limpar_legenda=False),
 dict(fala="Banco não pede senha.", item="Banco não pede senha."),
 dict(fala="Banco não busca cartão.", item="Banco não busca cartão."),
 dict(fala="Conta segura não existe.", item="Conta segura não existe."),
 dict(fala="Polícia não pede Pix.", item="Polícia não pede Pix."),
 dict(fala="E na dúvida, desliga e liga você, no número que está no verso do cartão.", item="Na dúvida, desligue e ligue você."),
 dict(fala="Quase aconteceu. Manda esse vídeo pra alguém que precisa ver.", final=dict(selo="FIM DA SÉRIE", pergunta="Quase aconteceu. Manda pra quem precisa ver.", chamada="Segue para a <span class=k>próxima história</span><small>começa amanhã</small>")),
 dict(fala="Segue pra não perder a próxima história.", mostrar_chamada=True)],
 capa=dict(selo="FINAL", titulo=f"QUASE<br>{R}ACONTECEU</span>", faixa="As 5 regras que salvaram a Dona Neide", quadro=8.0))

for n, d in P.items():
    d = {"nome": f"s01p{n}", **d}
    json.dump(d, open(os.path.join(D, f"parte-{n}.json"), "w"), ensure_ascii=False, indent=1)
print("ok")
