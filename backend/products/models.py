from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=230)
    product_discription = models.TextField()
    product_price = models.FloatField()

    def __str__(self):
        return self.product_name