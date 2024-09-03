from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.list_of_all_months), 
    path("<int:month>",views.monthly_challenges_by_number),
    path("<str:month>",views.monthly_challenges , name = "month-challenge")
    ]
