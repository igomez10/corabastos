import requests
import csv
from bs4 import BeautifulSoup
from datetime import timedelta, date
import threading
prices = []

def scrape(aDate):
    url = "http://www.corabastos.com.co/sitio/historicoApp2/reportes/historicos.php"

    querystring = {"c":"202802","d":["ok","ok"],"f":aDate,"l":""}

    headers = {
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        'origin': "http://www.corabastos.com.co",
        'accept': "*/*",
        'referer': "http://www.corabastos.com.co/sitio/historicoApp2/reportes/prueba.php",
        'accept-encoding': "gzip, deflate",
        'accept-language': "es-ES,es;q=0.8,en;q=0.6,fr;q=0.4",
        'cookie': "_gat=1; _ga=GA1.3.520864531.1491490329; _ga=GA1.3.520864531.1491490329",
        'cache-control': "no-cache",
        'postman-token': "ae176d62-086b-c592-f8a5-6ab5339a2f2f"
        }

    try:
        with open('prices.csv','a') as f:
            response = requests.request("GET", url, headers=headers, params=querystring)
            soup = BeautifulSoup(response.text, 'html.parser')
            register = str(soup.find_all('td')[6].text.replace('$',''))
            print(register)
            fieldnames = ['date', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({'date':str(aDate),'price':str(register)})
            register=''
            f.close()
    except IndexError:
        f.close()
        aDate=''
        register=''
        print('no')



# scrape("2015-05-26")
# scrape("2015-05-27")

d = date(2009,8,18)
delta = timedelta(days=1)
while d <= date(2017,4,15):
    scrape( d.strftime("%Y-%m-%d") )
    d += delta
