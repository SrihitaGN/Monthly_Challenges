from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

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

def monthly_challenges_by_number(request,month):
    forward_month = list(monthly_challenges_dict.keys())
    if month > len(monthly_challenges_dict):
        return(HttpResponseNotFound("Invalid Month!"))
    
    forward_month = forward_month[month-1]
    return(HttpResponseRedirect("/challenges/" + forward_month)) 

def monthly_challenges(request,month):
    try:
        return_str = monthly_challenges_dict[str(month)]
        return(HttpResponse(return_str))
    except:
        return(HttpResponseNotFound("This month is not supported!"))

