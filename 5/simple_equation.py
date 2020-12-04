from copy import deepcopy
from random import random, randrange
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm

class SimpleEquation(Chromosome):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fitness(self):
        return 6 * self.x - self.x**2 + 4 * self.y - self.y**2

    @classmethod
    def random_instance(cls):
        return SimpleEquation(randrange(100), randrange(100))

    def crossover(self, other):
        child_0 = deepcopy(self)
        child_1 = deepcopy(other)
        child_0.y = other.y
        child_1.y = self.y

        return child_0, child_1

    def mutate(self):
        if random() > 0.5:
            if random() > 0.5:
                self.x += 1
            else:
                self.x -= 1
        else:
            if random() > 0.5:
                self.y += 1
            else:
                self.y -= 1

    def __str__(self):
        return f'x: {self.x} y: {self.y} fitness {self.fitness()}'

if __name__ == '__main__':
    initial_population = [SimpleEquation.random_instance() for _ in range(20)]
    genetic_algorithm = GeneticAlgorithm(initial_population, threshold=13.0, max_generations=100, mutation_chance=0.1, crossover_chance=0.7)
    result = genetic_algorithm.run()

    print(result)
