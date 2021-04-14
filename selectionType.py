from bestSelection import BestSelection
from roulette_wheel import Roulette_wheel
from tournamentSelection import ToutnamentSelection


class SelectionType:

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    def selType(self, variable_config, func_solution, popul):
        if variable_config.chooseSel == 1:
            print("turniej")
            # TURNIEJ
            tournam = ToutnamentSelection(variable_config)

            tournamentSelection = tournam.tourn(variable_config, func_solution, popul)
            selection = tournamentSelection
            # print(tournamentSelection)

        if variable_config.chooseSel == 2:
            # BEST SELECTION
            print("bestsel")
            bestsel = BestSelection(variable_config)
            bestselection = bestsel.bests(variable_config, func_solution, popul)
            selection = bestselection
            # print(bestselection)

        if variable_config.chooseSel == 3:
            # ROULETTE
            print("roullette")
            roulet = Roulette_wheel(variable_config)
            roulette = roulet.roulette(variable_config, func_solution, popul)
            selection = roulette
            # print(roulette)

        return selection