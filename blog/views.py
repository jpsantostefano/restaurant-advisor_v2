from django.shortcuts import render
from .models import Post, Comment, Profile


# Create your views here.

# Home view
def index(request):
    # Shows all the posts
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})