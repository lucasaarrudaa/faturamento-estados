from r_e_w_json.escreve_dados import CriaJson
from src.faturamento_estados import FaturamentoEstados, FaturamentoEstadosDataFrame

faturamento = CriaJson(r'.\r_e_w_json\jsons\faturamento.json')
faturamento.escrever_arquivo_json()

faturamento = FaturamentoEstados(r'.\r_e_w_json\jsons\faturamento.json')
faturamento.carrega_dados()

df_faturamento = FaturamentoEstadosDataFrame(faturamento)
df = df_faturamento.gera_dataframe()

print(df)
