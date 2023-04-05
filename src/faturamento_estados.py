import json
import pandas as pd

class FaturamentoEstados:
    """
    Classe responsável por carregar e manipular dados de faturamento de estados em um arquivo JSON.
    """
    
    def __init__(self, file_path):
        """
        Construtor da classe.

        Parâmetros:
        ----------
        file_path : str
            Caminho do arquivo JSON com os dados de faturamento dos estados.
        """
        self.file_path = file_path
        self.dados_estados = {}
        self.total = 0
        
    def carrega_dados(self):
        """
        Carrega os dados de faturamento dos estados a partir do arquivo JSON e armazena no atributo dados_estados.
        """
        with open(self.file_path) as f:
            dados = json.load(f)
            for estado, valor in dados.items():
                self.dados_estados[estado] = valor
                self.total += valor
    
    def calculo_perc(self, estado):
        """
        Calcula e retorna o percentual que um estado possui do valor total de vendas da empresa.

        Parâmetros:
        ----------
        estado : str
            Sigla do estado que se deseja calcular o percentual de faturamento.

        Retorna:
        -------
        float
            Percentual de faturamento do estado em relação ao total de faturamento da empresa.
        """
        return round(self.dados_estados[estado] / self.total * 100, 2)
    
    def get_faturamento_sp(self):
        """
        Retorna o valor de faturamento do estado de São Paulo.

        Retorna:
        -------
        float
            Valor de faturamento do estado de São Paulo.
        """
        return self.dados_estados['SP']
    
    def get_faturamento_rj(self):
        """
        Retorna o valor de faturamento do estado do Rio de Janeiro.

        Retorna:
        -------
        float
            Valor de faturamento do estado do Rio de Janeiro.
        """
        return self.dados_estados['RJ']
    
    def get_faturamento_mg(self):
        """
        Retorna o valor de faturamento do estado de Minas Gerais.

        Retorna:
        -------
        float
            Valor de faturamento do estado de Minas Gerais.
        """
        return self.dados_estados['MG']
    
    def get_faturamento_es(self):
        """
        Retorna o valor de faturamento do estado de Espírito Santo.

        Retorna:
        -------
        float
            Valor de faturamento do estado de Espírito Santo.
        """
        return self.dados_estados['ES']
    
    def get_faturamento_outros(self):
        """
        Retorna o valor da soma de faturamento de outros estados.

        Retorna:
        -------
        float
            Valor da soma de faturamento de outros estados.
        """
        return self.dados_estados['Outros']
   
    def get_dict_percentuais(self):
        dict_percentuais = {}
        for estado in self.dados_estados:
            dict_percentuais[estado] = str(self.calculo_perc(estado)) + '%'
        return dict_percentuais
    
class FaturamentoEstadosDataFrame:
    """
    Classe para geração de um dataframe contendo o percentual de faturamento por estado.
    """

    def __init__(self, faturamento_estados):
        """
        Parâmetros
        ----------
        faturamento_estados : FaturamentoEstados
            Objeto da classe FaturamentoEstados com os dados de faturamento por estado.

        """
        self.faturamento_estados = faturamento_estados

    def gera_dataframe(self):
        """
        Gera o dataframe contendo o percentual de faturamento por estado.

        Returns
        -------
        pandas.DataFrame
            Dataframe contendo o percentual de faturamento por estado.

        """
        dict_percentuais = self.faturamento_estados.get_dict_percentuais()
        df = pd.DataFrame.from_dict({'Estados': list(dict_percentuais.keys()),
                                     'Faturamento por estado': list(dict_percentuais.values())})
        df = df.reset_index(drop=True)
        df.index += 1
        return df