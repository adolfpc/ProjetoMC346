#Nome: Adolf Pereira da Costa RA: 164933
#Nome: Renan Clarindo Amorim  RA: 186454
#Projeto 3 - Python MC346

import sys
import random

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
        self.vel_reais = list(args)
    
    def get_tempo(self):
        tamanho_lista = len(self.vel_reais)
        vel_ref = 0
        
        if tamanho_lista == 0:
            vel_ref = self.vel_max
        else:
            ind_rand = random.randint(0,(tamanho_lista-1))
            vel_ref = self.vel_reais[ind_rand]
        
        vel_ref = float(vel_ref)
        if vel_ref == 0:
            res = -1
        else:
            comp = float(self.comprimento)
            res = (comp/vel_ref)*60
        
        return res


class Nodes:
    def __init__(self, no1, no2, tempo):
        self.no1 = no1
        self.filhos = []
        if no2 != "":
            aux = (no2, tempo)
            self.filhos.append(aux)
        self.distancia = float("inf")
        self.caminho = []



class Grafo:
    def __init__(self):
        self.nodes = []
        
    def adiciona_node(self, no1, no2, tempo):
        for x in self.nodes:
            if x.no1 == no1:
                for y in x.filhos:
                    if y[0] == no2:
                        return
                x.filhos.append((no2, tempo))
                return
        aux = Nodes(no1, no2, tempo)
        self.nodes.append(aux)
        return
    def retorna_node(self, node):
        for x in self.nodes:
            if x.no1 == node:
                return x

    
       
        

def criar_grafo(dados, conexoes):
    grafo = Grafo()
    for x in dados[1:]:
        if x == []:
            break
        tempo = 0
        for y in conexoes:
            if y.no1 == x[0] and y.no2 == x[1]:
                tempo = y.get_tempo()
        if tempo == -1:
            continue
        grafo.adiciona_node(x[0], x[1], tempo)
    return grafo
        


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

def imprimir_grafo(grafo):
    for x in grafo.nodes:
        out = '''
        no1 = {no1}
        distancia = {dist}
        filhos = {filhos}
        ---------------------------------------------------------------------
        \n'''.format(no1 = x.no1, dist = x.distancia, filhos = x.filhos)
        print (out, end='')

def check_nodes(res, no1):
    for x in res:
        if x.no1 == no1:
            return True
    return False

def remove_nodes(res, no1):
    for x in res:
        if x.no1 == no1:
            res.remove(x)
    return 

def return_nodes(res, no1):
    for x in res:
        if x.no1 == no1:
            return x
    return None

def criar_lista_nodes(grafo):
    res = []
    for x in grafo.nodes:
        for y in x.filhos:
            if check_nodes (res, y[0]):
                continue
            else:
                res.append(Nodes(y[0], "", 0))
        remove_nodes(res, x.no1)
        res.append(x)
    return res

def imprime_lista_nodes(nodes):
    for x in nodes:
        out = '''
        no1 = {no1}
        distancia = {dist}
        filhos = {filhos}
        caminho = {caminho}
        ---------------------------------------------------------------------
        \n'''.format(no1 = x.no1, dist = x.distancia, filhos = x.filhos, caminho = x.caminho)
        print (out, end='')


def dijkstra(grafo, lista_nodes, raiz, destino):
    visitados = []
    nodes = lista_nodes


    aux = grafo.retorna_node(raiz)
    aux.distancia = 0
    aux.caminho.append(aux.no1)
    visitados.append(aux)
    lista_nodes.remove(aux)

    

    for x in visitados:
        for y in x.filhos:
            aux = return_nodes(nodes, y[0])
            if (aux == None):
                continue
            val1 = x.distancia + y[1]
            val2 = aux.distancia
            if val1 < val2:
                aux.distancia = val1
                aux.caminho = x.caminho + list(aux.no1)
        lista_nodes.sort(key = lambda x: x.distancia)
        if len(lista_nodes) == 0:
            break
        else:
            visitados.append(lista_nodes.pop(0))
    res = return_nodes(visitados, destino)
    return (res.distancia, res.caminho)
             
        
def melhores_caminhos (qtd, dados, lista_conexoes):
    lista = []
    for x in range(qtd):
        grafo = criar_grafo(dados, lista_conexoes)
        lista_nodes = criar_lista_nodes(grafo)
        lista.append(dijkstra(grafo, lista_nodes, dados[-2][0], dados[-1][0]))
    
    lista.sort(key = lambda x: x[0])

    for x in lista[:2]:
        out ="{tempo:.1f}".format(tempo = x[0])
        out +="\n"
        for y in x[1]:
            out += "{caminho} ".format(caminho = y)
        print (out)


def melhores_caminhos_diferentes (qtd, dados, lista_conexoes):
    lista = []
    #cria 100 amostras
    for x in range(qtd):
        grafo = criar_grafo(dados, lista_conexoes)
        lista_nodes = criar_lista_nodes(grafo)
        lista.append(dijkstra(grafo, lista_nodes, dados[-2][0], dados[-1][0]))
    
    lista.sort(key = lambda x: x[0])

    old = (0.0, "")
    count = 0
    for x in lista:
        if count == 2:
            break
        if old[1] == x[1]:
            continue
        count += 1
        out ="{tempo:.1f}".format(tempo = x[0])
        out +="\n"
        for y in x[1]:
            out += "{caminho} ".format(caminho = y)
        print (out)
        old = x
    
    if count == 1:
        for x in lista:
            if count == 2:
                break
            if old == x:
                continue
            count += 1
            out ="{tempo:.1f}".format(tempo = x[0])
            out +="\n"
            for y in x[1]:
                out += "{caminho} ".format(caminho = y)
            print (out)

    if count == 1:
        if count == 2:
            return
        x = lista[-1]
        count += 1
        out ="{tempo:.1f}".format(tempo = x[0])
        out +="\n"
        for y in x[1]:
            out += "{caminho} ".format(caminho = y)
        print (out)

    return

       



def main():
    dados = ler_dados()
    lista_conexoes = criar_conexoes(dados)
    melhores_caminhos_diferentes(100, dados, lista_conexoes)

if __name__ == "__main__":
     main()
