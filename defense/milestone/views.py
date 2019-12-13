from django.shortcuts import render
from django.contrib.auth import models
from .models import news
# Create your views here.

def home(request):
    latest_news = news.objects.order_by('-id')[:4]
    return render(
        request,
        'index.html',
        {
            'latest_news': latest_news
        }
    )


def profile(request):
    group = models.Group.objects.get(name='teachers')
    list_teachers = group.user_set.all()
    if request.method == 'POST':
        try:
            name = request.POST.get("news_name")
            txt = request.POST.get("news_text")
            print(request.POST)
            news1 = news(news_name=name,news_text=txt)
            news1.save()

        except:
            print('the comments cannot be added')
    return render(
        request,
        'profile.html',
        {
            'list_teachers': list_teachers
        }
    )

def students(request):
    group = models.Group.objects.get(name='students')
    list_students = group.user_set.all()
    return render(
        request,
        'students.html',
        {
            'list_students' : list_students
        }
    )

def teachers(request):
    group = models.Group.objects.get(name='teachers')
    list_teachers = group.user_set.all()
    return render(
        request,
        'teachers.html',
        {
            'list_teachers' : list_teachers
        }
    )

