import unittest
import numpy as np
from statsmodels.tsa.arima_process import ArmaProcess
from simulation import theoretical, from_innovations, simulate, sample_acf


class ARMATests(unittest.TestCase):
    def test_manual_recurrence(self):
        actual = from_innovations([1, 2, 3, 4], c=2, phi=.5, theta=.25, initial=0)
        np.testing.assert_allclose(actual, [4.25, 7.625, 10.5625])

    def test_theory_against_independent_library(self):
        for phi, theta in [(.95, .25), (.3, -.4), (-.4, .6)]:
            result = theoretical(phi=phi, theta=theta)
            reference = ArmaProcess(np.array([1, -phi]), np.array([1, theta]))
            np.testing.assert_allclose(result['acf'], reference.acf(lags=21), atol=1e-12)
            self.assertAlmostEqual(result['variance'], reference.acovf(nobs=1)[0])

    def test_white_noise_theory(self):
        out = theoretical(c=0, phi=0, theta=0, innovation_variance=2)
        self.assertEqual(out['mean'], 0); self.assertEqual(out['variance'], 2)
        np.testing.assert_array_equal(out['acf'][1:], 0)

    def test_seed_and_sample_length(self):
        a = simulate(n=100, burn=50); b = simulate(n=100, burn=50)
        self.assertEqual(a.shape, (100,)); np.testing.assert_array_equal(a, b)

    def test_infinite_variance_setting_rejected(self):
        with self.assertRaises(ValueError): simulate(nu=2)

    def test_nonstationary_setting_rejected(self):
        with self.assertRaises(ValueError): simulate(phi=1)

    def test_acf_normalization(self):
        self.assertAlmostEqual(sample_acf(np.arange(30.), 10)[0], 1)

    def test_constant_acf_rejected(self):
        with self.assertRaises(ValueError): sample_acf(np.ones(40), 10)


if __name__ == '__main__': unittest.main()
