"""
Homework 2: LU Decomposition
Name: Ian Lumsden
NetID: ilumsden

This script solves problem 15 from Problem Set 2.1 of the textbook.
It performs LU Decompositions of systems of equations based on Hilbert Matrices
of increasing size. Each equation is of the form Ax = b, where A is a Hilbert Matrix
of size n, and b is a vector with each element equal to the sum of the elements in the
corresponding row of A. After each system is solved, an error measure is calculated
based on the expected solution vector x = [1 1 1 1 ...]^T of size n. The decomposition is
repeated for increasing values of n until the error measure is greater than 1e-6.
The code for the LU decomposition is stored in the LUdecomp module.
"""

# Imports various required numpy functions and the functions from the LUdecomp module
import numpy as np
from numpy import zeros, ones, array, float64, inf
from numpy import linalg
from LUdecomp import *

# numpy.linalg.norm is renamed to norm for ease of use
norm = linalg.norm  

# Sets the initial values for tolerance, the error measure, and n.
TOL = 1e-6
err = 0
n = 0
# This code will continue until the error of the calculated solution is greater than 1e-6
while err < TOL:
    # Updates n and initializes A, b, and the correct solution vector.
    n +=1
    a = zeros((n,n),dtype=float64)
    b = zeros((n),dtype=float64)
    soln = ones((n), dtype=float64) # The correct solution is all 1's

    # a is set to be a Hilbert Matrix of size (n, n).
    for i in range(n):
        for j in range(n):
            a[i,j] = 1/(i+j+1)
    # b is set to be a vector with elements equal to the sum of the elements of a's corresponding rows
    b = np.sum(a, axis=1)

    # Call appropriate functions from the LUdecomp.py module to
    # solve the equations A x = b with the b-vector being overridden
    # by the solution vector x.

    a = LUdecomp(a)
    b = LUsolve(a, b)

    # Data about the number of equations, the solution, and the calculated error
    # are printed to stdout.
    print("\n", n, " equations. ", "The solution is:\n", b)
    err = norm(b-soln, ord=inf)
    print("Error (inf-norm of difference)): ", err)

# Prints info to stdout stating the maximum number of equations for which the error
# was less than 1e-6.
print("^^^(Greater than TOL = ", TOL, ")^^^\n")
print("********************************************\n")
print("Max number of equations while error remains less than ", TOL, " is: ", n-1, "\n") 
print("********************************************")
