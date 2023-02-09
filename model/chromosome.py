# Binary representation of chromosomes

# Value is the sum of the values of the items chosen
# Filling rate is calculated as the quotient of the total area of all packed pieces and the container area
# Representation is an array of binary values (0 if item is not chosen and 1 if item is chosen)
# Layers is a two-dimensional array representing the items' position inside the container

class Chromosome:

    def __init__(self, total_value, filling_rate, representation, layers):
        self._total_value = total_value
        self._filling_rate = filling_rate
        self._representation = representation
        self._layers = layers

    @property
    def total_value(self):
        return self._total_value

    @property
    def filling_rate(self):
        return self._filling_rate

    @property
    def representation(self):
        return self._representation

    @property
    def layers(self):
        return self._layers

    @total_value.setter
    def total_value(self, value):
        self._total_value = value

    @filling_rate.setter
    def filling_rate(self, value):
        self._filling_rate = value

    @representation.setter
    def representation(self, value):
        self._representation = value

    @layers.setter
    def layers(self, value):
        self._layers = value

    def __str__(self):
        return "Chromosome{\n" + \
               "total_value = " + str(self._total_value) + ";\n" + \
               "filling rate = " + str(self._filling_rate) + ";\n" + \
                "representation = " + str(self._representation) + ";\n" + \
                "layers = " + str([self._layers[i].width_and_height() for i in range(len(self._layers))]) + "\n" + \
                "}"
