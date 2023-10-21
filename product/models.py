from django.db import models

# Create your models here.
# Importation des modules nécessaires
from django.db import models

# Modèle Cadeau
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    recipient = models.CharField(max_length=255)
    delivery_date = models.DateField()
    occasion = models.CharField(max_length=255)
    packaging_condition = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    personal_note = models.TextField()
    delivery_status = models.CharField(max_length=255)
    weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    surprise_level = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

   

    def __str__(self):
        return self.name