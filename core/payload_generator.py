import json
from pathlib import Path

def load_payloads():
    path = Path(__file__).parent.parent / "attacks" / "payloads.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    all_payloads = []
    for category, payloads in data.items():
        for p in payloads:
            all_payloads.append({"category": category, "payload": p})
    return all_payloads