from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges_dict = {
"january" : "This is january !!! \n Eat no meat for the entire month! ",
"february": "This is february !!! \n Walk for atleast 20 min every day! " ,
"march": " This is march !!! \n Learn any language for atleast 20min a day! ",
"april": " This is april !!! \n Eat no meat for the entire month! ",
"may": " This is may !!! \n Walk for atleast 20 min every day! ",
"june": " This is june !!! \n Learn any language for atleast 20min a day!",
"july": " This is july !!! \n Eat no meat for the entire month! ",
"august": " This is august !!! \n Walk for atleast 20 min every day! ",
"september": " This is september !!! \n Learn any language for atleast 20min a day!",
"october": " This is october !!! \n Eat no meat for the entire month! ",
"november": " This is november !!! \n Walk for atleast 20 min every day! ",
"december": " This is december !!! \n Learn any language for atleast 20min a day!"
}

def list_of_all_months(request):
    list_items = ""
    months = list(monthly_challenges_dict.keys())
    for each in months:
        month_path = reverse("month-challenge", args=[each])
        capitalize_month = each.capitalize()
        list_items += f"<li><a href =\"{month_path}\">{capitalize_month}</a></li>"

    response_data = f"<ul> {list_items} </ul>"
    return HttpResponse(response_data)

def monthly_challenges_by_number(request,month):
    forward_month = list(monthly_challenges_dict.keys())
    if month > len(monthly_challenges_dict):
        return(HttpResponseNotFound("Invalid Month!"))
    forward_month = forward_month[month-1]
    redirect_path = reverse("month-challenge", args=[forward_month])
    return(HttpResponseRedirect(redirect_path)) 

def monthly_challenges(request,month):
    try:
        return_str = monthly_challenges_dict[str(month)]
        response_data = f"<h1>{return_str}</h1>"
        return(HttpResponse(response_data))
    except:
        return(HttpResponseNotFound("<h1>This month is not supported!</h1>"))

