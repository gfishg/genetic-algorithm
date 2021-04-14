import sys
import numpy as np
import matplotlib.pyplot as plt
from click.testing import Result

from chromosome import Chromosome
from population import Population
from variable_configuration import VariableConfig
from evaluateFitness import evaluateFitness
from roulette_wheel import Roulette_wheel
from tournamentSelection import ToutnamentSelection
from bestSelection import BestSelection
from crossingOver import CrossingOver
from mutation import Mutation
from inversion import Inversion
from combinatePopulAndOffspring import Combinate
from selectionType import SelectionType


variable_config = VariableConfig(4, 5, 2, 0, 30, 2, 'min', 80, 0.8, 3, 0.3, 3, 0.5, 20, 2, 2)
#chrom = Chromosome(variable_config)
#chrom = chrom.initialChromosome(variable_config)
#print(chrom)
tab_epoch = []
tab_mean = []
tab_std = []
tab_mean2 = []
tab_std2 = []
tab_epoch2 = []
tab_elitary = []
#generujemy populację
pop = Population(variable_config)
popul = pop.initialPopulation(variable_config)
#print(popul)


randomBinSol = evaluateFitness(variable_config)
#pojedyncze x
decision_variables = randomBinSol.decVariables(variable_config, popul)
#print(decision_variables)

#dekodujemy na odpowiedniki dziesietne
decimal = randomBinSol.decoding(decision_variables,variable_config)
#print(decimal)

#zamieniamy na zmienne rzeczywiste
real = randomBinSol.realVariables(variable_config, decimal)
#print(real)

#obliczamy wartosc funkcji dla kazdej kolumny
func_solution = randomBinSol.funcSolution(variable_config, real)
print("printuje func_solution")
print(func_solution)
#tab_mean.append(np.mean(func_solution))
#tab_std.append(np.std(func_solution))
#tab_epoch.append(0)
print("tab mean")
print(tab_mean)
print(tab_std)
counter = 1
selType = SelectionType(variable_config)
while(counter<=variable_config.T):

    selection = selType.selType(variable_config, func_solution, popul)

    '''
    if variable_config.chooseSel == 1:
        print("turniej")
        #TURNIEJ
        tournam = ToutnamentSelection(variable_config)

        tournamentSelection = tournam.tourn(variable_config, func_solution, popul)
        selection = tournamentSelection
        #print(tournamentSelection)

    if variable_config.chooseSel == 2:
        #BEST SELECTION
        print("bestsel")
        bestsel = BestSelection(variable_config)
        bestselection = bestsel.bests(variable_config, func_solution, popul)
        selection = bestselection
        #print(bestselection)

    if variable_config.chooseSel == 3:
        #ROULETTE
        print("roullette")
        roulet = Roulette_wheel(variable_config)
        roulette = roulet.roulette(variable_config, func_solution, popul)
        selection = roulette
        #print(roulette)
    '''

    #KRZYŻOWANIE
    #print("KRZYŻOWANIE")
    crosov = CrossingOver(variable_config)
    crosingover = crosov.crosingOver(variable_config, selection)
    #print(crosingover)

    #MUTACJA
    #print("MUTACJA")
    mutat = Mutation(variable_config)
    mutation = mutat.mutation(variable_config, crosingover)
    #print(mutation)

    #INWERSJA
    #print("INWERSJA")
    inver = Inversion(variable_config)
    inversion = inver.inversion(variable_config, mutation)
    #print(inversion)

    offspring = np.asarray(inversion)
    #print(offspring)


    decision_variables2 = randomBinSol.decVariables(variable_config, offspring)
    #print(decision_variables2)

    #dekodujemy na odpowiedniki dziesietne
    decimal2 = randomBinSol.decoding(decision_variables2,variable_config)
    #print(decimal2)

    #zamieniamy na zmienne rzeczywiste
    real2 = randomBinSol.realVariables(variable_config, decimal2)
    #print(real2)

    #obliczamy wartosc funkcji dla kazdej kolumny

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
    if counter != 1:
        tab_mean2.append(np.mean(func_solution))
        tab_std2.append(np.std(func_solution))
        tab_epoch2.append(counter)
    print("counter", counter)
    print(popul)
    print(func_solution)
    counter+=1
print(tab_mean)
print(tab_std)
print(tab_epoch)
print(tab_elitary)


plt.figure()
plt.scatter(tab_epoch, tab_mean)
plt.title("Wykres zależności średniej wartości funkcji od epoki")
plt.xlabel("epoka")
plt.ylabel("średnia wartość funkcji")
#plt.show()


plt.figure()
plt.scatter(tab_epoch2, tab_mean2)
plt.title("Wykres zależności średniej wartości funkcji od epoki")
plt.xlabel("epoka")
plt.ylabel("średnia wartość funkcji")
#plt.show()

plt.figure()
plt.scatter(tab_epoch, tab_std)
plt.title("Wykres zależności odchylenia standardowego od epoki")
plt.xlabel("epoka")
plt.ylabel("odchylenie standardowe")
plt.show()

plt.figure()
plt.scatter(tab_epoch2, tab_std2)
plt.title("Wykres zależności średniej wartości funkcji od epoki")
plt.xlabel("epoka")
plt.ylabel("średnia wartość funkcji")
plt.show()

plt.figure()
plt.scatter(tab_epoch, tab_elitary)
plt.title("Wykres zależności Wartości funkcji od epoki")
plt.xlabel("epoka")
plt.ylabel("wartość funkcji")
plt.show()


print(sys.version)
with open("wyniki.txt","w") as f:
    f.write("{0},{1}\n".format('epoka', 'srednia'))
    for (epoch,mean) in zip(tab_epoch,tab_mean):
        f.write("{0},{1}\n".format(epoch,mean))
    f.write("{0},{1}\n".format('epoka', 'odchylenie st'))
    for (epoch, std) in zip(tab_epoch, tab_std):
        f.write("{0},{1}\n".format(epoch, std))
    f.write("{0},{1}\n".format('epoka', 'wartosc funkcji'))
    for (epoch, func) in zip(tab_epoch, tab_elitary):
        f.write("{0},{1}\n".format(epoch, func))