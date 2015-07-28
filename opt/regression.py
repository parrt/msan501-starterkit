import numpy as np
from pylab import imshow, plot
import matplotlib.pyplot as plt

def minimize(f, B0, eta, h, precision):
	trace = []
	...
	return (B,steps,trace)

def heatmap(X, Y, f, trace=None): # trace is a list of [b1, b2] pairs
	...
