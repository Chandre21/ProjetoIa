
from Definicoes import *

def criarMapa () :

    mapa = Mapa ()

    cidade1 = Cidade ("Lego city 1", 20, 0, [Conexao('cidade2', 2, "carro")])
    # cidade1.nome = "Lego city 1"
    # cidade1.necessidade = 20
    # cidade1.mantimentos_atuais = 0
    # cidade1.conexoes = [Conexao('cidade2', 2, "carro")]

    cidade2 = Cidade ("Lego city 2", 30, 0, [Conexao('cidade1', 2, "carro")])
    # cidade2.nome = "Lego city 2"
    # cidade2.necessidade = 30
    # cidade2.mantimentos_atuais = 0
    # cidade2.conexoes = [Conexao('cidade1', 2, "carro")]

    mapa.cidades.append (cidade1)
    mapa.cidades.append (cidade2)

    return mapa

