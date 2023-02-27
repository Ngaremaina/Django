from django.shortcuts import render
import requests 
# Create your views here.
def index(request):
    query_set = "pork"
    response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+query_set+"&app_id=4b55aada&app_key=%2062b760835f3546d3d7111edd448b68f9")

    json_response=response.json()
    recipes = json_response['hits']
    
    return render(request, 'recipes/index.html', {
        "recipes":recipes
    })

def recipe_search(request):
    if request.method == 'post':
        user_text = request.POST.get('user_text')
        response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+user_text+"&app_id=4b55aada&app_key=%2062b760835f3546d3d7111edd448b68f9")
        json_response = response.json()
        recipes = json_response['hits']
        return render(request, 'recipes/index.html',{
            "recipes": recipes
        })
    else:
        return render(request, 'recipes/index.html')
    
    
def about(request):
    return render(request, 'recipes/about.html')

def contact(request):
    name = "kenya"
    url = f"https://restcountries.com/v2/name/{name}"
    respnse=requests.get(url).json()
    flag = respnse[0]['flags']['png']
    return render(request, 'recipes/contact.html',{
        'flag':flag
    })

