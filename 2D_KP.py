# Genetic algorithm for the Two Dimensional Knapsack Problem

# Given a set of rectangular pieces and a rectangular container, the two-dimensional knapsack problem
# (2D-KP) consists of orthogonally packing a subset of the pieces within the container such that the sum of
# the values of the packed pieces is maximized.
# If the value of a piece is given by its area, the objective is to maximize the covered area of the container.

# Four types of 2D-KP:
# RF: Pieces can be rotated by 90 degrees (R), the guillotine cutting constraint is not required (F);
# RG: Pieces can be rotated by 90 degrees (R), the guillotine cutting constraint is required (G);
# OF: Orientation of all pieces is fixed (O), the guillotine cutting constraint is not required (F);
# and
# OG: Orientation of all pieces is fixed (O), the guillotine cutting constraint is required (G).

import pandas as pd
from ga_methods.mutation import mutation
from ga_methods.crossover import crossover
from ga_methods.selection import elitist_selection, delete_worst_selection
from ga_methods.init_population import init_population
from util.read import read_input
from ga_statistics.box_plots import *


def genetic_algorithm(kp_type, generation, pop_size, its, cont, crs, crs_p, p_c, p_m, mut_type, sel_type):
    population = init_population(kp_type, pop_size, its, cont)

    for _ in range(generation):
        crossover(kp_type, crs, crs_p, p_c, pop_size, population, its, cont)
        mutation(kp_type, p_m, population, its, cont, mut_type)
        if sel_type == "elitist":
            population = elitist_selection(pop_size, population)
        else:
            population = delete_worst_selection(pop_size, population)
    return population


def show_plots():
    box_plot_final_populations(all_final_population,
                               crossover_type,
                               nr_of_crossover_points,
                               probability_mutation,
                               crossover_rate,
                               generation_number,
                               selection_type)
    plt.savefig("image1")
    box_plot_for_best_offsprings(best_offspring_values,
                                 crossover_type,
                                 nr_of_crossover_points,
                                 crossover_rate,
                                 probability_mutation,
                                 generation_number)
    plt.savefig("image2")
    plt.show()


def do_experiments():
    for experiment in range(number_of_experiments):
        # print(experiment, ". experiment: ")
        final_population = genetic_algorithm(knapsack_problem_type,
                                             generation_number,
                                             population_size,
                                             items,
                                             container,
                                             crossover_type,
                                             nr_of_crossover_points,
                                             crossover_rate,
                                             probability_mutation,
                                             mutation_type,
                                             selection_type)
        # print("Best offspring in", experiment + 1, "experiment", final_population[0])
        best_offspring_values.append(final_population[0].filling_rate)
        print(best_offspring_values)
        population_filling_rates = []
        for chromosome in final_population:
            population_filling_rates.append(chromosome.filling_rate)
        label = "exp. " + str(experiment + 1)
        all_final_population[label] = population_filling_rates

    return [all_final_population, best_offspring_values]


if __name__ == '__main__':
    print('Solution for the two dimensional knapsack problem')

    [items, container] = read_input("input/container_big.txt", "input/items_big.txt")

    knapsack_problem_type = "OF"  # possible 2D-KP types: RF, OF

    generation_number = 10
    population_size = 25

    crossover_type = "n-point"  # possible crossover types: n-point, uniform
    nr_of_crossover_points = 10  # not important in case of uniform crossover
    crossover_rate = 0.7

    probability_mutation = 0.1  # the probability of mutation depends on the population size
    mutation_type = "all"   # possible mutation types: once, all

    selection_type = "elitist"  # possible selection types: elitist, delete-worst

    number_of_experiments = 30

    best_offspring_values = []
    all_final_population = pd.DataFrame()
    do_experiments()

    show_plots()
