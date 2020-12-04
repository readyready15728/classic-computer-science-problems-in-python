from enum import Enum
from heapq import nlargest
from random import choices, random
from statistics import mean
from chromosome import Chromosome

class GeneticAlgorithm:
    selection_type = Enum('selection_type', 'roulette tournament')

    def __init__(
        self,
        initial_population,
        threshold,
        max_generations=100,
        mutation_chance=0.01,
        crossover_chance=0.7,
        selection_type=selection_type.tournament
    ):
        self._population = initial_population
        self._threshold = threshold
        self._max_generations = max_generations
        self._mutation_chance = mutation_chance
        self._crossover_chance = crossover_chance
        self._selection_type = selection_type
        self._fitness_key = type(self._population[0]).fitness

    # Use the probability distribution wheel to pick two parents
    # Note: will not work with negative fitness results
    def _pick_roulette(self, wheel):
        return tuple(choices(self._population, weights=wheel, k=2))

    # Choose num_participants at random and take the best two
    def _pick_tournament(self, num_participants):
        participants = choices(self._population, k=num_participants)
        return tuple(nlargest(2, participants, key=self._fitness_key))

    # Replace the population with a new generation of individuals
    def _reproduce_and_replace(self):
        new_population = []

        # Keep going until we've filled the new generation
        while len(new_population) < len(self._population):
            # Pick the two parents
            if self._selection_type == type(self).selection_type.roulette:
                parents = self._pick_roulette([x.fitness() for x in self._population])
            else:
                parents = self._pick_tournament(len(self._population) // 2)

            # Potentially crossover the two parents
            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)

        # If we had an odd number (how?), we'll have one extra, so we remove it
        if len(new_population) > len(self._population):
            new_population.pop()

        # Replace reference
        self._population = new_population

    # With self._mutation_chance probability mutate each individual
    def _mutate(self):
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()

    # Run the genetic algorithm for max_generations iterations and return the best individual found
    def run(self):
        best = max(self._population, key=self._fitness_key)

        for generation in range(self._max_generations):
            # Early exit if we beat threshold
            if best.fitness() >= self._threshold:
                return best

            print(f'Generation {generation} Best {best.fitness()} Average {mean(map(self._fitness_key, self._population))}')

            self._reproduce_and_replace()
            self._mutate()
            highest = max(self._population, key=self._fitness_key)

            if highest.fitness() > best.fitness():
                # Found a new best
                best = highest

        return best
