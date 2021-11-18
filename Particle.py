import random
import numpy as np
from functions import assess_fitness, target

alpha = 0.1
beta = 1
gamma = 1
delta = 1
epsilon = 1

class Particle:
    def __init__(self, target, velocity, position, name):
        self.velocity = velocity
        self.position = position
        self.p_best = position
        self.id = name
        self.target = target
        self.prev_fit = np.inf

    def assess_fitness(self):
        return assess_fitness(self.position, self.target)
    
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

def find_best(swarm,target):
    fitnesses = [assess_fitness(x.p_best,target) for x in swarm]
    most_fit = min(fitnesses)
    fittest_particle = fitnesses.index(most_fit)
    return swarm[fittest_particle]

class PSO:

    def __init__(self,target,swarmsize,dimensions,num_informants):
        self.target = target
        self.swarmsize=swarmsize
        self.num_informants = num_informants
        self.swarm = [Particle(target, np.zeros(dimensions), np.random.rand(
            dimensions), i) for i, x in enumerate(range(swarmsize))]
        self.g_best = np.random.choice(self.swarm,1)[0]
    
    def update_swarm(self):
        for particle in self.swarm:
            informants = np.random.choice(self.swarm,self.num_informants)
            if particle not in informants:
                np.append(informants,particle)
            i_best = find_best(informants,self.target)
            particle.update(i_best,self.g_best)

    def update_gbest(self):
        most_fit = find_best(self.swarm, self.target)
        g_best_fitness = self.g_best.assess_fitness()
        if(most_fit.assess_fitness()<g_best_fitness):
            self.g_best = most_fit

    def improve(self, epochs):
        for i in range(epochs):
            self.update_swarm()
            self.update_gbest()
            print(self.g_best.position)

pso = PSO(target,40,2,5)
pso.improve(1000)