from django.shortcuts import render
from django.template import loader
from hacks.models import Hack
from hackers.models import Hacker


def index(request):
    context = {
        'hacks': Hack.objects.all()
    }
    return render(request, 'hackers/index.html', context)


def hackers(request):
    context = {
        'hackers_list': Hacker.objects.order_by(id)
    }

    return render(request, 'hackers/hackers_list.html', context)
