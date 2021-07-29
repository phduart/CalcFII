import time
import datetime
import csv
from selenium import webdriver
path="C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\geckodriver.exe"
wd = webdriver.Firefox(executable_path=path)
wd.get("https://fundamentus.com.br/fii_resultado.php")
time.sleep(6)
table = wd.find_element_by_id("tabelaResultado")
tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")
listaDeAtivos = []
field_names = ['nome', 'setor', 'dividendoPago']
for x in rows:
    item = x.find_elements_by_tag_name("td")
    ativo = {
        'nome': item[0].text,
        'setor': item[1].text,
        'dividendoPago': item[5].text
    }
    listaDeAtivos.append(ativo)
    print(ativo.values())
wd.close()
x = datetime.datetime.now()
nomeCSV = 'CapturaDadosFii-' + x.strftime("%Y-%m-%d") + '.csv'
with open(nomeCSV, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(listaDeAtivos)