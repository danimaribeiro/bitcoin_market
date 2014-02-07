from django.db import models

# Create your models here.

class Trade(models.Model):
    tid = models.BigIntegerField('identificador', primary_key=True)
    date = models.DateTimeField('data')
    price = models.DecimalField('preco', max_digits=28, decimal_places=8)
    amount  = models.DecimalField('quantidade',max_digits=28, decimal_places=8)
    type = models.CharField('Tipo', max_length=5)
    coin = models.CharField('Moeda', max_length=3)
        
        
class Order(models.Model):
    tid = models.BigIntegerField('Identificador')
    price = models.DecimalField('preco',max_digits=28, decimal_places=8)
    amount  = models.DecimalField('quantidade',max_digits=28, decimal_places=8)
    type = models.CharField('Tipo', max_length=5)
    sincronized = models.BooleanField('Sincronizada')
    
