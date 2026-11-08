# Resource & Benchmark Plan
**Status:** plan; measurements NOT RUN.

## Metrics
Quality: task accuracy/F1/MAE as appropriate; uncertainty calibration; evidence coverage; unsupported claim rate.
Performance: wall-clock, throughput, batch, per-item latency, cold/warm start.
Memory: peak RSS/VRAM, weights, activations, optimizer state, cache, disk.
Efficiency: quality/sec, quality/GB, energy if measured, cost/run.
Engineering: dependencies, install effort, failure rate, reproducibility.
Visualization: render time, graph size, label overlap, SVG bytes/readability.

## Graph slice baseline
Synthetic fixtures of 10, 50, 100, 500 nodes; measure runtime, RSS where possible, artifact size, and tests. No results declared before execution.

## Neural experiment
Choose task first; choose MLP/GRU/GNN baseline accordingly. Add one component at a time; same data split, seeds, training budget, device and metric. Repeat seeds and report uncertainty where feasible.

## Resource accounting
Weights lower bound = parameter count × bytes/parameter. Include training optimizer/activations; inference KV cache; sparse indices/overhead. Record hardware, OS, runtime versions, precision, batch, sequence, dataset, wall time, peak memory and energy if instrumented. Distinguish estimates from measured peak.

## Dataset governance
Use lawful/public or user-authorized data; document license, consent/privacy, splits, duplicates. Group related samples to prevent leakage. Never commit private samples.

## Ablation matrix
A0 baseline; A1 + spatial representation; A2 + feedback; A3 + denoising/filter; A4 + modular routing; A5 combined only if isolated effects justify. Record harms/instability as well as gains.

## Run receipt
Config hash, commit, model/version, split, seed, metrics, resource measurements, logs, artifacts, status PASS/FAIL/NOT RUN/BLOCKED.