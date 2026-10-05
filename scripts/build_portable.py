#!/usr/bin/env python3
"""Build a self-contained THE RIZEN HTML file for offline or fallback use.

The live GitHub Pages site remains the preferred experience. This builder inlines
local assets, CSS, database helpers, and application code into one HTML file.
Third-party features still require the browser and the original provider:
Google Maps, Spotify, weather, and MyCB Radio open or fetch normally when online.
"""
from __future__ import annotations

import base64
import mimetypes
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "THE_RIZEN_LIVE.html"


def data_url(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    mime = mime or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def inline_css_assets(css: str) -> str:
    def replace(match: re.Match[str]) -> str:
        raw_path = match.group(1)
        asset = ROOT / raw_path.lstrip("./")
        if not asset.is_file():
            raise FileNotFoundError(f"CSS references missing asset: {asset}")
        return f'url("{data_url(asset)}")'

    return re.sub(r"url\(['\"](\./assets/[^'\"]+)['\"]\)", replace, css)


def main() -> None:
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    css = inline_css_assets((ROOT / "styles.css").read_text(encoding="utf-8"))
    db = (ROOT / "db.js").read_text(encoding="utf-8")
    app = (ROOT / "app.js").read_text(encoding="utf-8")

    # Classic inline scripts cannot use ES module export/import syntax.
    db = re.sub(r"\bexport\s+", "", db)
    app = re.sub(
        r"^import\s*\{.*?\}\s*from\s*'\./db\.js\?v=\d+';\s*\n\s*",
        "",
        app,
        count=1,
        flags=re.DOTALL,
    )
    if app.startswith("import "):
        raise RuntimeError("Could not remove app module import")

    crown = data_url(ROOT / "assets" / "rizen-crown.svg")
    index = re.sub(r'\s*<link rel="manifest"[^>]*>\s*', "\n", index)
    index = re.sub(r'<link rel="icon"[^>]*>', f'<link rel="icon" href="{crown}" type="image/svg+xml" />', index)
    index = re.sub(r'<link rel="stylesheet"[^>]*>', f'<style>{css}</style>', index)
    inline_script = f'<script>\n{db}\n\n{app}\n</script>'
    index = re.sub(r'<script type="module"[^>]*></script>', lambda _match: inline_script, index)

    OUTPUT.write_text(index, encoding="utf-8")
    print(f"Built {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
