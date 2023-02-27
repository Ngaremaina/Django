from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def all_posts(request):
    return render(request, "blog/all-posts.html")


def single_post(request):
    return render(request, "blog/single-post.html")
