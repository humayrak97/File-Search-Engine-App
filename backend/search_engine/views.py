from django.shortcuts import render, redirect
from django.contrib import messages
from search_engine.forms import People, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.decorators import login_required

# Create your views here.

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

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

def signup(request):
    if request.method == 'POST':
        form = People(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('search_engine-login')
    else:
        form = People()
    return render(request, 'search_engine/signup.html', {'form': form})

def log_in(request):
    return render(request, 'search_engine/login.html', {'title': 'login'})

@login_required
def dashboard(request):
    return render(request, 'search_engine/dashboard.html', {'title': 'dashboard'})

def search(request):
    return render(request, 'search_engine/search.html', {'title': 'search'})

@login_required
def searchClusters(request):
    return render(request, 'search_engine/searchClusters.html', {'title': 'searchClusters'})

def about(request):
    return render(request, 'search_engine/about.html', {'title': 'about'})

@login_required
def user(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('search_engine-user')
        
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'search_engine/user.html', context)
