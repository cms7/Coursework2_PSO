import numpy as np
from pyrecord import Record

class PSO:
    """
    An implementation for Particle Swarm Optimisation to optimise the ANN.
    """

    def __init__(self, dimensions, evaluate, iterations=50, alpha=0.7, beta=1.2, gamma=1.2, delta=1.2, seed=None,
                 informants=5, step=1, particles=40, min_val=-1, max_val=1):
        # Save initial arguments for later use
        self.iterations = iterations
        self.evaluate = evaluate
        self.a = alpha
        self.b = beta
        self.c = gamma
        self.d = delta
        self.step = step
        self.min = min_val
        self.max = max_val
        self.particles = particles
        self.dimensions = dimensions

        if seed is not None:
            np.random.seed(seed)

        # Initialise neighbourhoods
        self.neighbours = np.random.randint(particles - 1, size=(particles, informants))

        # Initialise position and velocity randomly
        self.positions = (max_val - min_val) * np.random.rand(particles, dimensions) + min_val
        self.velocities = ((max_val - min_val) * np.random.rand(particles, dimensions) + min_val - self.positions) / 2

        # Initialise best locations
        self.local_best = self._get_fitness()
        self.social_best = self._get_social_fitness()
        self.global_best = self._get_global_best()

    def optimise(self):
        best_of_epoch = []
        for epoch in range(1, self.iterations, self.step):
            self._iterate_once()
            best_of_epoch.append((self.global_best.position, self.global_best.value))
            print(f"Epoch {epoch} out of {self.iterations}.")
        return best_of_epoch

    def _iterate_once(self):
        a = np.random.rand(self.particles, self.dimensions) * self.a
        b = np.random.rand(self.particles, self.dimensions) * self.b
        c = np.random.rand(self.particles, self.dimensions) * self.c
        d = np.random.rand(self.particles, self.dimensions) * self.d
        self.velocities = a * self.velocities + \
                          b * (self.local_best.position - self.positions) + \
                          c * (self.social_best.position - self.positions) + \
                          d * (self.global_best.position - self.positions)
        new_positions = self.positions + self.velocities

        min_mask = [new_positions<self.min]
        max_mask = [new_positions > self.max]

        new_positions[min_mask] = self.min
        new_positions[max_mask] = self.max

        self.velocities[min_mask] = self.velocities[min_mask] * -0.5
        self.velocities[max_mask] = self.velocities[max_mask] * -0.5
        self.positions = new_positions
        self._update_best()

    def _update_best(self):
        local_fitness = self._get_fitness()
        local_mask = local_fitness.value < self.local_best.value
        self.local_best.position[local_mask] = local_fitness.position[local_mask]
        self.local_best.value[local_mask] = local_fitness.value[local_mask]

        social_fitness = self._get_social_fitness()
        social_mask = social_fitness.value < self.social_best.value
        self.social_best.position[social_mask] = social_fitness.position[social_mask]
        self.social_best.value[social_mask] = social_fitness.value[social_mask]

        self.global_best = self._get_global_best()

    Landscape = Record.create_type("Landscape","position","value")

    def _get_fitness(self):
        return Landscape(self.positions, np.apply_along_axis(self.evaluate, 1, self.positions))

    def _get_social_fitness(self):
        position = []
        value = []
        for informants in self.neighbours:
            min_i = np.argmin(self.local_best.value[informants])
            position.append(self.local_best.position[min_i])
            value.append(self.local_best.value[min_i])
        return Landscape(position, value)

    def _get_global_best(self):
        min_i = np.argmin(self.local_best.value)
        return Landscape(self.local_best.position[min_i], self.local_best.value[min_i])
