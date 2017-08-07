from pylab import show, text, imshow, plot
import matplotlib.pyplot as plt

from minimize import *

# Average hourly wage
HOURLY_WAGE = [2.98, 3.09, 3.23, 3.33, 3.46, 3.6, 3.73, 2.91, 4.25, 4.47, 5.04, 5.47, 5.76]
# Number of homicides per 100,000 people
MURDERS = [8.6, 8.9, 8.52, 8.89, 13.07, 14.57, 21.36, 28.03, 31.49, 37.39, 46.26, 47.24, 52.33]

def Cost(B,X=HOURLY_WAGE,Y=MURDERS):
	cost = 0.0
	for i in xrange(0,len(X)):
		...
	return cost


def heatmap(f, trace=None): # trace is a list of [b1, b2] pairs
	...


random.seed(int(round(time.time() * 1000)))

begin = time.time()
(m,steps,trace) = minimize(Cost, B0, LEARNING_RATE, h, PRECISION)
end = time.time()

heatmap(Cost, trace)

# Add text to heatmap
plt.plot(B0[0], B0[1], "ro")
plt.text(B0[0]-.2, B0[1]+0.8, "start", fontsize=16)
...

show()
