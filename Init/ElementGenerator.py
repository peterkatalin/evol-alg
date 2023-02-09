import numpy as np
from Init.Constants import *


def generateProfitMatrix(profitRate, size: int,):
    array = np.random.randint(profitRate, size=(size, size))
    for i in range(size):
        for j in range(size):
            if i < j:
                array[j][i] = array[i][j]
    return (array)


def writeMatrixToFile(matrix, filename):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(','.join([str(x) for x in row]))
            f.write('\n')


def readMatrixFromFile(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = [int(x) for x in line.strip().split(',')]
            matrix.append(row)
    return matrix


def generateArray(higherValue, size: int):
    return (np.random.randint(higherValue, size=(size)))


def writeArrayToFile(array, filename: int):
    with open(filename, 'w') as f:
        for element in array:
            f.write(str(element) + '\n')


def readArrayFromFile(filename):
    array = []
    with open(filename, 'r') as f:
        for line in f:
            array.append(int(line.strip()))
    return array


def writeResultToFile(filename, track):
    with open(filename, 'w') as f:
        for i, j in zip(track[0], track[1]):
            f.write("Generation = " + i + " --> Value = " +  str(j.value) + " Weight = " + str(j.weight))
            f.write('\n')

