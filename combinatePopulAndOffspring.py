import numpy as np


class Combinate:

    def newPopulation(self, popul, offspring, func_solution, func_solution2, variable_config):
        Np = variable_config.Np
        nextPop = variable_config.elitStr
        print(nextPop)
        tab = []

        for i in popul:
            tab.append(i)
        for i in offspring:
            tab.append(i)

        tab = np.array(tab)
        #print("tab")
        #print(tab)
        func_solution = np.array(func_solution)
        func_solution2 = np.array(func_solution2)

        tab_func_solution = []
        for i in func_solution:
            tab_func_solution.append(i)
        for i in func_solution2:
            tab_func_solution.append(i)

        print(tab_func_solution)
        #counter = Np
        counter = nextPop
        newPopulindex = []
        tabWithFunction = []
        tabBest = []
        if (variable_config.fminormax == 'min'):
            tab_func_solution2 = []
            for i, v in enumerate(tab_func_solution):
                tab_func_solution2.append([v, i])
            tab_func_solution2 = sorted(tab_func_solution2)
            tabBest.append(tab_func_solution2[0][0])
            for i in range(0, counter):
                # print(lista2[i])
                tabWithFunction.append(tab_func_solution2[i][0])
                newPopulindex.append(tab_func_solution2[i][1])

        '''
        if(variable_config.fminormax == 'min'):
            for i in range(counter):
                min_value = min(tab_func_solution)
                #print(min_value)
                min_index = tab_func_solution.index(min_value)
                #print(min_index)
                newPopulindex.append(min_index)
                tabWithFunction.append(min_value)
                tab_func_solution[min_index] = 999999999999999
                #print(tab_func_solution)
'''
        if (variable_config.fminormax == 'max'):
            for i in range(counter):
                max_value = max(tab_func_solution)
                #print(max_value)
                max_index = tab_func_solution.index(max_value)
                #print(max_index)
                newPopulindex.append(max_index)
                tabWithFunction.append(max_value)
                tab_func_solution[max_index] = 0
                # print(tab_func_solution)
                if i == 0:
                    tabBest.append(max_value)

        #print("indeksy")
        #print(newPopulindex)
        newPopulation = []

        for i in newPopulindex:
            for j in range(len(tab)):
                if i == j:
                    newPopulation.append(tab[j])

        newPopulation = np.array(newPopulation)
        #print(newPopulation)
        #print(popul)
        #print(type(func_solution))
        #print(tabWithFunction)
        return newPopulation, tabWithFunction, tabBest