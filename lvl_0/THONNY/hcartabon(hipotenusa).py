import math

def hipotenusa(c1, c2):
    h = math.sqrt(c1*c1 + c2*c2)
    return h

def hcartabon(l):
    return hipotenusa(l, l)

cateto1 = 3
cateto2 = 4

_hcartabon = hcartabon(cateto1)
_hipotenusa = hipotenusa(cateto1, cateto2)
