from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'passgen/home.html')

def information(request):
    return render(request, 'passgen/information.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    lenght = int(request.GET.get('lenght', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('#$%^&'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'passgen/password.html', {'password': thepassword})
