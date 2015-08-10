from stats import *
from sqrt import *
import numpy as np
import math

seed_666 = [0.00521236192678, 0.604166903349, 0.233144581892,
            0.460987861017, 0.822980116505, 0.826818094508,
            0.331714398848, 0.1239014343, 0.411406287184,
            0.505468696591]

seed_235423 = [0.8425073301617556, 0.02069802862624546, 0.8717671213074434]

# Alabama, Alaska, ..., Wyoming alchohol consumption
beer_per_cap = [21.94, 22, 24.19, 19.58, 19.04, 23.31, 16.94, 25.43, 23.93, 20.26, 24.12,
                20.86, 22.2, 19.97, 25.02, 21.12, 19.06, 26.4, 23.25, 18.45, 20.12, 20.59,
                21.8, 25.09, 23.79, 30.3, 25.63, 30.62, 31.61, 17.23, 26.15, 16.84, 21.2,
                30.41, 23.41, 20.3, 22.61, 22.08, 20.56, 25.87, 26.88, 21.03, 25.42,
                12.67, 23.42, 21, 20.12, 23.34, 27.52, 26.5]

wine_per_cap = [1.24238268, 2.552182, 2.145361, 0.94119689, 3.1935822, 2.4987453,
                3.360638, 3.519633, 2.9281906, 1.5588692, 3.0396061, 2.1405284, 2.1986082,
                1.3979203, 0.9813412, 0.94928628, 0.97898253, 1.5799767, 2.6431797,
                2.0777099, 3.6961575, 1.7342842, 1.8754873, 0.70148546, 1.6677339,
                2.1428993, 1.1796579, 3.8256018, 4.4116669, 3.2394561, 1.7459815,
                2.6410147, 1.6767241, 1.15415267, 1.4621656, 0.99553168, 3.0251772,
                1.41815774, 3.2586038, 1.4748841, 1.06093604, 1.15305843, 1.3476804,
                0.79689661, 3.7446437, 2.2460391, 2.9223839, 0.66951223, 1.9217346,
                1.3835459]


def test_666():
    setseed(666)
    for x in seed_666:
        assert np.isclose(runif01(), x)

def test_seed_235423():
    setseed(235423)
    for x in seed_235423:
        assert np.isclose(runif01(), x)


def test_mean():
    assert np.isclose(mean(beer_per_cap),np.mean(beer_per_cap))
    assert np.isclose(mean(wine_per_cap),np.mean(wine_per_cap))

def test_var():
    assert np.isclose(var(beer_per_cap),np.var(beer_per_cap,ddof=1))
    assert np.isclose(var(wine_per_cap),np.var(wine_per_cap,ddof=1))

def test_cov():
    COV = np.cov(beer_per_cap,wine_per_cap)
    assert np.isclose(cov(beer_per_cap, wine_per_cap),COV[0,1])

def test_sqrt():
    def check(n):
        assert np.isclose(sqrt(n), math.sqrt(n))
    check(125348)
    check(100)
    check(1)
    check(0)


def test_binomial():
    N = 500
    P = 0.4
    SAMPLES=10
    setseed(341)
    X = [binomial(N, P) for i in range(SAMPLES)]
    expecting = [195, 199, 213, 196, 196, 208, 194, 188, 187, 202]
    assert expecting==X

def test_exp():
    N = 10
    LAMBDUH = 1.5
    setseed(341)
    X = [rexp(LAMBDUH) for i in range(N)]
    X = ["%1.4f" % x for x in X]
    expecting = ['0.0018', '1.2845', '0.7220', '0.3402', '0.7465', '0.7292', '0.0288', '0.4527', '0.6812', '0.8736']
    assert expecting==X

def test_norm01():
    N = 10
    setseed(341)
    X = [rnorm01() for i in range(N)]
    X = ["%1.4f" % x for x in X]
    expecting = ['1.1369', '-0.6816', '0.1131', '-1.3395', '0.5905', '1.0185', '-0.8848', '0.7579', '0.3714', '-2.5268']
    assert expecting==X

def test_norm():
    N = 10
    setseed(341)
    mean = 2
    variance = 2
    X = [rnorm(mean, variance) for i in range(N)]
    X = ["%1.4f" % x for x in X]
    expecting = ['3.6078', '1.0361', '2.1599', '0.1056', '2.8351', '3.4404', '0.7488', '3.0718', '2.5253', '-1.5735']
    assert expecting==X
