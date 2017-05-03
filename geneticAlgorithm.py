# First attempt at a genetic algorithm
import random
import copy


class individual():

    def __init__(self, value='0000' ):
        self.fitness = 0 # integer
        self.value = value # string
        self.binaryLength = len(value) # integer used for mutations
        self.intValue = int(value, 2)
        self.updateFitness()

    def bitSwitch(self, x, y):
        x = list(x)
        y = list(y)
        for i in range(0, len(y)):
            if y[i] == '1':
                if x[i] == '1':
                    x[i] = '0'
                else:
                    x[i] = '1'
        return ''.join(x)


    def mutate(self):   # right now does 50% mutation rate, hope to make it more later
        mutateString = ''
        for i in range(0, self.binaryLength) :
            mutateString += str(random.randint(0,1))
        self.value = self.bitSwitch(self.value, mutateString)
        self.updateFitness()
        return
        # mutateString = ''
        # for i in range(0, self.maxBinaryLength) :
        #     mutateString += str(random.randint(0,1))
        #
        # print(bin(int(mutateString, 2 )))
        # print(bin(self.value))
        #
        # self.value = int(bin(self.value & int(mutateString, 2 )), 2 )

    def updateFitness(self):
        # this is where you would put the function to calculate fitness, for this
        # example im just going to use the int value for the bits
        self.fitness = int(self.value, 2 )



class GeneticAlgorithm():

    def __init__(self, populationSize=10, indiviuals=[]):
        self.populationSize = populationSize
        self.individuals = []

    def generateRandomIndividuals(self):
        # genereates a random set of starting individuals
        while len(self.individuals) < self.populationSize:
            val = ''.join([random.choice('10') for _ in range(4)])
            print(val)
            self.individuals.append(individual(value=val))
        return

    def crossover(self, x, y):
        #x,y are indiviuals of class individual
        # returns new individual

        binaryLength= x.binaryLength
        halfLength = binaryLength / 2
        x = list(x.value)
        y = list(y.value)

        crossoverList = []
        if random.randint(0,1) == 1:
            for i in range(0,halfLength):
                crossoverList.append(x[i])
            for l in range(halfLength, binaryLength):
                crossoverList.append(y[l])
        else:
            for i in range(0,halfLength):
                crossoverList.append(y[i])
            for l in range(halfLength, binaryLength):
                crossoverList.append(x[l])
        newInd = individual(value=''.join(crossoverList))
        newInd.mutate()
        return newInd

    def selection(self):
        # returns two random individuals from the list
        listCopy = copy.deepcopy(self.individuals)
        a = listCopy.pop(random.randint(0, len(listCopy)-1))
        b = listCopy.pop(random.randint(0, len(listCopy)-1))
        return a, b

    def run(self, epochs=10):
        iterations = 0
        while iterations<epochs:
            print("Iteration ", iterations)
            x, y = self.selection()
            newInd = self.crossover(x, y)
            self.individuals.append(newInd)
            self.individuals.sort(key=lambda x: x.fitness, reverse=True)
            self.individuals.pop()
            iterations += 1
        return





# binary in python
# a = int('1000', 2)
# print(bin(a & int('1110', 2)))
# print(a.bit_length())
# print("Radansdfjasdf", random.randint(0,12)))
# print(''.join([random.choice('10') for _ in range(4)]))
#
# print(bin(0b101 & 0b1111))
# print("yert?", 0b101.bit_length())
#
# print("random", random.randint(0, 15))
# print(bin(random.randint(0, 15)))



g = GeneticAlgorithm()
g.generateRandomIndividuals()
g.run(epochs=10)


for i in range(0, len(g.individuals)):
    print(g.individuals[i].value, g.individuals[i].fitness)


# b = [a,m,d]
# b.sort()
# b.sort(key=lambda x: x.fitness, reverse=True)
# print(b[0].value, b[1].value, b[2].value)

# a = [1,2,3,4]
# print(a.pop(1))
# print(a)

# print(m.fitness)
# print(m.value)
# m.mutate()
# print(m.value)
