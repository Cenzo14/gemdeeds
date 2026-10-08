"""Build the GemDeeds upload archives into Cloudflare's dist directory."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parent
dest = root / 'dist'
dest.mkdir(exist_ok=True)
archives = ['core.zip', 'classic.zip'] + [f'art-{n:02}.zip' for n in range(1, 8)]
for name in archives:
    with zipfile.ZipFile(root / name) as archive:
        for entry in archive.infolist():
            target = (dest / entry.filename).resolve()
            if not target.is_relative_to(dest.resolve()):
                raise ValueError(f'Invalid archive path: {entry.filename}')
        archive.extractall(dest)
page = dest / 'index.html'
html = page.read_text(encoding='utf-8')
html = html.replace('src:url(gf/', 'src:url(https://fonts.gstatic.com/')
html = html.replace("return own?[{js:'ml/js/',m:'ml/m/',h:'ml/h/'},dir]:[dir];", 'return [dir];')
page.write_text(html, encoding='utf-8')
(dest / '_redirects').write_text('/classic /classic/play/ 301\n', encoding='utf-8')
(dest / '_headers').write_text('/sw.js\n  Cache-Control: no-cache\n/classic/play/sw.js\n  Cache-Control: no-cache\n', encoding='utf-8')
for relative, before, after in [('sw.js', "var C='gd-v19'", "var C='gd-v20-cf'"), ('classic/play/sw.js', "var C='gdc-p1'", "var C='gdc-p2-cf'")]:
    path = dest / relative
    path.write_text(path.read_text(encoding='utf-8').replace(before, after), encoding='utf-8')
files = [p for p in dest.rglob('*') if p.is_file()]
assert len(files) < 20000
assert max(p.stat().st_size for p in files) < 25 * 1024 * 1024
assert "const KEY='gemdeeds-world-builder-v8'" in html
print(f'GemDeeds ready: {len(files)} files in dist; media preserved without recompression.')
