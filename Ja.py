import random

def printGegevensOverPeriode(minTemp, maxTemp, eindDag):
    Gemiddelde = []
    index = -1
    for i in maxTemp:
        index += 1
        Gemiddelde += ( i + minTemp[index]/2)
    print(f'De hittegolf gebeurde in het jaar {1900 + int(eindDag/365)}. De maximale temperatuur bedroeg {max(maxTemp)} en de minimale temperatuur bedroeg {min(minTemp)} De gemiddelde temperatuur bedroeg {int(sum(Gemiddelde)/len(Gemiddelde))}.')

def zoekHitteGolven(minTemperaturen, maxTemperaturen):
    maxTemp = []
    minTemp = []
    teller = 0
    eindDag = 0
    index = -1

    for i in maximumTemperaturen:
        if i >= 25:
            maxTemp.append(i)
            minTemp.append(minimumTemperaturen[index])
        if i < 25:
            for j in maxTemp:
                if j >= 30:
                    teller += 1
            if teller >= 2:
                eindDag = index - 1
                printGegevensOverPeriode(minTemp, maxTemp, eindDag)
                maxTemp.clear()
                minTemp.clear()
            else:
                maxTemp.clear()
                minTemp.clear()
            maxTemp.clear()
            minTemp.clear()
    index += 1

#Testfunctie
def leesMinimumTemperaturenIn():
    minimumTemperaturen = []
    for i in range(0, AANTAL_DAGEN):
        n = random.randint(1,25)
        minimumTemperaturen.append(n)
    return minimumTemperaturen
def leesMaximumTemperaturenIn():
    maximumTemperaturen = []
    for i in range(0, AANTAL_DAGEN):
        n = random.randint(1,10)
        maximumTemperaturen.append(minimumTemperaturen[i] + n)
    return maximumTemperaturen
# ______________________________________________________________________

AANTAL_DAGEN = 36500
minimumTemperaturen = [.0]*AANTAL_DAGEN
maximumTemperaturen = [.0]*AANTAL_DAGEN
minimumTemperaturen = leesMinimumTemperaturenIn()
maximumTemperaturen = leesMaximumTemperaturenIn()
zoekHitteGolven(minimumTemperaturen, maximumTemperaturen)