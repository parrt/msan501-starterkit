import numpy as np
from pylab import imshow, plot

def minimize(f, B0, eta, h, precision):
    trace = []
    B = B0
    steps = 0 
    while True:
        if steps % 10 == 0: # only capture every 10th value
            trace.append(B)
        steps += 1
        ...     
    ... 
    return (B, steps, trace)
