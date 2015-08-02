import numpy as np
from pylab import imshow, plot
import matplotlib.pyplot as plt

def Cost(B,X=HOURLY_WAGE,Y=MURDERS):
	cost = 0.0
	for i in xrange(0,len(X)):
		...
	return cost

def minimize(f, B0, eta, h, precision):
	trace = []
	...
	return (B,steps,trace)

