from copy import deepcopy
from pickle import dumps
from random import sample, shuffle
from sys import getsizeof
from zlib import compress
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm

people = [
    'Michael',
    'Sarah',
    'Joshua',
    'Narine',
    'David',
    'Sajid',
    'Melanie',
    'Daniel',
    'Wei',
    'Dean',
    'Brian',
    'Murat',
    'Lisa'
]

class ListCompression(Chromosome):
    def __init__(self, l):
        self.l = l

    @property
    def bytes_compressed(self):
        return getsizeof(compress(dumps(self.l)))

    def fitness(self):
        return 1 / self.bytes_compressed

    @classmethod
    def random_instance(cls):
        l_copy = deepcopy(people)
        shuffle(l_copy)
        return ListCompression(l_copy)

    def crossover(self, other):
        child_0 = deepcopy(self)
        child_1 = deepcopy(other)
        index_0, index_1 = sample(range(len(self.l)), k=2)
        l_0, l_1 = child_0.l[index_0], child_1.l[index_1]
        child_0.l[child_0.l.index(l_1)], child_0.l[index_1] = child_0.l[index_1], l_1
        child_1.l[child_1.l.index(l_0)], child_1.l[index_0] = child_1.l[index_0], l_0

        return child_0, child_1

    def mutate(self):
        index_0, index_1 = sample(range(len(self.l)), k=2)
        self.l[index_0], self.l[index_1] = self.l[index_1], self.l[index_0]

    def __str__(self):
        return f'Order: {self.l} Bytes: {self.bytes_compressed}'

if __name__ == '__main__':
    initial_population = [ListCompression.random_instance() for _ in range(1000)]
    genetic_algorithm = GeneticAlgorithm(
            initial_population=initial_population,
            threshold=1.0,
            max_generations=1000,
            mutation_chance=0.2,
            crossover_chance=0.7,
            selection_type=GeneticAlgorithm.selection_type.tournament
    )
    result = genetic_algorithm.run()
    print(result)
