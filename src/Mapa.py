# Classe grafo para representaçao de grafos,
import math
from queue import Queue

from Nodo import Nodo

class Mapa:
    def __init__(self):         #nodo [(nodo_final,custo,acessibljijaci, ativo?)]
        self.m_cidades = []     # lista de cidades
        self.m_graph = {}       # dicionario para armazenar os nodos e arestas (tuplo da informação - destino, custo, acessibilidade)
        self.heuristicas = {}           # dicionario para posterirmente armazenar as heuristicas para cada nodo -> pesquisa informada
        self.lista_preferencias = []

    ######################################
    #    escrever o grafo como string    #
    ######################################

    def __str__(self):

        out = ""

        for key in self.m_graph.keys():
            out = out + "cidade" + str(key) + ": " + str(self.m_graph[key].cidade) + "\n"
        return out

    ################################
    #   encontrar nodo pelo nome   #
    ################################

    def get_node_by_name(self, name):

        search_node = Nodo(name)

        for node in self.m_cidades:
            if node == search_node:
                return node

        return None

    ########################
    #   imprimir arestas   #
    ########################

    def imprime_aresta(self):

        listaA = ""
        lista = self.m_graph.keys()

        for nodo in lista:
            for (nodo2, custo, acessibilidade) in self.m_graph[nodo]:       #acessibilidade vai ser a lista dos tipos de veiculos
                listaA = listaA + nodo.cidade + " -> " + nodo2.cidade + ", custo: " + str(custo) + ", acessibilidade: " + str(acessibilidade) + "\n"
        return listaA

    #################################
    #   adicionar aresta no grafo   #
    #################################

    def add_edge(self, nodo1, nodo2, peso, acessibilidade):     #recebe o nome dos nodos basicamente, peso e LISTA da acessibilidade

        c1 = Nodo(nodo1)
        c2 = Nodo(nodo2)

        if (c1 not in self.m_cidades):
            c1_id = len(self.m_cidades)  # numeração sequencial
            c1.setId(c1_id)
            self.m_cidades.append(c1)
            self.m_graph[c1] = []
        else:
            c1 = self.get_node_by_name(nodo1)

        if (c2 not in self.m_cidades):
            c2_id = len(self.m_cidades)  # numeração sequencial
            c2.setId(c2_id)
            self.m_cidades.append(c2)
            self.m_graph[c2] = []
        else:
            c2 = self.get_node_by_name(nodo2)

        self.m_graph[c1].append((c2, peso, acessibilidade))       #só passar a acessibilidade como lista and we gucci
        self.m_graph[c2].append((c1, peso, acessibilidade))       #também vou assumir que posso fazer tuplo de 3 elementos
            #é tudo bidirecional

    ######################
    #   devolver nodos   #
    ######################

    def getNodes(self):
        return self.m_cidades

    def set_necessidade_cidade (self, nome_cidade, necessidade):
        nodo = self.get_node_by_name (nome_cidade)
        nodo.setNecessidade (necessidade)



####################
#  Popular o mapa  #
####################

def popularMapa (mapa : Mapa) :
    mapa.add_edge ("Cherry Tree Hills", "Auburn", 15, ["camiao", "heli"]) # 1 -> 2
    mapa.add_edge ("Cherry Tree Hills", "Albatross Island", 25, ["heli"]) # 1 -> 13
    mapa.add_edge ("Cherry Tree Hills", "Fort Meadows", 15, ["comboio"]) # 1 -> 10
    mapa.add_edge ("Cherry Tree Hills", "Festival Square", 15, ["camiao"]) # 1 -> 3
    mapa.add_edge ("Cherry Tree Hills", "Downtown", 15, ["heli"]) # 1 -> 5

    mapa.add_edge ("Albatross Island", "Downtown", 15, ["barco", "heli"]) # 13 -> 5

    mapa.add_edge ("Downtown", "Kings Court", 15, ["camiao", "heli"]) # 5 -> 4
    mapa.add_edge ("Downtown", "Festival Square", 15, ["camiao"]) # 5 -> 3

    mapa.add_edge ("Auburn", "Fort Meadows", 15, ["camiao", "heli"]) # 2 -> 10
    mapa.add_edge ("Auburn", "Lady Liberty Island", 15, ["barco"]) # 2 -> 12

    mapa.add_edge ("Bright Lights Plaza", "Lady Liberty Island", 15, ["barco"]) # 6 -> 12
    mapa.add_edge ("Bright Lights Plaza", "Crescent Park", 15, ["camiao", "heli"]) # 6 -> 7
    mapa.add_edge ("Bright Lights Plaza", "Paradise Sands", 15, ["camiao", "heli"]) # 6 -> 8
    mapa.add_edge ("Bright Lights Plaza", "Festival Square", 15, ["camiao"]) # 6 -> 3


    mapa.add_edge ("Paradise Sands", "Lego City Airport", 15, ["camiao"]) # 8 -> 9
    mapa.add_edge ("Paradise Sands", "Kings Court", 15, ["heli"]) # 8 -> 4

    mapa.add_edge ("Crescent Park", "Lego City Airport", 15, ["camiao"]) # 7 -> 9
    mapa.add_edge ("Crescent Park", "Bluebell National Park", 15, ["camiao", "heli", "comboio"]) # 7 -> 11

    mapa.add_edge ("Bluebell National Park", "Fort Meadows", 15, ["camiao", "heli", "comboio"]) # 11 -> 10

    # mapa.set_necessidade_cidade ("Cherry Tree Hills", 100)
    # mapa.set_necessidade_cidade ("Albatross Island", 100)
    # mapa.set_necessidade_cidade ("Downtown", valor)
    # mapa.set_necessidade_cidade ("Bright Lights Plaza", valor)
    # mapa.set_necessidade_cidade ("Paradise Sands", valor)
    # mapa.set_necessidade_cidade ("Crescent Park", valor)
    # mapa.set_necessidade_cidade ("Bluebell National Park", valor)
    # mapa.set_necessidade_cidade ("Lady Liberty Island", valor)
    mapa.set_necessidade_cidade ("Lego City Airport", 100)
    # mapa.set_necessidade_cidade ("Festival Square", valor)
    # mapa.set_necessidade_cidade ("Fort Meadows", valor)
    # mapa.set_necessidade_cidade ("Kings Court", valor)
    # mapa.set_necessidade_cidade ("Auburn", valor)
