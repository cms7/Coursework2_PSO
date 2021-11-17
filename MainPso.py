import numpy as np
from random import random, seed

class PSO:
#Declaration of variable

    def __init__(self, particles=40, alpha=0.7, beta=1.2, gamma=1.2, delta=1.2, j_size=1, informants=5, seed=None):
        self.particles = particles
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.jump_size = j_size


        np.random.seed(seed)

        np.random.randint(particles -1, size =(particles, informants))
    
    
    
swarm = PSO()
        



