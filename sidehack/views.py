from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'sidehack/index.html', context)


# Create your views here.
def login(request):
    if request.method == "GET":
        context = {}
        return render(request, 'sidehack/login.html', context)
    elif request.method == "POST":
        if authenticated:
            return route_request(request, entity_name)
        else:
            return HttpResponse()


def get_hacker(request, hacker_name):
    return HttpResponse("content for hacker : " + hacker_name)


def get_hacker_hack(request, hacker_name, hack):
    return HttpResponse(hack + " for hacker " + hacker_name)


def get_org(request, org_name):
    return HttpResponse("content for org : " + org_name)


def get_org_hack(request, org_name, hack):
    return HttpResponse(hack + " for org " + org_name)
