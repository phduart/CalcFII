def getDividens(divPago, qtdAtual):
    return divPago * qtdAtual

def createAtivo(nome, dividendo):
    ativo = {
      'nome': nome,
      'valor': dividendo
    }
    return ativo