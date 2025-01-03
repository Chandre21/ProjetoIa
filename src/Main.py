
from Mapa import *
from Veiculo import *
from AlgoritmosProcura import *

def clearScreen () :
    for a in range (50) :
        print ("")

def runCenario (mapa:Mapa, carga) :

    running = True

    while running :

        # Dispor algoritmos
        print ("Escolha um algoritmo:")
        print ("1 - A*")
        print ("2 - BFS")
        print ("3 - DFS")
        print ("9 - Voltar atras")

        # Ler numero obtido
        choice = int(input(": "))

        nodo_inicial_str = "Cherry Tree Hills"
        nodo_final_str = "Lego City Airport"

        nodo_inicial = mapa.get_node_by_name (nodo_inicial_str)
        nodo_final = mapa.get_node_by_name (nodo_final_str)

        if nodo_inicial is None or nodo_final is None: 
            print(f"Erro: Os nodos '{nodo_inicial_str}' ou '{nodo_final_str}' não foram encontrados no mapa.") 
            return

        if choice == 1 :
            clearScreen ()
            #A*
            (caminho_veiculos, custo) = procura_AEstrela(mapa, nodo_inicial, nodo_final, carga)

            print (f"custo: {custo}")
            print ("caminho percorrido:")
            for (nodoa, nodob, veiculo) in caminho_veiculos :
                print (f"{nodoa.cidade} -----> {nodob.cidade} = Veiculo escolhido: {veiculo.tipo}")

        elif choice == 2 :
            clearScreen ()
            # BFS
            (caminho_veiculos, custo) = procuraBFS (mapa, nodo_inicial, nodo_final, carga)

            print (f"custo: {custo}")
            print ("caminho percorrido:")
            for (nodoa, nodob, veiculo) in caminho_veiculos :
                print (f"{nodoa.cidade} -----> {nodob.cidade} = Veiculo escolhido: {veiculo.tipo}")

        elif choice == 3 :
            clearScreen ()
            # DFS
            (caminho_veiculos, custo) = procura_DFS(mapa, nodo_inicial, nodo_final, carga, caminho=[], visited=set())

            print (f"custo: {custo}")
            print ("caminho percorrido:")
            for (nodoa, nodob, veiculo) in caminho_veiculos :
                print (f"{nodoa.cidade} -----> {nodob.cidade} = Veiculo escolhido: {veiculo.tipo}")

        elif choice == 9 :
            clearScreen ()
            running = False


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
