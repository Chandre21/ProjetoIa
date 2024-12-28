from Definicoes import *

def movimentar_veiculo(entrega: Entrega, destino: Cidade):
        veiculo = entrega.veiculo
        cidade_atual = entrega.node_atual

        # Verificar se o destino está conectado à cidade atual
        conexao_destino = None
        for conexao in cidade_atual.conexoes:
            if conexao.node_final == destino:
                conexao_destino = conexao
                break

        # Se não houver conexão direta
        if not conexao_destino:
            return f"Erro: {destino.nome} não está diretamente conectado a {cidade_atual.nome}. Use um sistema de procura para encontrar a rota."

        # Verificar se o veículo pode acessar a conexão
        if veiculo.tipo not in conexao_destino.acessibilidade:
            return f"Erro: O veículo {veiculo.tipo} não pode acessar a conexão para {destino.nome}."

        # Verificar autonomia e combustível
        if veiculo.combustivel < conexao_destino.custo_do_salto:
            return f"Erro: Combustível insuficiente para alcançar {destino.nome}."
        if veiculo.autonomia < conexao_destino.custo_do_salto:
            return f"Erro: O veículo {veiculo.tipo} não tem autonomia suficiente para alcançar {destino.nome}."

        # Realizar movimentação
        veiculo.combustivel -= conexao_destino.custo_do_salto
        veiculo.autonomia -= conexao_destino.custo_do_salto
        entrega.custo_acumulado += conexao_destino.custo_do_salto
        entrega.node_atual = destino

        return f"Sucesso: O veículo {veiculo.tipo} moveu-se para {destino.nome}. Combustível restante: {veiculo.combustivel}."