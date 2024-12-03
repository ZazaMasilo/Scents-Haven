from django.shortcuts import render 
from .models import Post


# Create your views here.

def post_list(request): 
  posts = Post.objects.filter(status=1).order_by('created_on')
  return render(request, 'blog/post_list.html', {'posts': posts})