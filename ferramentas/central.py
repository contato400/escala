#!/usr/bin/env python3
"""Fala com o chefe no Cloudflare (telegram/worker.js) a partir da fábrica.

Uso:
  python3 ferramentas/central.py previa <id> "<título>" <legenda.txt> [video.mp4]
  python3 ferramentas/central.py pedidos            # imprime JSON com pedidos e itens
  python3 ferramentas/central.py lido <chave_pedido>... [--itens id1,id2]
  python3 ferramentas/central.py estado [--temas arq.txt] [--status arq.txt] [--aviso "texto"]

Endereço: variável ESCALA_CENTRAL (ex.: https://chefe.quaseaconteceu.workers.dev).
Chave: a rede da nuvem injeta o cabeçalho X-Fabrica-Key (segredo de rede do ambiente "escala").
Fora da nuvem, use a variável FABRICA_KEY. A chave nunca fica em arquivo.
Texto do usuário vai sempre por --form-string / JSON (nunca interpretado pelo curl).
"""
import json, os, subprocess, sys

BASE = os.environ.get('ESCALA_CENTRAL', '').rstrip('/')
CHAVE = os.environ.get('FABRICA_KEY', 'injetada-pela-rede')

def curl(args):
    if not BASE:
        sys.exit('Defina ESCALA_CENTRAL com o endereço do Worker.')
    r = subprocess.run(['curl', '-sS', '--max-time', '300', '-H', f'X-Fabrica-Key: {CHAVE}', '-w', '\n%{http_code}', *args],
                       capture_output=True, text=True)
    corpo, _, codigo = r.stdout.rpartition('\n')
    if r.returncode != 0 or not codigo.startswith('2'):
        sys.exit(f'Falhou ({codigo or r.returncode}): {corpo or r.stderr}'.strip())
    return corpo

def post_json(caminho, dados):
    return curl(['-X', 'POST', '-H', 'content-type: application/json', '--data-binary', json.dumps(dados, ensure_ascii=False), BASE + caminho])

def main(a):
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd == 'previa' and len(a) in (4, 5):
        _, ident, titulo, legenda_arq, *video = a
        legenda = open(legenda_arq, encoding='utf-8').read()
        args = ['-X', 'POST', '--form-string', f'id={ident}', '--form-string', f'titulo={titulo}', '--form-string', f'legenda={legenda}']
        if video:
            if os.path.getsize(video[0]) > 49 * 1024 * 1024:
                sys.exit('Vídeo acima de 49 MB: o Telegram não aceita. Comprima (crf 23) antes.')
            args += ['-F', f'video=@{video[0]};type=video/mp4']
        print(curl(args + [BASE + '/fabrica/previa']))
    elif cmd == 'pedidos':
        print(curl([BASE + '/fabrica/pedidos']))
    elif cmd == 'lido':
        itens = []
        chaves = [x for x in a[1:] if not x.startswith('--itens')]
        for x in a[1:]:
            if x.startswith('--itens'):
                itens = x.split('=', 1)[1].split(',') if '=' in x else []
        print(post_json('/fabrica/lido', {'pedidos': chaves, 'itens': itens}))
    elif cmd == 'estado':
        dados, i = {}, 1
        while i < len(a):
            if a[i] in ('--temas', '--status'):
                dados[a[i][2:]] = open(a[i + 1], encoding='utf-8').read(); i += 2
            elif a[i] == '--aviso':
                dados['aviso'] = a[i + 1]; i += 2
            else:
                sys.exit(f'Opção desconhecida: {a[i]}')
        print(post_json('/fabrica/estado', dados))
    else:
        sys.exit(__doc__)

if __name__ == '__main__':
    main(sys.argv[1:])
