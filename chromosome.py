import random
import numpy as np

class Chromosome:

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def initialChromosome(self, variable_config):
        chromosome = []
        for i in range(variable_config.n):
            chromosome.append(random.randrange(0,2))

        chromosome = np.array(chromosome)
        return chromosome

