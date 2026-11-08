# Vertical Slice 02 — Coupled Oscillators

**Status:** Implemented numerical prototype; independent external scientific review pending.  
**Model:** Kuramoto mean-field coupled-oscillator system.  
**Evidence class:** MODEL_OUTPUT.  
**Scope warning:** Generic mathematical oscillator model; not a biological brain or neural-circuit model.

## Objective
Provide a reproducible path from mathematical specification to simulation data and a renderer-independent analytical SceneSpec, with numerical checks against independent formulations and analytical special cases.

## Equation
For oscillator i:

`dθᵢ/dt = ωᵢ + (K/N) Σⱼ sin(θⱼ − θᵢ)`

- θᵢ: phase in radians.
- ωᵢ: intrinsic angular frequency in radians/second.
- K: coupling parameter in inverse seconds under this parameterization.
- N: oscillator count.
- t: seconds.

The production implementation uses the mean-field identity for O(N) work per step. The independent test reference evaluates the pairwise sum directly in O(N²), avoiding reuse of the optimized coupling expression.

## Numerical method
Heun's method (explicit second-order Runge–Kutta), fixed time step dt. Phases are wrapped to [0, 2π). A seeded pseudorandom generator initializes phases and normally distributed intrinsic frequencies.

## Configuration and outputs
Nodes, coupling K, dt, number of steps, seed, frequency mean and frequency standard deviation are explicit parameters. Each sample contains step, time_seconds, order_parameter r(t), and oscillator phases in radians. The order parameter is the magnitude of the mean complex phase vector and lies in [0,1] up to floating-point tolerance.

## Run
`PYTHONPATH=src python -m haa_d3.cli simulate-kuramoto --nodes 64 --coupling 1.5 --dt 0.02 --steps 500 --seed 7 --output artifacts/kuramoto-demo.json`

## Numerical verification contract
The repository test suite now includes `tests/test_kuramoto_validation.py`:

1. **Independent formulation:** compare the O(N) mean-field implementation against a separately coded O(N²) pairwise Heun solver; 7 oscillators, K=1.3, dt=0.01, 25 steps, seed 23; maximum circular phase error must remain below 2e-10 radians.
2. **Analytical special case:** with K=0, compare every phase sample against `θᵢ(t) = (θᵢ(0) + ωᵢt) mod 2π`; 9 oscillators, dt=0.037, 31 steps, seed 41; maximum circular error below 2e-11 radians.
3. **Convergence:** compare dt=0.1, 0.05 and 0.025 against a pairwise reference at dt=0.0005 over one second; each halving must reduce the global phase error by at least 3.2×, consistent with second-order Heun convergence.
4. Existing tests cover deterministic seeded output, order-parameter bounds, invalid input rejection, sample count and SceneSpec provenance.

These are reproducible numerical software checks. They do not constitute peer review, empirical validation, comparison with published experimental data, or validation of a biological model. CI status is authoritative for whether these tests have passed on a commit.

## Research-to-scene bridge — implemented
The `kuramoto-scene` CLI maps each phase to a 2D position using x=R*cos(theta), y=R*sin(theta), and maps r(t) to a global coherence indicator. The mapping records its formula, source model, parameters and MODEL_OUTPUT evidence class in SceneSpec metadata/data bindings. Music synchronization remains an artistic mapping unless a separate scientific hypothesis is defined.

## Non-goals
No claim about consciousness, intelligence, cognition, brain-wide synchronization or therapeutic effects. No biological data are used.
