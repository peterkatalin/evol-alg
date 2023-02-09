import numpy as py
from Init.ElementGenerator import *
from Init.Constants import *


class individual:

    def __init__(self, size=0, rep=[], value=0, weight=0, profitMatrix=readMatrixFromFile(matrixFileName)):
        self.size = size
        self.rep = rep
        self.value = value
        self.weight = weight
        self.profitMatrix = profitMatrix

    def setSize(self, s):
        self.size = s

    def setRep(self, r):
        if (len(r) == self.size):
            self.rep = r

    def setValue(self, v):
        self.value = v

    def setWeight(self, w):
        self.weight = w

    def calculate_weight(self, arr):
        if (self.size == len(arr)):
            aux = 0
            for i in range(len(arr)):
                aux = aux + (self.rep[i] * arr[i])

            self.weight = aux

    def calculateQuadraticValue(self, arr):
        if (self.size == len(arr)):
            aux = 0
            for i in range(len(arr)):
                aux = aux + (self.rep[i] * arr[i])

            for i in range(self.size):
                for j in range(self.size):
                    if ((i <= j) and self.rep[i] and self.rep[j]):
                        aux = aux + self.profitMatrix[i][j]

            self.value = aux

    def getSize(self):
        return self.size

    def getRep(self):
        return self.rep

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight
