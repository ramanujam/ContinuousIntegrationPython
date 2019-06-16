"""
Unit tests for the calculator library
"""

import temperature


class TestTemperature:

    def test_c2f(self):
        assert -40 == temperature.c2f(-40)

    def test_f2c(self):
        assert 0 == temperature.f2c(32)