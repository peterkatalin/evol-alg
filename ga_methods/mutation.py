import random
from util.build_chromosome import build_chromosome_from_representation


def mutation(kp_type, p_m, population, its, cont, mutation_type):
    for chromosome_index in range(0, len(population) - 1):
        if random.uniform(0, 1) <= p_m:
            new_representation = population[chromosome_index].representation
            
            if mutation_type == "once":
                flip_bit_index = random.randint(0, len(new_representation) - 1)
                # randomly changing one gene of the representation if it is successful
                new_representation[flip_bit_index] = abs(new_representation[flip_bit_index] - 1)
                new_chromosome = build_chromosome_from_representation(kp_type,
                                                                      new_representation,
                                                                      its,
                                                                      cont)
                if new_chromosome.total_value > 0:
                    population[chromosome_index] = new_chromosome

            if mutation_type == "all":
                for representation_index in range(0, len(new_representation) - 1):
                    if random.uniform(0, 1) <= p_m:
                        # changing the gene randomly for each index of chromosome
                        new_representation[representation_index] = abs(new_representation[representation_index] - 1)
                        new_chromosome = build_chromosome_from_representation(kp_type,
                                                                              new_representation,
                                                                              its,
                                                                              cont)
                        # if the mutation.py did not create a successful offspring, we don't change it
                        if new_chromosome.total_value > 0:
                            population[chromosome_index] = new_chromosome
