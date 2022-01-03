# Api-Key = QR0JTD77RB5HWWOF

import requests
import os
from prettytable import PrettyTable
import json
import matplotlib.pyplot as plt
import numpy as np


url = "https://www.alphavantage.co"


banner = """
////////////////////////////////
//                            //
//       Consult Actions      //
//                            //
////////////////////////////////
"""



class Api:
   def __init__(self,url,apikey):
      self.apikey = apikey
      self.url = url
   
   def consult(self,function,from_symbol,to_symbol,**kwargs):
      urlconsult = url+f'/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={self.apikey}'
      if kwargs.items():
         for key, value in kwargs.items():
            urlconsult += f'&{key}={value}'
      response = requests.get(urlconsult)
      response_dict = json.loads(response.text)
      return [response,response_dict]
   
key = str(input('Api-Key:'))
api = Api(url,key)
while True:
   os.system('cls')
   print(banner)
   function = str(input('Qual função deseja:'))
   if function.strip() == ('FX_DAILY' or 'FX_WEEKLY' or 'FX_MONTHLY'):
      from_money = str(input('De moeda:'))
      to_money = str(input('Para moeda:'))
      dias = int(input('Quantos dias quer ver:').strip())
      response = api.consult(function,from_money,to_money)
      dados = response[1]['Time Series FX (Daily)']
      total = 0
      closing = []
      high = []
      low = []
      up = []
      date = []
      opening = []
      for c in dados:
         total += 1
         date.append(c)
         high.append(float(dados[c]['2. high']))
         low.append(float(dados[c]['3. low']))
         up.append(float(dados[c]['1. open'])-float(dados[c]['4. close']))
         opening.append(float(dados[c]['1. open']))
         closing.append(float(dados[c]['4. close']))
         if total == dias:
            break
      print('DADOS > \n')
      x = PrettyTable()
      x.add_column('Datas', date)
      x.add_column('Abertura', opening)
      x.add_column('Alto', high)
      x.add_column('Baixo', low)
      x.add_column('Fechamento',closing)
      x.add_column('Ganho',up)
      x.align['Abertura'] = 'r'
      x.align['Alto'] = 'r'
      x.align['Baixo'] = 'r'
      x.align['Fechamento'] = 'r'
      x.align['Ganho'] = 'r'
      print(x)
      
      teste = input()