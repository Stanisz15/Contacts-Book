from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    description = models.TextField(null=True)


class Address(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    house_num = models.CharField(max_length=32)
    apartment_num = models.CharField(max_length=32)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Phone(models.Model):
    number = PhoneNumberField(unique=True)
    type = models.CharField(max_length=32)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):
    mail = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=32)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Groups(models.Model):
    name = models.CharField(max_length=32)
    persons = models.ManyToManyField(Person)
