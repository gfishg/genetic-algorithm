import random
class Mutation:

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def mutation(self, variable_config, offspring):
        pm = variable_config.pm
        whichm = variable_config.whichm
        D = variable_config.D
        n = variable_config.n
        #print(offspring)
        offspringAfterMutation = []
        if whichm == 1:
            for i in offspring:
                isMutationPerformed = random.random()
                #print(isMutationPerformed)
                if isMutationPerformed < pm:
                    if i[len(i)-1] == 1:
                        i[len(i) - 1] = 0
                    elif i[len(i)-1] == 0:
                        i[len(i) - 1] = 1
                offspringAfterMutation.append(i)
        if whichm == 2:
            for i in offspring:
                isMutationPerformed = random.random()
                #print(isMutationPerformed)
                randomNumber = random.randrange(0, (D*n - 1))
                if isMutationPerformed< pm:
                    for j in range(len(i)):
                        if j == randomNumber:
                            if i[j] == 0:
                                i[j] = 1
                            elif i[j] == 1:
                                i[j] = 0
                offspringAfterMutation.append(i)
        if whichm == 3:
            for i in offspring:
                isMutationPerformed = random.random()
                # print(isMutationPerformed)
                randomNumber = random.randrange(0, (D * n - 1))
                randomNumber2 = random.randrange(0, (D * n - 1))
                if isMutationPerformed < pm:
                    for j in range(len(i)):
                        if j == randomNumber:
                            if i[j] == 0:
                                i[j] = 1
                            elif i[j] == 1:
                                i[j] = 0
                        if j == randomNumber2:
                            if i[j] == 0:
                                i[j] = 1
                            elif i[j] == 1:
                                i[j] = 0
                offspringAfterMutation.append(i)

        return offspringAfterMutation