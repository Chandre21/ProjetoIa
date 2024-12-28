
from Definicoes import *

def criarMapa () :

    mapa = Mapa ()

    # Criar cidades
    cidade1 = Cidade ("Lego city 1", 100, 20, [])

    cidade2 = Cidade ("Lego city 2", 50, 10, [])

    cidade3 = Cidade ("Lego city 3", 80, 40, [])

    cidade4 = Cidade ("Lego city 4", 70, 20, [])

    cidade5 = Cidade ("Lego city 5", 120, 50, [])

    cidade6 = Cidade ("Lego city 6", 90, 60, [])

    cidade7 = Cidade ("Lego city 7", 60, 30, [])

    cidade8 = Cidade ("Lego city 8", 40, 20, [])

    cidade9 = Cidade ("Lego city 9", 50, 0, [])

    cidade10 = Cidade ("Lego city 10", 120, 80, [])

    cidade11 = Cidade ("Lego city 11", 25, 15, [])

    cidade12 = Cidade ("Lego city 12", 30, 10, [])

    cidade13 = Cidade ("Lego city 13", 95, 45, [])

    #Conexoes cidade 1
    cidade1.conexoes.append(Conexao(cidade2, 2, ["camiao","helicoptero"]))
    cidade1.conexoes.append(Conexao(cidade3, 5, ["camiao"]))
    cidade1.conexoes.append(Conexao(cidade5, 7, ["helicoptero"]))
    cidade1.conexoes.append(Conexao(cidade13, 9, ["helicoptero"]))

    #Conexoes cidade 2
    cidade2.conexoes.append(Conexao(cidade1, 2, ["camiao","helicoptero"]))
    cidade2.conexoes.append(Conexao(cidade10, 4, ["camiao","helicoptero"]))
    cidade2.conexoes.append(Conexao(cidade12, 5, ["barco"]))

    #Conexoes cidade 3
    cidade3.conexoes.append(Conexao(cidade1, 5, ["camiao"]))
    cidade3.conexoes.append(Conexao(cidade5, 2, ["camiao"]))
    cidade3.conexoes.append(Conexao(cidade6, 4, ["camiao"]))

    #Conexoes cidade 4
    cidade4.conexoes.append(Conexao(cidade5, 2, ["camiao","helicoptero"]))
    cidade4.conexoes.append(Conexao(cidade8, 5, ["helicoptero"]))

    #Conexoes cidade 5
    cidade5.conexoes.append(Conexao(cidade1, 7, ["helicoptero"]))
    cidade5.conexoes.append(Conexao(cidade3, 2, ["camiao"]))
    cidade5.conexoes.append(Conexao(cidade4, 2, ["camiao","helicoptero"]))
    cidade5.conexoes.append(Conexao(cidade13, 6, ["barco","helicoptero"]))

    #Conexoes cidade 6
    cidade6.conexoes.append(Conexao(cidade3, 4, ["camiao"]))
    cidade6.conexoes.append(Conexao(cidade7, 3, ["camiao","helicoptero"]))
    cidade6.conexoes.append(Conexao(cidade8, 5, ["camiao","helicoptero"]))
    cidade6.conexoes.append(Conexao(cidade12, 6, ["barco"]))

    #Conexoes cidade 7
    cidade7.conexoes.append(Conexao(cidade6, 3, ["camiao","helicoptero"]))
    cidade7.conexoes.append(Conexao(cidade9, 2, ["camiao"]))
    cidade7.conexoes.append(Conexao(cidade11, 10, ["camiao","comboio","helicoptero"]))

    #Conexoes cidade 8
    cidade8.conexoes.append(Conexao(cidade4, 5, ["helicoptero"]))
    cidade8.conexoes.append(Conexao(cidade6, 5, ["camiao","helicoptero"]))
    cidade8.conexoes.append(Conexao(cidade9, 2, ["camiao"]))

    #Conexoes cidade 9
    cidade9.conexoes.append(Conexao(cidade7, 2, ["camiao"]))
    cidade9.conexoes.append(Conexao(cidade8, 2, ["camiao"]))

    #Conexoes cidade 10
    cidade10.conexoes.append(Conexao(cidade1, 9, ["comboio"]))
    cidade10.conexoes.append(Conexao(cidade2, 4, ["camiao","helicoptero"]))
    cidade10.conexoes.append(Conexao(cidade11, 3, ["camiao","comboio","helicoptero"]))

    #Conexoes cidade 11
    cidade11.conexoes.append(Conexao(cidade7, 10, ["camiao","comboio","helicoptero"]))
    cidade11.conexoes.append(Conexao(cidade10, 3, ["camiao","comboio","helicoptero"]))

    #Conexoes cidade 12
    cidade12.conexoes.append(Conexao(cidade2, 5, ["barco"]))
    cidade12.conexoes.append(Conexao(cidade6, 6, ["barco"]))

    #Conexoes cidade 13
    cidade13.conexoes.append(Conexao(cidade1, 2, ["helicoptero"]))
    cidade13.conexoes.append(Conexao(cidade5, 2, ["barco","helicoptero"]))

    mapa.cidades.extend([cidade1, cidade2, cidade3, cidade4, cidade5, cidade6, cidade7, cidade8, cidade9, cidade10, cidade11, cidade12, cidade13])
    
    return mapa

