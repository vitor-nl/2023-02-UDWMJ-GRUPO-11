from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField('Nome', max_length=50)
    date_fabrication = models.CharField('Data Fabricacao', max_length=50) 
    is_active = models.BooleanField('Ativo', default=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name