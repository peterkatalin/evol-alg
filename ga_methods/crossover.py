import random
from util.build_chromosome import build_chromosome_from_representation


def n_point_crossover(child_1_representation, child_2_representation, crs_p, parents):
    # crs_p number of crossover_points created
    crossover_points = [random.randint(0, len(parents[0].representation) - 1) for _ in range(crs_p)]

    crossover_index = 0
    parent_index = 0
    for offspring_creation_index in range(len(parents[0])):
        if offspring_creation_index < crossover_points[crossover_index]:
            child_1_representation[offspring_creation_index] = parents[parent_index][offspring_creation_index]
            child_2_representation[offspring_creation_index] = parents[parent_index - 1][offspring_creation_index]
        else:
            crossover_index += 1
            parent_index = abs(parent_index - 1)
            child_1_representation[offspring_creation_index] = parents[parent_index][offspring_creation_index]
            child_2_representation[offspring_creation_index] = parents[parent_index - 1][offspring_creation_index]

    return [child_1_representation, child_2_representation]


def uniform_crossover(child_1_representation, child_2_representation, parents):
    for offspring_creation_index in range(len(parents[0])):
        if random.randint(0, 1) == 1:
            child_1_representation[offspring_creation_index] = parents[0][offspring_creation_index]
            child_2_representation[offspring_creation_index] = parents[1][offspring_creation_index]
        else:
            child_1_representation[offspring_creation_index] = parents[1][offspring_creation_index]
            child_2_representation[offspring_creation_index] = parents[0][offspring_creation_index]

    return [child_1_representation, child_2_representation]


def crossover(kp_type, crs, crs_p, p_c, pop_size, population, its, cont):
    # TODO multi-parent recombination
    for _ in range(int(pop_size / 2)):
        # a number of pop_size new chromosomes are created
        # TODO selection pressure -> not only random parents
        parent_1 = population[random.randint(0, pop_size - 1)]
        parent_2 = population[random.randint(0, pop_size - 1)]
        if random.uniform(0, 1) < p_c:
            child_1_representation = [0 for _ in range(len(parent_1.representation))]
            child_2_representation = [0 for _ in range(len(parent_1.representation))]
            if crs == "n_point":
                # two offsprings created through recombination with n-point crossover
                n_point_crossover(child_1_representation,
                                  child_2_representation,
                                  crs_p,
                                  [parent_1.representation, parent_2.representation])
            else:
                # two offsprings created through recombination with uniform crossover
                uniform_crossover(child_1_representation,
                                  child_2_representation,
                                  [parent_1.representation, parent_2.representation])
            # the offsprings are added to the population only if they are valid
            child_1 = build_chromosome_from_representation(kp_type, child_1_representation, its, cont)
            child_2 = build_chromosome_from_representation(kp_type, child_2_representation, its, cont)
            if child_1.total_value > 0:
                population.append(child_1)
            if child_2.total_value > 0:
                population.append(child_2)
        else:
            # two offsprings created asexually (copy of parents)
            population.append(parent_1)
            population.append(parent_2)
