'''
Web Scrapper
'''
import requests
from bs4 import BeautifulSoup

def scrap(URL:str):
    '''
    Scrap the URL
    '''
    page = requests.get(URL)
    return page

def get_exchange_rate(dom):
    exchange_rates={}
    for row in dom.find_all('p'):
        print(f"{row}")
        title=row.text.strip()
        if title[0] == 'C':
            title='Compra'
        elif title[0] == 'V':
            title='Venta'
        
        value=row.find('span')
        value=value.text.strip()
        exchange_rates[title]=value

    return exchange_rates


def main():
    url='https://bit.ly/dolarInfo'
    pagina=scrap(url)
    soup=BeautifulSoup(pagina.content, 'html.parser')
    results=soup.find(class_="exchangeRate")
    ex=get_exchange_rate(results)
    print(ex)


if __name__ == '__main__':
    main()