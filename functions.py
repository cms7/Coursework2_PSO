from math import sqrt
import numpy as np
# a list of test functions that are used throughout 

def assess_fitness(particle):
    return rastrigin(particle)

def rastrigin(coordinates):
    X = coordinates[0]
    Y = coordinates[1]
    Z = X**2 - 10 * np.cos(2 * np.pi * X) + (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20
    return Z

def ackley(coordinates):
    X = coordinates[0]
    Y = coordinates[1]
    Z = 0#-20*np.exp(-0.2*sqrt(0.5*(X**2+Y**2)))- np.exp(0.5*(np.cos(2*np.pi*X)+np.cos(2*np.pi*Y))+np.exp+20)
    return Z

def beale(coordinates):
    X = coordinates[0]
    Y = coordinates[1]
    Z = (1.5 - X + X*Y)**2 + (2.25-X+(X*Y)**2)**2 + (2.625 - X + (X*Y)**3)**2
    return Z

