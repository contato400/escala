from pathlib import Path
# Motor de Reels narrados do WG. Uso:
#   python3 gerar_serie.py parte.json            -> MP4 completo
#   python3 gerar_serie.py parte.json --quadros  -> só a folha de conferência (8 quadros)
#   python3 gerar_serie.py parte.json --capa     -> só a capa
# O JSON descreve a fala de cada trecho e o que acontece na tela quando ele começa (ver SKILL video-serie-wg).
import json, os, sys, subprocess, wave, numpy as np
from playwright.sync_api import sync_playwright

MOTOR = os.path.dirname(os.path.abspath(__file__))
SCR = '/tmp/claude-0/-home-claude/18ecb643-e46a-54b4-bb6c-bb4a8009ab64/scratchpad'
VOZ = os.path.join(SCR, 'voz', 'pt_BR-faber-medium.onnx')
SR, FPS = 44100, 30

spec_path = sys.argv[1]
S = json.load(open(spec_path))
OUTDIR = os.path.dirname(os.path.abspath(spec_path))
NOME = S['nome']
TMP = os.path.join(SCR, 'serie_' + NOME); os.makedirs(TMP, exist_ok=True)

def baixar_voz():
    if os.path.exists(VOZ): return
    os.makedirs(os.path.dirname(VOZ), exist_ok=True)
    for f in ['pt_BR-faber-medium.onnx', 'pt_BR-faber-medium.onnx.json']:
        subprocess.run(['curl', '-sSL', '-o', os.path.join(os.path.dirname(VOZ), f),
                        f'https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/{f}'], check=True)
def ler(path):
    d = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(d, np.int16).astype(np.float64) / 32768

# ---------- narração ----------
baixar_voz()
FILTRO = {'tel': 'asetrate=22050*0.93,aresample=44100,highpass=f=350,lowpass=f=3200,volume=1.6',
          'porta': 'asetrate=22050*0.9,aresample=44100,lowpass=f=1800,aecho=0.6:0.5:40:0.3,volume=1.8'}
falas = []
for i, seg in enumerate(S['trechos']):
    raw = f'{TMP}/s{i:02d}.wav'
    voz = seg.get('voz', 'narrador')
    # Voz Gemini (padrão desde 20/11) pelo serviço /voz; se falhar, cai na Piper e avisa.
    g = subprocess.run([str(Path(__file__).resolve().parents[3] / 'rotinas' / 'voz.sh'), seg['fala'], raw + '.g.wav', seg.get('voz_gemini', 'Koda'), seg.get('estilo', '')], capture_output=True)
    if g.returncode == 0:
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw + '.g.wav', '-ar', '22050', '-ac', '1', raw], check=True)
    else:
        print('AVISO: voz Gemini falhou, usando Piper:', g.stderr.decode()[:200])
        subprocess.run(['python3', '-m', 'piper', '-m', VOZ, '-f', raw, '--length-scale', str(seg.get('ritmo', 1.0))],
                       input=seg['fala'].encode(), check=True, capture_output=True)
    if voz in FILTRO:
        f2 = f'{TMP}/s{i:02d}_{voz}.wav'
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, '-af', FILTRO[voz], f2], check=True); raw = f2
    x = ler(raw); nz = np.where(np.abs(x) > 0.01)[0]
    falas.append(x[max(0, nz[0] - 400): nz[-1] + 1200] if len(nz) else x)

t = 0.6; pos = []
for i, seg in enumerate(S['trechos']):
    t += seg.get('antes', 0); pos.append(t)
    t += len(falas[i]) / SR + seg.get('pausa', 0.35)
TOTAL = t + 2.2
dur = [len(f) / SR for f in falas]

# ---------- linha do tempo ----------
TL = {'total': TOTAL, 'badge': S.get('selo', ''), 'pixtela': S.get('pix_tela'), 'caps': [], 'calls': [], 'bubbles': [], 'shakes': [], 'beats': [], 'rule': [], 'knocks': []}
phone_on = door_on = pix_on = None; bub_open = []; tense = []; caps = []
for i, seg in enumerate(S['trechos']):
    a, d = pos[i], dur[i]; fim = a + d
    if 'legenda' in seg: caps.append({'t': a - 0.1, 'h': seg['legenda']})
    if seg.get('limpar_legenda'): caps.append({'t': a - 0.1, 'h': ''})
    if seg.get('telefone') == 'on': phone_on = a - 0.3
    if seg.get('telefone') == 'off' and phone_on is not None: TL['phone'] = [phone_on, a]; phone_on = None
    if 'chamada' in seg:
        c = seg['chamada']; TL['calls'].append({'t': a - 0.2, 'a': fim + 0.15, 'name': c['nome'], 'icon': c.get('icone', 'bank')})
        for b in bub_open: b['end'] = a - 0.2
        bub_open = []
    if 'bolha' in seg:
        b = {'t': a, 'txt': seg['bolha'], 'cps': len(seg['bolha']) / max(0.5, d), 'top': 250 + 190 * len(bub_open), 'lb': seg.get('rotulo', 'ELE DISSE:')}
        TL['bubbles'].append(b); bub_open.append(b)
    if seg.get('encerrar'): TL['ended'] = [a, a + 1.8]
    if seg.get('pix') == 'on': pix_on = a - 0.2
    if seg.get('pix') == 'cancelar': TL['pixx'] = a
    if seg.get('pix') == 'off' and pix_on is not None: TL['pix'] = [pix_on, a]; pix_on = None
    if seg.get('dedo'): TL['finger'] = [a, fim + 0.3]
    if seg.get('porta') == 'on': door_on = a - 0.3
    if seg.get('porta') == 'off' and door_on is not None: TL['door'] = [door_on, a]; door_on = None
    if seg.get('batida'): TL['knocks'] += [a - 0.5, a - 0.15]
    if 'voz_porta' in seg: TL['voice'] = {'t': a, 'end': fim + 1.0, 'txt': seg['voz_porta'], 'cps': len(seg['voz_porta']) / max(0.5, d)}
    if 'regra' in seg: TL['rule'].append({'t': a - 0.1, 'end': fim + 0.4, 'txt': seg['regra'], 'sm': seg.get('regra_titulo', 'FICA A DICA')})
    if seg.get('tensao'): tense.append([a - 0.1, fim + 0.6]); TL['shakes'].append({'t': a - 0.1, 'd': min(3.4, d + 0.6)})
    if seg.get('escurecer'): TL['dim'] = [a - 0.1, a + 60]
    if seg.get('lista') == 'on': TL['rules'] = {'t': a - 0.2, 'end': TOTAL + 5, 'items': []}
    if 'item' in seg: TL['rules']['items'].append({'t': a - 0.05, 'txt': seg['item']})
    if seg.get('lista') == 'off': TL['rules']['end'] = a
    if 'final' in seg:
        f = seg['final']; TL['fin'] = {'t': a - 0.35, 'badge': f.get('selo', 'FIM DA PARTE'), 'q': f['pergunta'], 'cta': f['chamada'], 'cta_t': None}
        caps.append({'t': a - 0.35, 'h': ''})
    if seg.get('mostrar_chamada'): TL['fin']['cta_t'] = a - 0.05
end = TOTAL + 5
if phone_on is not None: TL['phone'] = [phone_on, TL['fin']['t'] if 'fin' in TL else end]
if door_on is not None: TL['door'] = [door_on, TL['fin']['t'] if 'fin' in TL else end]
if pix_on is not None: TL['pix'] = [pix_on, end]
if 'rules' in TL and TL['rules']['end'] > TOTAL and 'fin' in TL: TL['rules']['end'] = TL['fin']['t']
if 'fin' in TL and TL['fin']['cta_t'] is None: TL['fin']['cta_t'] = TL['fin']['t'] + 1.3
TL['caps'] = caps; TL['beats'] = tense
for c in TL['calls']: pass

# ---------- som ----------
N = int(TOTAL * SR); mix = np.zeros(N); rng = np.random.default_rng(7)
at = lambda x: int(x * SR)
def add(sig, x, v=1.0):
    i = at(x); j = min(N, i + len(sig))
    if 0 <= i < N: mix[i:j] += sig[:j - i] * v
def env(n, a=0.005, r=0.1):
    e = np.ones(n); A = max(1, int(a * SR)); R = max(1, int(r * SR)); e[:A] = np.linspace(0, 1, A); e[-R:] *= np.linspace(1, 0, R); return e
def tone(f, d, a=0.005, r=0.1):
    tt = np.arange(int(d * SR)) / SR; return np.sin(2 * np.pi * f * tt) * env(len(tt), a, r)
noise = lambda d: rng.uniform(-1, 1, int(d * SR))
lp = lambda x, k: np.convolve(x, np.ones(k) / k, mode='same')
def whoosh(d=0.4):
    n = int(d * SR); x = noise(d); k = np.linspace(40, 4, n); y = np.zeros(n); acc = 0.0
    for i in range(n): acc += (x[i] - acc) / k[i]; y[i] = acc
    return y * np.sin(np.linspace(0, np.pi, n)) * 3
def thump(f=55, d=0.16):
    tt = np.arange(int(d * SR)) / SR; return np.sin(2 * np.pi * f * tt * (1 - 0.4 * tt / d)) * np.exp(-tt * 22)
def impact(d=1.2):
    tt = np.arange(int(d * SR)) / SR; return np.sin(2 * np.pi * 48 * tt * (1 - 0.5 * tt / d)) * np.exp(-tt * 3.5) + lp(noise(d), 3) * np.exp(-tt * 25) * 0.5
def key():
    d = 0.025; return lp(noise(d), 2) * env(int(d * SR), 0.001, 0.02) + tone(rng.uniform(1800, 2600), d, 0.001, 0.02) * 0.2
def knock():
    d = 0.12; tt = np.arange(int(d * SR)) / SR; return (np.sin(2 * np.pi * 120 * tt) + lp(noise(d), 6) * 0.8) * np.exp(-tt * 40)
for c in TL['calls']:  # toque até atender
    s = c['t'] + 0.1
    while s < c['a'] - 0.3:
        tt = np.arange(int(0.95 * SR)) / SR
        add((np.sin(2 * np.pi * 425 * tt) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 25 * tt)))) * env(len(tt), 0.01, 0.05), s, 0.14)
        add(np.sin(2 * np.pi * 140 * tt) * (np.sin(2 * np.pi * 12 * tt) > 0) * env(len(tt), 0.01, 0.05), s, 0.08); s += 1.4
    add(lp(noise(0.03), 3) * env(int(0.03 * SR), 0.001, 0.02), c['a'], 0.5)
for c in caps[1:]:
    if c['h']: add(whoosh(0.35), c['t'] - 0.1, 0.10)
for b in TL['bubbles'] + ([TL['voice']] if 'voice' in TL else []):
    for i, ch in enumerate(b['txt']):
        if ch != ' ': add(key(), b['t'] + i / b['cps'] + rng.uniform(-0.008, 0.008), 0.09)
if 'ended' in TL: add(tone(480, 0.25, 0.005, 0.05) + tone(620, 0.25, 0.005, 0.05), TL['ended'][0], 0.25); add(tone(480, 0.25, 0.005, 0.05) + tone(620, 0.25, 0.005, 0.05), TL['ended'][0] + 0.4, 0.25)
if 'pix' in TL: add(whoosh(0.4), TL['pix'][0], 0.12)
if 'pixx' in TL: add(impact(1.0), TL['pixx'], 0.6)
for k in TL['knocks']:
    for j in range(3): add(knock(), k + j * 0.17, 0.9)
for r in TL['rule']: add(tone(880, 1.0, 0.002, 0.9) * 0.5 + tone(1320, 1.0, 0.002, 0.9) * 0.25, r['t'], 0.22); add(whoosh(0.35), r['t'] - 0.15, 0.12)
if 'rules' in TL:
    for it in TL['rules']['items']: add(tone(660, 0.12, 0.002, 0.1) + tone(990, 0.12, 0.002, 0.1) * 0.5, it['t'], 0.3)
for w in tense:
    add(impact(), w[0], 0.6); x = w[0]
    while x < w[1]: add(thump(), x, 0.9); add(thump(50), x + 0.22, 0.6); x += 0.86
if 'fin' in TL:
    add(impact(1.4), TL['fin']['t'], 0.7); add(whoosh(0.4), TL['fin']['t'] + 0.2, 0.12)
    add(tone(660, 0.12, 0.002, 0.1) + tone(990, 0.12, 0.002, 0.1) * 0.5, TL['fin']['cta_t'], 0.35)
tt = np.arange(N) / SR; pad = np.zeros(N)
for f, v in [(55, 0.5), (110, 0.35), (130.81, 0.22), (164.81, 0.2), (220, 0.08)]:
    pad += v * np.sin(2 * np.pi * f * tt + np.sin(2 * np.pi * 0.2 * tt) * 0.8)
pad *= 0.6 + 0.4 * np.sin(2 * np.pi * 0.12 * tt)
lvl = np.full(N, 0.11); lvl[:at(0.5)] = np.linspace(0, 0.11, at(0.5)); lvl[-at(1.2):] *= np.linspace(1, 0, at(1.2))
for w in tense: lvl[at(w[0]):at(min(TOTAL, w[1]))] = 0.03
mix += pad * lvl
x = 0.8
while x < TOTAL - 1.2:
    if not any(w[0] <= x < w[1] for w in tense): add(thump(70, 0.12), x, 0.2)
    x += 0.6
voz = np.zeros(N)
for i, f in enumerate(falas):
    a = at(pos[i]); b = min(N, a + len(f)); voz[a:b] += f[:b - a]
voz = voz / max(1e-9, np.abs(voz).max()) * 0.95
mix = mix / max(1e-9, np.abs(mix).max()) * 0.55 + voz
mix = mix / max(1e-9, np.abs(mix).max()) * 0.89
WAV = f'{TMP}/som.wav'
with wave.open(WAV, 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())

# ---------- imagem ----------
def abrir(pw):
    b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto('file://' + os.path.join(MOTOR, 'serie.html')); pg.wait_for_timeout(600)
    pg.evaluate('tl => { TL = tl; init(); }', TL); return b, pg
with sync_playwright() as pw:
    b, pg = abrir(pw)
    if '--quadros' in sys.argv:
        from PIL import Image
        ts = [round(TOTAL * k / 8 + 0.6, 2) for k in range(8)]; ims = []
        for a in sys.argv:
            if a.startswith('--em='): ts = [float(v) for v in a[5:].split(',')][:8]  # tempos escolhidos (s)
        for x in ts:
            pg.evaluate(f'render({x})'); f = f'{TMP}/q_{x}.png'; pg.screenshot(path=f); ims.append(Image.open(f).resize((270, 480)))
        W = Image.new('RGB', (270 * 4, 480 * 2)); [W.paste(im, ((i % 4) * 270, (i // 4) * 480)) for i, im in enumerate(ims)]
        out = os.path.join(OUTDIR, f'{NOME}_conferencia.png'); W.save(out); print('conferencia', out, 'duracao', round(TOTAL, 1)); b.close(); sys.exit()
    if '--capa' in sys.argv:
        C = S['capa']; pg.evaluate(f"render({C.get('quadro', 1.5)})")
        pg.evaluate("""c=>{document.querySelector('#cap').style.display='none';document.querySelector('#tag').style.display='none';document.querySelector('#badge').style.display='none';
          document.querySelector('#redflash').style.opacity=.8;
          document.querySelector('#stage').insertAdjacentHTML('beforeend',`<div style="position:absolute;inset:0">
          <div style="position:absolute;top:300px;left:50%;transform:translateX(-50%) rotate(-3deg);background:#ff3341;font:800 46px I;letter-spacing:4px;padding:12px 34px;border-radius:14px;box-shadow:0 10px 40px rgba(255,51,65,.5);white-space:nowrap">${c.selo}</div>
          <div style="position:absolute;top:410px;left:90px;width:900px;text-align:center;font:800 108px/1.0 I;letter-spacing:-3px;text-shadow:0 8px 40px rgba(0,0,0,.9)">${c.titulo}</div>
          <div style="position:absolute;top:1450px;left:110px;width:860px;text-align:center"><span style="display:inline-block;background:#ffd23f;color:#0a0a0a;font:800 52px/1.15 I;padding:18px 30px;border-radius:18px;transform:rotate(-1.5deg)">${c.faixa}</span></div></div>`)}""", C)
        out = os.path.join(OUTDIR, f'{NOME}_capa.jpg'); pg.screenshot(path=out, type='jpeg', quality=95); print('capa', out); b.close(); sys.exit()
    FR = f'{TMP}/fr'; os.makedirs(FR, exist_ok=True)
    for f in os.listdir(FR): os.remove(os.path.join(FR, f))
    for i in range(int(TOTAL * FPS)):
        pg.evaluate(f'render({i / FPS})'); pg.screenshot(path=f'{FR}/f{i:04d}.jpg', type='jpeg', quality=92)
    b.close()
OUT = os.path.join(OUTDIR, f'{NOME}.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{FR}/f%04d.jpg', '-i', WAV, '-c:v', 'libx264', '-preset', 'veryfast',
                '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', OUT], check=True)
print('ok', OUT, round(TOTAL, 1), 's')
