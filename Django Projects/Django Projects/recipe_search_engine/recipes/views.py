from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    query_set = "chicken"
    response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+query_set+"&app_id=4b55aada&app_key=%2062b760835f3546d3d7111edd448b68f9")
    json_response = response.json()
    recipes = json_response['hits']
    return render(request, "recipes/index.html", {
        "recipes": recipes
    })
    
    
def recipe_search(request):
    if request.method == 'POST':
        userText = request.POST.get('userText')
        response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+userText+"&app_id=4b55aada&app_key=%2062b760835f3546d3d7111edd448b68f9")
        json_response = response.json()
        recipes = json_response['hits']
        return render(request, 'recipes/index.html', {
            "recipes": recipes
        })
    else:
        return render(request, 'recipes/index.html')


def about(request):
    return render(request, "recipes/about.html")


def contact(request):
    name = "uganda"
    url = f"https://restcountries.com/v2/name/{name}"
    response = requests.get(url).json()
    flag = response[0]['flags']['png']
    return render(request, "recipes/contact.html", {
        'flag':flag
    })
