from django.db import models
#from django.db import User




class Brus(models.Model):
    soda = models.CharField(max_length=20)
    cost = models.IntegerField(default=15)

    def __str__(self):
        return '%s %s' % (self.soda, self.cost)


class Person(models.Model):
    name = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
    #user = models.ForeignKey(User, related_name="person")

    def setName(self, name):
        self.name = name
        self.save(force_update=name)

    def deposit_money(self, amount):
        self.balance += amount
        self.save()

    def withdraw_money(self, amount):
        self.balance -= amount
        self.save()

    def __str__(self):
        return '%s %s' % (self.name, self.balance)

"""class User(PersistentModel):


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...
"""