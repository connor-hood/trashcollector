from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse

from .models import Employee
from django.utils import timezone


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
    if request.method == 'POST':
        emp_name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_info = Employee(name=emp_name, zip_code=zip_code)
        new_info.save()
        return HttpResponseRedirect(reverse('index.html'))
    else:
        return render(request, 'employees/index.html', context)


def today_customers(request, one_employee):
    Customer = apps.get_model('customers.Customer')
    one_employee = Employee.objects.get(pk=one_employee)
    today = timezone.now().day
    for one_customer in Customer:
        if one_customer.zip_code == one_employee.zip_code or one_customer.is_suspended == False:
            if one_customer.collect_day == today or one_customer.special_day == today:
                return one_customer.name
    context = {
        'one_customer': one_customer
    }
    return render(request, 'employees/index.html', context)