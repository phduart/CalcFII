import pandas as pd

carteiraAtivos = {"ABCP11": 57, "BTLG11": 34, "IRDM11": 16, "RCRB11": 76, "TRXF11": 45, "XPLG11": 88, "XPML11": 23}
resultCarteira = []
def getDividens(divPago, qtdAtual):
  return divPago * qtdAtual

ativos = pd.read_csv("C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\CapturaDadosFii-2021-07-28.csv", sep=',', decimal=",", encoding='latin')
print(ativos.head())

for index, row in ativos.iterrows():
  if row['nome'] in carteiraAtivos:
    dividendo =  getDividens(0.97, carteiraAtivos[row['nome']])
    ativo = {
      'nome' : row['nome'],
      'valor' : dividendo
    }
    resultCarteira.append(ativo)

resultCarteira = pd.DataFrame.from_dict(resultCarteira)
somaCarteira = resultCarteira['valor'].sum()
print("Soma dos Valores Carteira: R$" + str(somaCarteira))

