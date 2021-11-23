import random
import numpy as np
from functions import get_fitness, beale, rastrigin, squared_error
'''''''''''''''''''''''
this class is the implementation for 1 particle in a swarm

'''''''''''''''''''''''
# these are the weight values used in the velocity equation
alpha = 0.5
beta = 1
gamma = 1
delta = 1
epsilon = 1

#this constructor involves all elements of particle

#velocity:   a value for the velocity of particle
#position:   a positional vector for the particle of n dimensions
#name:       used to keep track of particle easily

class Particle:
    def __init__(self, velocity, position, name):
        self.velocity = velocity
        self.position = position
        self.p_best = position
        self.id = name
        self.prev_fit = np.inf

# function which takes the position of the particle as argument and returns a value 
# of fitness. This rastrigin is the current function we are trying to optimise
# this can be changed easily by opening functions.py and changing the function to another

    def get_fitness(self):
        return rastrigin(self.position)

# the function is ued to chamge the velocity and position of particle once
# i_best = informant best position
# g_best = global best position

    def move_particle(self, i_best, g_best):
        # The position is updated
        self.position += self.velocity*epsilon

        # The function generates a random weight between 0 and the defined values of hyperparameter 
        cognitive = random.uniform(0,beta)
        social = random.uniform(0,gamma)
        glob = random.uniform(0,delta)

        self.velocity = (self.velocity*alpha+cognitive*(self.p_best-self.position)+social*(i_best.p_best-self.position)+glob*(g_best.p_best-self.position))
        
        # The new velocity is calculated and then checks if the new position is fitter than the previous best fitness
        # if so this is updated and set as new best 
        cur_fit = self.get_fitness()
        if(cur_fit < self.prev_fit):
            self.p_best = self.position
        self.prev_fit = cur_fit

# the following function looks to get the best particle in the swarm and this will help assign
# the global best value for the entire swarm.

def find_best_in_swarm(swarm):
    
    # get fitness of each particle in swarm and store into a list 
    list_of_fitnesses = [get_fitness(particle.p_best) for particle in swarm]
    # take the minimum of the list to get most fit
    most_fit = np.min(list_of_fitnesses)
    # reference the particle and get its index which we can return as the most fit and get position
    fittest_particle = list_of_fitnesses.index(most_fit)
    return swarm[fittest_particle]

