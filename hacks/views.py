from django.shortcuts import render
from django.http import HttpResponse
import hackers
import orgs


def index(request):
    return HttpResponse("This is where hack views are shown")
