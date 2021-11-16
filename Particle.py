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
        self.fitness = 1e7
         
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


seed(1)    
size = 20
swarm = [Particle(np.random.uniform(-1,1,2), np.random.rand(2),i) for i , x in enumerate(range(size))] 
print(swarm)
for i in range(10):
    for j in range(size):
        swarm[j].update_position([0,0],swarm[j].position)
        print(swarm[j].position)