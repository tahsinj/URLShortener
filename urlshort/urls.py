from django.urls import path
from .views import home, generate, redirect

urlpatterns = [
    path('', home, name='home'),
    path('generate/', generate, name='generate'),
    path('<str:url>', redirect, name='redirect')
]