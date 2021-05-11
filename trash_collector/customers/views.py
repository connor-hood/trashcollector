from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    try:
        logged_in_customer = Customer.get(user=user)
        # create context dictionary
    except:
        return HttpResponseRedirect(reverse('customers:detail'))
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')


def detail(request):
    if request.method == 'GET':
        name = request.GET.get('customer_name')
        detail_info = Customer(name=name)
        detail_info.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/cust_detail.html')


def edit(request):
    if request.method == 'POST':
        name = request.POST.get('customer_name')
        user = request.user
        zip_code = request.POST.get('zip_code')
        collect_day = request.POST.get('collect_day')
        special_day = request.POST.get('special_day')
        new_info = Customer(user=user, name=name, zip_code=zip_code, collect_day=collect_day, special_day=special_day)
        new_info.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/edit.html')
