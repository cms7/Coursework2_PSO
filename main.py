from random import random, seed
from functions import assess_fitness
import numpy as np
from Particle import Particle, current_best

swarmsize = int(input("Enter Swarmsize: "))
alpha = 0.5
beta = 1
gamma = 1
delta = 1 
epsilon = 0.5

iterations = 20
epoch = 0

swarm = [Particle(np.random.uniform(-1,1,2),np.random.uniform(2),i) for i, x in enumerate(range(swarmsize))]

while(epoch<iterations):
    current_best(swarm)



