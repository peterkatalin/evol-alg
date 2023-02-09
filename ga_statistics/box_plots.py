import matplotlib.pyplot as plt


def box_plot_final_populations(all_final_population, crossover_type, nr_of_crossover_points, p_m, p_c, generation_number, select):
    # Box plot for the final populations' values
    plt.rcParams["figure.figsize"] = (10, 6)
    fig1, ax1 = plt.subplots()
    ax1.boxplot(all_final_population.values)
    ax1.set_xticklabels(all_final_population.keys(), rotation=40, ha='right', rotation_mode='anchor')
    if crossover_type == "n-point":
        plt.title('Box plot for the filling rates of final population in each experiment \n' +
                  'with ' + str(generation_number) + ' generations, ' +
                  'using ' + select + ' selection, ' +
                  crossover_type + " crossover (n = " + str(nr_of_crossover_points) + ", p_c = " + str(p_c) +
                  ") and p_m = " + str(p_m))
    else:
        plt.title('Box plot for the filling rates of final population in each experiment \n' +
                  'with ' + str(generation_number) + ' generations, ' +
                  'using elitist selection, ' +
                  crossover_type + " crossover (p_c = " + str(p_c) +
                  ") and p_m = " + str(p_m))


def box_plot_for_best_offsprings(best_offspring_values, crossover_type, nr_of_crossover_points, p_c, p_m, generation_number):
    # Box plot for best offspring values
    plt.rcParams["figure.figsize"] = (9, 5)
    fig2, ax2 = plt.subplots()
    if crossover_type == "n-point":
        plt.title('Box plot for best offspring values in each experiment \n' +
                  'with ' + str(generation_number) + ' generations, ' +
                  'using elitist selection, ' +
                  crossover_type + " crossover (n = " + str(nr_of_crossover_points) + ", p_c = " + str(p_c) +
                  ") and p_m = " + str(p_m))
    else:
        plt.title('Box plot for best offspring values in each experiment \n' +
                  'with ' + str(generation_number) + ' generations, ' +
                  'using elitist selection, ' +
                  crossover_type + " crossover (p_c = " + str(p_c) +
                  ") and p_m = " + str(p_m))
    ax2.boxplot(best_offspring_values)
