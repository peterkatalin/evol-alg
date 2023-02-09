import random;
import numpy as np;


input_size=100
knapsack_capacity=2500

with open('values.txt', 'w') as f:

    for i in range(input_size):
        n = random.randint(1,99)
        f.writelines('%d\n'%n)

f.close()

with open('weights.txt', 'w') as f:

    for i in range(input_size):
        n = random.randint(1,99)
        f.writelines('%d\n'%n)

f.close()
    
with open('knap.txt', 'w') as f:
    f.writelines('%d'%knapsack_capacity)
f.close()