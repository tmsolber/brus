from django.db import models


class Brus(models.Model):
    soda = models.CharField(max_length=20)
    cost = models.IntegerField(default=15)

    def __str__(self):
        return '%s %s' % (self.name, self.money)


class Person(models.Model):
    name = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)

    def deposit_money(self, amount):
        self.money += amount
        self.save()

    def withdraw_money(self, amount):
        self.money -= amount
        self.save()

