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

def custo_discount (posicao):
    match posicao:
        case 0:
            return 0.7
        case 1:
            return 0.8
        case 2:
            return 0.85
        case _:
            return 0.9

def menor_custo (mapa : Mapa, nodo1, nodo2, carga_atual) :

    menorcusto = float ('inf') # Numero maior que todos os outros
    melhorveiculo = None

    for (nodo,distancia,acessibilidade, _) in mapa.m_graph [nodo1]: # Verificar se o destino está conectado à cidade atual
        if nodo == nodo2:

            for tipo in acessibilidade: # Itera sobre todos os veiculos naquela conexão

                veiculo = Veiculo (tipo)
                cargaCopy = carga_atual

                veiculos_necessarios = math.ceil (cargaCopy / veiculo.getCapacidade())
                combustivel_gasto = veiculo.calcula_combustivel_consumido (distancia) * veiculos_necessarios

                custo = 0.5 * combustivel_gasto + ( 500 / (veiculo.getVelocidade ()))      
                
                print (f"tipo_veiculo: {tipo}   combustive gasto: {combustivel_gasto}   veiculos necessarios: {veiculos_necessarios}   velocidade: {veiculo.getVelocidade ()}")
                print (f"custo resultado deste tipo: {custo}")
                print ("")

                if custo < menorcusto: # Agora verifica se muda ou não o método de transporte
                    menorcusto = custo
                    melhorveiculo = veiculo

            if nodo2 in mapa.lista_preferencias :
                custo = custo * custo_discount(mapa.lista_preferencias.index (nodo2))

    print (f"escolhi o {melhorveiculo.tipo}")
    print ("")

    return (menorcusto, melhorveiculo)

def calcula_custo(mapa, caminho, carga):

        caminho_veiculos = []
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

def iterator (mapa: Mapa, nodo_inicial_input, carga, algoritmo) :

    caminho_veiculos_total = []
    custo_total = 0

    nodo_inicial = nodo_inicial_input

    while mapa.lista_preferencias != [] :
        print (f"{nodo_inicial.cidade} -> {mapa.lista_preferencias [0].cidade}")
        match algoritmo:


            case "BFS" :
                (caminho_veiculos, custo) = procuraBFS (mapa, nodo_inicial, mapa.lista_preferencias [0], carga)

            case "DFS" :
                (caminho_veiculos, custo) = procura_DFS (mapa, nodo_inicial, mapa.lista_preferencias [0], carga, caminho = [], visited = set())

            case "A*" :
                (caminho_veiculos, custo) = procura_AEstrela (mapa, nodo_inicial, mapa.lista_preferencias [0], carga)

        caminho_veiculos_total = caminho_veiculos_total + caminho_veiculos
        custo_total += custo

        for (_, nodob, _) in caminho_veiculos :
            if nodob in mapa.lista_preferencias :
                if nodob.necessidade > carga :
                    nodob.mantimentos_atuais = carga
                    nodob.necessidade -= carga
                    carga = 0
                    print("Ficou sem carga em: " + nodob.cidade)
                    return (caminho_veiculos_total, custo_total)
                
                carga -= nodob.necessidade
                nodob.mantimentos_atuais = nodob.necessidade
                mapa.set_necessidade_cidade(nodob.cidade, 0)        #reset à necessidade para 0
                mapa.lista_preferencias.remove (nodob)

                print ("")
                print (f"descarregou no nodo {nodob.cidade}")
                print ("")

        (_, nodo_inicial, _) = caminho_veiculos [-1]

    return (caminho_veiculos_total, custo_total)



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
            for (adjacente, _, _, ativo) in mapa.m_graph[nodo_atual] : # Procura adjacentes
                if adjacente not in visited and ativo == True : # Apenas nao visitados e !ativos!

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

    for (adjacente, _, _, ativo) in mapa.m_graph[nodo_inicial] :# Recursivo para cada branch que parte deste nodo

        if adjacente not in visited and ativo == True:      # verifica se é ativo também

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

def procura_AEstrela(mapa, start, end, carga):

    open_list = {start}
    closed_list = set()

    g = {}
    g[start] = 0

    parents = {}
    parents[start] = start

    while len(open_list) > 0:

        n = None

        for v in open_list:
            if n is None or g[v] + mapa.getH(v) < g[n] + mapa.getH(n):
                n = v

        mapa.setAllH(n)  # Atualiza as heurísticas

        if n is None:
            print('Path does not exist!')
            return None

        if n == end:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)
            reconst_path.reverse()
            print(reconst_path)
            caminho_veiculos, custo = calcula_custo(mapa, reconst_path, carga)
            return (caminho_veiculos, custo)

        for (m, weight, acessibilidade, ativo) in mapa.m_graph[n]:
            if ativo:  # Verifica se a aresta está ativa
                temp_custo, _ = menor_custo(mapa, n, m, carga)
                print(f"{temp_custo}")
                print(f" heuristica {mapa.getH(n)}")
                print(f"{g[n]}")
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + temp_custo
                else:
                    if g[m] > g[n] + temp_custo:
                        g[m] = g[n] + temp_custo
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None