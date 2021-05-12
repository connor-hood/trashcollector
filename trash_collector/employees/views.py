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
    user_info_id = request.user.id
    Customer = apps.get_model('customers.Customer')
    current_employee = Employee.objects.get(pk=user_info_id)
    context = {
        'Customer': Customer,
        'current_employee': current_employee
    }
    return render(request, 'employees/index.html', context)


def details(request):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        zipcode = request.POST.get('zipcode')
        new_info = Employee(emp_name=emp_name, zipcode=zipcode)
        new_info.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/index.html')


def today_customers(request):
    Customer = apps.get_model('customers.Customer')
    user_info_id = request.user.id
    customer_id = Customer.id
    one_employee = Employee.objects.get(pk=user_info_id)
    one_customer = Customer.objects.get(pk=customer_id)
    context = {
        'Customer': Customer,
        'one_customer': one_customer
    }
    today = timezone.now().day

    if one_customer.zip_code == one_employee.zipcode and one_customer.is_suspended == False:
        if one_customer.collect_day == today or one_customer.special_day == today:
            return one_customer.name


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