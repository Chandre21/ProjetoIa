
class Veiculo :
    capacidade_carga : int
    carga_atual : int
    combustivel : int # Quantos nodes pode andar até proximo reabastecimento
    autonomia : int # Quantos nodes consegue andar sem reabastecer
    velocidade : int
    tipo : str # Aereo Terrestre Maritimo

    def __init__(self, capacidade_carga: int, carga_atual: int, combustivel: int, autonomia: int, velocidade: int, tipo: str):
        self.capacidade_carga = capacidade_carga
        self.carga_atual = carga_atual
        self.combustivel = combustivel
        self.autonomia = autonomia
        self.velocidade = velocidade
        self.tipo = tipo



class Node :
    nome : str
    necessidade : int # carga total necessária
    mantimentos_atuais : int # carga atual
    acessibilidade : list [str]

    next_nodes : list ['Node']

    def __init__(self, nome: str, necessidade: int, mantimentos_atuais: int, acessibilidade: list[str], next_nodes: list['Node']):
        self.nome = nome
        self.necessidade = necessidade
        self.mantimentos_atuais = mantimentos_atuais
        self.acessibilidade = acessibilidade
        self.next_nodes = next_nodes



class Entrega :
    veiculo : Veiculo
    node_atual : Node

    def __init__(self, veiculo: Veiculo, node_atual: Node) :
        self.veiculo = veiculo
        self.node_atual = node_atual


