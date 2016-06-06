from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("This is the main page")


def login(request):
    return HttpResponse("Login page")


def hackers(request):
    hacker_list = Hacker.objects.order_by(id)
    template = loader.get_template('hacks/index.html')
    context = {
        'hacker_list': hacker_list
    }

    return HttpResponse(template.render(context, request))
