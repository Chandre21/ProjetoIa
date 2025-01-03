
from Mapa import *
from Veiculo import *
from AlgoritmosProcura import *

def clearScreen () :
    for a in range (50) :
        print ("")

def runCenario (mapa:Mapa, carga) :

    running = True

    while running :

        mapa.popular_lista_preferencias()       # manter ativa se utilizarmos lista já baked in, desativa se não

        if carga <= 0:
                carga = sum(nodo.necessidade for nodo in mapa.lista_preferencias)       #carga automática

        clearScreen ()

        # Dispor algoritmos
        print ("Escolha um algoritmo:")
        print ("1 - A*")
        print ("2 - BFS")
        print ("3 - DFS")
        print ("9 - Voltar atras")

        # Ler numero obtido
        choice = int(input(": "))
        clearScreen ()

        nodo_inicial_str = "Cherry Tree Hills"

        nodo_inicial = mapa.get_node_by_name (nodo_inicial_str)

        if choice == 1 :
            #A*
            (caminho_veiculos, custo) = iterator (mapa, nodo_inicial, carga, "A*")


        elif choice == 2 :
            # BFS
            (caminho_veiculos, custo) = iterator (mapa, nodo_inicial, carga, "BFS")


        elif choice == 3 :
            # DFS
            (caminho_veiculos, custo) = iterator (mapa, nodo_inicial, carga, "DFS")

        elif choice == 9 :
            running = False
            continue

        print (f"custo: {custo}")
        print ("caminho percorrido:")
        for (nodoa, nodob, veiculo) in caminho_veiculos :
            print (f"{nodoa.cidade} -----> {nodob.cidade} = Veiculo escolhido: {veiculo.tipo}")

        input ()


def main () :

    mapa = Mapa ()

    mapa.popularMapa()

    mapa.activateAll()      #para se fecharmos o programa mete tudo direito outra vez

    running = True

    # GUIzinha marota
    while running :
        clearScreen ()

        # Dispor operacoes
        print ("Escolha uma operacao:")
        print ("1 - Executar cenario")
        print ("2 - Definir necessidade de cidades")
        print ("3 - Simular eventos metereológicos")
        print ("4 - Reativar conexões")
        print ("9 - Sair")

        # Ler numero obtido
        choice = int(input(": "))

        if choice == 1 :
            clearScreen ()
            carga = int (input ("Insira a carga inicial (0 se quiser cálculo automático): "))

            runCenario (mapa, carga)

        elif choice == 2 :
            clearScreen ()

            cidade = str(input("Indique o nome da cidade: "))
            nec = int(input("Indique a necessidade da cidade: "))

            nodo = mapa.get_node_by_name(cidade)

            if nodo is None:                    # verifica se o nodo existe no sistema
                print("A cidade não existe. :o")
                continue
            else:
                print("A necessidade da cidade " + cidade + f" foi corretamente atualizada para {nec}.")

            nodo.setNecessidade(nec)
            
            mapa.lista_preferencias.append(nodo)
            mapa.lista_preferencias.sort(key=lambda nodo: nodo.necessidade, reverse = True)        #ordenar a lista por ordem decrescente

        elif choice == 3 :
            clearScreen ()
            
            print ("Escolha uma simulação:")
            print ("1 - Desativar pontes")
            print ("2 - Restringir espaço aéreo")
            print ("9 - Voltar atras")

            choice = int(input(": "))

            match choice:
                case 1:
                    mapa.bridgesBeGone()
                    print("Conexão: Cherry Tree Hills <-> Festival Square [Encerrada]")
                    print("Conexão: Auburn <-> Fort Meadows [Encerrada]")
                    print("Conexão: Crescent Park <-> Bluebell National Park [Encerrada]")
                case 2:
                    mapa.restrictedAirspace()
                    print("Conexão: Cherry Tree Hills <-> Albatross Island [Encerrada]")
                    print("Conexão: Cherry Tree Hills <-> Downtown [Encerrada]")
                    print("Conexão: Paradise Sands <-> Kings Court [Encerrada]")
                    print("Conexão: Paradise Sands <-> Bright Lights Plaza [Encerrada]")
                case 9:
                    continue
        
        elif choice == 4 :
            clearScreen ()

            mapa.activateAll()
            print("Todas as conexões foram restabelecidas")

        elif choice == 9 :
            clearScreen ()
            running = False



if __name__ == "__main__":
    main ()
