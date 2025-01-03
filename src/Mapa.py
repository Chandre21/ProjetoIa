# Classe grafo para representaçao de grafos,
import math
import random
from queue import Queue

from Nodo import Nodo

class Mapa:
    def __init__(self):         #nodo [(nodo_final,custo,acessibilidade, ativo)]
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
            for (nodo2, custo, acessibilidade, _) in self.m_graph[nodo]:       #acessibilidade vai ser a lista dos tipos de veiculos
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

        self.m_graph[c1].append((c2, peso, acessibilidade, True))       #só passar a acessibilidade como lista and we gucci
        self.m_graph[c2].append((c1, peso, acessibilidade, True))       #também vou assumir que posso fazer tuplo de 3 elementos
            #é tudo bidirecional, ativo por default

    ######################
    #   devolver nodos   #
    ######################

    def getNodes(self):
        return self.m_cidades

    def set_necessidade_cidade (self, nome_cidade, necessidade):
        nodo = self.get_node_by_name (nome_cidade)
        nodo.setNecessidade (necessidade)

    ############################
    #   devolver heuristicas   #
    ############################

    def getH(self,nodo):
        return self.heuristicas.get(nodo, float('inf'))

    def setH(self,nome_nodo,heuristica):
        nodo = self.get_node_by_name(nome_nodo)
        if nodo:
            self.heuristicas[nodo] = heuristica
        
    def setAllH(self, nodob):       #define a heuristica de acordo com o nodo em que está

        for nodoi in self.m_cidades:
            
            if nodoi != nodob:

                diferenca = abs(nodob.getId() - nodoi.getId())      #calcula a diferença dos ints

                self.heuristicas[nodoi] = diferenca     #IT WORKSSSSSSSSSSSS
            else:
                self.heuristicas[nodob] = 0         #heuristica 0 para si proprio


    ##############################
    #   Ativar/desativar nodos   #
    ##############################

    def ativarCon(self, nodo1, nodo2):

        for (nodo, _, _, ativo) in self.m_graph [nodo1]:        #1 --ativo-> 2
            if nodo == nodo2:
                ativo == True

        for (nodo, _, _, ativo) in self.m_graph [nodo2]:        #2 --ativo-> 1
            if nodo == nodo1:
                ativo == True
    
    def desativarCon(self, nodo1, nodo2):

        for (nodo, _, _, ativo) in self.m_graph [nodo1]:        #1 --desativo-> 2
            if nodo == nodo2:
                ativo == False

        for (nodo, _, _, ativo) in self.m_graph [nodo2]:        #2 --desativo-> 1
            if nodo == nodo1:
                ativo == False

    def bridgesBeGone(self):        #desativa todas as conexões de pontes (exceto aquela de comboio)

        self.desativarCon(self.get_node_by_name("Cherry Tree Hills"), self.get_node_by_name("Festival Square"))
        self.desativarCon(self.get_node_by_name("Auburn"), self.get_node_by_name("Fort Meadows"))
        self.desativarCon(self.get_node_by_name("Crescent Park"), self.get_node_by_name("Bluebell National Park"))
        
    def restrictedAirspace(self):       #desativa rotas exclusivas de helicoptero e bright lights paradise

        self.desativarCon(self.get_node_by_name("Cherry Tree Hills"), self.get_node_by_name("Albatross Island"))
        self.desativarCon(self.get_node_by_name("Cherry Tree Hills"), self.get_node_by_name("Downtown"))
        self.desativarCon(self.get_node_by_name("Paradise Sands"), self.get_node_by_name("Kings Court"))
        self.desativarCon(self.get_node_by_name("Paradise Sands"), self.get_node_by_name("Bright Lights Plaza"))

    ####################
    #  Popular o mapa  #
    ####################

    def popularMapa (self) :
        self.add_edge ("Cherry Tree Hills", "Auburn", 10, ["camiao", "heli"]) # 1 -> 2
        self.add_edge ("Cherry Tree Hills", "Albatross Island", 25, ["heli"]) # 1 -> 13
        self.add_edge ("Cherry Tree Hills", "Fort Meadows", 16, ["comboio"]) # 1 -> 10
        self.add_edge ("Cherry Tree Hills", "Festival Square", 12, ["camiao"]) # 1 -> 3
        self.add_edge ("Cherry Tree Hills", "Downtown", 15, ["heli"]) # 1 -self

        self.add_edge ("Albatross Island", "Downtown", 15, ["barco", "heli"]) # 13 -self

        self.add_edge ("Downtown", "Kings Court", 8, ["camiao", "heli"]) # 5 -> 4
        self.add_edge ("Downtown", "Festival Square", 9, ["camiao"]) # 5 -self

        self.add_edge ("Auburn", "Fort Meadows", 16, ["camiao", "heli"]) # 2 -> 10
        self.add_edge ("Auburn", "Lady Liberty Island", 15, ["barco"]) # 2 ->self

        self.add_edge ("Bright Lights Plaza", "Lady Liberty Island", 12, ["barco"]) # 6 -> 12
        self.add_edge ("Bright Lights Plaza", "Crescent Park", 8, ["camiao", "heli"]) # 6 -> 7
        self.add_edge ("Bright Lights Plaza", "Paradise Sands", 13, ["camiao", "heli"]) # 6 -> 8
        self.add_edge ("Bright Lights Plaza", "Festival Square", 10, ["camiao"]) # 6 -self

        self.add_edge ("Paradise Sands", "Lego City Airport", 8, ["camiao"]) # 8 -> 9
        self.add_edge ("Paradise Sands", "Kings Court", 20, ["heli"]) # 8 -self

        self.add_edge ("Crescent Park", "Lego City Airport", 8, ["camiao"]) # 7 -> 9
        self.add_edge ("Crescent Park", "Bluebell National Park", 17, ["camiao", "heli", "comboio"]) # 7 ->self

        self.add_edge ("Bluebell National Park", "Fort Meadows", 10, ["camiao", "heli", "comboio"]) # 11 ->self

        #self.set_necessidade_cidade ("Cherry Tree Hills", 200)
        #self.set_necessidade_cidade ("Albatross Island", 500)
        # mapa.set_necessidade_cidade ("Downtown", valor)
        # mapa.set_necessidade_cidade ("Bright Lights Plaza", valor)
        # mapa.set_necessidade_cidade ("Paradise Sands", valor)
        # mapa.set_necessidade_cidade ("Crescent Park", valor)
        # mapa.set_necessidade_cidade ("Bluebell National Park", valor)
        # mapa.set_necessidade_cidade ("Lady Liberty Island", valor)
        self.set_necessidade_cidade ("Lego City Airport", 100)
        # mapa.set_necessidade_cidade ("Festival Square", valor)
        # mapa.set_necessidade_cidade ("Fort Meadows", valor)
        # mapa.set_necessidade_cidade ("Kings Court", valor)
        # mapa.set_necessidade_cidade ("Auburn", valor)


    def popular_lista_preferencias (self) :

        self.lista_preferencias = []
        for node in self.m_cidades :

            # heuristica make pls

            if node.necessidade == 0 :
                continue

            i = 0
            while i < len (self.lista_preferencias) and node.necessidade < self.lista_preferencias [i].necessidade :
                i = i + 1

            self.lista_preferencias.insert(i, node)

        # print ("[")
        # for node in mapa.lista_preferencias :
        #     print(f"{node.necessidade},")
        # print ("]")

