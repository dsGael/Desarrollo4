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
        title=row.text.strip()
        if title[0] == 'C':
            title='Compra'
        elif title[0] == 'V':
            title='Venta'
        
        value=row.find('span')
        value=value.text.strip()
        exchange_rates[title]=value

    return exchange_rates

def get_company(dom):
    companies={}
    body=dom.find('tbody')
    
    
    for row in body.find_all('tr') :
       i=0
       leng=len(row.find_all('td'))
       for col in row.find_all('td'):
            if leng<5:
                if i==0:
                    company=col.find(class_="small-hide")
                    company=company.text.strip()
                    companies[company]={}
                if i==3:
                    compra=float(col.text.strip())
                    venta=compra
                    companies[company]={'Compra':compra,'Venta':venta}
            else:

                if i==0:
                    company=col.find(class_="small-hide")
                    company=company.text.strip()
                    companies[company]={}
                if i==3:
                    compra=float(col.text.strip())
                    companies[company]={'Compra':compra}
                if i==4:
                    venta=float(col.text.strip())
                    companies[company]['Venta']=venta
                    
            i+=1
    return companies

def maximo_Compra(compañias:dict):
    mayor=0
    bancoName=''

    for k in compañias:
        compra=compañias[k]['Compra']
        if mayor<compra:
            mayor=compra
            bancoName=k    
    d={bancoName:mayor}           
    return d

def main():
    url='https://bit.ly/dolarInfo'
    pagina=scrap(url)
    soup=BeautifulSoup(pagina.content, 'html.parser')
    #results=soup.find(class_="exchangeRate")
    resultados= soup.find(id="dllsTable")
    #ex=get_exchange_rate(results)
    compañias=get_company(resultados)
   # print(compañias)
    menor=maximo_Compra(compañias)
    print(menor)


if __name__ == '__main__':
    main()