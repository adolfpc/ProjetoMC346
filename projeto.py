#Nome: Adolf Pereira da Costa RA: 164933
#Nome: Renan Clarindo Amorim  RA: 186454

import sys



class Conexoes:
    velocidade = 0
    def __init__(self, no1, no2, comprimento, vel_max=-1):
        self.vel_reais = []
        self.no1 = no1
        self.no2 = no2
        self.comprimento = comprimento
        if vel_max == -1:
            self.vel_max = self.velocidade
        else:
            self.vel_max = vel_max     
    

    def insere_vel(self, *args):
        self.vel_reais = args


def ler_dados():
    txt_raw = sys.stdin.read()
    txt_temp = txt_raw.splitlines()
    txt = []
    for x in txt_temp:
        txt.append(x.split())
    return txt

def criar_conexoes(dados):
    lista_conexoes = []
    Conexoes.velocidade = dados[0][0]
    for x in dados[1:]:
        if x != []:
            aux = Conexoes(*x)
            lista_conexoes.append(aux)
        else:
            break
    for x in reversed(dados[:-2]):
        if x == []:
            break
        for y in lista_conexoes:
            if (y.no1 == x[0] and y.no2 == x[1]):
                y.insere_vel(*x[2:])
    return lista_conexoes

def imprimir_conexoes(lista):
    for x in lista:
        out = '''
        no1 = {no1}
        no2 = {no2}
        comprimento = {comp}
        vel_max = {vel_max}
        vel_reais = {vel_list}
        ---------------------------------------------------------------------
        '''.format(no1 = x.no1, no2 = x.no2, comp = x.comprimento, vel_max = x.vel_max, vel_list = x.vel_reais)
        print (out, end='')

def main():
    dados = ler_dados()
    lista_conexoes = criar_conexoes(dados)
    imprimir_conexoes(lista_conexoes)





if __name__ == "__main__":
     main()
