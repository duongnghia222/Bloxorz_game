import random
from functions import check_win_dna
from math import sqrt
from block import Block
#  "up", "right", "down", "left" = [1,2,3,4]

U = "up"
R = "right"
D = "down"
L = "left"
direction = [U, R, D, L]

class DNA:
    def __init__(self, no_of_moves):
        self.gene_length = no_of_moves
        self.genes = []
        self.fitness = 0.0

        for i in range(no_of_moves):
            self.genes.append(random.choice(direction))

    def calculate_fitness(self, block, target):
        for gene in self.genes:
            if gene == 1:
                block.move_up()
            elif gene == 2:
                block.move_right()
            elif gene == 3:
                block.move_down()
            else:
                block.move_left()
            distance = sqrt(((block.x - target[1][0]) ** 2) + \
                            ((block.y - target[1][0]) ** 2))
            self.fitness += 1/distance

    def crossover(self, other_dna):
        child = DNA(self.gene_length)
        mid_point = random.randint(0, self.gene_length)

        for i in range(0, self.gene_length):
            if i < mid_point:
                child.genes[i] = other_dna.genes[i]
            else:
                child.genes[i] = self.genes[i]

        return child

    def mutate(self, rate):
        for i in range(self.gene_length):
            num = random.random()
            if num < rate:
                self.genes[i] = random.choice(direction)


class Population:
    def __init__(self, block, target, no_of_moves,mutation_rate, max_population):
        self.block = block
        self.target = target
        self.mutation_rate = mutation_rate
        self.max_population = max_population
        self.generation = 0
        self.matingPool = []
        self.population = []
        self.finished = False
        self.got = None

        for i in range(max_population):
            self.population.append(DNA(no_of_moves))

    def calculate_fitness(self):
        for dna in self.population:
            dna.calculate_fitness(self.block, self.target)

    def evaluate(self):
        for dna in self.population:
            if check_win_dna(dna, self.block):
                self.finished = True
                self.got = dna

    def print_best_dna(self):
        max_fitness = 0
        best_dna = None
        for dna in self.population:
            if dna.fitness > max_fitness:
                max_fitness = dna.fitness
                best_dna = dna
        print(self.generation, max_fitness, best_dna.genes)

    def selection(self):
        self.matingPool = []
        max_fitness = 0
        for dna in self.population:
            if dna.fitness > max_fitness:
                max_fitness = dna.fitness
        fitness = 0
        for dna in self.population:
            if max_fitness != 0:
                fitness = dna.fitness / max_fitness
            n = int(round(fitness * 100))
            for i in range(n):
                self.matingPool.append(dna)

    def generate(self):
        if len(self.matingPool) != 0:
            for i in range(len(self.population)):
                a = random.randint(0, len(self.matingPool) - 1)
                b = random.randint(0, len(self.matingPool) - 1)
                dna_A = self.matingPool[a]
                dna_B = self.matingPool[b]

                new_dna = dna_A.crossover(dna_B)

                new_dna.mutate(self.mutation_rate)

                self.population[i] = new_dna

        self.generation += 1


def ga(block):
    start_x = block.x
    start_y = block.y
    g = [0, 0]
    for i, r in enumerate(block.game_map):
        if 'G' in r:
            g = [r.index('G'), i]
            break
    start_point = [start_x, start_y]
    target = [start_point, g]
    population_num = 100
    mutation_rate = 0.1
    no_of_moves = 15
    population = Population(block, target, no_of_moves, mutation_rate, population_num)
    while not population.finished:
        population.evaluate()
        population.calculate_fitness()
        population.print_best_dna()
        population.selection()
        population.generate()



