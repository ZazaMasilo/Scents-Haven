from django.shortcuts import render 
from django.http import HttpResponse


# Create your views here.

posts = [
  {
    'author': 'Zandile Masilo',
    'title': 'Blog Post 1',
    'content': 'This is my first blog post',
    'date_posted': '28th November, 2021'
  },
  {
    'author': 'Bonnie Masilo',
    'title': 'Blog Post 2',
    'content': 'This is my second blog post',
    'date_posted': '29th November, 2021'

  },
]

def my_blog(request):
  return HttpResponse("Hello, Blog!")

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)



