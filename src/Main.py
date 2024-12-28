
from Definicoes import *
from CriarMapa import *
from CriarVeiculos import *
from Movimentacao import *

def main () :

    mapa = criarMapa ()

    veiculos = criar_veiculos()

    cidade_inicial = mapa.cidades[0]
    veiculo = veiculos[0]

    entrega = Entrega(veiculo,cidade_inicial)

    print(f"Início da entrega em {cidade_inicial.nome} com o veículo {veiculo.tipo}.")

    cidade_final1 = mapa.cidades[1]

    resultado = movimentar_veiculo(entrega, cidade_final1)
    print(resultado)

    print(f"Cidade atual: {entrega.node_atual.nome}")
    print(f"Custo acumulado: {entrega.custo_acumulado}")

    cidade_final2 = mapa.cidades[9]

    resultado = movimentar_veiculo(entrega, cidade_final2)
    print(resultado)

    print(f"Cidade atual: {entrega.node_atual.nome}")
    print(f"Custo acumulado: {entrega.custo_acumulado}")    

if __name__ == "__main__":
    main ()