# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.utils import timezone

# Create your views here.
context = {'moment': timezone.now()}

def index(request):
	return render(request, 'main/index.html', context)

def contacts(request):
	return render(request, 'main/contacts.html', context)