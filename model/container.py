# Representation of container
# A container has two properties: width and height

class Container:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self):
        return "Container{ width = " + str(self._width) + \
               "; height = " + str(self._height) + "}"
