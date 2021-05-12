from django.urls import path, include

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('update_info', views.update_info, name="update_info"),
    path('details', views.details, name="details"),
    path('today_customers', views.today_customers, name="today_customers")
]