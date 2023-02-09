

import random

from Models.Individual import *


def init_population(n, n_pop, values, weights):
    lista = []
    for j in range(n_pop):
        kromoszoma = []
        for i in range(n):
            kromoszoma.append(random.randint(0, 1))
        e = individual(n, kromoszoma)
        e.calculateQuadraticValue(values)
        e.calculate_weight(weights)
        lista.append(e)
    return lista
