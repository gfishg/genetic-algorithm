import random

class Inversion:
    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def inversion(self, variable_config, mutation):
        D = variable_config.D
        n = variable_config.n
        pi = variable_config.pi
        offspringAfterInversion = []
        for i in mutation:
            isInversionPerformed = random.random()
            if isInversionPerformed < pi:
                tabToInversion = []
                inversionSite = random.randrange(1, (D * n - 1))
                inversionSite2 = random.randrange(1, (D * n - 1))
                if inversionSite == inversionSite2:
                    while inversionSite == inversionSite2:
                        inversionSite2 = random.randrange(1, (D * n - 1))
                tabToInversion.append(inversionSite)
                tabToInversion.append(inversionSite2)
                tabToInversion.sort()
                #print(tabToInversion)
                stack = []
                #print(i)
                offspringInv = []
                for j in range(tabToInversion[0]):
                    offspringInv.append(i[j])
                for j in range(tabToInversion[0], tabToInversion[1]):
                    stack.append(i[j])
                #print(stack)
                stack.reverse()
                for j in range(len(stack)):
                    offspringInv.append(stack[j])
                for j in range(tabToInversion[1], n * D):
                    offspringInv.append(i[j])
                del stack
                del tabToInversion
                #print(i)
                #print(offspringInv)
                offspringAfterInversion.append(offspringInv)
            else:
                offspringAfterInversion.append(i)
        return offspringAfterInversion