# Classe grafo para representaçao de grafos

from Definicoes import Cidade

class Grafo:
    cidades : list [Cidade]
    def __init__(self):     #construtor, grafo tem nodos, arestas, e heurísticas
        self.cidades = []  
        #self.m_graph = {}  # dicionario para armazenar os nodos e arestas   |   guarda par (nodo2, custo) por cada nodo, ou seja, indice é nodo, nodo2 é o outro, custo é associado
        self.heur = {}      # dicionario para posterirmente armazenar as heuristicas para cada nodo -> pesquisa informada

    ######################################
    #    escrever o grafo como string    #          #basicamente a mesma que imprimir arestas
    ######################################
    def __str__(self):
        out = ""
        for cidade in self.cidades:
            for conexao in cidade.conexoes:
                out = out + cidade.nome + " -> " + conexao.node_final + ", custo: " + str(conexao.custo_do_salto) + ", acessível por: " + str(conexao.acessibilidade) + "\n"
        return out

    ################################
    #   encontrar nodo pelo nome   #
    ################################
    def get_node_by_name(self, name):
        search_node = Cidade(name)

        for node in self.cidades:
            if node == search_node:
                return node
          
        return None

    #################################
    #   adicionar aresta no grafo   #
    #################################
    def add_edge(self, node1, node2, custo, acessibilidade):
        n1 = Cidade(node1)
        n2 = Cidade(node2)

        if (n1 not in self.cidades):
            n1_id = len(self.cidades)        #numeração sequencial
            n1.setId(n1_id)
            
            self.cidades.append(n1)
        else:
            n1 = self.get_node_by_name(node1)

        if (n2 not in self.cidades):
            n2_id = len(self.cidades)        #numeração sequencial
            n2.setId(n2_id)
            
            self.cidades.append(n2)
        else:
            n2 = self.get_node_by_name(node2)

        #agora faltava meter o custo, acessibilidade e yada yada yada

