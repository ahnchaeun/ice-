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
    path('sf/',genresf,name='sf'),
    path('horror/',genrehorror,name='horror'),
    path('drama/',genredrama,name='drama'),
    path('romance/',genreromance,name='romance'),
    path('melo/',genremelo,name='melo'),
    path('mystery/',genremystery,name='mystery'),
    path('criminal/',genrecriminal,name='criminal'),
    path('thriller/',genrethriller,name='thriller'),
    path('ani/',genreani,name='ani'),
    path('action/',genreaction,name='action'),
    path('comedy/',genrecomedy,name='comedy'),
    path('fantasy/',genrefantasy,name='fantasy'),
    path('all/',gradeall,name='all'),
    path('12/',grade12,name='12'),
    path('15/',grade15,name='15'),
    path('adult/',gradeadult,name='adult'),
    

]
