from django.urls import path
from recipes.views import index, about, contact,recipe_search

urlpatterns = [
    path('', index, name="home-page"),
    path('search', recipe_search, name = "recipe-search"),
    path('about', about, name="about-page"),
    path('contact', contact, name="contact-page"),
]