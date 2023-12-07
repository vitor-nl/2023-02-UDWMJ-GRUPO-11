from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField('Nome', max_length=50)
    date_fabrication = models.DateField('Data Fabricacao', max_length=50) 
    is_active = models.BooleanField('Ativo', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name