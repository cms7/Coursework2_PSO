from Particle import Particle
import numpy as np
from Particle import find_best
from functions import assess_fitness
from random import seed

class PSO:

    def __init__(self,swarmsize,dimensions,num_informants):
        self.swarmsize=swarmsize
        self.num_informants = num_informants
        self.swarm = [Particle( np.zeros(dimensions), np.random.rand(
            dimensions), i) for i, x in enumerate(range(swarmsize))]
        self.g_best = np.random.choice(self.swarm,1)[0]
    
    def update_swarm(self):
        for particle in self.swarm:
            informants = np.random.choice(self.swarm,self.num_informants)
            if particle not in informants:
                np.append(informants,particle)
            i_best = find_best(informants)
            particle.update(i_best,self.g_best)

    def update_gbest(self):
        most_fit = find_best(self.swarm)
        g_best_fitness = self.g_best.assess_fitness()
        if(most_fit.assess_fitness()<g_best_fitness):
            self.g_best = most_fit

    def improve(self, epochs):
        for i in range(epochs):
            self.update_swarm()
            self.update_gbest()
            B = assess_fitness(self.g_best.position)
            X = self.g_best.position[0]
            Y = self.g_best.position[1]
            print('Epoch = %i, Y = %f, X = %f ' % (i,X,Y))
    
seed(1)
pso = PSO(100,2,10)
pso.improve(100)