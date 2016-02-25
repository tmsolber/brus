from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Brus , Person

def index(request):
    persons = Brus.objects.all()
    context = {'persons': persons }
    return render(request, 'brus/index.html', context)

def detail(request, name_id):
    navn = Person.objects.get(id=name_id).name
    return HttpResponse("Navn %s: %s" % (name_id, navn))

def penger(request, name_id):
    money = Brus.objects.get(id=name_id).money
    return HttpResponse("This is how much money you've got: %s" % money)
