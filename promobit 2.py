import requests
from bs4 import BeautifulSoup

#definindo maximo de paginas
def trade_spider(max_pages):
   #pagina inicial
    page =1
   #laço pra percorrer pagina
    while page <= max_pages:
       #url de busca
        url = 'https://www.promobit.com.br/page/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
       #entra onde precizamos pra encontrar o link das ofertas
        for link in soup.findAll('a',{'class':'access_url'}):
            #une o começo do link com o href que faz gerar o link do produto
            href ="https://www.promobit.com.br/" + link.get('href')
            title = link.string
            #printa o link da oferta
            print(href)
            #printa o titulo
            print(title)

        #inclementando
        page += 1
#uma pagina por vez
trade_spider(1)

