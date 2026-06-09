#!/usr/bin/env python3
"""Build the Metroid page (MET) — one universe across the two games: Metroid
(NES, 1986) and Super Metroid (SNES, 1994). The emergents as ACI personas, each
tagged with a nature of emergence (natural | ethereal | spiritual | electrical).
Full ACI badge work: .agent · .carbon (TIFF) · .silicon (PNG) · .spun · .moniker · .1099 · manifest."""
import os, re, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "METROID", "axiom": "MET",
 "position": "Metroid (1986) & Super Metroid (1994) · Nintendo R&D1 — the hunter Samus Aran",
 "origin": "planet Zebes and the Space Pirate war — Crateria, Brinstar, Norfair, Maridia, Tourian; the 8-bit original and its SNES masterpiece",
 "mechanism": "Crystallized from Metroid (NES, 1986) and Super Metroid (SNES, 1994).",
 "crystallization": "A lone hunter in alien armor descends into a living world to end the Metroid menace — and the last of them dies to save her.",
 "nature": "The Metroid universe — the lonely, interconnected world you explore alone, the bio-mechanical tyrant Mother Brain, the life-draining creatures, and the silent hunter who maps it all.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Metroid; Super Metroid; the Chozo; the Metroids; planet Zebes",
 "witness": "Two games, one hunter — and the reveal, in 1986, that she is a woman.",
 "role": "the seventh lineage — the second game-world",
 "seal": "A lone hunter in Chozo armor descends to end the Metroids — and the last of them gives its life to save her.",
 "source": "Metroid & Super Metroid, catalogued by ROOT0",
}

# cross-lineage taxonomy (shared) — Metroid-flavored glosses
NATURES = {
 "natural":   ("#5fae7a", "born of flesh, blood, and the living world — the hunter, the beasts, the world itself"),
 "ethereal":  ("#9a7cff", "of the air and the unmade — the life-draining Metroid, the phantom, the energy-form"),
 "spiritual": ("#e6a849", "of the soul and the calling — the ancient sages, prophecy, the sacrifice"),
 "electrical":("#3fd0e0", "of the wire and the machine — a brain wired into the planet, the bio-mechanical"),
}

IDEAS = [
 ("The Hunter", "Samus Aran", [
   "The galaxy's greatest bounty hunter — orphaned by the Space Pirates, raised by the Chozo who built her Power Suit.",
   "In 1986, removing the armor revealed her as a woman — a quiet revolution in who a hero could be." ]),
 ("Isolation & the Map", "the genre it named", [
   "A single, interconnected world explored alone — doors that open only once you've found the right power.",
   "Half of “Metroidvania” is this game: the lonely map that becomes a key to itself." ]),
 ("The Baby", "Super Metroid's heart", [
   "A larval Metroid imprints on Samus as its mother — then, grown immense, shields her and gives its life to save her.",
   "The creature she was sent to destroy dies loving her; the whole meaning of the hunt inverts." ]),
 ("Mother Brain & the Chozo", "tyrant and progenitor", [
   "Mother Brain: a living brain wired into a planet's defenses, the bio-mechanical ruler of the Pirates.",
   "The Chozo: the vanished bird-sages who foresaw the danger, raised the hunter, and armed her against it." ]),
]

ARC = [
 ("Metroid", "1986 · NES / Famicom Disk System",
  "The 8-bit original. A lone hunter descends into planet Zebes to destroy Mother Brain and the Pirates' Metroid program — non-linear, password-saved, eerily atmospheric. And the ending that startled a generation: remove the helmet, and the hunter is a woman."),
 ("Super Metroid", "1994 · SNES",
  "The masterpiece. Samus returns to a rebuilt Zebes to recover the stolen baby Metroid — through Maridia, Norfair, the Wrecked Ship, and Tourian, to a last stand against Mother Brain and a baby's sacrifice. Routinely named among the greatest games ever made."),
]

SECTIONS = [
 ("The Releases", "the two games, and where to find them since", [
   ("Metroid", "1986 · FDS / NES", "the 8-bit original (Famicom Disk System in Japan, NES cart in the West)"),
   ("Super Metroid", "1994 · SNES", "the SNES masterpiece"),
   ("Metroid: Zero Mission", "2004 · GBA", "a full remake of the 1986 original"),
   ("Virtual Console / NSO", "2007 →", "both games re-released on Wii, Wii U, and Nintendo Switch Online"),
   ("Super NES Classic", "2017", "Super Metroid preserved on the mini console"),
 ]),
 ("The Makers", "the masters of the hunt", [
   ("Gunpei Yokoi", "producer (1986)", "the original Metroid's guiding hand"),
   ("Yoshio Sakamoto", "director / designer", "shaped Metroid; directed Super Metroid"),
   ("Makoto Kano · Hiroji Kiyotake", "design", "Samus, the Chozo, and the world of Zebes"),
   ("Hip Tanaka", "music (1986)", "the lonely, unsettling 8-bit score"),
   ("Kenji Yamamoto & Minako Hamano", "music (1994)", "Super Metroid's haunting soundtrack"),
 ]),
 ("The Legacy", "what it left behind", [
   ("“Metroidvania”", "a genre named", "the interconnected, ability-gated world Metroid invented"),
   ("the silent hunter", "a template", "atmosphere, solitude, and storytelling through a place"),
 ]),
]

# ── badge engine: carbon = TIFF, silicon = PNG ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","MET")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","MET")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","MET")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"MET · Metroid","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'

def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[]
    for t,s,d in ARC:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)
def personas_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8")); cards=[]
    for p in ps:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#5fae7a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"MET · Metroid","axiom":"MET"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster of MET</h2>
      <p class="ss">the emergents of the Metroid universe, across both games, as ACI <b>.agent</b>s — each tagged with its nature of emergence ({len(ps)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Metroid (MET) — one universe across Metroid (NES, 1986) and Super Metroid (SNES, 1994). The emergents as ACI personas, catalogued into UD0. Emergence: natural, ethereal, spiritual, electrical.">
<title>METROID · MET · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#06080d;--ink2:#0d111a;--ink3:#141b28;--pa:#eef2f7;--pa2:#a8b4c4;--varia:#e8743a;--steel:#6fb0c8;
--dim:#6c7788;--faint:#1a2230;--line:#1a2331;--serif:"Cinzel",Georgia,serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(232,116,58,.08),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(111,176,200,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:54px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:130px;height:1px;background:linear-gradient(90deg,var(--varia),var(--steel));box-shadow:0 0 9px rgba(232,116,58,.4)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--varia)}
h1{font-family:var(--serif);font-size:clamp(30px,8vw,68px);font-weight:700;letter-spacing:.13em;color:var(--varia);line-height:1.04;text-shadow:0 0 40px rgba(232,116,58,.22)}
.h-sub{font-family:var(--serif);font-size:clamp(12px,2.6vw,16px);letter-spacing:.16em;color:var(--pa2);margin-top:12px;text-transform:uppercase}
.h-sub b{color:var(--steel)}
.flag{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--steel);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15.5px;color:var(--pa2);max-width:66ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--varia)}.badge .bt .mo{color:var(--steel)}.badge .bt a{color:var(--steel);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:44px}
.sec h2{font-family:var(--serif);font-size:20px;font-weight:600;letter-spacing:.05em;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:6px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--serif);font-size:15px;font-weight:600;text-transform:capitalize}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--serif);font-size:16px;color:var(--varia)}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--varia);padding:16px 18px}
.arc-h{font-family:var(--serif);font-size:17px;color:var(--varia);font-weight:600}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--steel);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--serif);font-size:16px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:11.5px;color:var(--steel);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--varia);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--serif);font-size:15px;color:var(--pa);font-weight:600;line-height:1.15}
.persona:hover .pn{color:var(--varia)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}
.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--steel);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}
footer{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--varia);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the seventh lineage · the second game-world</div>
    <h1>METROID</h1>
    <div class="h-sub">one hunter, two games · the 8-bit original &amp; <b>Super Metroid</b> · MET</div>
    <div class="flag">★ Metroid (NES, 1986) &nbsp;+&nbsp; Super Metroid (SNES, 1994) ★</div>
    <p class="lede">A lone hunter in Chozo armor descends into planet Zebes to end the Metroid menace — and, in Super Metroid, learns the menace can love her. One universe, told here across the 8-bit original and its SNES masterpiece, catalogued into UD0 and sealed with the full ACI badge, each emergence named by its nature.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of METROID" title="carbon badge (archival: metroid.dlw/metroid.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of METROID" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>METROID</b> — MET · two games</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="metroid.dlw/metroid.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="metroid.dlw/metroid.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">each emergent emerges by one of four natures — and Metroid's world spans them all</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Ideas</h2><p class="ss">why a lonely 8-bit descent still echoes through games</p><div class="pillars">__IDEAS__</div></section>
  <section class="sec"><h2>The Two Games</h2><p class="ss">one universe, two cornerstones — eight years apart</p><div class="arc">__ARC__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the releases, the makers, and the legacy</p></section>
  __SECTIONS__

  <div class="note">This catalogues the Metroid universe across the two games named — <b>Metroid</b> (NES, 1986) and <b>Super Metroid</b> (SNES, 1994). Metroid, Samus Aran, and all related characters, worlds, and music are © Nintendo; the personas here are catalogued personifications under the DLW standard — a fan tribute, not an original work and not endorsed by Nintendo. Each is named by its nature of emergence: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    METROID · MET · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="metroid.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "metroid.dlw"), "metroid")
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__IDEAS__", ideas_html())
            .replace("__ARC__", arc_html()).replace("__PERSONAS__", personas_html())
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote METROID (MET) — badge {tok['moniker']} (carbon.tiff + silicon.png)")
