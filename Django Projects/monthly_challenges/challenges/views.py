from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here. monthly_challenges["january"]
monthly_challenges = {
    "january": "Eat No Meat For the entire month",
    "february": "Walk for at least 20 minutes everyday",
    "march": "Learn Django for 30 minutes everyday",
    "april": "Eat No Meat For the entire month",
    "may": "Walk for at least 20 minutes everyday",
    "june": "Learn Django for 30 minutes everyday",
    "july": "Eat No Meat For the entire month",
    "august": "Walk for at least 20 minutes everyday",
    "september": "Learn Django for 30 minutes everyday",
    "october": "Eat No Meat For the entire month",
    "november": "Walk for at least 20 minutes everyday",
    "december": "Learn Django for 30 minutes everyday",
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    redirect_month = months[month - 1]
    # "http://127.0.0.1:8000/challenges/redirect_month"
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)


# def january(request):
#     return HttpResponse("Eat No Meat For the entire month")


# def february(request):
#     return HttpResponse("Walk for at least 20 minutes everyday")


# def march(request):
#     return HttpResponse("Learn Django 30 minutes daily")


# def april(request):
#     return HttpResponse("Today is a sunny day. Hoorah!!")

def monthly_challenge(request, month):
    # challenge_text = ""
    # if month == "january":
    #     challenge_text = "Eat No Meat For the entire month"
    # elif month == "february":
    #     challenge_text = "Walk for at least 20 minutes everyday"
    # elif month == "march":
    #     challenge_text = "Learn Django 30 minutes daily"
    # else:
    #     challenge_text = "Invalid Month."
        
    # return HttpResponse(challenge_text)
    # try:
    #     challenge_text = monthly_challenges[month]
    #     return HttpResponse(challenge_text)
    # except:
    #     return HttpResponseNotFound("<h1>Invalid Month</h1>")
    
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {
        "challenge_text": challenge_text,
        "month": month
    })
    
    
    
