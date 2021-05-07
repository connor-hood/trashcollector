import datetime

from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zipcode = models.IntegerField(max_length=5)
    collect_day = models.DateField
    special_day = models.DateField(datetime.datetime)
    balance = models.IntegerField(max_length=3)
