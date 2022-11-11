import random
from functions import check_win

#  "up", "right", "left", "down" = [1,2,3,4]
direction = [1, 2, 3, 4]

class DNA:
    def __init__(self, gene_length):
        self.gene_length = gene_length
        self.genes = []
        self.fitness = 0.0

        for i in range(len(gene_length)):
            self.genes.append(random.choice(direction))

    def calculate_fitness(self, target):
        pass




class Population:
    def __init__(self, target, mutation_rate, max_population):
        self.target = target
        self.mutation_rate = mutation_rate
        self.max_population = max_population
        self.generation = 0
        self.matingPool = []
        self.population = []
        self.finished = False
        self.got = None

        for i in range(max_population):
            self.population.append(DNA(len(target)))

    def calculate_fitness(self):
        for dna in self.population:
            dna.calculate_fitness(self.target)

    def evaluate(self):
        for dna in self.population:
            if check_win(dna):
                self.finished = True
                self.got = dna




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
    population_num = 1000
    mutation_rate = 0.01
    population = Population(target, mutation_rate, population_num)
    while not population.finished:
        population.evaluate()
        population.calculate_fitness()



