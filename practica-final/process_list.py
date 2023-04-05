from functools import reduce

def process_list(elements):
    '''
    Recibe una lista de numeros y devueve una nueva, 
    con los elementos cambiados. Cada elemento de la nueva, 
    sera el promedio del valor antiguo y el de sus vecinos
    '''
    # Creo una lista vacia donde ire acumulando
    processed_list = []

    if len(elements) == 1:
        processed_list = elements
    else:
        # por cada elemento de la lista..
        for index, element in enumerate(elements):
            #lo proceso
            new_element = process_element(index, elements)
            #lo añado a la lista
            processed_list.append(new_element)

    #devuelvo la nueva lista
    return processed_list    
    
def process_element(index, elements):
    '''
    Recibe el indice de un elemento y la lista en la que esta,
    calcula su promedio con sus vecinos y devuelve dicho promedio
    '''
    # obtengo la lista de vecinos
    indices = get_neighbour_index(index, elements)
    values = get_neighbour_values(indices, elements)

    # calculo su promedio
    average = get_average(values)
    
    # lo promedio con el elemento en si
    # devuelvo el valor final
    return average

def get_neighbour_index(index, elements):

    indices = []

    indices.append(index)
    indices.append(index + 1)
    indices.append(index - 1)
    
    indices = list(filter(lambda x : x >= 0 and x <=len(elements)-1, indices))  #el filtro no funciona del todo, falla en los indices siguientes!!

    return indices


def get_neighbour_values(indices, elements):
    """
    Devuelve el valor de cada indice pedido de una ista de elementos  
    """

    values = []
    for index in indices:
        values.append(elements[index])
    return values



def get_average(numbers):
    '''
    Recibe una lista de numeros y devuelve su promedio
    '''
    return reduce(lambda a, b: a + b, numbers, 0) / len(numbers)
    # return reduce(lambda accum, b: accum + b, values, 0) / len(values)


print(process_list([3,5,7,1]))
print(process_element(3, [3,5,7,1]))
print(get_neighbour_index(2, [3,5,7,1]))
print(get_neighbour_values([3, 2, 0], [3,5,7,1]))
print(get_average([3,5,7,1,3,5]))
