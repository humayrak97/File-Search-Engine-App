from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from search_engine.models import People
from django.contrib.auth.models import User, auth
#from django.contrib.auth import authenticate, login

# Create your views here.

def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        #user = authenticate(email = email, pwd = pwd)
        #if user is not None:
        if People.objects.filter(email=email, pwd=pwd).exists():
            #login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('search_engine-signup')
        else:
            messages.info(request, 'Invalid email/ password')
            return redirect('/')
    return render(request, 'search_engine/login.html', {'title': 'Login'})

def accountRecovery(request):
    return render(request, 'search_engine/recoveryPass.html', {'title': 'accountRecovery'})

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if People.objects.filter(email=email).exists():
                messages.success(request, 'An account with that email already exists.')
                return redirect('search_engine-signup')
            else:
                user = People()
                user.email = email
                user.pwd = pass1
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('search_engine-login')

        else:
            messages.info(request, 'The passwords do not match.')


    return render(request, 'search_engine/signup.html', {'title': 'Signup'})

def dashboard(request):
    return render(request, 'search_engine/dashboard.html', {'title': 'dashboard'})

def search(request):
    return render(request, 'search_engine/search.html', {'title': 'search'})

def searchClusters(request):
    return render(request, 'search_engine/searchClusters.html', {'title': 'searchClusters'})