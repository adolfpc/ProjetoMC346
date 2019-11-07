def soma (a,b,c=0):
    return (2*a)+b+c


lista = [1,2]

a = soma (*lista)

print (a)

    for x in reversed(dados[:-2]):
        if x == []:
            break
        for y in lista_conexoes:
            if y[0] == x[0] and y[1] == x[1]:
                x.insere_vel(*x[2:])
