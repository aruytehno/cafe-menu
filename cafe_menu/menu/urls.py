from django.urls import path
from .views import home, menu

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
]