"""Test MultifractionalBrownianMotion."""
# flake8: noqa
import pytest

from stochastic.continuous import MultifractionalBrownianMotion


def test_multifractional_brownian_motion_str_repr(hurst_func, t):
    instance = MultifractionalBrownianMotion(hurst_func, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_multifractional_brownian_motion_sample(hurst_func, t, n, zero):
    instance = MultifractionalBrownianMotion(hurst_func, t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)

def test_multifractional_brownian_motion_invalid_hurst(hurst_invalid, t):
    with pytest.raises(ValueError):
        instance = MultifractionalBrownianMotion(hurst_invalid, t)
        s = instance.sample(16)
