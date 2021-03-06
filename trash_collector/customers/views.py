from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user_info_id = request.user.id
    print(request)
    try:
        logged_in_customer = Customer.objects.get(pk=user_info_id)
        context = {
            'logged_in_customer': logged_in_customer
        }
    except:
        return HttpResponseRedirect(reverse('customers:detail'))
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    return render(request, 'customers/index.html', context)


def detail(request):
    print(request.method)
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('customer_name')
        zip_code = request.POST.get('zip_code')
        collect_day = request.POST.get('collect_day')
        special_day = request.POST.get('special_day')
        new_info = Customer(user=user, name=name, zip_code=zip_code, collect_day=collect_day, special_day=special_day)
        new_info.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/display_detail.html')


def display(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user_info_id = request.user.id
    print(request)
    try:
        logged_in_customer = Customer.objects.get(pk=user_info_id)
        context = {
            'logged_in_customer': logged_in_customer
        }
    except:
        return HttpResponseRedirect(reverse('customers:display_detail'))
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    return render(request, 'customers/index.html', context)
