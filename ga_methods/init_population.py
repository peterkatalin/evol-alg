from model.chromosome import Chromosome
from model.layer import Layer
import random
from util.build_chromosome import can_put_in_item, put_in_item


def init_population(kp_type, pop_size, its, cont):
    # create the chromosomes for the initial population

    population = []

    for _ in range(pop_size):
        total_value = 0
        representation = []
        layers = [Layer(width=0,
                        height=0,
                        volume=0,
                        items=[])]

        for item_index in range(0, len(its)):
            chosen = random.randint(0, 1)
            if chosen == 1 and can_put_in_item(kp_type, layers, its[item_index], cont):
                # print("Putting in item: " + str(its[item_index]))
                put_in_item(kp_type, layers, its[item_index], cont)
                representation.append(1)  # mark added item in representation
                total_value += its[item_index].item_value  # set the chromosome's total value
            else:
                # print("Not putting in item: " + str(its[item_index]))
                representation.append(0)
        population.append(Chromosome(total_value=total_value,
                                     filling_rate=sum([layer.volume for layer in layers]) / (cont.width * cont.height),
                                     representation=representation,
                                     layers=layers))
        # print(population[len(population) - 1])
    return population
