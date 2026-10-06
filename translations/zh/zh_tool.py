"""Maintain the Chinese markdown cells that sit below each English markdown cell.

    python translations/zh/zh_tool.py dump    <notebook.ipynb>
    python translations/zh/zh_tool.py extract <notebook.ipynb> <translation.txt>
    python translations/zh/zh_tool.py apply   <notebook.ipynb> <translation.txt>

dump     prints the English markdown cells, one block per cell id.
extract  writes the notebook's existing Chinese cells to a translation file.
apply    inserts a Chinese cell (id "<english id>-zh") below each English cell.
         Cells that already have a Chinese cell are left alone, so it is safe
         to re-run after taking the upstream version of a notebook.

Translation file format, one block per English cell id:

    =====<cell id>
    <chinese markdown>
"""
import json
import re
import sys
from pathlib import Path

SUFFIX = "-zh"


def dump_json(nb):
    return json.dumps(nb, indent=1, ensure_ascii=False) + "\n"


def load(path):
    raw = path.read_text(encoding="utf-8")
    nb = json.loads(raw)
    assert dump_json(nb) == raw, f"{path.name}: serializer does not round-trip"
    return nb


def english_markdown(nb):
    return [
        c for c in nb["cells"]
        if c["cell_type"] == "markdown" and not c["id"].endswith(SUFFIX) and "".join(c["source"]).strip()
    ]


def read_translations(path):
    parts = re.split(r"^=====(\S+)[ \t]*\n", path.read_text(encoding="utf-8"), flags=re.M)
    assert parts[0].strip() == "", "text before first delimiter"
    zh = {parts[i]: parts[i + 1].strip("\n") for i in range(1, len(parts), 2)}
    assert len(zh) == (len(parts) - 1) // 2, "duplicate id in translation file"
    return zh


def cmd_dump(nb_path):
    for c in english_markdown(load(nb_path)):
        print(f"====={c['id']}")
        print("".join(c["source"]))


def cmd_extract(nb_path, zh_path):
    nb = load(nb_path)
    blocks = [
        f"====={c['id'][: -len(SUFFIX)]}\n{''.join(c['source'])}\n"
        for c in nb["cells"]
        if c["cell_type"] == "markdown" and c["id"].endswith(SUFFIX)
    ]
    zh_path.parent.mkdir(parents=True, exist_ok=True)
    zh_path.write_text("".join(blocks), encoding="utf-8")
    print(f"{zh_path}: {len(blocks)} blocks")


def cmd_apply(nb_path, zh_path):
    nb = load(nb_path)
    zh = read_translations(zh_path)
    ids = [c["id"] for c in english_markdown(nb)]
    missing, stale = set(ids) - set(zh), set(zh) - set(ids)
    if missing:
        print(f"  untranslated cells (new or changed upstream): {sorted(missing)}")
    if stale:
        print(f"  translations with no matching cell (removed upstream): {sorted(stale)}")
    existing = {c["id"] for c in nb["cells"]}
    out, added = [], 0
    for c in nb["cells"]:
        out.append(c)
        if c["cell_type"] == "markdown" and c["id"] in zh and c["id"] + SUFFIX not in existing:
            lines = zh[c["id"]].split("\n")
            source = [line + "\n" for line in lines[:-1]] + [lines[-1]]
            out.append({"cell_type": "markdown", "id": c["id"] + SUFFIX, "metadata": {}, "source": source})
            added += 1
    assert len({c["id"] for c in out}) == len(out), "duplicate cell ids"
    nb["cells"] = out
    nb_path.write_text(dump_json(nb), encoding="utf-8")
    print(f"{nb_path.name}: +{added} zh cells, total {len(out)}")


if __name__ == "__main__":
    command, args = sys.argv[1], [Path(a) for a in sys.argv[2:]]
    {"dump": cmd_dump, "extract": cmd_extract, "apply": cmd_apply}[command](*args)
