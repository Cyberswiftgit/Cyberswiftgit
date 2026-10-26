
from pathlib import Path
import json
import html

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "assets" / "profile.json"
OUTPUT = ROOT / "assets" / "projects.svg"

def main():
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    projects = data.get("projects", [])

    if not projects:
        raise ValueError("Add at least one project to profile.json")

    cards = []
    for project in projects:
        name = html.escape(project["name"])
        description = html.escape(project["description"])
        status = html.escape(project.get("status", "In progress"))

        cards.append((name, description, status))

    width = 900
    card_height = 112
    height = 58 + len(cards) * (card_height + 12) + 12

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" rx="16" fill="#0b1220"/>',
        '<text x="28" y="36" fill="#00ffc8" font-family="monospace" font-size="20">SELECTED PROJECTS</text>'
    ]

    for i, (name, description, status) in enumerate(cards):
        y = 58 + i * (card_height + 12)
        svg.extend([
            f'<rect x="20" y="{y}" width="860" height="{card_height}" rx="10" fill="#111c2b" stroke="#284052"/>',
            f'<text x="40" y="{y + 30}" fill="#e5f7ff" font-family="sans-serif" font-size="18" font-weight="bold">{name}</text>',
            f'<text x="40" y="{y + 55}" fill="#a9bdcc" font-family="sans-serif" font-size="13">{description[:100]}</text>',
            f'<text x="40" y="{y + 84}" fill="#00ffc8" font-family="monospace" font-size="12">STATUS: {status}</text>'
        ])

    svg.append("</svg>")
    OUTPUT.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated project cards for {len(cards)} projects.")

if __name__ == "__main__":
    main()
