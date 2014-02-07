# import urllib2
# import json
# import calendar
# from datetime import datetime, timedelta
# 
# from market.models import Trade
# from background_task import background
# 
# 
# @background(schedule=120)
# def atualizar_trade(user_id):
#     pesquisa =  datetime.utcnow() - timedelta(minutes=10)    
#     segundos = calendar.timegm(pesquisa.utctimetuple())
#     
# 
#     request = urllib2.urlopen("https://www.mercadobitcoin.com.br/api/trades_litecoin/" + str(segundos) )
#     jsonstr = request.read().decode("utf-8")
#     obj = json.loads(jsonstr)
#      
#     for item in obj:
#         t = Trade()
#         t.tid = item["tid"]
#         t.date = datetime.fromtimestamp(item["date"]) - timedelta(hours=2)
#         t.price = item["price"]
#         t.amount = item["amount"]
#         t.type = item["type"]
#         t.coin = "ltc"
#         t.save()    
