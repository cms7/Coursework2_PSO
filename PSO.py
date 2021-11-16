
from Particle import Particle
import numpy as np
from random import seed

class PSO:
    seed(1)        
    size = int(input("Please enter swarmsize"))
    swarm = [Particle(np.random.uniform(-1,1,2), np.random.rand(2),i) for i , x in enumerate(range(size))]
    print(swarm[1].velocity)

optimize = PSO()
