from django.urls import path
from . import views
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.search, name='search_engine-search'),
    path('signup/', views.signup, name='search_engine-signup'),
    path('accountRecovery/', views.accountRecovery, name='search_engine-accountRecovery'),
    path('dashboard/', views.dashboard, name='search_engine-dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name = 'search_engine/login.html'), name='search_engine-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'search_engine/logout.html'), name='search_engine-logout'),
    path('searchClusters/', views.searchClusters, name='search_engine-searchClusters'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
