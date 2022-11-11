import random as rnd

class DNA:
    def __init__(self, gene_length):
        self.gene_length = gene_length
        self.genes = []
        self.fitness = 0.0

        for i in range(gene_length):
            self.genes.append(self.newChar())

    def newChar(self):
        c = round(rnd.randint(63, 122))
        if c == 63:
            c = 32
        if c == 64:
            c = 46
        return chr(int(c))

    def getPhrase(self):
        return "".join(self.genes)

    def calcFitness(self, target):
        score = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score+=1

        self.fitness = score / float(len(target))


    def crossover(self, other_dna):
        child = DNA(self.gene_length)
        mid_point = rnd.randint(0, self.gene_length)

        for i in range(0, self.gene_length):
            if i < mid_point:
                child.genes[i] = other_dna.genes[i]
            else:
                child.genes[i] = self.genes[i]

        return child


    def mutate(self, rate):
        for i in range(self.gene_length):
            num = rnd.random()
            if num < rate:
                self.genes[i] = self.newChar()




class Population:
    def __init__(self, target, mutationRate, popmax):
        self.target = target
        self.mutationRate = mutationRate
        self.popmax = popmax
        self.generation = 0
        self.matingPool = []
        self.population = []
        self.finished = False
        self.got = ""

        for i in range(popmax):
            self.population.append(DNA(len(target)))

    def calcFitness(self):
        for dna in self.population:
            dna.calcFitness(self.target)

    def naturalSelection(self):
        self.matingPool = []
        maxFitness = 0
        for dna in self.population:
            if dna.fitness > maxFitness:
                maxFitness = dna.fitness

        fitness = 0
        for dna in self.population:
            if maxFitness != 0:
                fitness = dna.fitness / maxFitness
            n = int(round(fitness * 100))
            for i in range(n):
                self.matingPool.append(dna)

    def generate(self):
        if len(self.matingPool) != 0:
            for i in range(len(self.population)):
                a = rnd.randint(0, len(self.matingPool) - 1)
                b = rnd.randint(0, len(self.matingPool) - 1)
                dna_A = self.matingPool[a]
                dna_B = self.matingPool[b]

                new_dna = dna_A.crossover(dna_B)

                new_dna.mutate(self.mutationRate)

                self.population[i] = new_dna

        self.generation += 1

    def evaluate(self):
        for dna in self.population:
            if dna.getPhrase() == self.target:
                self.finished = True
                self.got = dna.getPhrase()

    def printPop(self):
        arr = []
        for dna in self.population:
            arr.append(dna.getPhrase())
        print(arr)

    def printBest(self):
        maxFit = 0
        dd = None
        for dna in self.population:
            if dna.fitness > maxFit:
                maxFit = dna.fitness
                dd = dna
        print(self.generation, maxFit, dd.getPhrase())



target = "To be or not to be"
population_num = 1000
mutation_rate = 0.01

population = Population(target, mutation_rate, population_num)

while(not population.finished):
    # Will stop the loop if it found the target
    population.evaluate()

    # Will calculate the fitness for each DNA (Individual)
    population.calcFitness()

    # Will print the best fitness for each generation
    population.printBest()

    population.naturalSelection()

    population.generate()
