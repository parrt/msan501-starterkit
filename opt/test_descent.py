from descent import minimize
import numpy as np
import sys

LEARNING_RATE = 2.0
h = 0.00001
PRECISION = 0.00000001  # can't be too small as f(x)-f(xprev) prec is low


def cosf(x): return np.cos(3 * np.pi * x) / x


def x2(x): return (x - 2) ** 2 + 1


def x3(x): return 5 * x ** 3 + 2 * x ** 2 - 3 * x

def check(f, x0, minx):
    tracex = minimize(f, x0, LEARNING_RATE, h, PRECISION)

    start = tracex[0]
    stop = tracex[-1]

    assert round(stop*1000) == round(minx*1000)

def test_1(): check(cosf, 0.1, 0.29691298)
def test_2(): check(cosf, 0.8, 0.98865134)
def test_3(): check(cosf, 0.3, 0.29691298)
def test_4(): check(cosf, 1.2, 0.98865134)
def test_5(): check(cosf, 0.05, 0.29691298)

def test_6(): check(x2, 2.0, 2.0)
def test_7(): check(x2, -1.0, 2.0)
def test_8(): check(x2, -9.3, 2.0)

def test_9(): check(x3, 2.0, 1 / 3.0)
def test_10(): check(x3, 0.5, 1 / 3.0)
def test_11(): check(x3, 1 / 3.0, 1 / 3.0)
def test_12(): check(x3, 1.0, 1 / 3.0)
