"""Deterministic graph validation, SVG projection and provenance receipts."""
from __future__ import annotations
import hashlib, json, math
from typing import Any

MAX_CONCEPTS = 10_000
MAX_RELATIONS = 50_000

def canonical_json(value: dict[str, Any]) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def validate_graph(graph: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(graph, dict):
        return ["graph must be an object"]
    if graph.get("schema_version") != "0.1":
        errors.append("schema_version must be '0.1'")
    concepts, relations = graph.get("concepts"), graph.get("relations")
    if not isinstance(concepts, list):
        errors.append("concepts must be an array"); concepts = []
    if not isinstance(relations, list):
        errors.append("relations must be an array"); relations = []
    if len(concepts) > MAX_CONCEPTS:
        errors.append(f"concept limit exceeded ({MAX_CONCEPTS})")
        return errors
    if len(relations) > MAX_RELATIONS:
        errors.append(f"relation limit exceeded ({MAX_RELATIONS})")
        return errors
    identifiers: set[str] = set()
    for index, node in enumerate(concepts):
        if not isinstance(node, dict):
            errors.append(f"concepts[{index}] must be an object"); continue
        node_id, label = node.get("id"), node.get("label")
        if not isinstance(node_id, str) or not node_id.strip():
            errors.append(f"concepts[{index}].id must be a non-empty string")
        elif node_id in identifiers:
            errors.append(f"duplicate concept id: {node_id}")
        else:
            identifiers.add(node_id)
        if not isinstance(label, str) or not label.strip():
            errors.append(f"concepts[{index}].label must be a non-empty string")
        for axis in ("x", "y", "z"):
            coordinate = node.get(axis)
            if axis in node and (isinstance(coordinate, bool) or not isinstance(coordinate, (int, float)) or not math.isfinite(coordinate)):
                errors.append(f"concepts[{index}].{axis} must be finite numeric")
    for index, edge in enumerate(relations):
        if not isinstance(edge, dict):
            errors.append(f"relations[{index}] must be an object"); continue
        source = edge.get("source")
        target = edge.get("target")
        if not isinstance(source, str) or not source.strip():
            errors.append(f"relations[{index}].source must be a non-empty string")
        elif source not in identifiers:
            errors.append(f"relations[{index}] source is unknown: {source}")
        if not isinstance(target, str) or not target.strip():
            errors.append(f"relations[{index}].target must be a non-empty string")
        elif target not in identifiers:
            errors.append(f"relations[{index}] target is unknown: {target}")
        if not isinstance(edge.get("type"), str) or not edge["type"].strip():
            errors.append(f"relations[{index}].type must be a non-empty string")
    return errors

def _escape(value: Any) -> str:
    text = str(value)
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

def render_svg(graph: dict[str, Any], width: int = 1000, height: int = 600) -> str:
    errors = validate_graph(graph)
    if errors: raise ValueError("; ".join(errors))
    if isinstance(width, bool) or isinstance(height, bool) or not isinstance(width, int) or not isinstance(height, int) or width < 200 or height < 160:
        raise ValueError("width must be >= 200 and height must be >= 160")
    nodes, edges = graph["concepts"], graph["relations"]
    if not nodes:
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><title>{_escape(graph.get("title", "HAA-D-3 graph"))}</title><desc>Empty graph.</desc><rect width="100%" height="100%" fill="#0b1020"/></svg>\n'
    xs = [float(n.get("x", i * 100)) for i, n in enumerate(nodes)]
    ys = [float(n.get("y", i * 60)) for i, n in enumerate(nodes)]
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    pad = 70
    sx = (width - 2 * pad) / max(max_x - min_x, 1.0)
    sy = (height - 2 * pad) / max(max_y - min_y, 1.0)
    pos = {}
    for i, node in enumerate(nodes):
        x, y = float(node.get("x", i * 100)), float(node.get("y", i * 60))
        pos[node["id"]] = (pad + (x - min_x) * sx, pad + (y - min_y) * sy)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">', f'<title>{_escape(graph.get("title", "HAA-D-3 graph"))}</title>', '<desc>Deterministic graph projection from source coordinates and relations.</desc>', '<rect width="100%" height="100%" fill="#0b1020"/>']
    for edge in edges:
        x1, y1 = pos[edge["source"]]; x2, y2 = pos[edge["target"]]
        out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#64748b" stroke-width="2"/>')
        out.append(f'<text x="{(x1+x2)/2:.2f}" y="{(y1+y2)/2-7:.2f}" text-anchor="middle" font-size="11" fill="#cbd5e1">{_escape(edge["type"])}</text>')
    for node in nodes:
        x, y = pos[node["id"]]
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="27" fill="#142a45" stroke="#38bdf8" stroke-width="2"/>')
        out.append(f'<text x="{x:.2f}" y="{y+42:.2f}" text-anchor="middle" font-size="13" fill="#f8fafc">{_escape(node["label"])}</text>')
        if node.get("domain"):
            out.append(f'<text x="{x:.2f}" y="{y-37:.2f}" text-anchor="middle" font-size="10" fill="#94a3b8">{_escape(node["domain"])}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"

def create_receipt(graph: dict[str, Any], svg: str) -> dict[str, Any]:
    errors = validate_graph(graph)
    if errors: raise ValueError("; ".join(errors))
    return {"tool":"haa-d3-knowledge-graph","version":"0.2.0","input_sha256":sha256_hex(canonical_json(graph)),"output_svg_sha256":sha256_hex(svg.encode("utf-8")),"concept_count":len(graph["concepts"]),"relation_count":len(graph["relations"]),"status":"generated","evidence_class":"MODEL_OUTPUT","scientific_validation":"NOT_RUN"}
