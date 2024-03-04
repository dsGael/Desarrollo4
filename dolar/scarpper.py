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

def main():
    url='https://bit.ly/dolarInfo'
    pagina=scrap(url)
    print(pagina.content)


if __name__ == '__main__':
    main()