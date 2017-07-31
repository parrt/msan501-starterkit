from minimize import *
import numpy as np


# Average hourly wage
HOURLY_WAGE = [2.98, 3.09, 3.23, 3.33, 3.46, 3.6, 3.73, 2.91, 4.25, 4.47, 5.04, 5.47, 5.76]
# Number of homicides per 100,000 people
MURDERS     = [8.6, 8.9, 8.52, 8.89, 13.07, 14.57, 21.36, 28.03, 31.49, 37.39, 46.26, 47.24, 52.33]

LEARNING_RATE = ... # fill in with your values
h = ... # fill in with your values
PRECISION = 0.000001

def Cost(B,X=HOURLY_WAGE,Y=MURDERS):
	...


def check(B0, f, X, Y, eta, h, precision):
    print "starting at", B0
    (m, steps, trace) = minimize(f, B0, eta, h, precision)
    print "gradient descent gives ", m, "Cost", Cost(m)

    fit = np.polyfit(X, Y, 1)
    print "exact is               ", [fit[1], fit[0]]
    assert int(m[0]*1000) == int(fit[1]*1000)

def test_1():
    check([-23, 12], Cost, HOURLY_WAGE, MURDERS, LEARNING_RATE, h, PRECISION)

def test_2():
    check([-50, 10], Cost, HOURLY_WAGE, MURDERS, LEARNING_RATE, h, PRECISION)

def test_3():
    check([-36, 17], Cost, HOURLY_WAGE, MURDERS, LEARNING_RATE, h, PRECISION)

def test_4():
    check([-36, 15], Cost, HOURLY_WAGE, MURDERS, LEARNING_RATE, h, PRECISION)

def test_5():
    check([100, 17], Cost, HOURLY_WAGE, MURDERS, LEARNING_RATE, h, PRECISION)

def test_6():
    check([-15, 0],  Cost, HOURLY_WAGE, MURDERS, LEARNING_RATE, h, PRECISION)

test_1()
test_2()
test_3()
test_4()
test_5()
test_6()
