import json

class CriaJson:
    """
    Classe responsável por criar um arquivo JSON com dados de faturamento.
    """
    def __init__(self, filename):
        """
        Construtor da classe.

        :param filename: nome do arquivo a ser criado.
        """
        self.filename = filename
        self.dados_faturamento = {
            "SP": 67836.43,
            "RJ": 36678.66,
            "MG": 29229.88,
            "ES": 27165.48,
            "Outros": 19849.53
        }

    def escrever_arquivo_json(self):
        """
        Escreve o dicionário de faturamento em um arquivo JSON.
        """
        with open(self.filename, "w") as arquivo:
            json.dump(self.dados_faturamento, arquivo)
