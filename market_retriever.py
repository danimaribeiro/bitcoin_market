import urllib2
import json
from datetime import datetime, timedelta
from market.models import Trade
import calendar

if __name__ == '__main__':
    pesquisa =  datetime.utcnow() - timedelta(hours=8)    
    segundos = calendar.timegm(pesquisa.utctimetuple())
    
    request = urllib2.urlopen("https://www.mercadobitcoin.com.br/api/trades_litecoin/" + str(segundos) )
    jsonstr = request.read().decode("utf-8")
    obj = json.loads(jsonstr)
     
    for item in obj:
        t = Trade()
        t.tid = item["tid"]
        t.date = datetime.fromtimestamp(item["date"]) - timedelta(hours=2)
        t.price = item["price"]
        t.amount = item["amount"]
        t.type = item["type"]
        t.coin = "ltc"
        t.save()
        

        
        
    