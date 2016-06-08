from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the org profile page. All the hacks of an Org \
                        are shown here")
