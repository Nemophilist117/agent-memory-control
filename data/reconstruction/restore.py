"""Restore omitted benchmark rows locally from the pinned LongMemEval oracle file."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "data"
ORACLE_SHA256 = "821a2034d219ab45846873dd14c14f12cfe7776e73527a483f9dac095d38620c"


def serialize(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("oracle", type=Path)
    parser.add_argument("output", type=Path, help="New directory for restored rows")
    args = parser.parse_args()
    raw = args.oracle.read_bytes()
    if hashlib.sha256(raw).hexdigest() != ORACLE_SHA256:
        parser.error("Upstream file hash does not match the pinned oracle.")
    records = {row["question_id"]: row for row in json.loads(raw)}
    recipes = (ROOT / "reconstruction" / "recipes.jsonl").read_text(encoding="utf-8")
    outputs = {}
    for line in recipes.splitlines():
        recipe = json.loads(line)
        source = serialize(records[recipe["original_record_id"]])
        for name, spec in recipe["rows"].items():
            pieces = spec["pieces"]
            value = "".join(p if isinstance(p, str) else source[p[0]:p[1]] for p in pieces)
            if hashlib.sha256(value.encode()).hexdigest() != spec["sha256"]:
                raise ValueError(f"Restoration mismatch in {recipe['scenario_id']}, {name}")
            json.loads(value)
            outputs.setdefault(name, []).append(value)
    args.output.mkdir(parents=True, exist_ok=False)
    for name, lines in outputs.items():
        (args.output / (name + ".jsonl")).write_bytes(("\n".join(lines) + "\n").encode())


if __name__ == "__main__":
    main()
