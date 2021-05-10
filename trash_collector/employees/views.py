from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import Employee
from django.utils import timezone
from django.db.models import Q

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    context = {
        'Customer': Customer
    }
    return render(request, 'employees/index.html', context)


def details(request, one_employee):
    one_employee = Employee.objects.get(pk=one_employee)
    context = {
        'one_employee': one_employee
    }
    return render(request, 'employees/index.html', context)


def current_day(request):
    today = timezone.now().day
    context = {
        'today': today
    }
    return render(request, 'employees/index.html', context)

def filter(request):
    Customer = apps.get_model('customers.Customer')
    User = apps.get_model('user.User')
    if Customer.zipcode == User.zipcode and Customer.is_suspended == False:
        Customer.objects.filter(Q(Customer.collect_day == current_day()) | Q(Customer.special_day == current_day()))
    return render(request, 'employees/index.html')