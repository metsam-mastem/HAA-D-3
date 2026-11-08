# Initial Nature and GitHub Landscape

**Research date:** 2026-11-08  
**Scope:** selected references for neural simulation, scientific visualization, geometric learning and scientific animation. This is a shortlist, not a systematic review.

## Nature / Springer Nature
1. Neural Circuit Visualizer, Scientific Reports (2026): web platform for simulation and interactive visualization of full-scale point-neuron circuits, with movie recording. DOI: https://doi.org/10.1038/s41598-026-44588-0
2. MARBLE, Nature Methods (2025): geometric deep learning for interpretable representations of neural population dynamics and local flow fields. DOI: https://doi.org/10.1038/s41592-024-02582-2
3. Differentiable simulation for biophysical neural models, Nature Methods (2025): Jaxley and differentiable GPU-accelerated neural simulation. DOI: https://doi.org/10.1038/s41592-025-02933-7
4. Musical neurodynamics, Nature Reviews Neuroscience (2025): reviews links between neural oscillations and musical structure. Record theoretical debate and counterpoints. DOI: https://doi.org/10.1038/s41583-025-00915-4
5. Whole-brain modelling, Nature Reviews Methods Primers (2024): methodological context for whole-brain dynamics. DOI: https://doi.org/10.1038/s43586-024-00336-0

## GitHub / open source
| Project | Capability | Potential role |
|---|---|---|
| NeuralCircuitVisualizer | Web neural circuit visualization | Study UI, data flow and visualization |
| neuVid | JSON-driven Blender neuroscience animation | Scene-spec and render precedent |
| MARBLE | Geometric learning for neural dynamics | Optional research method |
| Jaxley | Differentiable biophysical neuron simulation | Optional simulation backend |
| Manim Community | Programmatic mathematical animation | Equation-led explainers |
| Blender | 3D modeling, animation and rendering | Cinematic production backend |
| PyVista / VTK | Scientific 3D visualization | Volumes and meshes |

A reference is not automatically a dependency. Reuse requires license review, version pinning, dependency isolation, compatibility tests and attribution. Prefer learning from architectural patterns over copying large subsystems.

## Initial recommendation
Use a renderer-independent SceneSpec. Keep simulation in Python adapters, use Blender for cinema and browser SVG/Canvas for fast review. Adopt a heavier backend only when the research question requires it.
