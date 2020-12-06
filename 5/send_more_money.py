from copy import deepcopy
from random import sample, shuffle
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm

class SendMoreMoney(Chromosome):
    def __init__(self, letters):
        self.letters = letters

    def fitness(self):
        s = self.letters.index('S')
        e = self.letters.index('E')
        n = self.letters.index('N')
        d = self.letters.index('D')
        m = self.letters.index('M')
        o = self.letters.index('O')
        r = self.letters.index('R')
        y = self.letters.index('Y')

        send = 1000 * s + 100 * e + 10 * n + d
        more = 1000 * m + 100 * o + 10 * r + e
        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

        difference = abs(money - (send + more))
        return 1 / (difference + 1)

    @classmethod
    def random_instance(cls):
        letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y', '', '']
        shuffle(letters)

        return SendMoreMoney(letters)

    def crossover(self, other):
        child_0 = deepcopy(self)
        child_1 = deepcopy(other)
        index_0, index_1 = sample(range(len(self.letters)), k=2)
        l_0, l_1 = child_0.letters[index_0], child_1.letters[index_1]

        child_0.letters[child_0.letters.index(l_1)], child_0.letters[index_1] = child_0.letters[index_1], l_1
        child_1.letters[child_1.letters.index(l_0)], child_1.letters[index_0] = child_1.letters[index_0], l_0

        return child_0, child_1

    def mutate(self):
        index_0, index_1 = sample(range(len(self.letters)), k=2)
        self.letters[index_0], self.letters[index_1] = self.letters[index_1], self.letters[index_0]

    def __str__(self):
        s = self.letters.index('S')
        e = self.letters.index('E')
        n = self.letters.index('N')
        d = self.letters.index('D')
        m = self.letters.index('M')
        o = self.letters.index('O')
        r = self.letters.index('R')
        y = self.letters.index('Y')
        send = 1000 * s + 100 * e + 10 * n + d
        more = 1000 * m + 100 * o + 10 * r + e
        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
        difference = abs(money - (send + more))

        return f'{send} + {more} = {money} Difference: {difference}'

if __name__ == '__main__':
    initial_population = [SendMoreMoney.random_instance() for _ in range(1000)]
    genetic_algorithm =  GeneticAlgorithm(
        initial_population=initial_population,
        threshold=1.0,
        max_generations=1000,
        mutation_chance=0.2,
        crossover_chance=0.7,
        selection_type=GeneticAlgorithm.selection_type.roulette
    )
    result = genetic_algorithm.run()

    print(result)
