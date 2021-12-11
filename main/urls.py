from django.urls import path
from .views import *

urlpatterns = [
    path('board', board, name='board'),
    path('', home, name='home'),
    path('edit/<int:pk>', boardEdit, name='edit'),
    path('delete/<int:pk>', boardDelete, name='delete'),
    path('search/', search, name='search'),
]
