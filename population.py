from chromosome import Chromosome
import numpy as np
import variable_configuration

class Population:

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def initialPopulation(self, variable_config):
        pop = []
        chrom = Chromosome(variable_config)
        for i in range(variable_config.D*variable_config.Np):
            pop.append(chrom.initialChromosome(variable_config))
        pop = np.array(pop)
        pop = pop.reshape((variable_config.Np, (variable_config.D*variable_config.n)))
        return pop