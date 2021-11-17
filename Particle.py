from random import random, seed
from functions import assess_fitness
import numpy as np

class Particle:
    
    # initialise the particle
    def __init__(self, position, velocity, particle_num):
        self.position = position
        self.velocity = velocity
        self.id = particle_num
        self.p_best = position
        self.fitness = 1e7 # this is just a high number to begin with

def current_best(swarm):
    fitnessess = [assess_fitness(swarm[i].position) for i in swarm]
    best_fitness = min(fitnessess)
    best_id = fitnessess.index(best_fitness)
    return swarm[best_id].position
         
# update function which will do one iteration for the particles movement
def update_position(self,i_best,current):
    alpha = 0.5
    self.position += self.velocity
    cognitive = random()
    social = random()
    self.velocity = (alpha*self.velocity) + cognitive*(self.p_best-self.position)+social*(i_best-self.position)
    #fitness of this position 
    cur_fitness = assess_fitness(current)
    if(cur_fitness < self.fitness):
        self.p_best = self.position
    self.fitness = cur_fitness
