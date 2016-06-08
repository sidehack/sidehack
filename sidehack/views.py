from django.shortcuts import render
from django.http import HttpResponse
from hackers.views import index as hackers_mainpage
from orgs.views import index as orgs_mainpage


def index(request):
    return HttpResponse("This is the front page")


# Create your views here.
def login(request):
    return HttpResponse("Login page")


def route_request(request, entity_name):
    # This function does the routing
    if entity_name == 'userfoo':
        return hackers_mainpage(request)
    elif entity_name == 'orgbar':
        return orgs_mainpage(request)
