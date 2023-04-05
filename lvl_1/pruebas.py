def reduce(seq, initial_value, combinator):
    accum = initial_value
    for element in seq:
        accum = combinator(accum, element) 
    return accum

def sum_all(items):
    return reduce(items, 0, lambda a,b: a + b)




