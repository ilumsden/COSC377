#!/usr/bin/env python3
"""
Homework 5
Name: Ian Lumsden
NetID: ilumsden

This script solves problems 17 and 19 from problem set 3.1 in the textbook.
It uses cubic spline interpolation to predict the drag coefficient of a sphere
given the Reynold's number and to predit the kinematic viscosity of water
given the temperature.
"""
from __future__ import print_function
from cubicSpline import *
from numpy import array,log10
""" Problem 17 """
# Creates arrays for the initial data for the interpolation
xData = array([0.2, 2.0, 20.0, 200.0, 2000.0, 20000.0])
yData = array([103.0, 13.9, 2.72, 0.8, 0.401, 0.433])
# Creates an array for the data to use for prediction
Re_array= array([5.0, 50.0, 500.0, 5000.0])
# Evaluates the logs of xData and yData for log-log interpolation later
logxData = log10(xData)
logyData = log10(yData)
# Calculates the spline curvatures
k = curvatures(xData, yData)


print('\nInterpolating for drag coefficients (C_D)...\n    Re\tC_D')

# Loops through the Re values to predict the drag coefficients
# using the cubic spline data previously calculated.
for Re in Re_array:
    logy = evalSpline(logxData, logyData, k, log10(Re))
    print('{:6.1f}\t{:5.3f}'.format(Re,10.0**logy)) # Re is an element from
                                                    # the RE_array
                                                    # logy is the y-coordinate
                                                    # corresp. to log10(Re)
""" Problem 19 """
# Generates the initial data
tData = array([0.0, 21.1, 37.8, 54.4, 71.1, 87.8, 100.0])
mData = array([1.79, 1.13, 0.696, 0.519, 0.338, 0.321, 0.296]) 
T_array = array([10.0, 30.0, 60.0, 90.0])
# Calculates the spline curvatures
k = curvatures(tData, mData)

print('\nInterpolating for kinematic viscosity (CMu_k)...\n    T\tMu_k')

# Loops through the temperature values to predict the kinematic viscosities
# using the cubic spline data previously calculated.
for temp in T_array:
    y = evalSpline(tData, mData, k, temp)
    print('{:6.1f}\t{:5.3f}'.format(temp,y)) # temp is an element from 
                                             # T_array
