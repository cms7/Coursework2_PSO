import random
import numpy as np
from functions import ackley, assess_fitness, beale, rastrigin

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
    most_fit = min(fitnesses)
    fittest_particle = fitnesses.index(most_fit)
    return swarm[fittest_particle]

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
            X = self.g_best.position[0]
            Y = self.g_best.position[1]
        print('Y = %f, X = %f' % (X, Y))

pso = PSO(50,2,10)
pso.improve(100)