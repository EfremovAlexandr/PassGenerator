from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'passgen/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    lenght = 10

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'passgen/password.html', {'password': thepassword})
