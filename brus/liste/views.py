from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Brus , Person
from .forms import DepositForm, AddNameForm



def index(request):
    persons = Person.objects.all().order_by('-name')
    context = {
        'persons': persons,
        'form1': DepositForm(),
        'formAdd': AddNameForm()
    }
    return render(request, 'brus/index.html', context)

def detail(request, name_id):
    navn = Person.objects.get(id=name_id).name
    return HttpResponse("Navn %s: %s" % (name_id, navn))

def penger(request, name_id):
    money = Brus.objects.get(id=name_id).money
    return HttpResponse("This is how much money you've got: %s" % money)

def pay(request, name_id):
    person = Person.objects.get(id=name_id)
    person.withdraw_money(15)
    return HttpResponseRedirect("/")

def deposit(request, name_id):
    person = Person.objects.get(id=name_id)
    person.deposit_money(int(request.POST.get('deposit_amount')))
    return HttpResponseRedirect("/")

def addPerson(request):
    Person.objects.create(name=request.POST.get('add_person'))
    return HttpResponseRedirect("/")

def deletePerson(request, name_id):
    Person.objects.get(id=name_id).delete()
    return HttpResponseRedirect("/")




