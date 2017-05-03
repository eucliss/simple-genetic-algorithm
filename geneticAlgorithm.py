# First attempt at a genetic algorithm
import random
import copy


# Class that makes up the population
class individual():

    # Just using strings to represent the bits
    def __init__(self, value='0000' ):
        self.fitness = 0 # integer
        self.value = value # string
        self.binaryLength = len(value) # integer used for mutations
        self.intValue = int(value, 2)
        self.updateFitness()

    # Function that basically just switches the bit values in the string x if the mutation string y says to
    # Not great but it works
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


    # Mutate function to decide if the bit should be mutated aka switched
    # uses a random number in range 0,1 to decide, so basically 50% of bits get mutated in an individual
    def mutate(self):   
        mutateString = ''
        for i in range(0, self.binaryLength) :
            mutateString += str(random.randint(0,1))
        self.value = self.bitSwitch(self.value, mutateString)
        self.updateFitness()
        return

    # This is where you would put the function to calculate fitness, for this
    #   example im just going to use the int value for the bits
    def updateFitness(self):
        self.fitness = int(self.value, 2 )

# Actual class that will run the algorithm 
class GeneticAlgorithm():

    # Initialize the variables for the algo
    def __init__(self, populationSize=10, indiviuals=[]):
        self.populationSize = populationSize
        self.individuals = []

    # Generates random individuals for the population size 
    def generateRandomIndividuals(self):
        while len(self.individuals) < self.populationSize:
            val = ''.join([random.choice('10') for _ in range(4)])
            print(val)
            self.individuals.append(individual(value=val))
        return

    # Crosses two individuals it takes as parameters to make a new individual and mutates it
    def crossover(self, x, y):
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
        # Mutate the new individual
        newInd.mutate()
        return newInd

    # Selects two random individuals from the population 
    def selection(self):
        # returns two random individuals from the list
        listCopy = copy.deepcopy(self.individuals)
        a = listCopy.pop(random.randint(0, len(listCopy)-1))
        b = listCopy.pop(random.randint(0, len(listCopy)-1))
        return a, b

    # Runs the algorithm for a certain number of iterations optimizing the population based on fitness
    #   epochs is a bad variable name here, cause it doesnt really go over the whole population, just picks two 
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
