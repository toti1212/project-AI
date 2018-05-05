""" # Test functions

Test functions for benchmarking optimization techniques.
"""
import random
from math import sin, sqrt, inf
from .problem import OptimizationProblem

# References:
# + [Test functions for optimization @ Wikipedia](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
# + [Test functions and datasets @ Virtual Library of Simulation Experiments](https://www.sfu.ca/~ssurjano/optimization.html)

def __eggholder__(elem):
    pass

def __sum_squares__(elem):
    (x,y) = elem

    suma = 0
    for i in range(2):
        suma += i*x**2+i*y**2

    return suma

SUM_SQUARES = OptimizationProblem(domains= ((-10,+10),)*2, objective=__sum_squares__)

#TODO: Eggholder y coloreo de grafos
