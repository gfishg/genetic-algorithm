import math
class BestSelection:

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def bests(self, variable_config, func_solution, popul):
        percent = variable_config.bestpercent
        fminormax = variable_config.fminormax
        Np = variable_config.Np
        #print(Np)
        func_sol = []
        for i in func_solution:
            func_sol.append(i)
        func_sol.sort()
        #print(func_sol)
        percentToNumber = (percent*Np / 100)
        percentToNumber = math.ceil(percentToNumber)
        #print(percentToNumber)
        tableBest = []
        matingpool = []
        while len(tableBest) != Np:
            if fminormax == "min":
                counter = 0
                for i in func_sol:
                    if counter < percentToNumber:
                        tableBest.append(i)
                    counter+=1
            #print(tableBest)

            if fminormax == "max":
                tmp = len(func_sol) - 1
                counter = 0
                while(counter<percentToNumber):
                    tableBest.append(func_sol[tmp])
                    tmp-=1
                    counter+=1
        #print(tableBest)

        for i in tableBest:
            count = 0
            while i != func_solution[count]:
                count+=1
            matingpool.append(popul[count])
        return matingpool