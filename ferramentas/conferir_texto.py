#!/usr/bin/env python3
"""Gate de texto da ESCALA: aponta travessão e palavras de estoque de IA.

Uso:
  python3 ferramentas/conferir_texto.py arquivo1 [arquivo2 ...] [--ignorar termo ...]

Aceita texto (.txt, .md), legenda (.srt, .vtt) e JSON (confere só os VALORES
de texto, dizendo o caminho do campo). Sem dependências, sem internet, sem IA.
Só LÊ: nunca altera o arquivo.

Aponta:
  1. travessão (—);
  2. "–" (meia-risca) usado como travessão. Intervalo de números como 10–20 passa;
  3. " -- " (dois hifens usados como travessão);
  4. expressões de cara de IA em português (lista abaixo).

Saída: uma linha por achado (arquivo:linha ou caminho do JSON, tipo, trecho).
Código de saída: 0 se limpo, 1 se achou algo, 2 se um arquivo não abriu.

Origem da lista: livros 'pacotes-zip' (gate de texto do site-de-10k) e
'guia-100-skills' (item 88), notas em conteudo/estudos/livros/. Acréscimos nossos
estão marcados. Dispositivo de marca deliberado (ex.: um trio desenhado) não é
procurado aqui: quem julga isso é o revisor, olhando a intenção.
"""
import json
import re
import sys

# (rótulo, regex). Tudo em minúsculas; o texto é comparado com casefold.
EXPRESSOES = [
    # palavras de estoque de IA (pacotes-zip, seção 1.D)
    ("estoque", r"\balavanc\w+"),
    ("estoque", r"\brobust[oa]s?\b"),
    ("estoque", r"\bempoder\w+"),
    ("estoque", r"\bdestrav\w+"),
    ("estoque", r"\bacion[aá]ve(l|is)\b"),
    ("estoque", r"\borientad[oa]s? (a|por) dados\b"),
    ("estoque", r"\bsolu[cç][aã]o\b|\bsolu[cç][oõ]es\b"),
    ("estoque", r"\bsinergi\w+"),
    ("estoque", r"\bescal[aá]ve(l|is)\b"),
    # conectivos e muletas de texto de IA (pacotes-zip 1.D e guia-100-skills C.1)
    ("muleta", r"\balém disso\b"),
    ("muleta", r"\bvale ressaltar\b"),
    ("muleta", r"\bé importante (ressaltar|destacar|lembrar|notar)\b"),
    ("muleta", r"\bmergulh(ar|e|ar|amos|em)\b"),
    ("muleta", r"\bpanorama\b"),
    ("muleta", r"\btestamento\b"),
    ("muleta", r"\belevar (o|a|os|as) \w+"),
    ("muleta", r"\bo futuro é promissor\b"),
    ("muleta", r"\bvoc[eê] já se perguntou\b"),
    # atribuição vaga (pacotes-zip 1.D)
    ("atribuição vaga", r"\bmuitos especialistas (dizem|afirmam|acreditam)\b"),
    ("atribuição vaga", r"\bestudos (mostram|apontam|indicam)\b"),
    # "não é só X, é Y" (pacotes-zip 1.D)
    ("não é só X, é Y", r"\bnão é (só|apenas|somente) [^.!?\n]{1,50}, (é|mas)\b"),
    # acréscimos nossos (marcados): aberturas e fechos de manual
    ("muleta (nosso)", r"\bno mundo (de hoje|atual|digital)\b"),
    ("muleta (nosso)", r"\bnos dias de hoje\b"),
    ("muleta (nosso)", r"\bem resumo\b|\bem suma\b|\bem conclusão\b"),
    ("muleta (nosso)", r"\bnavegar (pel[oa]s?|por) \w+"),
    ("muleta (nosso)", r"\bsem dúvida alguma\b"),
]

EXPRESSOES_COMPILADAS = [(rot, re.compile(rx, re.IGNORECASE)) for rot, rx in EXPRESSOES]
TRAVESSAO = re.compile("—")
MEIA_RISCA = re.compile("–")
DOIS_HIFENS = re.compile(r"(?<=\s)--(?=\s)")
INTERVALO_NUMERO = re.compile(r"\d–\d")


def textos_do_json(obj, caminho="$"):
    """Gera (caminho, texto) para cada string do JSON, inclusive chaves."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from textos_do_json(v, f"{caminho}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from textos_do_json(v, f"{caminho}[{i}]")
    elif isinstance(obj, str):
        yield caminho, obj


def trecho(texto, ini, fim, folga=25):
    a = max(0, ini - folga)
    b = min(len(texto), fim + folga)
    s = texto[a:b].replace("\n", " ")
    return ("..." if a > 0 else "") + s + ("..." if b < len(texto) else "")


def conferir_linha(texto, onde, ignorar):
    achados = []
    for m in TRAVESSAO.finditer(texto):
        achados.append((onde, "travessão (—)", trecho(texto, m.start(), m.end())))
    for m in MEIA_RISCA.finditer(texto):
        # intervalo de números (10–20) é uso correto; o resto é travessão disfarçado
        if INTERVALO_NUMERO.search(texto[max(0, m.start() - 1):m.end() + 1]):
            continue
        achados.append((onde, "meia-risca usada como travessão (–)", trecho(texto, m.start(), m.end())))
    for m in DOIS_HIFENS.finditer(texto):
        achados.append((onde, "dois hifens como travessão (--)", trecho(texto, m.start(), m.end())))
    for rot, rx in EXPRESSOES_COMPILADAS:
        for m in rx.finditer(texto):
            if any(t.casefold() in m.group(0).casefold() for t in ignorar):
                continue
            achados.append((onde, f"cara de IA: {rot}", f'"{m.group(0)}" em: ' + trecho(texto, m.start(), m.end())))
    return achados


def conferir_arquivo(caminho, ignorar):
    with open(caminho, encoding="utf-8") as f:
        bruto = f.read()
    achados = []
    if caminho.lower().endswith(".json"):
        try:
            dados = json.loads(bruto)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON inválido: {e}")
        for cam, texto in textos_do_json(dados):
            achados += conferir_linha(texto, f"{caminho} {cam}", ignorar)
    else:
        for n, linha in enumerate(bruto.splitlines(), 1):
            achados += conferir_linha(linha, f"{caminho}:{n}", ignorar)
    return achados


def main(argv):
    ignorar = []
    arquivos = []
    i = 0
    while i < len(argv):
        if argv[i] == "--ignorar":
            i += 1
            while i < len(argv) and not argv[i].startswith("--"):
                ignorar.append(argv[i])
                i += 1
            continue
        arquivos.append(argv[i])
        i += 1
    if not arquivos:
        print(__doc__)
        return 2
    total = 0
    falhou = False
    for a in arquivos:
        try:
            achados = conferir_arquivo(a, ignorar)
        except (OSError, UnicodeDecodeError, ValueError) as e:
            print(f"ERRO: não consegui ler {a}: {e}")
            falhou = True
            continue
        for onde, tipo, texto in achados:
            print(f"{onde} | {tipo} | {texto}")
        total += len(achados)
    if falhou:
        return 2
    if total:
        print(f"\n{total} achado(s). Reescreva e rode de novo até dar zero.")
        return 1
    print("Limpo: nenhum travessão nem expressão de cara de IA.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
