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
    for k in compañias:
        compra=compañias[k]['Compra']
        if mayor<compra:
            mayor=compra
            bancoName=k    
    d=compañias[bancoName]           
    return d

def minimo_Compra(compañias:dict):
    menor=100
    for k in compañias:
        compra=compañias[k]['Compra']
        if menor>compra:
            menor=compra
            bancoName=k    
    d=compañias[bancoName]           
    return d

def maximo_Venta(compañias:dict):
    mayor=0
    for k in compañias:
        venta=compañias[k]['Venta']
        if mayor<venta:
            mayor=venta
            bancoName=k    
    d=compañias[bancoName]           
    return d

def minimo_Venta(compañias:dict):
    menor=100
    
    for k in compañias:
        venta=compañias[k]['Venta']
        if menor>venta:
            menor=venta
            bancoName=k    
    d=compañias[bancoName]          
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
    mayorC=maximo_Compra(compañias)
    menorC=minimo_Compra(compañias)
    menorV=minimo_Venta(compañias)
    mayorV=maximo_Venta(compañias)
    print(f"Mayor Venta:{mayorV}")
    print(f"Menor Venta:{menorV}")
    print(f"Mayor Compra:{mayorC}")
    print(f"Menor Compra:{menorC}")
    

if __name__ == '__main__':
    main()