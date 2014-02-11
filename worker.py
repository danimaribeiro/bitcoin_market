#coding=utf-8
"""Trade Worker.

Usage:
  worker.py HORA_INICIAL HORA_FINAL
  worker.py (-h | --help)
  worker.py --version

Arguments:
  HORA_INICIAL Valor númerico que representa o inicio
  HORA_FINAL Hora final, sempre maior que hora inicial, 0 para buscar até a data atual

Options:
  -h --help     Show this screen.
  --version     Show version.
  """

from docopt import docopt
import urllib2
import json
from datetime import datetime, timedelta
import calendar
import os
import time
from market.models import Market



def buscarJson(url):
    request = urllib2.urlopen(url)
    jsonstr = request.read().decode("utf-8")
    return json.loads(jsonstr)

def executar(inicio, fim):   
    pesquisa =  datetime.utcnow() - timedelta(hours=inicio)    
    segundos = calendar.timegm(pesquisa.utctimetuple())
    
    pfim =  datetime.utcnow() - timedelta(hours=fim)    
    sfim = calendar.timegm(pfim.utctimetuple())
    
    
    sites = [
         { 'url': "https://www.mercadobitcoin.com.br/api/trades_litecoin/" + str(segundos) + "/" + str(sfim),
          'coin': 'ltc', 'market':'mercado_bitcoin'},
         {'url':"https://www.mercadobitcoin.com.br/api/trades/" + str(segundos) + "/" + str(sfim),
          'coin':'btc', 'market':'mercado_bitcoin'},
        {'url': "https://data.mtgox.com/api/1/BTCUSD/trades?since=" + str(segundos) + '000000', 
         'coin':'btc-usd', 'market':'mtgox' }
        ]
        
    for site in sites:
        obj = buscarJson(site['url'])
        if site['market']=='mtgox':
            obj = obj['return']
        
        for item in obj:
            t = Trade()
            t.tid = item["tid"]
            if site['market']!='mtgox':
                t.date = datetime.fromtimestamp(item["date"]) - timedelta(hours=2)
            else:
                t.date = datetime.fromtimestamp(int(item["tid"]) /  1000000) - timedelta(hours=2)
            t.price = item["price"]
            t.amount = item["amount"]
            t.type = item.get("type", item.get('trade_type',''))
            t.coin = site['coin']
            t.market = Market.objects.first()
            t.save()  
   
def validar_trades():
    from services import sms   
    #sms.send_sms('!')

if __name__ == '__main__':
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coinmarket.settings")
        from market.models import Trade
        
        arguments = docopt(__doc__, version='Worker 1.0')
        
        if arguments['HORA_FINAL'].isdigit() and arguments['HORA_INICIAL'].isdigit():
            if int(arguments['HORA_INICIAL']) > int(arguments['HORA_FINAL']):
                while True:
                    executar(int(arguments['HORA_INICIAL']), int(arguments['HORA_FINAL']))     
                    validar_trades()                 
                    time.sleep(120)                    
            else:
                print "Hora inicial deve ser maior que hora final"        
        else:
            print "Use numbers only"
    except Exception as e:
        print e.args


    