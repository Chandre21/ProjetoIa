class Nodo:         #cidades bro
    def __init__(self, cidade):
        self.id = 0
        self.cidade = cidade
        self.necessidade = 0
        self.mantimentos_atuais = 0

    def __str__(self):
        return "Cidade " + self.cidade

    def __repr__(self):
        return "Cidade " + self.cidade

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getName(self):
        return self.cidade

    def setNecessidade(self, necessidade):
        self.necessidade = necessidade

    def setMAtuais(self, mantimentos_atuais):
        self.mantimentos_atuais = mantimentos_atuais

    def __eq__(self, other):
        return self.cidade == other.cidade  # são iguais se nome for igual, não usa o id

    def __hash__(self):
        return hash(self.cidade)

#Classe nodo para armazenamento de cidades, vamos lá ver se resulta