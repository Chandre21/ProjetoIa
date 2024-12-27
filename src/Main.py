
from Definicoes import *
from CriarMapa import *

def main () :

    mapa = criarMapa ()

    for cidade in mapa.cidades :
        print (cidade.nome)


if __name__ == "__main__":
    main ()