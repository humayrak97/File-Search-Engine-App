from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='search_engine-login'),
]