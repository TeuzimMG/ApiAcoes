# Api-Key = QR0JTD77RB5HWWOF

import prettytable
import requests
import os
from prettytable import PrettyTable
import json
import matplotlib.pyplot as plt
import numpy as np
from requests.api import options


url = "https://www.alphavantage.co"


banner = """
////////////////////////////////
//                            //
//        FOREX CONSULT       //
//                            //
////////////////////////////////

   CREATED BY: MatheusMMS031
"""

options = """
   | 1 | FX_DAILY
   | 2 | FX_WEEKLY
   | 3 | FX_MONTHLY
   | 4 | FX_INTRADAY 
   
   | 5 | DIGITAL_CURRENCY_DAILY
   | 6 | DIGITAL_CURRENCY_WEEKLY
   | 7 | DIGITAL_CURRENCY_MONTHLY
   
   | 0 | EXIT
   

"""

forex = ['FX_DAILY','FX_WEEKLY','FX_MONTHLY','FX_INTRADAY']
crypto = ['DIGITAL_CURRENCY_DAILY','DIGITAL_CURRENCY_WEEKLY','DIGITAL_CURRENCY_MONTHLY']
commands = forex + crypto
class Api:
   def __init__(self,url,apikey):
      self.apikey = apikey
      self.url = url
   
   def consult_forex(self,function,from_symbol,to_symbol,**kwargs):
      urlconsult = url+f'/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={self.apikey}'
      if kwargs.items():
         for key, value in kwargs.items():
            urlconsult += f'&{key}={value}'
      response = requests.get(urlconsult)
      response_dict = json.loads(response.text)
      return [response,response_dict]
   
   def consult_crypto(self,function,symbol,market):
      urlconsult = url+f'/query?function={function}&symbol={symbol}&market={market}&apikey={self.apikey}'
      response = requests.get(urlconsult)
      responseObject = json.loads(response.text)
      return [response, responseObject]
   
api = Api(url,"QR0JTD77RB5HWWOF")

key = str(input('Api-Key:'))
api = Api(url,key)
while True:
   os.system('cls')
   print(banner)
   print(options)
   function = str(input('Qual função deseja:'))
   
   if function.strip() in forex:
      from_money = str(input('De moeda:'))
      to_money = str(input('Para moeda:'))
      dias = int(input('Quantos intervalos quer ver:').strip())
      responseObject = api.consult_forex(function,from_money,to_money)[1]
   
   if function.strip() in crypto:
      symbol = str(input('De simbolo:'))
      market = str(input('Para mercado:'))
      days = int(input('Quantos intervalos quer ver:').strip())
      responseObject = api.consult_crypto(function,symbol,market)[1]
      
   if function.strip() == 'EXIT':
      break
      
   if function.strip() in commands:
      dados = list(responseObject.values())[1]
      total = 0
      x = PrettyTable()
      items = list(list(dados.values())[0].keys())
      items.insert(0,'Data')
      x.field_names = items
      for c in dados:
         total += 1
         items_individual = list(dados[c].values())
         items_individual.insert(0,c)
         x.add_row(items_individual)
         if total == 10:
            break
      print(x)
      
   
   teste = input('Tecle enter para continuar com as consultas')