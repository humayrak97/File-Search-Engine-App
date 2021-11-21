from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from search_engine.models import People
from django.contrib.auth.models import User, auth
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

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

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

def dashboard(request):
    return render(request, 'search_engine/dashboard.html', {'title': 'dashboard'})

def search(request):
    return render(request, 'search_engine/search.html', {'title': 'search'})

def searchClusters(request):
    return render(request, 'search_engine/searchClusters.html', {'title': 'searchClusters'})