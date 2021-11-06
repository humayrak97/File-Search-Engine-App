from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='search_engine-login'),
    path('signup/', views.signup, name='search_engine-signup'),
    path('accountRecovery/', views.accountRecovery, name='search_engine-accountRecovery'),
]