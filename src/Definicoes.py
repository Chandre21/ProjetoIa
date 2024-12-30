class Veiculo :
    capacidade_carga : int
    carga_atual : int
    combustivel : int # Quantos nodes pode andar até proximo reabastecimento
    autonomia : int # Quantos nodes consegue andar sem reabastecer
    velocidade : int
    tipo : str # Camião, Helicóptero, Barco, Combóio

    def __init__(self, carga_atual: int, combustivel: int, tipo: str):
        self.carga_atual = carga_atual
        self.combustivel = combustivel
        self.tipo = tipo

        match tipo:
            case "camiao":              #valores rudimentares, depois muda-se, e no final, calcular tempo como inverso da vel
                self.capacidade_carga = 500
                self.autonomia = 5
                self.velocidade = 60

            case "heli":
                self.capacidade_carga = 150
                self.autonomia = 10
                self.velocidade = 200
            case "barco":
                self.capacidade_carga = 1000
                self.autonomia = 35
                self.velocidade = 40
            case "comboio":
                self.capacidade_carga = 800
                self.autonomia = 30
                self.velocidade = 140
            case _ :
                self.tipo = "carro"         #default, mas secalhar removo e meto camião
                self.capacidade_carga = 100
                self.autonomia = 20
                self.velocidade = 120

        

#class Mapa :
#    cidades : list ['Cidade']
#
#    def __init__ (self):
#        self.cidades = []          -> passou para a classe Grafo


class Cidade :
    id : int
    nome : str
    necessidade : int # carga total necessária
    mantimentos_atuais : int # carga atual

    conexoes : list ['Conexao'] # cidade, custo

    def __init__(self,id : int, nome: str, necessidade: int, mantimentos_atuais: int, conexoes: list['Conexao']):
        self.id = id
        self.nome = nome
        self.necessidade = necessidade
        self.mantimentos_atuais = mantimentos_atuais
        self.conexoes = conexoes

    def setId(self, id):
        self.id = id

class Conexao :
    node_final : Cidade
    custo_do_salto : int
    acessibilidade : list [str]     #lista de veiculos

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
        self.custo_acumulado = 0