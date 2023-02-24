from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_posts(request):
    return render(request, 'all-post.html')

def single_post(request, slug):
    return render(request, "single-post.html")