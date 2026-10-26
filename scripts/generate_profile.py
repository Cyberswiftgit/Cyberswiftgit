
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "assets" / "skills.json"
OUTPUT = ROOT / "assets" / "skills.svg"

def main():
    skills = json.loads(CONFIG.read_text(encoding="utf-8"))

    # This first version validates your skill data.
    # The SVG radar can then be updated from the same configuration.
    for name, score in skills.items():
        if not isinstance(score, int) or not 0 <= score <= 100:
            raise ValueError(f"{name}: score must be an integer from 0 to 100")

    print(f"Validated {len(skills)} skill ratings.")
    print("Edit assets/skills.svg to change the visual until SVG rendering is added.")

if __name__ == "__main__":
    main()

