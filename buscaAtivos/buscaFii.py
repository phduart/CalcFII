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
wd.close()
print("--------- EXPORTANDO ATIVOS ----------")
controller.exportCSV(listaDeAtivos)
try:
    shutil.move("C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\capturaDados.csv",
                "C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\captura")
    print("--------- ARQUIVO CRIADO -------------")
except:
    print("--------- REPLACE ARQUIVO ------------")
    os.replace("C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\capturaDados.csv",
              "C:\\Users\\Paulo Duarte\\Documents\\GitHub\\CalcFII\\buscaAtivos\\captura\\capturaDados.csv")
print("--------------------- FIM ---------------------")
