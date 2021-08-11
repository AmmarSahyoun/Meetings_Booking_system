from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This data was sent from the view to template",
                   "num_meetings": Meeting.objects.count()})

def date(request):
    return HttpResponse('This page was sweved at '+ str(datetime.now()))

def about(request):
    return HttpResponse("This page is created By Ammar on July2021, it aims to "
                        "create and manage meeting dates ")