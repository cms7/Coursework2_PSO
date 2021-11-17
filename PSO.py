
from Particle import Particle
import numpy as np
from random import seed

def get_best_possible_fitness(problem):
    optimal_solutions = problem.get_optimal_solutions()
    an_optimal_solution = optimal_solutions[0]
    problem.evaluate(an_optimal_solution)
    return an_optimal_solution.objective_values

class PSO:
    def __init__(self, problem, swarm_size, vector_length, num_informants=2):
        self.swarm_size = swarm_size
        self.num_informants = num_informants
        self.problem = problem
        self.swarm = [Particle(self.problem, np.random.rand(vector_length), np.random.rand(vector_length))
                      for x in range(swarm_size)]
        self.global_fittest = np.random.choice(self.swarm, 1)[0]
        
    def find_current_best(self, swarm):
        """Evaluates a given swarm and returns the fittest particle based on their best previous position"""
        fitnesses = [Particle.evaluate_position(x.fittest_position, self.problem) for x in swarm]
        best_value = min(fitnesses)
        best_index = fitnesses.index(best_value)
        return swarm[best_index], fitnesses
    
    def update_swarm(self):
        """Update each particle in the swarm"""
        for particle in self.swarm:
            informants = np.random.choice(self.swarm, self.num_informants)
            if (particle not in informants):
                np.append(informants, particle)
            fittest_informant, _ = self.find_current_best(informants)
            
            particle.update(fittest_informant, self.global_fittest)
    
    def improve(self, num_iterations=200):
        """Improves the population for a given number of iterations.

        Parameters
        ----------
        num_iterations : int, optional
            The number of iterations before stopping improving
        
        Returns
        -------
        results : list
            A list of the best fitness at each generation
        found_global_min_at : int
            The position at which the global min was found at, return -1 if not found
        """
        best_possible_fitness = get_best_possible_fitness(self.problem)
        fitnesses = []
        found_global_min_at = -1
        for i in range(num_iterations):
            fittest, _ = self.find_current_best(self.swarm)
            global_fittest_fitness = self.global_fittest.assess_fitness()
            if (fittest.assess_fitness() < global_fittest_fitness):
                self.global_fittest = fittest
            fitnesses.append(global_fittest_fitness)
            self.update_swarm()
            if math.isclose(best_possible_fitness, global_fittest_fitness, rel_tol=1e-1) :
                if found_global_min_at == -1:
                    found_global_min_at = i
        return fitnesses, found_global_min_at

