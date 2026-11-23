"""Public tests for Lab 10. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab10 as lab  # noqa: E402

def test_returns_probabilities():
    a, b = lab.em_two_coins([2, 8], 10, 0.4, 0.6, iters=3)
    assert 0 <= a <= 1 and 0 <= b <= 1
