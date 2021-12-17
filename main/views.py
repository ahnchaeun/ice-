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

   

    

               