"""Provider-neutral capability descriptors and deterministic adapter selection."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AdapterDescriptor:
    adapter_id: str
    version: str
    provides: tuple[str, ...]
    platforms: tuple[str, ...] = ("any",)
    offline: bool = False
    requires_gpu: bool = False
    license_id: str = "UNSPECIFIED"
    maturity: str = "experimental"


@dataclass(frozen=True)
class RuntimeProfile:
    platform: str
    offline_required: bool = False
    gpu_available: bool = False


def select_adapters(
    adapters: Iterable[AdapterDescriptor],
    required_capability: str,
    runtime: RuntimeProfile,
) -> list[AdapterDescriptor]:
    """Return compatible adapters without preferring a vendor or model brand.

    Results are sorted by adapter_id for deterministic behavior. Maturity and
    licensing are exposed to callers; this function does not silently approve
    licenses or treat experimental adapters as production-ready.
    """
    matches = []
    for adapter in adapters:
        if required_capability not in adapter.provides:
            continue
        if "any" not in adapter.platforms and runtime.platform not in adapter.platforms:
            continue
        if runtime.offline_required and not adapter.offline:
            continue
        if adapter.requires_gpu and not runtime.gpu_available:
            continue
        matches.append(adapter)
    return sorted(matches, key=lambda item: item.adapter_id)
