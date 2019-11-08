import random

def soma (a,b,c=0):
    return (2*a)+b+c


def number():
    res = random.randint(0,10)
    return res

lista = [1,2]

a = soma (*lista)

#print (a)


b = number



def func (*args):
    print (list(args))


lista = [1,2,3,4,5]

func (*lista[5:])