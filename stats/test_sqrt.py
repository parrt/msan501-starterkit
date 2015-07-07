from sqrt import *
import numpy as np
import math


def check(n):
    assert np.isclose(sqrt(n), math.sqrt(n))


def test_sqrt():
    check(125348)
    check(100)
    check(1)
    check(0)
