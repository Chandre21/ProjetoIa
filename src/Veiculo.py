class Veiculo :
    capacidade_carga : int      # Capacidade total para carga do veiculo
    consumo : int            # Quantos litros gasta por km (autonomia = combusivel / eficiencia) (combustive_de_salto = eficiencia * distancia)
    velocidade : int            # velocidade em km/algo
    tipo : str                  # Camião, Helicóptero, Barco, Combóio

    def __init__(self, tipo: str):
        self.tipo = tipo

        match tipo:
            case "camiao": # valores rudimentares, depois muda-se, e no final, calcular tempo como inverso da vel
                self.capacidade_carga = 500
                self.velocidade = 60
                self.consumo = 0.3

            case "heli":
                self.capacidade_carga = 150
                self.velocidade = 200
                self.consumo = 1

            case "barco":
                self.capacidade_carga = 3000
                self.velocidade = 40
                self.consumo = 3

            case "comboio":
                self.capacidade_carga = 1500
                self.velocidade = 140
                self.consumo = 2

        def calcula_combustivel_consumido (self, distancia) :
            return distancia * self.consumo

        def getVelodicade () :
            return self.velocidade

        def getCapacidade ():
            return self.capacidade_carga
