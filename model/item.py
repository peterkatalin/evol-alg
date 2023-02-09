class Item:

    def __init__(self, width, height, item_value):
        self._width = width
        self._height = height
        self._item_value = item_value

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def item_value(self):
        return self._item_value

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @item_value.setter
    def item_value(self, value):
        self._item_value = value

    def __str__(self):
        return "Item{\n" + \
               "width = " + str(self._width) + ";\n" +  \
               "height = " + str(self._height) + ";\n" + \
               "value = " + str(self._item_value) + ";\n" + \
               "}"
