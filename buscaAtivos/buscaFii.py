import time
import shutil
import os
from selenium import webdriver
from controller import controllerBusca as controller

path="C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\geckodriver.exe"
wd = webdriver.Firefox(executable_path=path)
print("--------------------- INICIO ---------------------")
wd.get("https://fundamentus.com.br/fii_resultado.php")
time.sleep(6)
table = wd.find_element_by_id("tabelaResultado")
tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")
print("--------- PROCESSANDO ATIVOS ---------")
listaDeAtivos = controller.processListaAtivo(rows)
print("--------- FECHANDO BROWSER -----------")
wd.close()
print("--------- EXPORTANDO ATIVOS ----------")
nomeCSV = controller.exportCSV(listaDeAtivos)
shutil.move("C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\" + nomeCSV,
            "C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\captura")
os.rename("C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\captura" + nomeCSV,
          "C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\captura\\capturaDados.csv")
print("--------------------- FIM ---------------------")
