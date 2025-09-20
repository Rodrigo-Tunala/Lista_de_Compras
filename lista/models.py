from django.db import models

# Create your models here.
class Item(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1)
    comprado = models.BooleanField(default=False)


    marca = models.CharField(max_length=50, blank=True, null=True)
    tamanho = models.CharField(max_length=50, blank=True, null=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)



    def __str__(self):
        return self.nome