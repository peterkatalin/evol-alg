import random


def quick_sort_by_filling_rate(population, low, high):
    if low < high:
        pi = partition_filling_rate(population, low, high)
        quick_sort_by_filling_rate(population, low, pi - 1)
        quick_sort_by_filling_rate(population, pi + 1, high)


def partition_filling_rate(population, low, high):
    pivot = population[high].filling_rate
    i = low - 1
    for j in range(low, high):
        if population[j].filling_rate >= pivot:
            i = i + 1
            (population[i], population[j]) = (population[j], population[i])
    (population[i + 1], population[high]) = (population[high], population[i + 1])
    return i + 1


def elitist_selection(pop_size, population):
    # steady state model (m+l -> m)
    # elitist approach to selection: the first pop_size values are chosen with the highest values
    quick_sort_by_filling_rate(population, 0, len(population) - 1)
    return population[:pop_size]


def delete_worst_selection(pop_size, population):
    # steady state model (m+l -> m)
    # delete-worst approach: delete the last 25% and some random
    quick_sort_by_filling_rate(population, 0, len(population) - 1)
    # delete last 25% == keep first 75%
    keep = int(len(population) * 75 / 100)
    if keep > pop_size:
        new_population = population[:keep]
    else:
        return population[:pop_size]
    while len(new_population) > pop_size:
        # delete from behind the first 25%
        index_to_delete = random.randint(int(pop_size * 25 / 100), len(new_population) - 1)
        del new_population[index_to_delete]

    return new_population
