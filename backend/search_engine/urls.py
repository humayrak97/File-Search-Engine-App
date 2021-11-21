from django.urls import path
from . import views
from .views import RegisterAPI

urlpatterns = [
    path('', views.search, name='search_engine-search'),
    #path('signup/', views.signup, name='search_engine-signup'),
    path('accountRecovery/', views.accountRecovery, name='search_engine-accountRecovery'),
    path('dashboard/', views.dashboard, name='search_engine-dashboard'),
    path('login/', views.log_in, name='search_engine-login'),
    path('searchClusters/', views.searchClusters, name='search_engine-searchClusters'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
]
