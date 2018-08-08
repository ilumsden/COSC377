#!/usr/bin/env python3
"""
Homework 9
Name: Ian Lumsden
NetID: ilumsden

This scipt solves problem 6.1.14 from the textbook. It solves for the function
g(u) from Debye's formula for heat capacity for a solid using Romberg
numerical integration.
"""
from romberg import *
from numpy import *
from math import exp
import matplotlib.pyplot as plt

# Evaluates the integrand at the provided value of x
def f(x):
  if x == 0: return 0
  else: return (x**4 * exp(x))/((exp(x) - 1)**2)

# Sets initial data and creates a list for the values of g(u)
u = arange(0,1.01,0.05)
print ("    u\t   g(u)")
gu = []

for i in u:
  if i == 0: g = 0.0;
  else:
    # Performs Romberg integration on f
    I,nPanels = romberg(f, 0, 1/i)  
    # Evaluates g(i)
    g = i**3 * I
  # Prints the values of u and g(u)
  print ('{:6.2f}{:13.6f}'.format(i,g))
  gu.append(g)

# Plots g(u) vs u and saves the plot to prob6_1_14.png
plt.plot(u, gu, "b-")
plt.xlabel("u")
plt.ylabel("g(u)")
plt.xlim(xmin=0.0, xmax=1.0)
plt.ylim(ymin=0.0)
plt.title("Problem 6.1.14")
plt.savefig("prob6_1_14.png")
plt.show()
#
# Place the code that creates the required plot using pylab here.
# Be sure to label axes and provide the same title as shown
# in the "prob6_1-14.png" image file on BB
#
# Table written to stdout for verification purposes:
#
#  u	     g(u)
# 0.00     0.000000
# 0.05     0.003247
# 0.10     0.025274
# 0.15     0.070997
# 0.20     0.122878
# 0.25     0.167686
# 0.30     0.202568
# 0.35     0.228858
# 0.40     0.248618
# 0.45     0.263608
# 0.50     0.275136
# 0.55     0.284136
# 0.60     0.291265
# 0.65     0.296992
# 0.70     0.301651
# 0.75     0.305487
# 0.80     0.308678
# 0.85     0.311359
# 0.90     0.313631
# 0.95     0.315573
# 1.00     0.317244
