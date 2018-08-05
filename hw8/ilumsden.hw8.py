#!/usr/bin/env python3
"""
Homework 8
Name: Ian Lumsden
NetID: ilumsden

This script solves problems 5.1.9 and 5.1.11 from the textbook.
"""
from numpy import array, polyfit, polyder, polyval

# Problem 5.1.9
#
# Uses central finite difference approximation and Richardson Extrapolation
# to evaluate f'(0.2) based on the provided data points.
print("Problem 5.1.9\n=============")
# Stores the provided data points as a dictionary of (x, y) pairs
data9 = { 0.0: 0.0, 0.1: 0.078348, 0.2: 0.138910, 0.3: 0.192916, 0.4: 0.244981 }
# Approximates f'(0.2) using a central difference FDA with h = 0.2
h1 = 0.2
x = 0.2
centralApprox1 = (data9[x+h1] - data9[x-h1])/(2*h1)
print("Central FDA Approximation (h = 0.2): %f" % centralApprox1)
# Approximates f'(0.2) using a central difference FDA with h = 0.1
# The round built-in is used to ensure the key value (x) can 
# correctly access the corresponding f(x) value.
h2 = h1 / 2.0
centralApprox2 = (data9[round(x+h2, 1)] - data9[round(x-h2, 1)])/(2*h2)
# Uses Richardson Extrapolation to improve the approximation of f'(0.2)
p = 2.0
richardsonExtrap = (2**p * centralApprox2 - centralApprox1)/(2**p - 1)
print("Richardson Extrapolation (h2 = h1 / 2, p = 2): %f" % richardsonExtrap)
# Problem 5.1.11
#
# Estimates f'(0) and f''(0) using polynomial interpolation and compares
# them to the actual values
print("\nProblem 5.1.11\n==============")
# Initial interpolation data points
xData = array([-2.2, -0.3, 0.8, 1.9])
yData = array([15.18, 10.962, 1.92, -2.04])
# Performs cubic interpolation on the inital data
p = polyfit(xData, yData, 3)
# Takes the first and second derivatives of the interpolation
d1 = polyder(p, 1) 
d2 = polyder(p, 2)
# Coeffcients of the actual polynomial
pActual = array([1, -0.3, -8.56, 8.448])
# Takes the first and second derivatives of the actual polynomial
d1Actual = polyder(pActual, 1)
d2Actual = polyder(pActual, 2)
# Evaluates the value of f'(0) using the interpolated polynomial and the 
# real polynomial. Then, prints the values and the error measure of the
# interpolated derivative.
fd = polyval(d1, 0)
fdActual = polyval(d1Actual, 0)

print("Interpolated f'(0): %f" % fd)
print("Actual f'(0): %f" % fdActual)
print("Error: %f\n" % (fdActual - fd))
# Evaluates the value of f''(0) using the interpolated polynomial and the 
# real polynomial. Then, prints the values and the error measure of the
# interpolated derivative.
sd = polyval(d2, 0)
sdActual = polyval(d2Actual, 0)

print("Interpolated f''(0): %f" % sd)
print("Actual f''(0): %f" % sdActual)
print("Error: %f" % (sdActual - sd))
#
# Outputs for verification:
#
# Problem 5.1.9
# =============
# Central FDA Approximation (h = 0.2): 0.612452
# Richardson Extrapolation (h2 = h1 / 2, p = 2): 0.559636
#
# Problem 5.1.11
# ==============
# Interpolated f'(0): -8.560000
# Actual f'(0): -8.560000
# Error: -0.000000
#
# Interpolated f''(0): -0.600000
# Actual f''(0): -0.600000
# Error: -0.000000
