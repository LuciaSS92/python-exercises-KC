from functools import reduce

def process_matrix(list_of_lists):
    '''
    Recibe una matriz y devuelve una nueva, 
    con los elementos cambiados. Cada elemento de la nueva, 
    sera el promedio del valor antiguo y el de sus vecinos
    '''
    # Creo una lista matriz donde ire acumulando
    processed_matrix = []
    peque_matrix = []

    if len(list_of_lists) == 1:
        processed_matrix = list_of_lists
    else:
        # por cada elemento dentro de cada lista
        for i, column in enumerate(list_of_lists):
            peque_matrix = []
            for j, value in enumerate(column):
                #lo proceso
                new_element = process_element(i, j, list_of_lists)
                #lo añado a la lista
                peque_matrix.append(new_element)
            processed_matrix.append(peque_matrix)

    #devuelvo la nueva matriz
    return processed_matrix                                                     
    
def process_element(i, j, matrix):
    '''
    Recibe el indice de un elemento y la lista en la que esta,
    calcula su promedio con sus vecinos y devuelve dicho promedio
    '''
    # obtengo la lista de vecinos
    values = get_neighbour_values(i, j, matrix)      

    # calculo su promedio
    average = get_average(values)
    
    # lo promedio con el elemento en si
    # devuelvo el valor final
    return average


'''
def get_neighbour_indices(i, j, matrix):
    
    new_list = []     

    new_list.extend([(i,j), (i+1,j), (i-1,j), (i,j+1), (i,j-1)])    

    i_new_list  = [tup for tup in new_list if (tup[0] >= 0 and tup[0] <=len(matrix)-1) and (tup[1] >= 0 and tup[1] <=len(matrix)-1)]

    return i_new_list
    '''


def get_neighbour_values(i, j, matrix):
    """
    Devuelve el valor de cada indice pedido de una matriz  
    """
    new_list = []

    new_list.append(matrix[i][j])
    
    if i == 0 and j == 0:
        new_list.append(matrix[i+1][j])
        new_list.append(matrix[i][j+1])

    elif i == 0 and j == len(matrix)-1:
        new_list.append(matrix[i+1][j])
        new_list.append(matrix[i][j-1])

    elif i == len(matrix)-1 and j == 0:
        new_list.append(matrix[i-1][j])
        new_list.append(matrix[i][j+1])

    elif i == len(matrix)-1 and j == len(matrix)-1:
        new_list.append(matrix[i-1][j])
        new_list.append(matrix[i][j-1])

    elif i == 0 and j > 0 and j < len(matrix)-1:
        new_list.append(matrix[i+1][j])
        new_list.append(matrix[i][j+1])
        new_list.append(matrix[i][j-1])

    elif j == 0 and i > 0 and i < len(matrix)-1:
        new_list.append(matrix[i][j+1])
        new_list.append(matrix[i+1][j])
        new_list.append(matrix[i-1][j])

    elif i == len(matrix)-1 and j > 0 and j < len(matrix)-1:
        new_list.append(matrix[i-1][j])
        new_list.append(matrix[i][j+1])
        new_list.append(matrix[i][j-1])

    elif j == len(matrix)-1 and i > 0 and i < len(matrix)-1:
        new_list.append(matrix[i][j-1 ])
        new_list.append(matrix[i+1][j])
        new_list.append(matrix[i-1][j])

    else: 
        new_list.append(matrix[i+1][j])
        new_list.append(matrix[i][j+1])
        new_list.append(matrix[i-1][j])
        new_list.append(matrix[i][j-1])

   
    return new_list

   

'''
def get_neighbour_values(index, matrix):
    
    values = []
    for i, column in enumerate(index):
        for j, value in enumerate(column):
            values.append(matrix[i][j])
    return values
'''

''' 
def get_neighbour_values(indexes, matrix):
   values = []
   for index in indexes:
    values.append(matrix[index])
    return values

'''


def get_average(numbers):
    '''
    Recibe una lista de numeros y devuelve su promedio
    '''
    return reduce(lambda a, b: a + b, numbers, 0) / len(numbers)
    # return reduce(lambda accum, b: accum + b, values, 0) / len(values)




mati = [[0,1,2,3,4,5],[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8,],[4,5,6,7,8,9],[5,6,7,8,9,10]]
print(process_matrix(mati))