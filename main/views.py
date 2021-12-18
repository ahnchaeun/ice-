from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user

        board = Board(
            title=title,
            content=content,
            user=user,
        )
        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'board.html', context)


def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.user = request.user

        board.save()
        return redirect('board')

    else:
        boardForm = BoardForm
        return render(request, 'update.html', {'boardForm':boardForm})        

def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')

def post(request):
    if request.method == 'POST':
        post = Post()
        post.text = request.POST['text']
        post.save()
        return redirect('post')
    else:
        post = Post.objects.get(id=1)
        return render(request, 'post_list.html', {'post':post})

def home(request):
    return render(request, 'home.html')   

def search(request):
    movie_list = movie.objects.order_by()
    context = {'movie_list':movie_list}
    return render(request,'search.html',context) 

def yeardown05(request):
    movie_1965 = movie.objects.filter(movie_Year=1965)
    movie_1978 = movie.objects.filter(movie_Year=1978)
    movie_1993 = movie.objects.filter(movie_Year=1993)
    movie_1996 = movie.objects.filter(movie_Year=1996)
    movie_1999 = movie.objects.filter(movie_Year=1999)
    movie_2000 = movie.objects.filter(movie_Year=2000)
    movie_2001 = movie.objects.filter(movie_Year=2001)
    movie_2002 = movie.objects.filter(movie_Year=2002)
    movie_2003 = movie.objects.filter(movie_Year=2003)
    movie_2004 = movie.objects.filter(movie_Year=2004)
    context = { 'movie_1965':movie_1965,
                'movie_1978':movie_1978,
                'movie_1993':movie_1993,
                'movie_1996':movie_1996,
                'movie_1999':movie_1999,
                'movie_2000':movie_2000,
                'movie_2001':movie_2001,
                'movie_2002':movie_2002,
                'movie_2003':movie_2003,
                'movie_2004':movie_2004,          
      }
    return render(request, 'down05.html',context)


        

def year05to10(request):
    movie_2005 = movie.objects.filter(movie_Year=2005)
    movie_2006 = movie.objects.filter(movie_Year=2006)
    movie_2007 = movie.objects.filter(movie_Year=2007)
    movie_2008 = movie.objects.filter(movie_Year=2008)
    movie_2009 = movie.objects.filter(movie_Year=2009)
    movie_2010 = movie.objects.filter(movie_Year=2010)
    context = {'movie_2005':movie_2005,
                'movie_2006':movie_2006,
                'movie_2007':movie_2007,
                'movie_2008':movie_2008,
                'movie_2009':movie_2009,
                'movie_2010':movie_2010,
      }
    return render(request, '0510.html',context)

def yearup10(request):
    movie_2011 = movie.objects.filter(movie_Year=2011)
    movie_2012 = movie.objects.filter(movie_Year=2012)
    movie_2013 = movie.objects.filter(movie_Year=2013)
    movie_2014 = movie.objects.filter(movie_Year=2014)
    movie_2015 = movie.objects.filter(movie_Year=2015)
    movie_2016 = movie.objects.filter(movie_Year=2016)
    movie_2017 = movie.objects.filter(movie_Year=2017)
    movie_2018 = movie.objects.filter(movie_Year=2018)
    movie_2019 = movie.objects.filter(movie_Year=2019)
    movie_2020 = movie.objects.filter(movie_Year=2020)
    movie_2021 = movie.objects.filter(movie_Year=2021)
    context = {'movie_2011':movie_2011,
                'movie_2012':movie_2012,
                'movie_2013':movie_2013,
                'movie_2014':movie_2014,
                'movie_2015':movie_2015,
                'movie_2016':movie_2016,
                'movie_2017':movie_2017,
                'movie_2018':movie_2018,
                'movie_2019':movie_2019,
                'movie_2020':movie_2020,
                'movie_2021':movie_2021,
      }
    return render(request, 'up10.html',context)

def genresf(request):
    genre_sf = genre.objects.filter(genre_name='SF')
    context = {'genre_sf':genre_sf}
    return render(request, 'sf.html',context)

def genrehorror(request):
    genre_horror = genre.objects.filter(genre_name='공포')
    context = {'genre_horror':genre_horror}
    return render(request, 'horror.html',context)

def genredrama(request):
    genre_drama = genre.objects.filter(genre_name='드라마')
    context = {'genre_drama':genre_drama}
    return render(request, 'drama.html',context)

def genreromance(request):
    genre_romance = genre.objects.filter(genre_name='로맨스')
    context = {'genre_romance':genre_romance}
    return render(request, 'romance.html',context)

def genremelo(request):
    genre_melo = genre.objects.filter(genre_name='멜로')
    context = {'genre_melo':genre_melo}
    return render(request, 'melo.html',context)

def genremystery(request):
    genre_mystery = genre.objects.filter(genre_name='미스터리')
    context = {'genre_mystery':genre_mystery}
    return render(request, 'mystery.html',context)

def genrecriminal(request):
    genre_criminal = genre.objects.filter(genre_name='범죄')
    context = {'genre_criminal':genre_criminal}
    return render(request, 'criminal.html',context)

def genrethriller(request):
    genre_thriller = genre.objects.filter(genre_name='스릴러')
    context = {'genre_thriller':genre_thriller}
    return render(request, 'thriller.html',context)

def genreani(request):
    genre_ani = genre.objects.filter(genre_name='애니메이션')
    context = {'genre_ani':genre_ani}
    return render(request, 'ani.html',context)

def genreaction(request):
    genre_action = genre.objects.filter(genre_name='액션')
    context = {'genre_action':genre_action}
    return render(request, 'action.html',context)

def genrecomedy(request):
    genre_comedy = genre.objects.filter(genre_name='코미디')
    context = {'genre_comedy':genre_comedy}
    return render(request, 'comedy.html',context)

def genrefantasy(request):
    genre_fantasy = genre.objects.filter(genre_name='판타지')
    context = {'genre_fantasy':genre_fantasy}
    return render(request, 'fantasy.html',context)

def gradeall(request):
    grade_all = grade.objects.filter(grade_age='전체관람가')
    context = {'grade_all':grade_all}
    return render(request, 'all.html',context)

def grade12(request):
    grade_12 = grade.objects.filter(grade_age='12세 관람가')
    context = {'grade_12':grade_12}
    return render(request, '12.html',context)    

def grade15(request):
    grade_15 = grade.objects.filter(grade_age='15세 관람가')
    context = {'grade_15':grade_15}
    return render(request, '15.html',context)    

def gradeadult(request):
    grade_adult = grade.objects.filter(grade_age='청소년 관람불가')
    context = {'grade_adult':grade_adult}
    return render(request, 'adult.html',context)    



   

    

               