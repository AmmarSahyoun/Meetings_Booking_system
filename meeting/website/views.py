from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("Welcome to the Planner!")

def date(request):
    return HttpResponse('This page was sweved at '+ str(datetime.now()))

def about(request):
    return HttpResponse("This page is created By Ammar on July2021, it aims to "
                        "create and manage meeting dates ")