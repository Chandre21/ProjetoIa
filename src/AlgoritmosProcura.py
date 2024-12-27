from Definicoes import *
import heapq

def Minimax ():
    pass


class UniformCostSearch:
    def __init__(self, mapa: Mapa):
        self.mapa = mapa

    def buscar(self, cidade_inicial: Cidade, cidade_destino: Cidade, veiculo: Veiculo):
        # Fila de prioridade para gerenciar os nós a serem explorados
        fronteira = []
        # Estado inicial
        estado_inicial = (0, cidade_inicial, veiculo, 0)  # (custo_acumulado, cidade_atual, veiculo, carga_entregue)
        heapq.heappush(fronteira, estado_inicial)
        # Conjunto de cidades visitadas
        visitados = set()

        while fronteira:
            custo_atual, cidade_atual, veiculo_atual, carga_entregue = heapq.heappop(fronteira)

            # Checar se já atingimos a cidade destino com as necessidades atendidas
            if cidade_atual == cidade_destino and cidade_destino.mantimentos_atuais >= cidade_destino.necessidade:
                print(f"Objetivo alcançado com custo {custo_atual}")
                return custo_atual

            # Se o nó já foi visitado, ignorá-lo
            if (cidade_atual, veiculo_atual.carga_atual, veiculo_atual.combustivel) in visitados:
                continue

            # Marcar como visitado
            visitados.add((cidade_atual, veiculo_atual.carga_atual, veiculo_atual.combustivel))

            # Explorar conexões
            for conexao in cidade_atual.conexoes:
                proxima_cidade = conexao.node_final
                custo_salto = conexao.custo_do_salto

                # Verificar se o veículo pode acessar a próxima cidade
                if veiculo_atual.tipo not in conexao.acessibilidade:
                    continue    #passa à próxima interação

                # Verificar se o veículo tem combustível suficiente
                if veiculo_atual.combustivel < custo_salto:
                    continue

                # Atualizar os mantimentos entregues
                mantimentos_a_entregar = min(
                    veiculo_atual.carga_atual,
                    proxima_cidade.necessidade - proxima_cidade.mantimentos_atuais
                )
                proxima_cidade.mantimentos_atuais += mantimentos_a_entregar
                veiculo_atual.carga_atual -= mantimentos_a_entregar

                # Atualizar combustível
                veiculo_atual.combustivel -= custo_salto

                # Adicionar o próximo estado na fila de prioridade
                novo_estado = (
                    custo_atual + custo_salto,
                    proxima_cidade,
                    veiculo_atual,
                    carga_entregue + mantimentos_a_entregar
                )
                heapq.heappush(fronteira, novo_estado)

        print("Não foi possível alcançar o objetivo.")
        return float('inf')
