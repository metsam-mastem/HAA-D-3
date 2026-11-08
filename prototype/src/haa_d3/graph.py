"""Standard-library graph validation, SVG projection, and provenance receipt."""
from __future__ import annotations
import hashlib, json, math
from typing import Any

def canonical_json(graph: dict[str, Any]) -> bytes:
    return json.dumps(graph, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def validate_graph(graph: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if graph.get("schema_version") != "0.1":
        errors.append("schema_version must be '0.1'")
    concepts, relations = graph.get("concepts"), graph.get("relations")
    if not isinstance(concepts, list):
        errors.append("concepts must be a list"); concepts = []
    if not isinstance(relations, list):
        errors.append("relations must be a list"); relations = []
    ids: set[str] = set()
    for i, node in enumerate(concepts):
        if not isinstance(node, dict):
            errors.append(f"concept[{i}] must be an object"); continue
        nid, label = node.get("id"), node.get("label")
        if not isinstance(nid, str) or not nid.strip():
            errors.append(f"concept[{i}].id must be non-empty")
        elif nid in ids:
            errors.append(f"duplicate concept id: {nid}")
        else:
            ids.add(nid)
        if not isinstance(label, str) or not label.strip():
            errors.append(f"concept[{i}].label must be non-empty")
        for axis in ("x", "y", "z"):
            if axis in node and (not isinstance(node[axis], (int, float)) or not math.isfinite(node[axis])):
                errors.append(f"concept[{i}].{axis} must be finite numeric")
    for i, edge in enumerate(relations):
        if not isinstance(edge, dict):
            errors.append(f"relation[{i}] must be an object"); continue
        if edge.get("source") not in ids: errors.append(f"relation[{i}] source unknown: {edge.get('source')}")
        if edge.get("target") not in ids: errors.append(f"relation[{i}] target unknown: {edge.get('target')}")
        if not isinstance(edge.get("type"), str) or not edge["type"].strip():
            errors.append(f"relation[{i}].type must be non-empty")
    return errors

def _esc(s: str) -> str:
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;").replace("'","&apos;")

def render_svg(graph: dict[str, Any], width: int = 1000, height: int = 600) -> str:
    errors = validate_graph(graph)
    if errors: raise ValueError("; ".join(errors))
    nodes, edges = graph["concepts"], graph["relations"]
    xs = [float(n.get("x", i*100)) for i,n in enumerate(nodes)]
    ys = [float(n.get("y", i*60)) for i,n in enumerate(nodes)]
    min_x,max_x=min(xs,default=0),max(xs,default=1)
    min_y,max_y=min(ys,default=0),max(ys,default=1)
    pad=70; sx=(width-2*pad)/max(max_x-min_x,1); sy=(height-2*pad)/max(max_y-min_y,1)
    pos={}
    for i,n in enumerate(nodes):
        x=float(n.get("x",i*100)); y=float(n.get("y",i*60))
        pos[n["id"]]=(pad+(x-min_x)*sx,pad+(y-min_y)*sy)
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}>',
         f'<title>{_esc(graph.get("title","HAA-D-3 graph"))}</title>',
         '<desc>Graph projection based only on the source JSON coordinates and relations.</desc>',
         '<rect width="100%" height="100%" fill="#0b1020"/>']
    for e in edges:
        x1,y1=pos[e["source"]]; x2,y2=pos[e["target"]]
        out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#64748b" stroke-width="2"/>')
        out.append(f'<text x="{(x1+x2)/2:.2f}" y="{(y1+y2)/2-7:.2f}" text-anchor="middle" font-size="11" fill="#cbd5e1">{_esc(e["type"])}</text>')
    for n in nodes:
        x,y=pos[n["id"]]
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="27" fill="#142a45" stroke="#38bdf8" stroke-width="2"/>')
        out.append(f'<text x="{x:.2f}" y="{y+42:.2f}" text-anchor="middle" font-size="13" fill="#f8fafc">{_esc(n["label"])}</text>')
        if n.get("domain"):
            out.append(f'<text x="{x:.2f}" y="{y-37:.2f}" text-anchor="middle" font-size="10" fill="#94a3b8">{_esc(str(n["domain"]))}</text>')
    out.append("</svg>")
    return "\n".join(out)+"\n"

def create_receipt(graph: dict[str, Any], svg: str) -> dict[str, Any]:
    return {"tool":"haa-d3-knowledge-graph","version":"0.1.0",
            "input_sha256":sha256_hex(canonical_json(graph)),
            "output_svg_sha256":sha256_hex(svg.encode("utf-8")),
            "concept_count":len(graph.get("concepts",[])),
            "relation_count":len(graph.get("relations",[])),
            "status":"generated"}
