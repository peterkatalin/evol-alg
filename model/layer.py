# Representation of layers
# A layer is composed of items in descending order of their size
# Height equals the container's height
# Width equals the largest item's width

class Layer:

    def __init__(self, width, height, volume, items):
        self._items = items
        self._width = width
        self._height = height
        self._volume = volume

    @property
    def items(self):
        return self._items

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def volume(self):
        return self._volume

    @items.setter
    def items(self, value):
        self._items = value

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @volume.setter
    def volume(self, value):
        self._volume = value

    def add_item(self, item, kp_type):
        self._items.append(item)
        self._volume += (item.width * item.height)
        if kp_type == "OF":
            if self._width == 0:
                self._width = item.width
            else:
                if item.width > self._width:
                    self._width = item.width
            self._height += item.height
        else:
            if self._width == 0:
                self._width = item.height
            else:
                if item.height > self._width:
                    self._width = item.height
            self._height += item.width

    def __str__(self):
        return "Layer{\n" + \
               "width = " + str(self._width) + ";\n" + \
               "height = " + str(self._height) + ";\n" + \
               "items = " + str([str(self.items[i]) for i in range(len(self.items))]) + ";\n" + \
               "}"

    def width_and_height(self):
        return "Layer{" + \
               "width = " + str(self._width) + "; " + \
               "height = " + str(self._height) + \
               "}"
