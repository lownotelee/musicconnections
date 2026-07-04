#!/usr/bin/env python3
"""
Validate data.json against the schema, plus cross-checks a JSON Schema can't express.
Run locally before opening a PR:  python scripts/validate.py
Exits non-zero (fails CI) if anything is wrong.
"""
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft7Validator
except ImportError:
    sys.exit("Missing dependency. Run:  pip install jsonschema")

ROOT = Path(__file__).resolve().parent.parent
schema = json.loads((ROOT / "schema" / "data.schema.json").read_text())
data = json.loads((ROOT / "data.json").read_text())

errors = []

# 1. Structural validation against the schema (types, enums, required fields,
#    the "source must be a credit not a streaming link" rule, unknown fields).
for e in sorted(Draft7Validator(schema).iter_errors(data), key=lambda e: list(e.path)):
    loc = "/".join(str(p) for p in e.path) or "(root)"
    errors.append(f"schema · {loc}: {e.message}")

artists = data.get("artists", [])
conns = data.get("connections", [])
ids = [a.get("id") for a in artists]
idset = set(ids)

# 2. Artist ids must be unique — a duplicate id silently merges two artists.
for dup in sorted({i for i in ids if ids.count(i) > 1 and i}):
    errors.append(f"artists · duplicate id '{dup}'")

# 3. Referential integrity — every connection must point at artists that exist.
#    (A typo'd id is the single most common way an open dataset breaks.)
for i, c in enumerate(conns):
    for end in ("from", "to"):
        ref = c.get(end)
        if ref and ref not in idset:
            errors.append(f"connections[{i}] · '{end}' points to unknown artist id '{ref}'")

# 4. No exact-duplicate connections.
seen = {}
for i, c in enumerate(conns):
    key = (c.get("from"), c.get("to"), c.get("rel"), c.get("song"))
    if key in seen:
        errors.append(f"connections[{i}] · duplicate of connections[{seen[key]}]")
    else:
        seen[key] = i

if errors:
    print(f"\u274c  {len(errors)} problem(s) found:\n")
    for e in errors:
        print("   -", e)
    sys.exit(1)

print(f"\u2705  data.json is valid \u2014 {len(artists)} artists, {len(conns)} connections.")
