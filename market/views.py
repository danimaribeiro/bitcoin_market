#coding=utf-8
import pygal, json, calendar, decimal
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from market.models import Trade
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

def home(request):
    return render(request, "market/graficos.html")

def Graficos(request):
    if request.is_ajax():
        base = datetime.utcnow() - timedelta(hours=2)
        inicio = base + timedelta(days=-7)
        negociacoes = Trade.objects.filter(date__gte=inicio, coin='btc-usd').order_by('date')      
        dados = [[ (calendar.timegm(x.date.timetuple()) * 1000), x.price ] for x in negociacoes]
        return HttpResponse(json.dumps(dados, default=decimal_default), content_type="application/json")
    
    return render(request, "market/graficos.html")


# Create your views here.
def index(request, coin="btc"):
    filtro = request.GET.get('filter', '')
          
    line_chart = pygal.Line(width=900, height=500,include_x_axis=False,
                            x_title="Horas", y_title="R$", 
                            legend_at_bottom=True)
    line_chart.title = 'Valor LiteCoin Mercado Bitcoin'

    obj = filter_trade(filtro, coin)
    line_chart.x_labels =obj['labels']
    
    line_chart.add('Compra' , obj['compra'])
    line_chart.add('Venda' , obj['venda'])    
    svg = line_chart.render()

    template = loader.get_template('market/index.html')
    context = RequestContext(request, {
        'svg': svg,
    })
    return HttpResponse(template.render(context))



def filter_trade(filtro, moeda):
    compra = []
    venda = []  
    labels = []
    base = datetime.utcnow() - timedelta(hours=2)
    inicio = base + timedelta(days=-1)
    horas = 25
    if filtro=="doze":
        inicio = base + timedelta(hours=-12)
        horas = 13
    elif filtro=="seis":
        inicio = base + timedelta(hours=-6)
        horas = 7
    elif filtro=="hora":
        inicio = base + timedelta(hours=-1)  
        horas =1  
    elif filtro=="2_dias":
        inicio = base + timedelta(hours=-49)  
        horas =49          
    
    negociacoes = Trade.objects.filter(date__gte=inicio, coin=moeda)
        
    dateList = [ base - timedelta(hours=(x)) for x in range(0, horas)]
    dateList.reverse()
    
    for i in dateList:
        labels.append(str(i.hour))
        comprasObj = filter(lambda x: (x.date.day == i.day and x.date.hour == i.hour 
                                       and x.type=="buy"), negociacoes)
        vendasObj = filter(lambda x: (x.date.day == i.day and x.date.hour == i.hour 
                                       and x.type!="buy"), negociacoes)
        total = len(comprasObj)
        if total>0:
            soma = sum([ x.price for x in comprasObj ])
            media = float(soma) / float(total)
            compra.append(media)
            print i
        else:
            compra.append(None)
            
        total = len(vendasObj)
        if total>0:
            soma = sum([ x.price for x in vendasObj ])
            media = float(soma) / float(total)
            venda.append(media)
            print i
        else:
            venda.append(None)

    return { 'venda': venda, 'compra': compra, 'labels':labels }




