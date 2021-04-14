class VariableConfig:

    def __init__(self, Np, n, D, xminfun, xmaxfun, k, fminormax, bestpercent, pc, whichco, pm, whichm, pi, T, chooseSel, elitStr):
        self.__Np = Np # wielkosc populacji
        self.__n = n  #bit length, dlugosc chromosomu
        self.__D = D # decision variables (osobnik)
        self.__xminfun = xminfun #dolny przedział funkcji
        self.__xmaxfun = xmaxfun #gorny przedzial funkcji
        self.__k = k # tournament size
        self.__fminormax = fminormax #czy szukamy minimum ('min') czy maksimum ('max')
        self.__bestpercent = bestpercent #procent wybieranych najlepszych
        self.__pc = pc #perform crossover
        self.__whichco = whichco #jakie crossingover -> jedno, dwu, trzypunktoowe lub jednorodne (odpowiednio 1, 2, 3, 4)
        self.__pm = pm #prawdopodobienstwo wystapienia mutacji
        self.__whichm = whichm #ktory rodzaj mutacji (1- brzegowa, 2- jednopunktowa 3- dwupunktowa
        self.__pi = pi #prawdopodobienstwo wystapienia inwersji
        self.__T = T #liczba epok
        self.__chooseSel = chooseSel #która metoda selekcji (1 - turniej, 2-bestsel 3-ruletka)
        self.__elitStr = elitStr #ilość zachowanych najlepszych osobników

    @property
    def Np(self):
        return self.__Np

    @property
    def n(self):
        return self.__n

    @property
    def D(self):
        return self.__D

    @property
    def xminfun(self):
        return self.__xminfun

    @property
    def xmaxfun(self):
        return self.__xmaxfun

    @property
    def fminormax(self):
        return self.__fminormax

    @property
    def k(self):
        return self.__k

    @property
    def bestpercent(self):
        return self.__bestpercent

    @property
    def pc(self):
        return self.__pc

    @property
    def whichco(self):
        return self.__whichco

    @property
    def pm(self):
        return self.__pm

    @property
    def whichm(self):
        return self.__whichm

    @property
    def pi(self):
        return self.__pi

    @property
    def T(self):
        return self.__T

    @property
    def chooseSel(self):
        return self.__chooseSel

    @property
    def elitStr(self):
        return self.__elitStr