#coding=utf=8
import json, decimal
from django.http import HttpResponse
from datetime import datetime, timedelta
from market.models import Trade
from django.db.models import Sum, Avg
import calendar
import pandas

# Create your views here.

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):        
        return float(obj)
    if isinstance(obj, datetime):
        return calendar.timegm(obj.timetuple()) * 1000
    return None

def filter_data(start, end, coin, interval, type):
    segundos = int(interval) * (60 if type=='min' else (3600 if type=='H' else 86400 ))
    extraClause = 'to_timestamp((extract (epoch from date)::int / %s) * %s)' % (segundos, segundos)
    
    q = Trade.objects.filter(date__gte=start, date__lte=end, coin=coin)
    q = q.extra(select={'hour': extraClause})
    q = q.values('coin', 'hour')   
    q = q.annotate(total=Sum('amount'))
    q = q.annotate(price=Avg('price'))      
    q = q.order_by('hour')
    print q.query
    return  [ [ x['hour'], x['price']] for x in q]   

def time_series(request):
    coin = request.GET.get('coin', '')
    interval = request.GET.get('interval', '')
    type_interval = request.GET.get('type_interval', '')
     
    #Get dates  
    start = request.GET.get('start', '') 
    end = request.GET.get('end', '')
    start = pandas.to_datetime(start, unit='s') if start != '' else datetime.utcnow() - timedelta(hours=6)
    end = pandas.to_datetime(end, unit='s') if end != '' else datetime.utcnow() - timedelta(hours=0)
    
    dados = pandas.date_range(start=start, end=end, freq='%s%s' % (interval, type_interval))        
    objetos = filter_data(start, end, coin, interval, type_interval)
    
    return HttpResponse(json.dumps(objetos, default=decimal_default ), content_type="application/json")