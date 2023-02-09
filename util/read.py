from model.container import Container
from model.item import Item


def read_input(container_input_file, items_input_file):
    f = open(container_input_file, "r")
    cont = f.read().split()
    f.close()

    cont = Container(int(cont[0]), int(cont[1]))

    f = open(items_input_file, "r")
    its_information = f.read().split("\n")
    f.close()

    nr_of_its = int(its_information[0])
    its = [Item(width=0, height=0, item_value=0) for _ in range(nr_of_its)]
    for item_index in range(1, len(its_information)):
        next_item = its_information[item_index].split()
        its[item_index - 1].width = int(next_item[0])
        its[item_index - 1].height = int(next_item[1])
        its[item_index - 1].item_value = int(next_item[0]) * int(next_item[1])

    return [its, cont]