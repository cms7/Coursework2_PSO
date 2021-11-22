import random
import numpy as np
from functions import ackley, assess_fitness, beale, rastrigin, squared_error

alpha = 0.5
beta = 1
gamma = 1
delta = 1
epsilon = 1

class Particle:
    def __init__(self, velocity, position, name):
        self.velocity = velocity
        self.position = position
        self.p_best = position
        self.id = name
        self.prev_fit = np.inf

    def assess_fitness(self):
        return rastrigin(self.position)
    
    def update(self, i_best, g_best):
        self.position += self.velocity*epsilon
        cognitive = random.uniform(0,beta)
        social = random.uniform(0,gamma)
        glob = random.uniform(0,delta)

        self.velocity = (self.velocity*alpha+cognitive*(self.p_best-self.position)+social*(i_best.p_best-self.position)+glob*(g_best.p_best-self.position))
        
        cur_fit = self.assess_fitness()
        if(cur_fit < self.prev_fit):
            self.p_best = self.position
        self.prev_fit = cur_fit

def find_best(swarm):
    fitnesses = [assess_fitness(x.p_best) for x in swarm]
    most_fit = np.min(fitnesses)
    fittest_particle = fitnesses.index(most_fit)
    return swarm[fittest_particle]

