import random

import numpy as np


class CrossingOver:

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def crosingOver(self, variable_config, mating_pool):
        #mating pool to parents
        pc = variable_config.pc
        Np = variable_config.Np
        n = variable_config.n
        D = variable_config.D
        whichco = variable_config.whichco
        mat_pool = []
        for i in mating_pool:
            mat_pool.append(i)
        offspring = []
        if whichco == 1:
            while len(offspring) != len(mating_pool):
                parent1, parent2 = random.sample(mat_pool, k=2)
                isCrossoverPerformed = random.random()
                if isCrossoverPerformed < pc:
                    crossoverSite = random.randrange(1, (D*n-1))
                    #print(crossoverSite)
                    offspring1 = []
                    offspring2 = []
                    for i in range(crossoverSite):
                        offspring1.append(parent1[i])
                    for i in range(crossoverSite, n*D):
                        offspring1.append(parent2[i])
                    for i in range(crossoverSite):
                        offspring2.append(parent2[i])
                    for i in range(crossoverSite, n*D):
                        offspring2.append(parent1[i])
                    #print(parent1)
                    #print(parent2)
                    #print(offspring1)
                    #print(offspring2)
                    offspring.append(offspring1)
                    if len(offspring) != len(mating_pool):
                        offspring.append(offspring2)
                else:
                    parent1 = parent1.tolist()
                    parent2 = parent2.tolist()
                    offspring.append(parent1)
                    if len(offspring) != len(mating_pool):
                        offspring.append(parent2)
        if whichco == 2:
            tabToCrossoverSite = []
            while len(offspring) != len(mating_pool):
                parent1, parent2 = random.sample(mat_pool, k=2)
                isCrossoverPerformed = random.random()
                #print(isCrossoverPerformed)
                if isCrossoverPerformed < pc:
                    crossoverSite = random.randrange(1, (D*n-1))
                    crossoverSite2 = random.randrange(1, (D*n-1))
                    if crossoverSite == crossoverSite2:
                        while crossoverSite == crossoverSite2:
                            crossoverSite2 = random.randrange(1, (D * n - 1))
                    tabToCrossoverSite.append(crossoverSite)
                    tabToCrossoverSite.append(crossoverSite2)
                    tabToCrossoverSite.sort()
                    #print(tabToCrossoverSite)
                    offspring1 = []
                    offspring2 = []
                    for i in range(tabToCrossoverSite[0]):
                        offspring1.append(parent1[i])
                    for i in range(tabToCrossoverSite[0], tabToCrossoverSite[1]):
                        offspring1.append(parent2[i])
                    for i in range(tabToCrossoverSite[1], n*D):
                        offspring1.append(parent1[i])
                    for i in range(tabToCrossoverSite[0]):
                        offspring2.append(parent2[i])
                    for i in range(tabToCrossoverSite[0], tabToCrossoverSite[1]):
                        offspring2.append(parent1[i])
                    for i in range(tabToCrossoverSite[1], n*D):
                        offspring2.append(parent2[i])
                    #print(parent1)
                    #print(parent2)
                    #print(offspring1)
                    #print(offspring2)
                    tabToCrossoverSite = []
                    offspring.append(offspring1)
                    if len(offspring) != len(mating_pool):
                        offspring.append(offspring2)
                else:
                    parent1 = parent1.tolist()
                    parent2 = parent2.tolist()
                    offspring.append(parent1)
                    if len(offspring) != len(mating_pool):
                        offspring.append(parent2)
        if whichco == 3:
            tabToCrossoverSite = []
            while len(offspring) != len(mating_pool):
                parent1, parent2 = random.sample(mat_pool, k=2)
                isCrossoverPerformed = random.random()
                #print(isCrossoverPerformed)
                if isCrossoverPerformed < pc:
                    crossoverSite = random.randrange(1, (D*n-1))
                    crossoverSite2 = random.randrange(1, (D*n-1))
                    crossoverSite3 = random.randrange(1, (D * n - 1))
                    if crossoverSite == crossoverSite2:
                        while crossoverSite == crossoverSite2:
                            crossoverSite2 = random.randrange(1, (D * n - 1))

                    if crossoverSite3 == crossoverSite or crossoverSite3 == crossoverSite2:
                        while crossoverSite3 == crossoverSite or crossoverSite3 == crossoverSite2:
                            crossoverSite3 = random.randrange(1, (D * n - 1))

                    tabToCrossoverSite.append(crossoverSite)
                    tabToCrossoverSite.append(crossoverSite2)
                    tabToCrossoverSite.append(crossoverSite3)
                    tabToCrossoverSite.sort()
                    #print(tabToCrossoverSite)
                    offspring1 = []
                    offspring2 = []
                    for i in range(tabToCrossoverSite[0]):
                        offspring1.append(parent1[i])
                    for i in range(tabToCrossoverSite[0], tabToCrossoverSite[1]):
                        offspring1.append(parent2[i])
                    for i in range(tabToCrossoverSite[1], tabToCrossoverSite[2]):
                        offspring1.append(parent1[i])
                    for i in range(tabToCrossoverSite[2], n*D):
                        offspring1.append(parent2[i])
                    for i in range(tabToCrossoverSite[0]):
                        offspring2.append(parent2[i])
                    for i in range(tabToCrossoverSite[0], tabToCrossoverSite[1]):
                        offspring2.append(parent1[i])
                    for i in range(tabToCrossoverSite[1], tabToCrossoverSite[2]):
                        offspring2.append(parent2[i])
                    for i in range(tabToCrossoverSite[2], n*D):
                        offspring2.append(parent1[i])
                    #print(parent1)
                    #print(parent2)
                    #print(offspring1)
                    #print(offspring2)
                    tabToCrossoverSite = []
                    offspring.append(offspring1)
                    if len(offspring) != len(mating_pool):
                        offspring.append(offspring2)
                else:
                    parent1 = parent1.tolist()
                    parent2 = parent2.tolist()
                    offspring.append(parent1)
                    if len(offspring) != len(mating_pool):
                        offspring.append(parent2)

        if whichco == 4:
            while len(offspring) != len(mating_pool):
                parent1, parent2 = random.sample(mat_pool, k=2)
                isCrossoverPerformed = random.random()
                #print(isCrossoverPerformed)
                if isCrossoverPerformed < pc:
                    offspring1 = []
                    offspring2 = []
                    counter = 0

                    while counter<len(parent1):
                        offspring1.append(parent1[counter])
                        offspring1.append(parent2[counter+1])
                        offspring2.append(parent2[counter])
                        offspring2.append(parent1[counter+1])
                        counter+=2
                    #print(parent1)
                    #print(parent2)
                    #print(offspring1)
                    #print(offspring2)
                    offspring.append(offspring1)
                    if len(offspring) != len(mating_pool):
                        offspring.append(offspring2)
                else:
                    parent1 = parent1.tolist()
                    parent2 = parent2.tolist()
                    offspring.append(parent1)
                    if len(offspring) != len(mating_pool):
                        offspring.append(parent2)

        return offspring