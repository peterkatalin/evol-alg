import random
from Models.Individual import *


def crossoverN(arr, select, crossP, popN, parentProbability, cuts):
    n = arr[0].size
    for i in range(select):
        if (random.uniform(0, 1) <= crossP):

            i1 = 0
            nr = random.uniform(0, 1)
            proportion = 0
            while (i1 < popN):
                proportion = proportion+parentProbability[i1]
                if (nr <= proportion):
                    break
                i1 = i1+1

            i2 = i1
            while (i2 == i1):
                i2 = 0
                nr = random.uniform(0, 1)
                proportion = 0

                while (i2 < popN):
                    proportion = proportion+parentProbability[i2]
                    if (nr <= proportion):
                        break
                    i2 = i2+1

            crossovers = set()
            times = cuts

            for i in range(times):
                crossover_index = random.randint(1, n-2)
                while (crossover_index in crossovers):
                    crossover_index = random.randint(1, n-2)
                crossovers.add(crossover_index)

            crossovers = list(sorted(crossovers))

            A = arr[i1].getRep()
            B = arr[i2].getRep()
            C = []
            D = []
            parity = 0
            crossover_index = crossovers[parity]
            for j in range(n):
                if ((parity % 2) == 0):
                    if (j < crossover_index):
                        C.append(A[j])
                        D.append(B[j])
                    else:
                        if (j == crossover_index):
                            C.append(A[j])
                            D.append(B[j])
                            parity = parity+1
                            if (parity < times):
                                crossover_index = crossovers[parity]
                        else:
                            C.append(A[j])
                            D.append(B[j])
                else:
                    if (j < crossover_index):
                        C.append(B[j])
                        D.append(A[j])
                    else:
                        if (j == crossover_index):
                            C.append(B[j])
                            D.append(A[j])
                            parity = parity+1
                            if (parity < times):
                                crossover_index = crossovers[parity]
                        else:
                            C.append(B[j])
                            D.append(A[j])

            firstChild = individual(n, C)
            secondChild = individual(n, D)
            arr.append(firstChild)
            arr.append(secondChild)
