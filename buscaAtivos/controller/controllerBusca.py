import datetime
import csv

def processListaAtivo(rows):
    listaDeAtivos = []
    for x in rows:
        item = x.find_elements_by_tag_name("td")
        ativo = createAtivoBusca(item[0].text, item[1].text, item[5].text)
        listaDeAtivos.append(ativo)
        print(ativo.values())
    return listaDeAtivos

def createAtivoBusca(nome, setor, dividendoPago):
    ativo = {
        'nome': nome,
        'setor': setor,
        'dividendoPago': dividendoPago
    }
    return ativo

def exportCSV(listaDeAtivos):
    field_names = ['nome', 'setor', 'dividendoPago']
    x = datetime.datetime.now()
    nomeCSV = 'CapturaDadosFii-' + x.strftime("%Y-%m-%d") + '.csv'
    with open('capturaDados.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(listaDeAtivos)
    return nomeCSV

