"""Generate the themed SVG assets for the GitHub profile README."""
import os, sys
from xml.sax.saxutils import escape as esc

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

SANS = "'Segoe UI',Inter,-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
BG = "#04050b"; CARD = "#0a0c1a"; GOLD = "#f5c451"; TEAL = "#2dd4bf"
TXT = "#eef1fa"; MUTED = "#98a1c0"; LINE = "#1d2647"

def write(name, body):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(body)

def frame(w, h, inner, extra_defs="", style=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0e1024"/><stop offset="1" stop-color="{BG}"/></linearGradient>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOLD}" stop-opacity=".55"/><stop offset=".5" stop-color="{TEAL}" stop-opacity=".25"/><stop offset="1" stop-color="{GOLD}" stop-opacity=".1"/></linearGradient>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#ffffff" stroke-opacity=".035"/></pattern>
  {extra_defs}
</defs>
<style>
  text{{font-family:{SANS}}} .m{{font-family:{MONO}}}
  {style}
</style>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="url(#bg)" stroke="url(#edge)" stroke-width="1.5"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="url(#grid)"/>
{inner}
</svg>"""

# ---------------------------------------------------------------- project cards
def chip_row(x, y, chips, color):
    out, cx = [], x
    for c in chips:
        w = 16 + len(c) * 7.6
        out.append(f'<rect x="{cx}" y="{y}" width="{w:.0f}" height="22" rx="11" fill="{color}" fill-opacity=".09" stroke="{color}" stroke-opacity=".38"/>'
                   f'<text x="{cx + w/2:.0f}" y="{y+15}" text-anchor="middle" class="m" font-size="12" font-weight="600" fill="{color}">{esc(c)}</text>')
        cx += w + 8
    return "".join(out)

def card(name, tag, title, lines, chips, accent, motif, cta):
    W, H = 600, 260
    ln = "".join(f'<text x="32" y="{124 + i*24}" font-size="17" fill="{MUTED}">{esc(l)}</text>' for i, l in enumerate(lines))
    inner = f"""
<rect x="1" y="1" width="5" height="{H-2}" rx="2" fill="{accent}" opacity=".85"/>
<g class="m" font-size="10.5" font-weight="700" letter-spacing="2.4">
  <circle cx="38" cy="40" r="4" fill="{accent}"><animate attributeName="opacity" values="1;.25;1" dur="2.4s" repeatCount="indefinite"/></circle>
  <text x="50" y="44" fill="{accent}">{esc(tag)}</text>
</g>
<text x="32" y="88" font-size="32" font-weight="800" fill="{TXT}" letter-spacing="-.5">{esc(title)}</text>
{ln}
{chip_row(32, 190, chips, accent)}
<text x="{W-32}" y="{H-26}" text-anchor="end" class="m" font-size="11" font-weight="700" letter-spacing="1.5" fill="{accent}">{esc(cta)} →</text>
<g transform="translate(470 96)">{motif}</g>"""
    write(f"card-{name}.svg", frame(W, H, inner))

foundry_motif = f"""
  <g fill="none" stroke-width="3">
    <circle r="34" stroke="#d9822b" opacity=".85"/><circle r="24" stroke="#a9b6c8" opacity=".85"/><circle r="14" stroke="{GOLD}"/>
  </g>
  <circle r="5" fill="{GOLD}"><animate attributeName="r" values="4;7;4" dur="2s" repeatCount="indefinite"/></circle>
  <g>
    <circle r="3.5" fill="#ef4444"><animateMotion dur="3s" repeatCount="indefinite" path="M-90,-30 C-60,-30 -40,0 0,0"/><animate attributeName="fill" values="#ef4444;#d9822b;#cbd5e1;{GOLD}" dur="3s" repeatCount="indefinite"/></circle>
    <circle r="3.5" fill="#a855f7"><animateMotion dur="3s" begin="-1s" repeatCount="indefinite" path="M-90,30 C-60,30 -40,0 0,0"/><animate attributeName="fill" values="#a855f7;#d9822b;#cbd5e1;{GOLD}" dur="3s" begin="-1s" repeatCount="indefinite"/></circle>
    <circle r="3.5" fill="#64748b"><animateMotion dur="3s" begin="-2s" repeatCount="indefinite" path="M-90,0 C-60,0 -40,0 0,0"/><animate attributeName="fill" values="#64748b;#d9822b;#cbd5e1;{GOLD}" dur="3s" begin="-2s" repeatCount="indefinite"/></circle>
  </g>"""

dhaba_motif = f"""
  <path d="M-38,4 Q-38,40 0,40 Q38,40 38,4 Z" fill="#e8366f" fill-opacity=".18" stroke="#e8366f" stroke-width="3"/>
  <line x1="-46" y1="4" x2="46" y2="4" stroke="#e8366f" stroke-width="3" stroke-linecap="round"/>
  <g fill="{TEAL}">
    {''.join(f'<rect x="{x}" y="-6" width="6" height="6" rx="1.5"><animate attributeName="y" values="-6;-52" dur="2.4s" begin="{b}s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0" dur="2.4s" begin="{b}s" repeatCount="indefinite"/></rect>' for x, b in [(-20, 0), (-3, -.8), (14, -1.6), (-11, -1.2), (6, -.4)])}
  </g>"""

passport_motif = f"""
  <text x="0" y="-26" text-anchor="middle" class="m" font-size="18" font-weight="800" fill="#7cc4ff">42.7M</text>
  <g stroke="#7cc4ff" stroke-opacity=".5" stroke-width="1.5" fill="none">
    <path d="M0,-16 L0,0 M0,0 L-30,22 M0,0 L30,22 M-30,22 L-40,44 M-30,22 L-16,44 M30,22 L22,44 M30,22 L42,44"/>
  </g>
  <g fill="#7cc4ff">
    <circle cx="0" cy="0" r="4"/><circle cx="-30" cy="22" r="4"/><circle cx="30" cy="22" r="4"/>
    <circle cx="-40" cy="44" r="3"/><circle cx="-16" cy="44" r="3"/><circle cx="22" cy="44" r="3"/><circle cx="42" cy="44" r="3"/>
  </g>
  <circle r="4" fill="#1f9d63"><animateMotion dur="2.6s" repeatCount="indefinite" path="M0,-16 L0,0 L-30,22 L-16,44"/></circle>
  <circle r="4" fill="#1f9d63"><animateMotion dur="2.6s" begin="-1.3s" repeatCount="indefinite" path="M0,-16 L0,0 L30,22 L42,44"/></circle>"""

deja_motif = f"""
  <circle r="36" fill="none" stroke="#f59e0b" stroke-opacity=".3" stroke-width="2" stroke-dasharray="4 6"/>
  <path d="M0,-36 A36,36 0 1,1 -25,26" fill="none" stroke="#f59e0b" stroke-width="3" stroke-linecap="round">
    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="6s" repeatCount="indefinite"/>
  </path>
  <text y="7" text-anchor="middle" class="m" font-size="18" font-weight="800" fill="{TEAL}">↺</text>
  <text y="60" text-anchor="middle" class="m" font-size="9.5" font-weight="700" letter-spacing="1.5" fill="#f59e0b">SEEN IT</text>"""

card("foundry", "LIVE · INTERACTIVE PORTFOLIO", "The Data Foundry",
     ["Watch a data pipeline run in 3D. Break it", "on purpose and see how it recovers."],
     ["Next.js", "Three.js", "live event stream"], GOLD, foundry_motif, "OPEN THE FOUNDRY")
card("dhaba", "LIVE · DATADHABA.IN", "Data Dhaba",
     ["A data engineering school I run: handbooks,", "SQL and Python labs, a 24-week path."],
     ["learn", "build", "get hired"], "#e8366f", dhaba_motif, "START LEARNING")
card("passport", "OPEN SOURCE · ON PyPI", "Number Passport",
     ["Trace any reported number back to its", "source rows, reconcile every hop, prove it."],
     ["Python", "lineage", "BCBS 239", "MCP"], "#7cc4ff", passport_motif, "VIEW REPO")
card("deja", "OPEN SOURCE · CLAUDE CODE PLUGIN", "deja",
     ["Memory for Claude Code and Codex that", "never debugs the same bug twice."],
     ["Node 22", "zero deps", "MCP"], "#f59e0b", deja_motif, "VIEW REPO")

# ---------------------------------------------------------------- section headers
def header(name, num, title, sub):
    W, H = 1200, 76
    inner = f"""
<text x="34" y="47" class="m" font-size="14" font-weight="800" fill="{GOLD}" letter-spacing="2">{num}</text>
<line x1="70" y1="42" x2="96" y2="42" stroke="{GOLD}" stroke-width="2"/>
<text x="110" y="49" font-size="24" font-weight="800" fill="{TXT}" letter-spacing="-.3">{esc(title)}</text>
<text x="{W-34}" y="47" text-anchor="end" class="m" font-size="11" font-weight="600" letter-spacing="2" fill="{MUTED}">{esc(sub)}</text>
<rect x="110" y="60" width="44" height="3" rx="1.5" fill="{GOLD}"><animate attributeName="width" values="44;120;44" dur="5s" repeatCount="indefinite"/></rect>"""
    write(f"h-{name}.svg", frame(W, H, inner))

header("work", "01", "Selected work", "LIVE PRODUCTS · OPEN SOURCE")
header("lifecycle", "02", "The whole data lifecycle", "FIRST BYTE TO LAST DASHBOARD")
header("principles", "03", "How I build", "PRINCIPLES I DON'T SKIP")
header("stack", "04", "Toolbox", "TOOLS I SHIP WITH")

# ---------------------------------------------------------------- lifecycle diagram
def lifecycle():
    W, H = 1200, 400
    stages = [
        ("INGEST", ["Batch & APIs", "Event streams", "Database CDC"], "#ef6b5b"),
        ("STORE", ["Lakehouse", "Warehouse", "Formats & partitions"], "#d9822b"),
        ("PROCESS", ["Spark batch", "Structured Streaming", "Incremental SQL"], "#a9b6c8"),
        ("MODEL", ["Bronze · silver · gold", "Star schemas", "SCD Type 2"], GOLD),
        ("SERVE", ["BI marts", "APIs & reverse ETL", "ML features · RAG"], TEAL),
    ]
    cw, gap, x0, y0 = 196, 38, 36, 40
    parts = []
    for i, (t, items, c) in enumerate(stages):
        x = x0 + i * (cw + gap)
        parts.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="176" rx="12" fill="{CARD}" stroke="{c}" stroke-opacity=".45"/>')
        parts.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="4" rx="2" fill="{c}"/>')
        parts.append(f'<text x="{x+20}" y="{y0+36}" class="m" font-size="11" font-weight="800" letter-spacing="2.4" fill="{c}">0{i+1}</text>')
        parts.append(f'<text x="{x+20}" y="{y0+64}" font-size="20" font-weight="800" fill="{TXT}" letter-spacing=".5">{t}</text>')
        for k, it in enumerate(items):
            parts.append(f'<circle cx="{x+24}" cy="{y0+95+k*26}" r="2.5" fill="{c}"/>')
            parts.append(f'<text x="{x+36}" y="{y0+100+k*26}" font-size="13.5" fill="{MUTED}">{esc(it)}</text>')
        if i < len(stages) - 1:
            ax = x + cw + 6
            parts.append(f'<path d="M{ax},{y0+88} h{gap-14}" stroke="{LINE}" stroke-width="2"/>'
                         f'<path d="M{ax+gap-16},{y0+83} l6,5 l-6,5" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    # flowing record across all stages
    flow = f'M{x0+cw},{y0+88} H{x0+4*(cw+gap)}'
    for b, col in [(0, "#ef4444"), (-1.5, "#d9822b"), (-3, GOLD)]:
        parts.append(f'<circle r="4.5" fill="{col}"><animateMotion dur="4.5s" begin="{b}s" repeatCount="indefinite" path="{flow}"/>'
                     f'<animate attributeName="fill" values="#ef4444;#d9822b;#cbd5e1;{GOLD};{TEAL}" dur="4.5s" begin="{b}s" repeatCount="indefinite"/></circle>')
    # cross-cutting bands
    bands = [
        ("ORCHESTRATION · CI/CD · OBSERVABILITY · COST", "Airflow DAGs with retries, SLAs and backfills · everything as code · tested before prod", TEAL),
        ("QUALITY · GOVERNANCE · LINEAGE · SECURITY", "Contracts at every boundary · quarantine, not silent corruption · catalogs, PII masking", GOLD),
    ]
    for j, (t, d, c) in enumerate(bands):
        y = 240 + j * 70
        parts.append(f'<rect x="{x0}" y="{y}" width="{W-2*x0}" height="56" rx="12" fill="{c}" fill-opacity=".06" stroke="{c}" stroke-opacity=".35" stroke-dasharray="5 5"/>')
        parts.append(f'<text x="{x0+22}" y="{y+24}" class="m" font-size="11.5" font-weight="800" letter-spacing="2" fill="{c}">{t}</text>')
        parts.append(f'<text x="{x0+22}" y="{y+44}" font-size="13.5" fill="{MUTED}">{esc(d)}</text>')
        parts.append(f'<circle cx="{W-x0-24}" cy="{y+28}" r="5" fill="{c}"><animate attributeName="opacity" values="1;.2;1" dur="{2+j*.6}s" repeatCount="indefinite"/></circle>')
    write("lifecycle.svg", frame(W, H, "".join(parts)))

lifecycle()

# ---------------------------------------------------------------- principles
def principles():
    W, H = 1200, 200
    ps = [
        ("Replayable", "Raw data is kept, every step can re-run, every write is idempotent.", "#d9822b"),
        ("Fail loudly", "Bad data stops at the edge and alerts. Nothing slips downstream.", "#ef6b5b"),
        ("One logic", "Batch and streaming share one model, so the numbers agree.", "#a9b6c8"),
        ("Next reader", "Documented tables, clear owners, lineage anyone can follow.", TEAL),
    ]
    cw, gap, x0 = 264, 20, 36
    parts = []
    for i, (t, d, c) in enumerate(ps):
        x = x0 + i * (cw + gap)
        parts.append(f'<rect x="{x}" y="28" width="{cw}" height="144" rx="12" fill="{CARD}" stroke="{LINE}"/>')
        parts.append(f'<rect x="{x+20}" y="48" width="28" height="4" rx="2" fill="{c}"/>')
        parts.append(f'<text x="{x+20}" y="84" font-size="20" font-weight="800" fill="{TXT}">{t}</text>')
        words, lines, cur = d.split(), [], ""
        for wd in words:
            if len(cur) + len(wd) + 1 > 29:
                lines.append(cur); cur = wd
            else:
                cur = (cur + " " + wd).strip()
        lines.append(cur)
        for k, l in enumerate(lines):
            parts.append(f'<text x="{x+20}" y="{114+k*22}" font-size="15.5" fill="{MUTED}">{esc(l)}</text>')
    write("principles.svg", frame(W, H, "".join(parts)))

principles()

# ---------------------------------------------------------------- stack
def stack():
    groups = [
        ("LANGUAGES", ["Python", "SQL", "PySpark", "Shell"], "#7cc4ff"),
        ("BIG DATA", ["Apache Spark", "Kafka", "Hadoop", "HDFS", "YARN", "Hive", "Sqoop"], "#ef6b5b"),
        ("LAKEHOUSE & WAREHOUSE", ["Databricks", "Delta Lake", "BigQuery"], GOLD),
        ("ORCHESTRATION & CLOUD", ["Airflow", "Azure", "Docker", "Linux"], TEAL),
        ("DEVOPS & TOOLING", ["Git", "GitHub Actions", "Jira"], "#c4b5fd"),
    ]
    W, row = 1200, 50
    H = 36 + len(groups) * row + 4
    parts = []
    for i, (g, tools, c) in enumerate(groups):
        y = 34 + i * row
        parts.append(f'<text x="36" y="{y+20}" class="m" font-size="11" font-weight="800" letter-spacing="2" fill="{c}">{esc(g)}</text>')
        x = 300
        for t in tools:
            w = 34 + len(t) * 8.2
            parts.append(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="30" rx="8" fill="{c}" fill-opacity=".08" stroke="{c}" stroke-opacity=".4"/>'
                         f'<circle cx="{x+15}" cy="{y+15}" r="3.5" fill="{c}"/>'
                         f'<text x="{x+26}" y="{y+20}" font-size="14" font-weight="600" fill="{TXT}">{esc(t)}</text>')
            x += w + 10
        if i < len(groups) - 1:
            parts.append(f'<line x1="36" y1="{y+row-10}" x2="{W-36}" y2="{y+row-10}" stroke="{LINE}" stroke-opacity=".6"/>')
    write("stack.svg", frame(W, H, "".join(parts)))

stack()

# ---------------------------------------------------------------- footer
def footer():
    W, H = 1200, 150
    inner = f"""
<text x="600" y="62" text-anchor="middle" font-size="28" font-weight="800" fill="{TXT}" letter-spacing="-.4">Let's build data people <tspan fill="{GOLD}">trust.</tspan></text>
<g transform="translate(600 100)">
  <rect x="-170" y="-16" width="340" height="32" rx="16" fill="#34d399" fill-opacity=".08" stroke="#34d399" stroke-opacity=".45"/>
  <circle cx="-146" cy="0" r="5" fill="#34d399"><animate attributeName="r" values="4;6;4" dur="1.6s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;.5;1" dur="1.6s" repeatCount="indefinite"/></circle>
  <text x="8" y="5" text-anchor="middle" class="m" font-size="12" font-weight="800" letter-spacing="2" fill="#5eead4">OPEN TO SENIOR DE ROLES</text>
</g>"""
    write("footer.svg", frame(W, H, inner))

footer()

# ---------------------------------------------------------------- impact strip
def impact():
    W, H = 1200, 150
    stats = [
        ("300+", "production pipelines", "migrated at eBay", GOLD),
        ("5 yrs", "building data platforms", "Spark · Databricks · Airflow", "#c4a3ff"),
        ("4", "industries", "e-commerce · auto · finance · IoT", "#7cc4ff"),
        ("4", "things I've shipped", "2 live sites · 2 open source", TEAL),
    ]
    cw = (W - 72) / 4
    parts = []
    for i, (n, l1, l2, c) in enumerate(stats):
        x = 36 + i * cw
        if i:
            parts.append(f'<line x1="{x:.0f}" y1="34" x2="{x:.0f}" y2="{H-34}" stroke="{LINE}"/>')
        cx = x + cw / 2
        d = .25 * i
        parts.append(f'<g><animate attributeName="opacity" values="0;0;1" keyTimes="0;{d/(d+.8):.2f};1" dur="{d+.8:.2f}s" fill="freeze"/>'
                     f'<text x="{cx:.0f}" y="72" text-anchor="middle" font-size="40" font-weight="900" fill="{c}" letter-spacing="-1">{esc(n)}</text>'
                     f'<text x="{cx:.0f}" y="98" text-anchor="middle" font-size="14.5" font-weight="700" fill="{TXT}">{esc(l1)}</text>'
                     f'<text x="{cx:.0f}" y="118" text-anchor="middle" class="m" font-size="10.5" font-weight="600" letter-spacing="1" fill="{MUTED}">{esc(l2)}</text></g>')
    write("impact.svg", frame(W, H, "".join(parts)))

impact()
print("ok")
