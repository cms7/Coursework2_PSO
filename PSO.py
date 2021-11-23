from Particle import Particle
import numpy as np
from Particle import find_best_in_swarm
from random import seed
#import matplotlib.pyplot as plt
''''''''''''''''''''''''''''''''''''''''
This is the class for the PSO
'''''''''''''''''''''''''''''''''''''''
class PSO:

    # this constructor involves all elements of particle

    # swarmsize:            a value for the number of particles per swarm
    # dimension:            a positional vector for the particle of n dimensions
    # num_informants:       number of informants assigned to each particle

    def __init__(self,swarmsize,dimensions,num_informants):
        self.swarmsize=swarmsize
        self.num_informants = num_informants
        # this will initialise a swarm when a PSO is initialised
        self.swarm = [Particle( np.zeros(dimensions), np.random.rand(dimensions), i) for i, x in enumerate(range(swarmsize))]
        # this choses a particle at random to be the global best at start
        self.g_best = np.random.choice(self.swarm,1)[0]
    
    # This function iterates the all particles in the swarm once and assigns informants to each particle

    def iterate_swarm(self):
        # for every particle in the swarm
        for particle in self.swarm:
            #this section will assign the informants to each particle
            informant = np.random.choice(self.swarm,self.num_informants)
            if particle not in informant:
                #particles are given the informants
                np.append(informant,particle)
            # the best informant is found out of the informants    
            i_best = find_best_in_swarm(informant)
            # then we iterate each particle in swarm once
            particle.move_particle(i_best,self.g_best)

    # this function determines the new global best out of all the particles in swarm

    def find_new_gbest(self):
        # this uses the method to find the most fit out of swarm from particle.py
        most_fit_from_swarm = find_best_in_swarm(self.swarm)
        # then the fitness of the global best is checked 
        global_best_fitness = self.g_best.get_fitness()
        # comparing these two values to check it there are any changes necescaary
        if(most_fit_from_swarm.get_fitness()<global_best_fitness):
            self.g_best = most_fit_from_swarm
        

    def improve(self, epochs):
        '''''''''
        fit = list()
        epochlol = list(range(1, 101))
        '''''''''
        for i in range(epochs):
            self.iterate_swarm()
            self.find_new_gbest()
            #fit.append(self.g_best.prev_fit)
            X = self.g_best.position[0]
            Y = self.g_best.position[1]
            print('Epoch = %i, Y = %f, X = %f ' % (i,X,Y))
        ''''''''''''''''''''''''''''''''''''''''
        uncomment this section to see plots along with the import

        plt.plot(epochlol, fit)
        plt.xlabel('Iterations')
        plt.ylabel('Fitness')
        plt.title('Assessing overall values fitness')
        plt.grid()
        plt.show()
        '''''''''''''''''''''''''''''''''''''''''
seed(1)

pso = PSO(100,2,6)
pso.improve(100)