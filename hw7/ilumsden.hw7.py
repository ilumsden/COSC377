#!/usr/bin/env python3
"""
Homework 7
Name: Ian Lumsden
NetID: ilumsden

This script solves problem 27 of problem set 4.1 from the textbook.
It uses the Newton-Raphson Method for nonlinear systems of equations
to estimate the minimum trajectory (rotational radius and angle) of a
satellite orbiting Earth. Three initial data points of (radius, angle) pairs
are given to initialize the function F for Newton-Raphson.
"""
from __future__ import print_function
from newtonRaphson2 import *
from math import sin, pi
import numpy as np
import matplotlib.pyplot as plt

# This is an in-depth description of the problem that this script solves
# It was provided with the template for the problem
#
#
# The trajectory of a satellite orbiting the earth is given by the equation
#
# R = C/(1+e*sin(theta + alpha)), which can also be written as
# R - C/(1+e*sin(theta + alpha)) = 0 (in order to exploit rootfinding methods).
#
#  Here, (R, theta) are the polar coordinates of the satellite, and 
#  C, e, and alpha are constants. Given the following data points 
#  in form (R, theta), this program should determine C, e, and alpha as 
#  well as the minimum trajectory of the satellite and
#  the angle at which the "minimum trajectory" occurs.
#
#  Given (R, theta) data pairs: (6870km, -30deg),(6728km, 0deg), (6615km, 30deg)
#
#  The Newton-Raphson method can be used to solve a nonlinear system of 
#  3 trajectory equations using the given data. The unknowns are stored in
#  the vector x = [ C, e, alpha], and the initial guess is [6800, 0.5, 0].
#
#   In solving the resulting nonlinear system for x, the derived constants 
#   can be used to determine the minimum trajectory and angle at which it
#   occurs. The trajectory equation of the satellite's orbit as well as
#   the point at which minimum trajectory occurs can be plotted.
#
# Create the vector-valued function F(x) whose root defines a system of 3 trajectory 
# equations (using given data); use radians for all angles.
#
# Let x[0]=C, x[1]=e, and x[2]=alpha, and 30 degrees be represented by pi/6.
# Then, we seek a vector x that solves R- x[0]]/(1+x[1]*sin(theta + x[2])) = 0, [Eqn1]
# for each data pair given above.
#

# Specifies the function F at the three initial data points so that
# it can be used in Newton-Raphson to solve for the elements of x.
# It simply involves substituting the radius and angle values from the points
# into [Eqn1] from above.
def F(x):
    f = zeros((len(x)), dtype=float64)
    f[0] = 6870 - x[0]/(1+x[1]*sin((-30*(pi/180)) + x[2]))
    f[1] = 6728 - x[0]/(1+x[1]*sin(x[2]))
    f[2] = 6615 - x[0]/(1+x[1]*sin((30*(pi/180)) + x[2]))
    return f

# Initial guess at the values of x
x = np.array([6800.0, 0.5, 0.0]) 

# Calls the Newton-Raphson Method (code provided) to solve for x
x = newtonRaphson2(F, x)

# Print the solution vector x from Newton-Raphson
print()
np.set_printoptions(precision = 3)
print('[ C  e  alpha] = ' + np.array_str(x))

# Calculate minimum trajectory and angle using components of x
minTheta = (pi/2) - x[2]
minR = x[0]/(1+x[1])

# Print minimum trajectory results
print('Minimum trajectory = %.3f km' % minR)
print('Angle at which minimum trajectory occurs = %.3f degrees' % minTheta)
print()

#-------------------------------------------------------------
# Outputs for verification:
# C  e  alpha] = [  6.819e+03   4.060e-02   3.408e-01]
# Minimum trajectory = 6553.239 km
# Angle at which minimum trajectory occurs = 70.475 degrees
#-------------------------------------------------------------

# Create arrays of points spaced every 0.01 radians around the satellite orbit
# (theta) and their respective trajectories (R)

theta = np.arange(0, 2*pi, 0.01)            # theta and R are arrays now
R = x[0] / (1 + x[1]*np.sin(theta + x[2]))

# Plot orbit and minimum trajectory point

ax = plt.subplot(111, polar = True)
ax.plot(theta, R, color = 'r', linewidth = 2, label = 'Path')
ax.plot(minTheta, minR, 'bo', label = 'Min')
ax.legend(numpoints = 1)
ax.grid(True)
ax.set_title("Satellite path")
plt.show()
