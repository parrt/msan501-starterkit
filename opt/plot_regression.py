from pylab import show, text

from regression import *

# Average hourly wage
HOURLY_WAGE = [2.98, 3.09, 3.23, 3.33, 3.46, 3.6, 3.73, 2.91, 4.25, 4.47, 5.04, 5.47, 5.76]
# Number of homicides per 100,000 people
MURDERS = [8.6, 8.9, 8.52, 8.89, 13.07, 14.57, 21.36, 28.03, 31.49, 37.39, 46.26, 47.24, 52.33]

def Cost(B,X=HOURLY_WAGE,Y=MURDERS):
	cost = 0.0
	for i in xrange(0,len(X)):
		...
	return cost

begin = time.time()
(m,steps,trace) = minimize(Cost, B0, LEARNING_RATE, h, PRECISION)
end = time.time()

heatmap(HOURLY_WAGE, MURDERS, Cost, trace)

show()
