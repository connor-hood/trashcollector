from django.db import models


# Create your models here.

# TODO: Create an Employee model with properties required by the user stories


class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zipcode = models.IntegerField()
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    days_of_week = [
        MONDAY,
        TUESDAY,
        WEDNESDAY,
        THURSDAY,
        FRIDAY,
    ]
    pickup_day = models.DateField(days_of_week)
