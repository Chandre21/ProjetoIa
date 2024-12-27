class Veiculo :
    capacidade_carga : int
    carga_atual : int
    combustivel : int # Quantos nodes pode andar até proximo reabastecimento
    autonomia : int # Quantos nodes consegue andar sem reabastecer
    velocidade : int
    tipo : str # Aereo Terrestre Maritimo, idk,mais tipo, carro, comboio, barco, coiso e tal

    def __init__(self, capacidade_carga: int, carga_atual: int, combustivel: int, autonomia: int, velocidade: int, tipo: str):
        self.capacidade_carga = capacidade_carga
        self.carga_atual = carga_atual
        self.combustivel = combustivel
        self.autonomia = autonomia
        self.velocidade = velocidade
        self.tipo = tipo

class Mapa :
    cidades : list ['Cidade']

    def __init__ (self):
        self.cidades = []


class Cidade :
    nome : str
    necessidade : int # carga total necessária
    mantimentos_atuais : int # carga atual

    conexoes : list ['Conexao'] # cidade, custo

    def __init__(self, nome: str, necessidade: int, mantimentos_atuais: int, conexoes: list['Conexao']):
        self.nome = nome
        self.necessidade = necessidade
        self.mantimentos_atuais = mantimentos_atuais
        self.conexoes = conexoes

class Conexao :
    # node_inicial : Cidade
    node_final : Cidade
    custo_do_salto : int
    acessibilidade : list [str]     #lista de veiculos? idk

    def __init__(self, node_final: Cidade, custo_do_salto: int, acessibilidade: list[str]) :
        self.node_final = node_final
        self.custo_do_salto = custo_do_salto
        self.acessibilidade = acessibilidade


class Entrega :
    veiculo : Veiculo
    cidade_atual : Cidade
    custo_acumulado : int # Custo que estamos a tentar minimizar

    def __init__(self, veiculo: Veiculo, node_atual: Cidade) :
        self.veiculo = veiculo
        self.node_atual = node_atual

    def move (cidade_adjacente) :
        node_atual = cidade_adjacente [0]
        custo_acumulado += cidade_adjacente [1]