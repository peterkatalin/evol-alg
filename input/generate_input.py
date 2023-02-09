import random

if __name__ == '__main__':
    nr_of_inputs = 1000
    filename = "items.txt"

    with open(filename, 'w') as outfile:
        outfile.write(str(nr_of_inputs) + "\n")
        for i in range(1, nr_of_inputs):
            x = random.randint(1, 500)
            y = random.randint(1, 500)
            print(str(x) + " - " + str(y))
            outfile.write(str(x) + " " + str(y) + "\n")

