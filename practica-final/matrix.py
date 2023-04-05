from functools import reduce

def process_matrix(list_of_lists):
    '''
    Recibe una matriz y devuelve una nueva, 
    con los elementos cambiados. Cada elemento de la nueva, 
    sera el promedio del valor antiguo y el de sus vecinos
    '''
    # Creo la saga donde ire acumulando
    processed_matrix = []
    
    if len(list_of_lists) == 1:
        processed_matrix = list_of_lists
    else:
        # Por cada elemento dentro de cada lista
        for i, column in enumerate(list_of_lists):
            prequel_matrix = []
            for j, value in enumerate(column):
                # Lo proceso
                new_element = process_element(i, j, list_of_lists)
                # Lo añado a la saga
                prequel_matrix.append(new_element)
            processed_matrix.append(prequel_matrix)

    # Devuelvo la nueva matriz
    return processed_matrix

def process_element(i, j, matrix):
    '''
    Recibe los indices de un elemento y la matriz en la que esta.
    Calcula su promedio con sus vecinos y devuelve dicho promedio
    '''
    # Obtengo la lista de vecinos
    indices = get_neighbour_index(i, j, matrix) 
    values = get_neighbour_values(indices, matrix)      

    # Calculo el promedio
    average = get_average(values)
    
    # Devuelvo el valor final
    return average

def get_neighbour_index(i, j, matrix):
    """
    Devuelve el indice de todos los vecinos dentro de la matriz
    """    
    new_list = []     

    new_list.extend([(i,j), (i+1,j), (i-1,j), (i,j+1), (i,j-1)])    

    index_new_list  = [index for index in new_list if (index[0] >= 0 and index[0] <=len(matrix)-1) and (index[1] >= 0 and index[1] <=len(matrix)-1)]            
    
    return index_new_list

def get_neighbour_values(index_list, matrix):
    """
    Devuelve el valor de cada indice pedido de una matriz  
    """
    values = []

    for index in index_list:
        values.append(matrix[index[0]][index[1]])
    return values


def get_average(numbers):
    '''
    Recibe una lista de numeros y devuelve su promedio
    '''    
    return reduce(lambda a, b: a + b, numbers, 0) / len(numbers)
    



neo = [[0,1,2,3,4,5],[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8,],[4,5,6,7,8,9],[5,6,7,8,9,10]]
print(process_matrix(neo))