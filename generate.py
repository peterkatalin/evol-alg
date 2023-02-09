from Init.ElementGenerator import *

writeMatrixToFile(generateProfitMatrix(
    const_profitLimit, const_size), matrixFileName)
print(readMatrixFromFile(matrixFileName))
writeArrayToFile(generateArray(const_values, const_size), valuesFileName)
print(readArrayFromFile(valuesFileName))
writeArrayToFile(generateArray(const_weights, const_size), weightsFileName)
print(readArrayFromFile(weightsFileName))
