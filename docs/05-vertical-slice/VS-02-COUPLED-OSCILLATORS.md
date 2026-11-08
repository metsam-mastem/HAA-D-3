# Vertical Slice 02 — Coupled Oscillators

**Status:** Implemented research prototype; independent scientific review pending.  
**Model:** Kuramoto mean-field coupled-oscillator system.  
**Evidence class:** MODEL_OUTPUT.  
**Scope warning:** This is a generic mathematical oscillator model, not a biological brain or neural-circuit model.

## Objective
Demonstrate a reproducible path from mathematical specification to simulation data and an explicit renderer-independent analytical SceneSpec.

## Equation
For oscillator i:

`dθᵢ/dt = ωᵢ + (K/N) Σⱼ sin(θⱼ − θᵢ)`

- θᵢ: phase in radians.
- ωᵢ: intrinsic angular frequency in radians/second.
- K: coupling parameter in inverse seconds under this parameterization.
- N: oscillator count.
- t: seconds.

The implementation uses the mean-field identity to evaluate the coupling term in O(N) per step instead of explicitly summing all N² pairs.

## Numerical method
Heun's method (explicit second-order Runge–Kutta), with fixed time step dt. Phases are wrapped to [0, 2π). A seeded pseudorandom generator initializes phases and normally distributed intrinsic frequencies.

## Configuration
Nodes, coupling K, dt, number of steps, seed, frequency mean and frequency standard deviation are explicit parameters. The same configuration and Python runtime produce deterministic output.

## Outputs
Each sample includes step, time_seconds, order_parameter r(t), and oscillator phases in radians. The order parameter is the magnitude of the mean complex phase vector and lies in [0,1] up to floating-point tolerance.

## Run
`PYTHONPATH=src python -m haa_d3.cli simulate-kuramoto --nodes 64 --coupling 1.5 --dt 0.02 --steps 500 --seed 7 --output artifacts/kuramoto-demo.json`

## Validation plan
- Deterministic output for fixed seed/configuration.
- Order parameter bounded in [0,1] within numerical tolerance.
- Invalid node counts, steps, dt and frequency spread rejected.
- K=0 case evolves at intrinsic frequencies without coupling.
- Time grid has exactly steps + 1 samples.
- Future work: convergence/time-step sensitivity, comparison with analytical special cases and published benchmark curves.

## Research-to-scene bridge — implemented
The `kuramoto-scene` CLI maps each phase to a 2D position using x=R*cos(theta), y=R*sin(theta), and maps r(t) to a global coherence indicator. The mapping records its formula, source model, parameters and MODEL_OUTPUT evidence class in SceneSpec metadata/data bindings. Music synchronization remains an artistic mapping unless a separate scientific hypothesis is defined.

## Non-goals
No claim about consciousness, intelligence, cognition, brain-wide synchronization or therapeutic effects. No biological data are used.
