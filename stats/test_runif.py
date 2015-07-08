from stats import *
import numpy as np

seed_666 = [0.00521236192678, 0.604166903349, 0.233144581892,
            0.460987861017, 0.822980116505, 0.826818094508,
            0.331714398848, 0.1239014343, 0.411406287184,
            0.505468696591]

seed_235423 = [0.8425073301617556, 0.02069802862624546, 0.8717671213074434]

def test_666():
    for x in seed_666:
        assert np.isclose(runif01(), x)

def test_seed_235423():
    setseed(235423)
    for x in seed_235423:
        assert np.isclose(runif01(), x)
