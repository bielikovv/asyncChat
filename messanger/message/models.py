from django.db import models
from django.contrib.auth.models import User
from datetime import datetime




class Profile(models.Model):
    user_login = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='login')
    username = models.CharField(max_length=100, verbose_name='Name')
    usersurname = models.CharField(max_length=100, verbose_name='Surname')
    password = models.CharField(max_length=32, verbose_name='Password')
    date_of_birth = models.DateField(verbose_name='Date of birth', blank=True)
    photo = models.ImageField(verbose_name='Photo', blank=True, upload_to='photo/%Y/%m/%d')

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255)
    room = models.CharField(max_length=255)

    class Meta:
        ordering = ['date', ]



