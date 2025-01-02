# BFS
# DFS
# A*

from queue import Queue

from Mapa import *
from Veiculo import *



##################################
#     Obter custo de caminho     #
##################################

def menor_custo (mapa : Mapa, nodo1, nodo2, carga_atual) :

    c1 = mapa.get_node_by_name(nodo1)
    c2 = mapa.get_node_by_name(nodo2)

    conexoesC1 = mapa.m_graph [c1]
    menorcusto = float ('inf') # Numero maior que todos os outros
    melhorveiculo = None

    for (nodo,distancia,acessibilidade) in conexoesC1: # Verificar se o destino está conectado à cidade atual
        if nodo == c2:

            if c2 in mapa.lista_preferencias :
                custo = - ((mapa.lista_preferencias.__len__ - mapa.lista_preferencias.index (c2)) * 10)
            else :
                custo = 0

            for tipo in acessibilidade: # Itera sobre todos os veiculos naquela conexão

                veiculo = Veiculo (tipo)
                cargaCopy = carga_atual

                veiculos_necessarios = math.ceil (cargaCopy / veiculo.getCapacidade())
                combustivel_gasto = veiculo.calcula_combustivel_consumido (distancia) * veiculos_necessarios

                custo += 0.5 * combustivel_gasto + 0.5 * veiculo.getVelocidade ()
                # 50% combustivel
                # 50% velocidade

                if custo < menorcusto: # Agora verifica se muda ou não o método de transporte
                    menorcusto = custo
                    melhorveiculo = veiculo

    return (menorcusto, melhorveiculo)

def calcula_custo(caminho, carga):

        caminho_veiculos = []
        caminho
        custo = 0
        i = 0

        while i + 1 < len (caminho) :

            nodoa = caminho[i]
            nodob = caminho[i + 1]

            (temp_custo, veiculo) = menor_custo(nodoa, nodob, carga)

            custo += temp_custo # Acrescenta o menor custo da aresta ao custo total
            caminho_veiculos.append((nodoa, nodob, veiculo)) # Lista com os nodos da aresta e o respetivo veiculo otimo
            i = i + 1 # Não me deixa fazer i++, outrageous :o

        return (caminho_veiculos, custo)



########################
#      Algoritmos      #
########################

def procuraBFS (mapa: Mapa, nodo_inicial, nodo_final, carga) :
    # definir nodos visitados para evitar ciclos
    visited = set ()
    fila = Queue ()
    custo = 0

    # adicionar o nodo inicial à fila e aos visitados
    fila.put(nodo_inicial)
    visited.add(nodo_inicial)

    parent = dict ()
    parent [nodo_inicial] = None

    encontrado = False
    while not fila.empty () and encontrado == False :
        nodo_atual = fila.get ()

        if nodo_atual == nodo_final :
            encontrado = True # Encontrou caminho

        else:
            for (adjacente, peso) in mapa.m_graph[nodo_atual] : # Procura adjacentes
                if adjacente not in visited : # Apenas nao visitados

                    fila.put (adjacente) # Mete para procurar
                    parent [adjacente] = nodo_atual
                    visited.add (adjacente) # Marca como visitado

    caminho = []

    if encontrado :
        caminho.append(nodo_final)

        while parent [nodo_final] is not None:
            caminho.append (parent[nodo_final])
            nodo_final = parent[nodo_final]

        caminho.reverse ()

        (caminho_veiculos, custo) = mapa.calcula_custo (caminho, carga)

    return (caminho_veiculos, custo)