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
    expecting = [0.001781572994290389, 1.2845295493089406, 0.7219864813074408, 0.3402115973972663, 0.7464782092122618, 0.7292474394945482, 0.028754028561498626, 0.4526565638171629, 0.6812386057098451, 0.8735744566322629]
    assert expecting==X

def test_norm01():
    N = 10
    setseed(341)
    X = [rnorm01() for i in range(N)]
    expecting = [1.1369166245081817, -0.681551133487586, 0.11306823358695245, -1.3395489132334599, 0.5904744606905199, 1.0185191933525879, -0.88476609128374728, 0.75788616855229118, 0.37143153139925705, -2.5268358543277682]
    assert expecting==X

def test_norm():
    N = 10
    setseed(341)
    mean = 2
    variance = 2
    X = [rnorm(mean, variance) for i in range(N)]
    expecting = [3.6078429096669105, 1.0361411435711001, 2.1599026294122372, 0.1055917594431004, 2.8350569905434724, 3.4404036567765344, 0.74875179417869275, 3.0718128983016317, 2.5252835091978376, -1.5734855350809362]
    assert expecting==X
