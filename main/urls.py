from django.urls import path
from .views import *

urlpatterns = [
    path('board', board, name='board'),
    path('', home, name='home'),
    path('edit/<int:pk>', boardEdit, name='edit'),
    path('delete/<int:pk>', boardDelete, name='delete'),
    path('search/', search, name='search'),
    path('0510/', year05to10, name='0510'),
    path('up10/', yearup10, name='up10'),
    path('down05/',yeardown05, name='down05'),
    

]
