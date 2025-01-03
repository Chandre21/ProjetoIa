
from Mapa import *
from Veiculo import *
from AlgoritmosProcura import *

def clearScreen () :
    for a in range (50) :
        print ("")

def runCenario (mapa:Mapa, carga) :

    running = True

    while running :

        popular_lista_preferencias (mapa)

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

        nodo_inicial_str = "Bright Lights Plaza"
        nodo_final_str = "Lego City Airport"

        nodo_inicial = mapa.get_node_by_name (nodo_inicial_str)
        nodo_final = mapa.get_node_by_name (nodo_final_str)

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

    popularMapa (mapa)

    running = True

    # GUIzinha marota
    while running :
        clearScreen ()

        # Dispor operacoes
        print ("Escolha uma operacao:")
        print ("1 - Executar cenario")
        print ("2 - Mudar prioridade de cidades")
        print ("3 - Encerrar conexoes entre cidades")
        print ("9 - Sair")

        # Ler numero obtido
        choice = int(input(": "))

        if choice == 1 :
            clearScreen ()
            carga = int (input ("Insira a carga inicial: "))
            runCenario (mapa, carga)

        elif choice == 2 :
            clearScreen ()
            pass

        elif choice == 3 :
            clearScreen ()
            pass

        elif choice == 9 :
            clearScreen ()
            running = False



if __name__ == "__main__":
    main ()
