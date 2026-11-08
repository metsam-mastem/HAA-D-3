"""Independent numerical checks for the Kuramoto mean-field implementation.

The reference integrator deliberately uses the O(N^2) pairwise equation rather
than the production O(N) mean-field identity.
"""
import math
import random
import unittest

from haa_d3.kuramoto import TAU, simulate_kuramoto


def pairwise_reference(nodes, coupling, dt, steps, seed, omega_mean=1.0, omega_std=0.25):
    rng = random.Random(seed)
    phases = [rng.uniform(-math.pi, math.pi) for _ in range(nodes)]
    frequencies = [rng.gauss(omega_mean, omega_std) for _ in range(nodes)]
    snapshots = [list(phases)]

    def derivative(state):
        return [
            frequencies[i] + coupling / nodes * sum(
                math.sin(state[j] - state[i]) for j in range(nodes)
            )
            for i in range(nodes)
        ]

    for _ in range(steps):
        k1 = derivative(phases)
        predictor = [(phase + dt * slope) % TAU for phase, slope in zip(phases, k1)]
        k2 = derivative(predictor)
        phases = [
            (phase + 0.5 * dt * (a + b)) % TAU
            for phase, a, b in zip(phases, k1, k2)
        ]
        snapshots.append(list(phases))
    return snapshots


def circular_error(left, right):
    return max(
        abs(math.atan2(math.sin(a - b), math.cos(a - b)))
        for a, b in zip(left, right)
    )


class KuramotoIndependentValidationTests(unittest.TestCase):
    def test_mean_field_implementation_matches_independent_pairwise_reference(self):
        config = dict(nodes=7, coupling=1.3, dt=0.01, steps=25, seed=23)
        actual = simulate_kuramoto(**config)["samples"]
        expected = pairwise_reference(**config)
        self.assertEqual(len(actual), len(expected))
        for index, sample in enumerate(actual):
            self.assertLess(
                circular_error(sample["phases_radians"], expected[index]),
                2e-10,
                msg=f"phase mismatch at step {index}",
            )

    def test_zero_coupling_matches_analytical_free_rotation(self):
        config = dict(nodes=9, coupling=0.0, dt=0.037, steps=31, seed=41)
        rng = random.Random(config["seed"])
        initial = [rng.uniform(-math.pi, math.pi) for _ in range(config["nodes"])]
        frequencies = [rng.gauss(1.0, 0.25) for _ in range(config["nodes"])]
        samples = simulate_kuramoto(**config)["samples"]
        for sample in samples:
            time = sample["time_seconds"]
            analytical = [
                (phase + omega * time) % TAU
                for phase, omega in zip(initial, frequencies)
            ]
            self.assertLess(circular_error(sample["phases_radians"], analytical), 2e-11)

    def test_heun_global_error_reduces_at_second_order_rate(self):
        nodes, coupling, seed, duration = 6, 1.7, 31, 1.0
        reference = pairwise_reference(
            nodes, coupling, 0.0005, 2000, seed
        )[-1]
        errors = []
        for dt in (0.1, 0.05, 0.025):
            steps = round(duration / dt)
            phases = simulate_kuramoto(
                nodes=nodes, coupling=coupling, dt=dt, steps=steps, seed=seed
            )["samples"][-1]["phases_radians"]
            errors.append(circular_error(phases, reference))
        self.assertLess(errors[1], errors[0] / 3.2)
        self.assertLess(errors[2], errors[1] / 3.2)
        self.assertGreater(errors[0] / errors[1], 3.2)
        self.assertGreater(errors[1] / errors[2], 3.2)


    def test_rejects_simulation_exceeding_snapshot_budget(self):
        with self.assertRaisesRegex(ValueError, "snapshot budget"):
            simulate_kuramoto(nodes=1000, steps=1000)

    def test_rejects_excessive_node_count(self):
        with self.assertRaisesRegex(ValueError, "nodes must be <="):
            simulate_kuramoto(nodes=10001, steps=1)


if __name__ == "__main__":
    unittest.main()
