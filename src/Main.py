
from Mapa import *
from Veiculo import *
from AlgoritmosProcura import *

def clearScreen () :
    for a in range (50) :
        print ("")

def runCenario () :

    running = True

    while running :

        # Dispor algoritmos
        print ("Escolha um algoritmo:")
        print ("1 - Minimax")
        print ("2 - Custo Uniforme")
        print ("3 - BFS")
        print ("4 - DFS")
        print ("9 - Voltar atras")

        # Ler numero obtido
        choice = int(input(":"))

        if choice == 1 :
            # run minimax
            pass

        elif choice == 2 :
            # run Custo Uniforme
            pass

        elif choice == 3 :
            # BFS
            pass

        elif choice == 3 :
            # DFS
            pass

        elif choice == 9 :
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
        choice = int(input(":"))

        if choice == 1 :
            runCenario ()

        elif choice == 2 :
            pass

        elif choice == 3 :
            pass

        elif choice == 9 :
            running = False



if __name__ == "__main__":
    main ()
