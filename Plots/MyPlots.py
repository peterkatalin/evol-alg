
import matplotlib.pyplot as plt


def myBoxPlot(data):
    _, ax = plt.subplots()
    bp = ax.boxplot(data)
    plt.show()


def myScatterPlot(best):
    generations = range(1, 51)
    fig2, ax2 = plt.subplots()
    sc = ax2.scatter(generations, best)
    plt.show()
