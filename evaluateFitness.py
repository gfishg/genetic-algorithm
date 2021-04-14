from function import Function
import numpy as np

class evaluateFitness():

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def decVariables(self, variable_config, popul):
        A = popul

        #Split all population to single decision variables
        E = []
        counter = 0
        for i in range(variable_config.D):
            E.append(A[0:variable_config.Np, counter:variable_config.n+i*variable_config.n])
            counter = counter + variable_config.n
            i=i+1

        E = np.array(E)
        return E
        #print(E)

    def decoding(self, E, variable_config):
        #decoding to decimals
        table = []
        for i in E:
            counter = 0
            while (counter<variable_config.Np):
                a = (i[counter,:])
                table.append(self.decimalDecoding(variable_config, a))
                counter+=1
        return table

    def decimalDecoding(self, variable_config, a):
        dlugosc = (len(a))
        counter = variable_config.n-1
        suma = 0
        for i in range(dlugosc):
            x = a[i] * (2**counter)
            suma += x
            counter -= 1
        return(suma)

    def realVariables(self, variable_config, decimal):
        decimal = np.array(decimal)
        tab = []
        for i in decimal:
            x = variable_config.xminfun + ((variable_config.xmaxfun - variable_config.xminfun)/(2 ** variable_config.n - 1))*i
            tab.append(x)
        tab = np.array(tab)
        tab = tab.reshape(variable_config.D, variable_config.Np)
        return tab

    def funcSolution(self, variable_config, real):
        counter = 0
        tab = []
        while(counter<variable_config.Np):
            for i in range(variable_config.Np):
                x = (real[:,counter])
                #print(x)
                tab.append(Function.functionEvaluate(x))
                counter+=1
            return tab
