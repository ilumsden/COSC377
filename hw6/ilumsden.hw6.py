#!/usr/bin/env python3
"""
Homework 6
Name: Ian Lumsden
NetID: ilumsden

This script solve problem 10 from problem set 3.2 in the textbook.
It uses curve fitting to predict the thermal efficiency of steam engines
in the year 2000 based on efficiency data from 1718 to 1906.
"""
from numpy import array,zeros
from polyFit import *
import pylab

# This is a provided function that is copied from the provided polyFit module.
def evalPoly(c,x): 
    m = len(c) - 1 
    p = c[m]
    for j in range(m):
        p = p*x + c[m-j-1]
    return p

# Sets the data to be used for curve fitting
xData = array([1718,1767,1774,1775,1792,1816,1828,1834,1878,1906])
yData = array([0.5,0.8,1.4,2.7,4.5,7.5,12.0,17.0,17.2,23.0])

# Sets a default value that standard deviation must be less than
minsdev=float("inf")
# Stores the size of the initial dataset for later
n=len(xData)
print('Degree  Stdev   2000P')
# Repeats curve fitting for polynomials of degree 1 to 5, inclusive.
for m in range(1,6):   
    # Initializes the y-coordinates calculated from the curve
    ys=zeros((n),dtype='float') 

    # Calculates the coefficients of the polynomial determined from the curve fit
    coeff = polyFit(xData, yData, m) 
    # Gets the standard deviation of the error in the fit
    stdev = stdDev(coeff, xData, yData) 
    # Evaluates the fitted polynomial at the year 2000
    proj  = evalPoly(coeff, 2000) 
    # Year 2000 projections >= 100 or < 0 are meaniningless        
    if (stdev < minsdev) and proj < 100 and proj > 0:
        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'viable'))
        # Calculates the y-coordinates of the fitted polynomial
        # using the x-coordinates in xData.
        ys = evalPoly(coeff, xData) 
        # Use Matplotlib to plot original data points with validated curve fitting
        pylab.xlabel("x")
        pylab.ylabel("Thermal Efficiency")
        my_title= 'Fit with poly degree = ' + str(m) + '; green dot is 2000 projection'
        pylab.title(my_title)
        # X-axis ranges from 1710 to 2015
        pylab.xlim(xmin=1710, xmax=2015)
        # Plots the estimated value at the year 2000 as a green dot
        pylab.plot(2000, proj, "g.")
        # Plots the original data as red points
        pylab.plot(xData, yData, "r.")
        # Plots the fited polynomial as a blue line
        pylab.plot(xData, ys, "b")
        pylab.grid()
        pylab.show()
    # Skips the plotting if the prediction is not viable
    else:
        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'not viable'))
#--------------------------------------------------------------------------------------
# Table to stdout should look similar to this...
#
# Degree Stdev   2000P
#   1 	 2.855	 34.986	    viable
#   2	 2.768	 45.419	    viable
#   3	 2.266	 -6.602	    not viable
#   4	 2.234	 112.391	not viable
#   5	 2.496	 113.726	not viable
#--------------------------------------------------------------------------------------
