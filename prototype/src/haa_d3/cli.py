from __future__ import annotations
import argparse, json
from pathlib import Path
from .graph import validate_graph, render_svg, create_receipt

def main() -> int:
    parser=argparse.ArgumentParser(description="Validate and render HAA-D-3 graph.")
    parser.add_argument("input",type=Path); parser.add_argument("--out",type=Path,default=Path("out"))
    args=parser.parse_args()
    try: graph=json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc: parser.error(f"cannot read graph JSON: {exc}")
    errors=validate_graph(graph)
    if errors:
        print(json.dumps({"status":"invalid","errors":errors},ensure_ascii=False,indent=2)); return 2
    svg=render_svg(graph); receipt=create_receipt(graph,svg)
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/"graph.json").write_text(json.dumps(graph,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (args.out/"graph.svg").write_text(svg,encoding="utf-8")
    (args.out/"receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"generated","out":str(args.out),"receipt":receipt},ensure_ascii=False,indent=2))
    return 0

if __name__=="__main__": raise SystemExit(main())
