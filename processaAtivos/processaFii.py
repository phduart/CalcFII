import pandas as pd
from controller import controllerFii as controller

carteiraAtivos = {"ABCP11": 6, "BTLG11": 5, "IRDM11": 16, "RCRB11": 5, "TRXF11": 6, "XPLG11": 3, "XPML11": 2}
resultCarteira = []

ativos = pd.read_csv("C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\captura\\capturaDados.csv",
                     sep=',', decimal=",", encoding='latin')

print("--------------------- RESUME ---------------------")
print(ativos.head())
print("--------------------------------------------------")

for index, row in ativos.iterrows():
    if row['nome'] in carteiraAtivos:
        resultCarteira.append(controller.createAtivo(row['nome'], controller.getDividens(0.97, carteiraAtivos[row['nome']])))

print("--------------------- ANALISE --------------------")
resultCarteira = pd.DataFrame.from_dict(resultCarteira)
somaCarteira = resultCarteira['valor'].sum()
print("Soma dos Valores Carteira: R$" + str(somaCarteira))
print("--------------------------------------------------")