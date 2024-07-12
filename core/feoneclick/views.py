from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
import json

def dashboard(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    texts = response.json()
    return render(request, 'main//dashboard.html', {'texts':texts})

def Profile(request):
    return render(request, 'main//profile.html', {})
