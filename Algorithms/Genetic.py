from Models.Individual import *
from Algorithms.Selection import *
from Algorithms.Evaluation import *
from Algorithms.Mutation import *
from Algorithms.Crossover import *

track = [[], []]


def geneticAlgorithm(chroms, gen, knapsack_size, values, weights, n_pop, select, p_cross, p_mut):

    evaluation(chroms, values, weights, knapsack_size)
    quickSort(chroms, 0, n_pop-1)
    bestChoice = individual(
        chroms[0].size, chroms[0].rep, chroms[0].value, chroms[0].weight, chroms[0].profitMatrix)
    best = []
    for i in range(gen):
        parent_probability = selection(chroms, n_pop)
        # keresztezodes(chroms,select,p_cross,n_pop,parent_probability)
        crossoverN(chroms, select, p_cross, n_pop, parent_probability, 10)
        multiBitMutation(chroms[n_pop:], p_mut)
        evaluation(chroms, values, weights, knapsack_size)
        quickSort(chroms, 0, len(chroms)-1)
        if (chroms[0].value > bestChoice.value):
            bestChoice.setRep(chroms[0].rep)
            bestChoice.setValue(chroms[0].value)
            bestChoice.setWeight(chroms[0].weight)
        # print("Generation "+str(i)+" best result: " +
            #   str(bestChoice.getRep()))
        # print(bestChoice)
        track[0].append(str(i))
        track[1].append(bestChoice)
        best.append(bestChoice.getValue()/100)

    writeResultToFile(resultFileName, track)
    parent_probability = selection(chroms, n_pop)
    last_generation_values = []
    for ch in chroms:
        last_generation_values.append(ch.getValue())
    return [best, last_generation_values]
