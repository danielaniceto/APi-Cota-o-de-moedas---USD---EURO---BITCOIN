import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes ["USDBRL"]['bid']
cotacao_euro = cotacoes ["EURBRL"]['bid']
cotacao_btc = cotacoes ["BTCBRL"]['bid']
print ('DOLAR = R$' + cotacao_dolar)
print('EURO = R$' + cotacao_euro)
print ('BITCOIN = R$' + cotacao_btc)
