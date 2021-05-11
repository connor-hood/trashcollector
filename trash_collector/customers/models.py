import datetime

from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zip_code = models.IntegerField()
    collect_day = models.CharField(max_length=10)
    special_day = models.DateField(datetime.datetime)
    balance = models.IntegerField(default=0)
    is_suspended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

