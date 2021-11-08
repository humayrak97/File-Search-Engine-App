from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from search_engine.models import People

# Create your views here.

def login(request):
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
                user.passs = pass1
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('search_engine-login')

        else:
            messages.info(request, 'The passwords do not match.')


    return render(request, 'search_engine/signup.html', {'title': 'Signup'})