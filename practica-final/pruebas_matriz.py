def get_neighbour_indices(i, j, matrix):
    
    new_list = []     

    new_list.extend([(i,j), (i+1,j), (i-1,j), (i,j+1), (i,j-1)])    

    i_new_list  = [tup for tup in new_list if (tup[0] >= 0 and tup[0] <=len(matrix)-1) and (tup[1] >= 0 and tup[1] <=len(matrix)-1)]            
    
    return i_new_list


mati = [[0,1,2,3,4,5],[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8,],[4,5,6,7,8,9],[5,6,7,8,9,10]]
print(get_neighbour_indices(2,3,mati))