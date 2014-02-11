#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.

ORDER_STATUS = (
                ('waiting', 'Esperando'),
                ('sent', 'Enviado'),
                ('executed', 'Executada'),
                ('cancelled', 'Cancelada'),
    )
    
class Market(models.Model):
    id = models.BigIntegerField('Identificador', primary_key=True)
    description = models.CharField('Descrição', max_length=100)
    url_api_public = models.CharField('Url API Pública', max_length=100)
    url_api_private = models.CharField('Url API Privada', max_length=100)   
    min_interval_query = models.IntegerField('Intervalo Minimo Consulta')
    
    __unicode__ = lambda self: u'%s' % (self.description)
    class Meta:
        verbose_name = "Mercado"        
    
class MarketConfiguration(models.Model):
    market = models.OneToOneField(Market)
    access_key = models.CharField('Chave de acesso', max_length=100)
    access_sign = models.CharField('Código de acesso', max_length=200)
    belongs_to = models.ForeignKey(User,verbose_name='Usuário', null=False)
    
    __unicode__ = lambda self: u'%s' % (self.market.description)
    
    class Meta:
        verbose_name = "Configurações mercado"
    
class Trade(models.Model):
    tid = models.BigIntegerField('identificador' )
    date = models.DateTimeField('data')
    price = models.DecimalField('preco', max_digits=28, decimal_places=8)
    amount  = models.DecimalField('quantidade',max_digits=28, decimal_places=8)
    type = models.CharField('Tipo', max_length=5)
    coin = models.CharField('Moeda', max_length=10)
    market = models.ForeignKey(Market, null=False, blank=False)
        
class Order(models.Model):
    tid = models.AutoField('Identificador', primary_key=True)
    price = models.DecimalField('preco',max_digits=28, decimal_places=8)
    amount  = models.DecimalField('quantidade',max_digits=28, decimal_places=8)
    type = models.CharField('Tipo', max_length=5)    
    sincronized = models.BooleanField('Sincronizada')
    status = models.CharField('Situação', max_length=10, choices=ORDER_STATUS, default='waiting')
    market = models.ForeignKey(Market, null=False, blank=False) 
    belongs_to = models.ForeignKey(User, verbose_name='Usuário', null=False)
    
    __unicode__ = lambda self: u'%s - Preço: %s Quantidade: %s' % (self.type, self.price, self.amount)
    
    class Meta:
        verbose_name = "Ordem de compra"
        verbose_name_plural = "Ordens de compra"

class BuySellOrder(models.Model):
    id = models.BigIntegerField('Identificador', primary_key=True)
    price = models.DecimalField('preco', max_digits=28, decimal_places=8)
    amount  = models.DecimalField('quantidade',max_digits=28, decimal_places=8)
    type = models.CharField('Tipo', max_length=5)
    coin = models.CharField('Moeda', max_length=10)
    market = models.ForeignKey(Market, null=False, blank=False) 

class Settings(models.Model):
    key = models.CharField(_('Chave'), max_length=50, null=False, blank=False, unique=True)
    value = models.CharField(_('Valor'), max_length=50)
    description = models.TextField(_(u'Descrição'), null=True, blank=True)

    __unicode__ = lambda self: u'%s = %s' % (self.key, self.value)
