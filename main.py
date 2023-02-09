import numpy as np
import random
from Algorithms.Genetic import *
from Models.Individual import *
from Algorithms.Selection import *
from Algorithms.Evaluation import *
from Algorithms.Mutation import *
from Algorithms.Crossover import *
from Init.ElementGenerator import *
from Init.Init import *
from Plots.MyPlots import *


values = readArrayFromFile(valuesFileName)
weights = readArrayFromFile(weightsFileName)
n = const_size

data = []
best_results = []
for i in range(0, 10):
    population = init_population(n, n_pop, values, weights)
    [best, last_generation_values] = geneticAlgorithm(
        population, gen, knapsack_size, values, weights, n_pop, select, p_cross, p_mut)
    data.append(last_generation_values)
    best_results.append(best[gen-1])


myScatterPlot(best)
