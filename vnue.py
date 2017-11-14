import requests
from bs4 import BeautifulSoup

#contador de paginas
page = 1
#contador de eventos na pagina
tempag = 1
query = input("Qual a data que deseja verificar, formato: \"SET-DIA-ANO\"")

#Enquanto tiver eventos na página ele ira exibir dados
while tempag != 0:
    site = requests.get("http://soumineiro.com.br/eventos/"+str(page))
    conteudo = BeautifulSoup(site.content, 'html.parser')

    # conta quantas vezes o evento aparece no site
    tempag = str(conteudo).count("col-xm-6 col-sm-4 col-md-3")
    pag = str(conteudo).count("col-xm-6 col-sm-4 col-md-3")

    # caso nao tenha mais eventos para o laço
    if pag == 0:
        break
    else:
        page = page+1

    for pag in range(0, pag):
        # antes de exibir, remove caracteres indesejados
        nomeDoEvento = conteudo.find_all(class_ = "item-title")[pag].get_text()
        nomeDoEvento = nomeDoEvento.replace("\n", " ")

        dataDoEvento = conteudo.find_all(class_ = "date-event")[pag].get_text()
        dataDoEvento = dataDoEvento.lstrip()
        dataDoEvento = dataDoEvento.rstrip()
        dataDoEvento = dataDoEvento.replace("\n", "-")
        if dataDoEvento == query:
            print("Evento:", nomeDoEvento)
            print("Data:", dataDoEvento, "\n")

        pag = pag-1
