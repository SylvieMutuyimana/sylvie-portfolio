from django.http import HttpResponse
from django.shortcuts import render


def check(request):
    return HttpResponse('My profile app, Server successfully connected')

# HOME
def home(request):
    context = {}
    return render(request, "mainpages/01home.html", context)

def about(request):
    context = {}
    return render(request, "mainpages/02about.html", context)

def contact(request):
    context = {}
    return render(request, "mainpages/02contact.html", context)

def profile_card(request):
    context = {}
    return render(request, "mainpages/03profilecard.html", context)
