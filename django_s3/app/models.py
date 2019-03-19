from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=200)
	picture = models.FileField(null=True, blank=True)

class Product(models.Model):
	customer = models.ForeignKey(Customer, blank=True, null=True, on_delete = models.SET_NULL)
	name = models.CharField(max_length=200)
	price = models.FloatField(null=True, blank=True, default=None)
	picture = models.FileField(null=True)