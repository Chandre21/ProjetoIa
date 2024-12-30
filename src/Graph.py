# Classe grafo para representaçao de grafos,
import math
from queue import Queue

from Nodo import Nodo


# Constructor
# Number of edges
# Adjacancy matrix, adjacency list, list of edges

# Methods for adding edges

# Methods for removing edges

# Methods for searching a graph
# BFS, DFS, A*, Greedy


class Graph:
    def __init__(self):#nodo [(nodo_final,custo,acessibljijaci, ativo?)]
        self.m_cidades = []       # lista de cidades
        self.m_graph = {}       # dicionario para armazenar os nodos e arestas (tuplo da informação - destino, custo, acessibilidade) 
        self.m_h = {}           # dicionario para posterirmente armazenar as heuristicas para cada nodo -> pesquisa informada

    ######################################
    #    escrever o grafo como string    #
    ######################################

    def __str__(self):

        out = ""

        for key in self.m_graph.keys():
            out = out + "cidade" + str(key) + ": " + str(self.m_graph[key]) + "\n"
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
                listaA = listaA + nodo + " -> " + nodo2 + ", custo: " + str(custo) + ", acessibilidade: " + str(acessibilidade) + "\n"
        return listaA
    
    #################################
    #   adicionar aresta no grafo   #
    #################################

    def add_edge(self, nodo1, nodo2, peso, acessibilidade):     #recebe o nome dos nodos basicamente, peso e LISTA da acessibilidade

        c1 = Nodo(nodo1)
        c2 = Nodo(nodo2)

        if (c1 not in self.m_cidades):
            c1_id = len(self.m_nodes)  # numeração sequencial
            c1.setId(c1_id)
            c1.setNecessidade = 0;      #necessidade e mantimentos atuais a 0,0
            c1.setMAtuais = 0;
            self.m_cidades.append(c1)
            self.m_graph[nodo1] = []
        else:
            c1 = self.get_node_by_name(nodo1)

        if (c2 not in self.m_cidades):
            c2_id = len(self.m_nodes)  # numeração sequencial
            c2.setId(c2_id)
            c2.setNecessidade = 0;      #necessidade e mantimentos atuais a 0,0
            c2.setMAtuais = 0;
            self.m_cidades.append(c2)
            self.m_graph[nodo2] = []
        else:
            n2 = self.get_node_by_name(nodo2)

        self.m_graph[nodo1].append((nodo2, peso, acessibilidade))       #só passar a acessibilidade como lista and we gucci
        self.m_graph[nodo2].append((nodo1, peso, acessibilidade))       #também vou assumir que posso fazer tuplo de 3 elementos
            #é tudo bidirecional

    ######################
    #   devolver nodos   #
    ######################

    def getNodes(self):
        return self.m_cidades
    
    ######################################
    #   devolver o custo de uma aresta   #
    ######################################

    def get_arc_cost(self, nodo1, nodo2):

        custoT = math.inf
        a = self.m_graph[nodo1]             #lista de arestas para aquele nodo

        for (nodo, custo, _) in a:          #aqui a acessibilidade não interessa
            if nodo == nodo2:
                custoT = custo

        return custoT
    
    ###############################################
    #   devolver a acessibilidade de uma aresta   #
    ###############################################

    def get_arc_acess(self, nodo1, nodo2):

        access = list[str]                  #declarar que é lista de string
        a = self.m_graph[nodo1]             #lista de arestas para aquele nodo

        for (nodo, _, acessibilidade) in a:          #aqui a acessibilidade não interessa
            if nodo == nodo2:
                access = acessibilidade

        return access

    ############################################
    #   menor custo entre 2 nodos adjacentes   #
    ############################################

    def menor_custo(self, nodo1, nodo2, carga):
        

    ###########################################
    #   dado um caminho calcula o seu custo   #     -> vai precisar da função de custo, só devolve o custo, 
    ###########################################     

    #função de custo, ciclo para passar a carga toda de um nodo para o próximo, influenciada por capacidade, velocidade, autonomia