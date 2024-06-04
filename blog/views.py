from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_home(request):
    posts = Post.objects.all()
    return render(request, 'blog/bloglist.html', {'posts': posts})
    

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})