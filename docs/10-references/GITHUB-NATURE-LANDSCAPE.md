# Nature and GitHub Landscape — Verified Reference Register

**Research date:** 2026-11-08  
**Scope:** selected research and open-source precedents for neural simulation, neural dynamics, scientific visualization and scientific animation. This is a curated shortlist, not a systematic review.

## Nature / Springer Nature

1. **Neural Circuit Visualizer (NCV), Scientific Reports (2026).** A web platform for uploading, visualizing and analyzing large-scale hippocampal circuits and activity; supports CSV/HDF5/SONATA H5, 3D visualization, playback and movie capture. The paper describes integration with remote HPC. DOI: https://doi.org/10.1038/s41598-026-44588-0. Code: https://github.com/cnr-ibf-pa/NeuralCircuitVisualizer.
2. **MARBLE, Nature Methods (2025).** Geometric deep learning for interpretable representations of neural population dynamics, decomposing dynamics into local flow fields and mapping them to a common latent space. DOI: https://doi.org/10.1038/s41592-024-02582-2. Code: https://github.com/Dynamics-of-Neural-Systems-Lab/MARBLE.
3. **Jaxley, Nature Methods (2025).** Differentiable simulation for detailed biophysical neuron models; supports optimization through automatic differentiation and CPU/GPU execution. DOI: https://doi.org/10.1038/s41592-025-02895-w. Code: https://github.com/jaxleyverse/jaxley.
4. **Musical neurodynamics, Nature Reviews Neuroscience (2025).** Review of relationships between neural oscillations and musical structure. Treat as a research review, not a universal mapping from frequency to emotion. DOI: https://doi.org/10.1038/s41583-025-00915-4.
5. **Whole-brain modelling, Nature Reviews Methods Primers (2024).** Methodological context for whole-brain dynamics. DOI: https://doi.org/10.1038/s43586-024-00336-0.

### DOI correction
An earlier draft associated Jaxley with DOI `10.1038/s41592-025-02933-7`, which is a related News & Views item, not the primary Jaxley research article. The primary research article is `10.1038/s41592-025-02895-w`. Keep both references distinct.

## GitHub projects — repository and README inspected

| Project | Verified repository | Capability and potential HAA-D-3 role | License status from inspected root files |
|---|---|---|---|
| Neural Circuit Visualizer | https://github.com/cnr-ibf-pa/NeuralCircuitVisualizer | Django/web workflow, 3D circuit/activity visualization, file import, playback and HPC integration; study data flow and interaction | No common root LICENSE file verified; do not assume reuse permission |
| neuVid | https://github.com/connectome-neuprint/neuVid | JSON-described neuroscience scenes rendered through Blender; useful precedent for declarative scene choreography and camera sequences | Janelia Open Source License; review its exact conditions |
| MARBLE | https://github.com/Dynamics-of-Neural-Systems-Lab/MARBLE | Geometric deep learning for neural population dynamics; possible optional analysis adapter | MIT |
| Jaxley | https://github.com/jaxleyverse/jaxley | Differentiable biophysical neuron simulator using JAX; CPU/GPU/TPU backends | Apache-2.0 |
| Manim Community | https://github.com/ManimCommunity/manim | Programmatic 2D mathematical and explanatory animation | MIT |
| Blender | https://github.com/blender/blender | Full 3D creation pipeline: modeling, rigging, animation, simulation, rendering, compositing and video editing | GPL-3.0; evaluate process boundary and asset/code distribution implications |
| PyVista | https://github.com/pyvista/pyvista | Scientific 3D visualization and mesh analysis on VTK | MIT |
| VTK | https://github.com/Kitware/VTK | Image processing, 3D graphics, volume rendering and scientific visualization algorithms | License not verified in this quick root-file check; review before integration |

## Architectural deductions

1. **Do not make any of these projects the HAA-D-3 core.** Use them behind adapters and stable contracts.
2. **SceneSpec is the interchange layer.** neuVid is a useful precedent for JSON-driven Blender scenes; it should inform our contract, not become the contract itself.
3. **Separate research backends from visual backends.** Jaxley and MARBLE solve different research problems; Blender, Manim, PyVista and VTK solve different presentation problems.
4. **NCV is a workflow reference, not a default embedded dependency.** Its Django, database, three.js and remote-HPC architecture may be useful for studying large-circuit interaction, but it is heavier than the initial offline-first core.
5. **Use Manim for equation-led 2D sequences and Blender for cinematic 3D.** Keep both optional.
6. **Use PyVista/VTK only when scientific geometry, meshes or volume data justify them.**
7. **License review is a release gate.** Public source availability does not grant permission to redistribute code, datasets, figures, fonts, music or video.

## Initial adoption recommendation

- Core: standard-library Python contracts and CLI.
- Research: add Jaxley or MARBLE only for a specific research question and after environment/resource tests.
- Visual explanation: Manim adapter for equations and 2D diagrams.
- Cinema: Blender adapter driven by renderer-independent SceneSpec.
- Scientific geometry: optional PyVista/VTK adapter.
- Web reference: study NCV interaction patterns; implement a smaller portable viewer rather than importing its entire stack.
- Scene choreography: study neuVid's JSON-to-Blender pattern and retain our own versioned contract.

## Unresolved research tasks
- Inspect each repository's current release, maintenance activity, dependencies, security posture and platform support.
- Read and compare full license texts, including Janelia's license.
- Map NCV and neuVid input formats to candidate HAA-D-3 interchange contracts.
- Reproduce selected paper results before treating methods as validated within HAA-D-3.
