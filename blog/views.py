from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Profile
from django.contrib import messages


# Create your views here.

# Home view
def index(request):
    # Shows all the posts
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

# Post views
def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post':post})
