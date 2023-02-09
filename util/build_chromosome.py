from model.layer import Layer
from model.chromosome import Chromosome


def can_add_new_layer(layers, it, cont, kp_type):
    width = 0
    for layer in layers:
        width += layer.width
    if kp_type == "OF" and width + it.width > cont.width:
        return False
    if kp_type == "RF" and width + it.height > cont.width:
        return False
    return True


def can_add_new_layer_by_cutting(layers, it, cont):
    return False


def can_put_in_item(kp_type, layers, it, cont):
    # based on the knapsack problem's type (kp_type) we decide if we can put in the item or not
    #   kp_type == "OF" => can not cut and can not rotate
    #   kp_type == "RF" => can not cut and can rotate

    if layers[len(layers) - 1].height + it.height > cont.height:
        # can not put on top of last layer without rotation or cut
        if kp_type == "OF":
            if not(can_add_new_layer(layers, it, cont, kp_type)):
                # try adding it into a new layer if we can not rotate
                return False
        if kp_type == "RF":  # try rotating it if we can to add to that layer
            if layers[len(layers) - 1].height + it.width > cont.height:
                # if rotating won't help try again to add to another layer
                if not(can_add_new_layer(layers, it, cont, kp_type)):
                    return False

    return True


def put_in_item(kp_type, layers, it, cont):
    if kp_type == "OF":
        if layers[len(layers) - 1].height + it.height > cont.height:
            layers.append(Layer(width=it.width,
                                height=it.height,
                                volume=it.width * it.height,
                                items=[it]))
        else:
            # put item on top of the next layer
            layers[len(layers) - 1].add_item(it, kp_type)  # add item to the last layer

    if kp_type == "RF":
        if layers[len(layers) - 1].height + it.width > cont.height:
            layers.append(Layer(width=it.height,
                                height=it.width,
                                volume=it.width * it.height,
                                items=[it]))
        else:
            # put item on top of the next layer
            layers[len(layers) - 1].add_item(it, kp_type)  # add item to the last layer


def build_chromosome_from_representation(kp_type, representation, its, cont):
    total_value = 0
    layers = [Layer(width=0, height=0, volume=0, items=[])]

    for item_index in representation:
        if item_index == 1:
            if can_put_in_item(kp_type, layers, its[item_index], cont):
                put_in_item(kp_type, layers, its[item_index], cont)
                total_value += its[item_index].item_value
            else:
                # if the offspring does not respect the boundaries, it is going to be "ignored"
                return Chromosome(total_value=-1,
                                  filling_rate=0,
                                  representation=[],
                                  layers=[])

    return Chromosome(total_value=total_value,
                      filling_rate=sum([layer.volume for layer in layers]) / (cont.width * cont.height),
                      representation=representation,
                      layers=layers)
