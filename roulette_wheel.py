import matplotlib.pyplot as plt
import numpy as np
from pip._vendor.webencodings import labels
import random

class Roulette_wheel:
    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def roulette(self, variable_config, func_solution, popul):
        mating_pool = []
        Np = variable_config.Np
        #for i in range(mating_pool_size):
        func_sol = []
        fminormax = variable_config.fminormax
        for i in func_solution:
            func_sol.append(i)
        while len(mating_pool) < Np:
            if(fminormax == "max"):
                sumFunction = 0
                for i in func_sol:
                    sumFunction += i

                #print(sumFunction)

                probability = []
                dystrybuanta = []
                for i in func_sol:
                    probability.append(i/sumFunction)
                #print("probability")
                #print(probability)

                sumDystrybuanta = 0
                for i in probability:
                    sumDystrybuanta+= i
                    dystrybuanta.append(sumDystrybuanta)

                #print(dystrybuanta)

                randomRooulette = random.random()
                #print(randomRooulette)
                counter = 0
                # print(func_solution[counter])
                for i in range(len(dystrybuanta)):
                    if dystrybuanta[counter] < randomRooulette and randomRooulette < dystrybuanta[counter + 1]:
                        answer = func_solution[counter]
                        #print(answer)
                        #print(popul[counter])
                        mating_pool.append(popul[counter])
                    counter += 1
            #print("dystrybuanta")
            #print(dystrybuanta)


            if fminormax == "min":
                invertedfunc_sol = []
                for i in func_sol:
                    invertedfunc_sol.append(1/i)
                #print("invertedfunc_sol")
                #print(invertedfunc_sol)
                invertedSum = 0
                for i in invertedfunc_sol:
                    invertedSum+=i
                #print("invertedSum")
                #print(invertedSum)
                probabilityMin = []
                for i in invertedfunc_sol:
                    probabilityMin.append(i/invertedSum)
                #print("probabilityMin")
                #print(probabilityMin)
                sumDystrybuantaMin = 0
                dystrybuantaMin = []
                for i in probabilityMin:
                    sumDystrybuantaMin+=i
                    dystrybuantaMin.append(sumDystrybuantaMin)
                #print("dystrybuantaMin")
                #print(dystrybuantaMin)

                randomRooulette = random.random()
                #print(randomRooulette)
                counter = 0
                #print(func_solution[counter])
                for i in range(len(dystrybuantaMin)):
                    if dystrybuantaMin[counter] < randomRooulette and randomRooulette < dystrybuantaMin[counter+1]:
                        answer = func_solution[counter]
                        #print(answer)
                        #print(popul[counter])
                        mating_pool.append(popul[counter])
                    counter+=1

        return mating_pool