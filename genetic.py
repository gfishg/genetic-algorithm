import numpy as np
import time

from population import Population

from evaluateFitness import evaluateFitness

from crossingOver import CrossingOver
from mutation import Mutation
from inversion import Inversion
from combinatePopulAndOffspring import Combinate
from selectionType import SelectionType
import matplotlib.pyplot as plt

class Genetic:

    def __init__(self, algorithm_config):
        start = time.time()
        variable_config = algorithm_config
        tab_epoch = []
        tab_mean = []
        tab_std = []
        tab_mean2 = []
        tab_std2 = []
        tab_epoch2 = []
        tab_elitary = []
        tab_epoch3 = []
        tab_epoch4 = []
        tab_elitary2 = []
        # chrom = Chromosome(variable_config)
        # chrom = chrom.initialChromosome(variable_config)
        # print(chrom)

        # generujemy populację
        pop = Population(variable_config)
        popul = pop.initialPopulation(variable_config)
        # print(popul)

        randomBinSol = evaluateFitness(variable_config)
        # pojedyncze x
        decision_variables = randomBinSol.decVariables(variable_config, popul)
        # print(decision_variables)

        # dekodujemy na odpowiedniki dziesietne
        decimal = randomBinSol.decoding(decision_variables, variable_config)
        # print(decimal)

        # zamieniamy na zmienne rzeczywiste
        real = randomBinSol.realVariables(variable_config, decimal)
        # print(real)

        # obliczamy wartosc funkcji dla kazdej kolumny

        func_solution = randomBinSol.funcSolution(variable_config, real)
        # print(func_solution)
        tab_mean.append(np.mean(func_solution))
        tab_std.append(np.std(func_solution))
        tab_epoch.append(0)

        counter = 1
        countEp = 0
        selType = SelectionType(variable_config)
        while (counter < variable_config.T):
            selection = selType.selType(variable_config, func_solution, popul)

            # KRZYŻOWANIE
            # print("KRZYŻOWANIE")
            crosov = CrossingOver(variable_config)
            crosingover = crosov.crosingOver(variable_config, selection)
            # print(crosingover)

            # MUTACJA
            # print("MUTACJA")
            mutat = Mutation(variable_config)
            mutation = mutat.mutation(variable_config, crosingover)
            # print(mutation)

            # INWERSJA
            # print("INWERSJA")
            inver = Inversion(variable_config)
            inversion = inver.inversion(variable_config, mutation)
            # print(inversion)

            offspring = np.asarray(inversion)
            # print(offspring)

            decision_variables2 = randomBinSol.decVariables(variable_config, offspring)
            # print(decision_variables2)

            # dekodujemy na odpowiedniki dziesietne
            decimal2 = randomBinSol.decoding(decision_variables2, variable_config)
            # print(decimal2)

            # zamieniamy na zmienne rzeczywiste
            real2 = randomBinSol.realVariables(variable_config, decimal2)
            # print(real2)

            # obliczamy wartosc funkcji dla kazdej kolumny

            func_solution2 = randomBinSol.funcSolution(variable_config, real2)

            combin = Combinate()
            combination = combin.newPopulation(popul, offspring, func_solution, func_solution2, variable_config)
            popul = combination[0]
            func_solution = combination[1]
            best = combination[2]

            tab_mean.append(np.mean(func_solution))
            tab_std.append(np.std(func_solution))
            tab_epoch.append(counter)
            tab_elitary.append(best)
            tab_epoch3.append(countEp)
            print(tab_elitary)
            if counter != 1:
                tab_mean2.append(np.mean(func_solution))
                tab_std2.append(np.std(func_solution))
                tab_epoch2.append(counter)

            if countEp != 0:
                tab_epoch4.append(countEp)
                tab_elitary2.append(best)

            counter += 1
            countEp += 1

        end = time.time()
        print("wynik czasu")
        el_time = (end - start)

        self.__el_time = el_time
        self.__tab_mean = tab_mean
        self.__tab_std = tab_std
        self.__tab_epoch = tab_epoch
        self.__tab_mean2 = tab_mean2
        self.__tab_std2 = tab_std2
        self.__tab_epoch2 = tab_epoch2
        self.__tab_elitary = tab_elitary
        self.__tab_epoch3 = tab_epoch3
        self.__tab_elitary2 = tab_elitary2
        self.__tab_epoch4 = tab_epoch4

    @property
    def el_time(self):
        return self.__el_time

    @property
    def tab_mean(self):
        plt.figure(figsize=(16,6))
        plt.subplot(1, 2, 1)
        plt.scatter(self.__tab_epoch, self.__tab_mean)
        plt.title("Wykres zależności średniej wartości funkcji od epoki")
        plt.xlabel("epoka")
        plt.ylabel("średnia wartość funkcji")
        plt.subplot(1, 2, 2)
        plt.scatter(self.__tab_epoch2, self.__tab_mean2)
        plt.title("Wykres zależności średniej wartości funkcji od epoki")
        plt.xlabel("epoka")
        plt.ylabel("średnia wartość funkcji")
        return plt.show()

    @property
    def tab_std(self):
        plt.figure(figsize=(16,6))
        plt.subplot(1, 2, 1)
        plt.scatter(self.__tab_epoch, self.__tab_std)
        plt.title("Wykres zależności odchylenia standardowego od epoki")
        plt.xlabel("epoka")
        plt.ylabel("odchylenie standardowe")
        plt.subplot(1, 2, 2)
        plt.scatter(self.__tab_epoch2, self.__tab_std2)
        plt.title("Wykres zależności odchylenia standardowego od epoki")
        plt.xlabel("epoka")
        plt.ylabel("odchylenie standardowe")
        return plt.show()

    @property
    def tab_elitary(self):
        plt.figure(figsize=(16, 6))
        plt.subplot(1, 2, 1)
        plt.scatter(self.__tab_epoch3, self.__tab_elitary)
        plt.title("Wykres zależności Wartości funkcji od epoki")
        plt.xlabel("epoka")
        plt.ylabel("wartość funkcji")
        plt.subplot(1, 2, 2)
        plt.scatter(self.__tab_epoch4, self.__tab_elitary2)
        plt.title("Wykres zależności Wartości funkcji od epoki")
        plt.xlabel("epoka")
        plt.ylabel("wartość funkcji")
        return plt.show()

    @property
    def fileResult(self):
        with open("wyniki.txt", "w") as f:
            f.write("{0},{1}\n".format('epoka', 'srednia'))
            for (epoch, mean) in zip(self.__tab_epoch, self.__tab_mean):
                f.write("{0},{1}\n".format(epoch, mean))
            f.write("{0},{1}\n".format('epoka', 'odchylenie st'))
            for (epoch, std) in zip(self.__tab_epoch, self.__tab_std):
                f.write("{0},{1}\n".format(epoch, std))
            f.write("{0},{1}\n".format('epoka', 'wartosc funkcji'))
            for (epoch, func) in zip(self.__tab_epoch, self.__tab_elitary):
                f.write("{0},{1}\n".format(epoch, func))
