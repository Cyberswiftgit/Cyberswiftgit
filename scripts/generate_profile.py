
from pathlib import Path
import json
import math
import html

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "assets" / "profile.json"
OUTPUT = ROOT / "assets" / "skills.svg"

WIDTH, HEIGHT = 600, 360
CENTER_X, CENTER_Y = 300, 190
RADIUS = 100

def point(index, radius, count):
    angle = -math.pi / 2 + (2 * math.pi * index / count)
    return (
        CENTER_X + radius * math.cos(angle),
        CENTER_Y + radius * math.sin(angle)
    )

def polygon(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)

def generate():
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    skills = data["skills"]

    if len(skills) < 3:
        raise ValueError("Add at least three skills.")

    for skill in skills:
        if not isinstance(skill["level"], int) or not 0 <= skill["level"] <= 100:
            raise ValueError(f"Invalid level for {skill['name']}")

    count = len(skills)
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        '<rect width="100%" height="100%" rx="14" fill="#0b1220"/>',
        '<text x="300" y="28" fill="#e5f7ff" font-family="monospace" font-size="16" text-anchor="middle">SKILL RADAR</text>'
    ]

    for fraction in (0.25, 0.5, 0.75, 1):
        points = [point(i, RADIUS * fraction, count) for i in range(count)]
        svg.append(
            f'<polygon points="{polygon(points)}" fill="none" stroke="#284052"/>'
        )

    values = [
        point(i, RADIUS * skill["level"] / 100, count)
        for i, skill in enumerate(skills)
    ]

    svg.append(
        f'<polygon points="{polygon(values)}" fill="#00ffc8" '
        'fill-opacity="0.18" stroke="#00ffc8" stroke-width="2"/>'
    )

    for i, skill in enumerate(skills):
        x, y = point(i, RADIUS + 25, count)
        name = html.escape(skill["name"])
        svg.append(
            f'<text x="{x:.1f}" y="{y:.1f}" fill="#d8e8f0" '
            f'font-family="monospace" font-size="12" text-anchor="middle">'
            f'{name}</text>'
        )

    svg.extend([
        '<text x="300" y="340" fill="#7e9baa" font-family="monospace" font-size="11" text-anchor="middle">Self-reported learning ratings, not proficiency tests</text>',
        '</svg>'
    ])

    OUTPUT.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated {OUTPUT.name} from {len(skills)} skills.")

if __name__ == "__main__":
    generate()
