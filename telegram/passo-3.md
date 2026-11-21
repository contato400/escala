# Passo 3: bot que conversa + chave da fábrica (clique por clique)

Tempo: uns 15 minutos, no computador (o painel do Cloudflare pelo celular é ruim).
Atalho: cole este arquivo no chat do Cowork e peça "faz comigo o passo 3". Ele faz os cliques; você só digita a senha.

## A. Entrar no Worker
1. Abra **dash.cloudflare.com** e entre com a conta da ESCALA (e-mail Victor Augusto).
2. No menu da esquerda, clique em **Compute (Workers)**. Se não aparecer, procure **Workers e Pages**.
3. Na lista, clique em **chefe**.
Você está na página do Worker. No topo tem as abas: Visão geral, Métricas, Implantações, **Configurações** (Settings)...

## B. Colar o código novo (o bot passa a conversar)
1. No canto de cima, à direita, clique no botão **Editar código** (ícone `</>`, às vezes escrito "Edit code").
2. Abre um editor. Clique dentro do código, aperte **Ctrl+A** (seleciona tudo) e **Delete**.
3. Abra o arquivo `worker.js` que eu mandei, selecione tudo (Ctrl+A), copie (Ctrl+C) e cole no editor (Ctrl+V).
4. Clique no botão azul **Implantar** (Deploy), em cima à direita. Confirme se perguntar.
5. Volte para a página do Worker (seta "voltar" ou clique em "chefe" no topo).

## C. Ligar a IA grátis
1. Aba **Configurações** (Settings).
2. Procure a seção **Vinculações** (Bindings). Clique em **Adicionar** (Add).
3. Escolha **Workers AI**.
4. Em "Nome da variável" escreva exatamente: `AI` (duas letras maiúsculas).
5. Clique em **Adicionar vinculação** (Add binding) / **Implantar**.
Na lista de vinculações tem que aparecer `FILA` (KV) e `AI` (Workers AI).

## D. Trocar a chave da fábrica
**1. Criar a senha nova** (32 letras e números, sem símbolo). Jeito mais fácil:
- No celular Android ou no Chrome: abra **passwords.google.com** > Adicionar > "Gerar senha forte". Se vier com símbolo, apague os símbolos até ficar só letras e números.
- Ou no iPhone: Ajustes > Senhas > + > na senha, toque em "Senha forte".
- Ou digite você mesmo 32 letras e números misturados, sem padrão (ex.: tipo "k8Qm2..." mas inventado na hora).
Guarde essa senha num lugar seguro (o próprio gerenciador). **Não mande no chat.**

**2. Colocar no Cloudflare:**
1. Worker `chefe` > aba **Configurações** > seção **Variáveis e segredos** (Variables and Secrets).
2. Na linha **FABRICA_KEY**, clique no lápis ou nos 3 pontinhos > **Editar** (Edit).
3. O campo do valor vem vazio (é segredo, não mostra o antigo). Cole a senha nova.
4. Confira que o tipo continua **Secret** (Segredo). Clique em **Salvar** / **Implantar** (Deploy). Se aparecer "Salvar e implantar", é esse.

**3. Me avisar:** escreva aqui "chave trocada". Eu abro o formulário seguro e você cola **a mesma senha** lá. O formulário guarda na rede da nuvem; eu nunca vejo o valor.

## E. Testar no Telegram
Mande para o bot:
- "oi, o que você faz?" → ele tem que responder com frase própria (não só "Anotado").
- "quero um vídeo de GTA 6 sobre as notas dos jogadores" → ele confirma e diz que passa para a fábrica.
Se ele só responder "Anotado na fila da fábrica", a vinculação `AI` (item C) não pegou: confira o nome `AI`.
