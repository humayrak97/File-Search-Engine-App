from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request, 'search_engine/login.html', {'title': 'Login'})

def signup(request):
    return render(request, 'search_engine/signup.html', {'title': 'Signup'})

def accountRecovery(request):
    return render(request, 'search_engine/recoveryPass.html', {'title': 'accountRecovery'})