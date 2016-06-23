from django.shortcuts import render
from django.http import HttpResponse
from hackers.views import index as hackers_mainpage
from orgs.views import index as orgs_mainpage


def index(request):
    context = {}
    return render(request, 'sidehack/index.html', context)


# Create your views here.
def login(request):
    if request.method == "get":
        template = loader.get_template('sidehack/login.html')
        context = {}
        return HttpResponse(context, request)
    elif request.method == "post":
        if authenticated:
            return route_request(request, entity_name)
        else:
            return HttpResponse()


def get_hacker(request, hacker_name):
    return HttpResponse("content for hacker : " + hacker_name)


def get_org(request, org_name):
    return HttpResponse("content for org : " + org_name)


# def route_request(request, entity_name):
#     # This function does the routing
#     if entity_name == 'userfoo':
#         return hackers_mainpage(request)
#     elif entity_name == 'orgbar':
#         return orgs_mainpage(request)
