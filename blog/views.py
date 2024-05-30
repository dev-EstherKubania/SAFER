from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_home(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.title, post.content)
    return render(request, 'blog/home.html', {'posts': posts})
    

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def homepage(request):
    # Fetch all posts from the database ordered by date_posted
    posts = Post.objects.all().order_by('-date_posted')

    # Debugging: Print the posts to the console to check if they are fetched
    print("Posts fetched:", posts)

    # Pass the fetched posts to the template as context
    return render(request, 'safer/homepage.html', {'posts': posts})