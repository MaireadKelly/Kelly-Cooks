import re, os, sys, pathlib

root = pathlib.Path(".")
paths = ["README.md", "TESTING.md"]
img_re_md = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
img_re_html = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.I)
bare_re = re.compile(r'(?<!\()(?<!\!)\bdocs/[^\s)"]+\.(?:png|jpe?g|gif|webp)', re.I)

refs = set()
for p in paths:
    try:
        text = pathlib.Path(p).read_text("utf-8", errors="ignore")
    except:
        continue
    for m in img_re_md.finditer(text):
        refs.add(m.group(1).strip().lstrip("./"))
    for m in img_re_html.finditer(text):
        refs.add(m.group(1).strip().lstrip("./"))
    # also catch bare paths in TESTING.md
    if p.lower() == "testing.md":
        for m in bare_re.finditer(text):
            refs.add(m.group(0).strip().lstrip("./"))

missing = []
for r in sorted(refs):
    if r.startswith(("http://", "https://", "mailto:")):
        continue
    r2 = r.split("?")[0].split("#")[0].replace("\\", "/")
    if not root.joinpath(r2).exists():
        missing.append(r2)

print("Total refs:", len(refs))
print("Missing files:", len(missing))
for m in missing:
    print(" -", m)
