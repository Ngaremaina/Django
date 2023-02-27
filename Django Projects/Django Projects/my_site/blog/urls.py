from django.urls import path

from blog import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("posts/", views.all_posts, name="all-posts"),
    path("posts/my-first-post", views.single_post, name="single-post"),
]
