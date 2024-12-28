from Definicoes import *

#Eu para já meti stats não muito precisos, depois temos que ver melhor

def criar_veiculos():
    veiculos = []

    # Criar veículos terrestres
    veiculo1 = Veiculo(capacidade_carga=50, carga_atual=0, combustivel=10, autonomia=10, velocidade=60, tipo="camiao")
    veiculo2 = Veiculo(capacidade_carga=70, carga_atual=0, combustivel=15, autonomia=15, velocidade=55, tipo="camiao")
    veiculo3 = Veiculo(capacidade_carga=60, carga_atual=40, combustivel=20,autonomia=20,velocidade=50,tipo="camiao")

    # Criar veículos aéreos
    veiculo4 = Veiculo(capacidade_carga=20, carga_atual=0, combustivel=10, autonomia=10, velocidade=90, tipo="helicoptero") 
    veiculo5 = Veiculo(capacidade_carga=15, carga_atual=0, combustivel=12, autonomia=10, velocidade=100, tipo="helicoptero")

    # Criar veículos ferroviários
    veiculo6 = Veiculo(capacidade_carga=100, carga_atual=80, combustivel=15, autonomia=15, velocidade=40, tipo="comboio")

    #Criar veículos aquáticos
    veiculo7 = Veiculo(capacidade_carga=90, carga_atual=40,combustivel=20,autonomia=10,velocidade=30,tipo="barco")

    veiculos.extend([veiculo1, veiculo2, veiculo3, veiculo4, veiculo5, veiculo6, veiculo7])

    return veiculos

