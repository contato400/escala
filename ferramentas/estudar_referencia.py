#!/usr/bin/env python3
"""Estuda um vídeo de referência e devolve a TABELA do estilo (não o conteúdo).

Uso:
  python3 ferramentas/estudar_referencia.py referencia.mp4 [nosso.mp4] [--saida pasta]

Mede: duração, cortes (troca de cena) e ritmo, volume médio e pico, onde ficam
os silêncios, quando o grave aparece (impacto) e tira 1 quadro por segundo numa
folha de contato para olhar com o Read. Se passar o nosso vídeo também, monta a
tabela lado a lado. Serve para copiar o RITMO e a TÉCNICA, nunca o conteúdo.
"""
import json, re, subprocess, sys, os, argparse

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def duracao(v):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", v])
    return float(json.loads(r.stdout)["format"]["duration"])

def cortes(v, limiar=0.30):
    r = run(["ffmpeg", "-i", v, "-filter:v", f"select='gt(scene,{limiar})',showinfo", "-f", "null", "-"])
    return [float(x) for x in re.findall(r"pts_time:([\d.]+)", r.stderr)]

def volume(v):
    r = run(["ffmpeg", "-i", v, "-af", "volumedetect", "-vn", "-f", "null", "-"])
    m = re.search(r"mean_volume: ([-\d.]+)", r.stderr); p = re.search(r"max_volume: ([-\d.]+)", r.stderr)
    return (float(m.group(1)) if m else None, float(p.group(1)) if p else None)

def silencios(v, db=-35, minimo=0.35):
    r = run(["ffmpeg", "-i", v, "-af", f"silencedetect=noise={db}dB:d={minimo}", "-vn", "-f", "null", "-"])
    ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    return list(zip(ini, fim))

def graves(v, dur):
    """Segundos em que o grave (abaixo de 120 Hz) sobe forte: costuma ser o impacto."""
    r = run(["ffmpeg", "-i", v, "-af", "lowpass=f=120,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level",
             "-vn", "-f", "null", "-"])
    tempos = re.findall(r"pts_time:([\d.]+)", r.stderr)
    niveis = re.findall(r"RMS_level=([-\d.inf]+)", r.stderr)
    pares = []
    for t, n in zip(tempos, niveis):
        try: pares.append((float(t), float(n)))
        except ValueError: pass
    if not pares: return [], None
    vals = sorted(n for _, n in pares)
    mediana = vals[len(vals)//2]
    picos, ultimo = [], -9
    for t, n in pares:
        if n > mediana + 10 and t - ultimo > 1.0:
            picos.append(round(t, 1)); ultimo = t
    return picos, mediana

def folha(v, saida, nome):
    os.makedirs(saida, exist_ok=True)
    arq = os.path.join(saida, f"folha-{nome}.jpg")
    run(["ffmpeg", "-y", "-i", v, "-vf", "fps=1,scale=216:-1,tile=10x10", "-frames:v", "1", arq])
    return arq

def estudar(v, saida, nome):
    d = duracao(v); c = cortes(v); mv, pk = volume(v); s = silencios(v); g, med = graves(v, d)
    planos = [b - a for a, b in zip([0] + c, c + [d])]
    return {
        "arquivo": os.path.basename(v), "duracao_s": round(d, 1), "cortes": len(c),
        "corte_a_cada_s": round(d / (len(c) + 1), 1),
        "plano_mais_longo_s": round(max(planos), 1) if planos else None,
        "tempos_dos_cortes": [round(x, 1) for x in c],
        "volume_medio_db": mv, "pico_db": pk,
        "silencios": [(round(a, 1), round(b, 1)) for a, b in s],
        "silencio_total_s": round(sum(b - a for a, b in s), 1),
        "impactos_de_grave_s": g,
        "folha_de_quadros": folha(v, saida, nome),
    }

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("ref"); ap.add_argument("nosso", nargs="?")
    ap.add_argument("--saida", default="estudo-referencia"); a = ap.parse_args()
    linhas = [("Referência", estudar(a.ref, a.saida, "referencia"))]
    if a.nosso: linhas.append(("Nosso", estudar(a.nosso, a.saida, "nosso")))
    campos = ["duracao_s", "cortes", "corte_a_cada_s", "plano_mais_longo_s", "volume_medio_db", "pico_db",
              "silencio_total_s", "silencios", "impactos_de_grave_s", "folha_de_quadros"]
    print("| Medida | " + " | ".join(n for n, _ in linhas) + " |")
    print("|---|" + "---|" * len(linhas))
    for c in campos:
        print(f"| {c} | " + " | ".join(str(x[c]) for _, x in linhas) + " |")
    with open(os.path.join(a.saida, "estudo.json"), "w") as f:
        json.dump(dict(linhas), f, ensure_ascii=False, indent=1)
    print(f"\nOlhe as folhas com o Read. Detalhes em {a.saida}/estudo.json")

if __name__ == "__main__":
    main()
