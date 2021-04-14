import random
class ToutnamentSelection:

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def tourn(self, variable_config, func_solution, popul):
        numberOfTournaments = variable_config.Np
        k = variable_config.k
        fminormax = variable_config.fminormax
        matingpool = []

        func_sol = []
        for i in func_solution:
            func_sol.append(i)
        counter = 0
        zbior = {0}
        lista_zbiorow = []
        for i in range(numberOfTournaments):
            X = []
            x1 = func_sol[counter]
            #print("x1")
            #print(x1)
            func_sol.remove(func_sol[counter])
            #print(func_sol)
            x = random.sample(func_sol, k=k-1)
            #print(x)
            X.append(x1)
            if counter == 0:
                for i in x:
                    X.append(i)
            if counter > 0:
                for i in x:
                    X.append(i)
                temp = set(X)
                for i in lista_zbiorow:
                    if temp == i:
                        while temp == i:
                            X=[]
                            X.append(x1)
                            x = random.sample(func_sol, k=k - 1)
                            for i in x:
                                X.append(i)
                            temp = set(X)
            #print(X)
            temp = X[0]
            if fminormax == "min":
                for n in X:
                    if n < temp:
                        temp = n
                #print(temp)
            elif fminormax == "max":
                for n in X:
                    if n > temp:
                        temp = n
                #print(temp)
            count = 0
            for i in func_solution:
                if i == temp:
                    matingpool.append(popul[count])
                count+=1
            #matingpool.append(temp)
            el_zbioru = set(X)
            lista_zbiorow.append(el_zbioru)
            #print(lista_zbiorow)
            del func_sol
            func_sol = []
            for i in func_solution:
                func_sol.append(i)
            counter+=1
        return matingpool