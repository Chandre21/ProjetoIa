# BFS
# DFS
# A*

from queue import Queue

from Mapa import *
from Veiculo import *
from Nodo import *



##################################
#     Obter custo de caminho     #
##################################

def menor_custo (mapa : Mapa, nodo1, nodo2, carga_atual) :

    conexoesC1 = mapa.m_graph [nodo1]
    menorcusto = float ('inf') # Numero maior que todos os outros
    melhorveiculo = None

    for (nodo,distancia,acessibilidade) in conexoesC1: # Verificar se o destino está conectado à cidade atual
        if nodo == nodo2:

            if nodo2 in mapa.lista_preferencias :
                custo_base = - ((mapa.lista_preferencias.__len__ - mapa.lista_preferencias.index (nodo2)) * 10)
            else :
                custo_base = 0

            for tipo in acessibilidade: # Itera sobre todos os veiculos naquela conexão

                custo = custo_base

                veiculo = Veiculo (tipo)
                cargaCopy = carga_atual

                veiculos_necessarios = math.ceil (cargaCopy / veiculo.getCapacidade())
                combustivel_gasto = veiculo.calcula_combustivel_consumido (distancia) * veiculos_necessarios

                custo += 0.5 * combustivel_gasto - 0.1 * veiculo.getVelocidade ()
                # 50% combustivel
                # 50% velocidade
                print (f"tipo_veiculo: {tipo}   combustive gasto: {combustivel_gasto}   veiculos necessarios: {veiculos_necessarios}   velocidade: {veiculo.getVelocidade ()}")
                print (f"custo resultado deste tipo: {custo}")
                print ("")

                if custo < menorcusto: # Agora verifica se muda ou não o método de transporte
                    menorcusto = custo
                    melhorveiculo = veiculo

    print (f"escolhi o {melhorveiculo.tipo}")

    return (menorcusto, melhorveiculo)

def calcula_custo(mapa, caminho, carga):

        caminho_veiculos = []
        caminho
        custo = 0
        i = 0

        while i + 1 < len (caminho) :

            nodoa = caminho[i]
            nodob = caminho[i + 1]

            (temp_custo, veiculo) = menor_custo(mapa, nodoa, nodob, carga)

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

    # Dicionario para obter pais através dos nodos filho
    parent = dict ()
    parent [nodo_inicial] = None

    encontrado = False
    while not fila.empty () and encontrado == False :
        nodo_atual = fila.get ()

        if nodo_atual == nodo_final :
            encontrado = True # Encontrou caminho

        else:
            for (adjacente, _, _) in mapa.m_graph[nodo_atual] : # Procura adjacentes
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

        (caminho_veiculos, custo) = calcula_custo (mapa, caminho, carga)

    return (caminho_veiculos, custo)


def procura_DFS(mapa, nodo_inicial, nodo_final, carga, caminho=[], visited=set()): # Por omissao caminho = [] e visited = set()


    caminho.append (nodo_inicial)
    visited.add (nodo_inicial)

    if nodo_inicial == nodo_final : # Encontrou caminho

        (caminho_veiculos, custo) = calcula_custo (mapa, caminho, carga)
        return (caminho_veiculos, custo)

    for (adjacente, _, _) in mapa.m_graph[nodo_inicial] :# Recursivo para cada branch que parte deste nodo

        if adjacente not in visited:

            resultado = procura_DFS (mapa, adjacente, nodo_final, carga, caminho, visited)

            if resultado is not None:
                return resultado

    caminho.pop () # se nao encontra remove o ultimo node procurado do caminho para passar a outra branch
    return None


    # Se tiver na lista de prioridade das cidades

    # if nodo_atual in mapa.lista_preferencias :
    #     carga -= nodo_atual.necessidade
    #     nodo_atual.mantimentos_atuais = nodo_atual.necessidade
    #     mapa.lista_preferencias.remove (nodo_atual)

