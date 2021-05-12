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


def details(request):
    current_user = request.user
    employees_id = current_user.id
    current_employee = Employee.objects.get(user_id=employees_id)
    context = {
        'current_employee': current_employee
    }
    return render(request, 'employees/index.html', context)


def today_customers(request):
    Customer = apps.get_model('customers.Customer')
    one_employee = Employee.objects.get(pk=Employee.pk)
    today = timezone.now().day
    for one_customer in Customer:
        if one_customer.zip_code == one_employee.zipcode or one_customer.is_suspended == False:
            if one_customer.collect_day == today or one_customer.special_day == today:
                return one_customer.name
        context = {
            'one_customer': one_customer
        }
        return render(request, 'employees/index.html', context)


# adding new ones not updating
def update_info(request):
    user_info_id = request.user.id
    if request.method == 'POST':
        current_employee = Employee.objects.get(pk=user_info_id)
        current_employee.emp_name = request.POST.get('emp_name')
        current_employee.zipcode = request.POST.get('zipcode')
        current_employee.save(update_fields=['emp_name', 'zipcode'])
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/index.html')