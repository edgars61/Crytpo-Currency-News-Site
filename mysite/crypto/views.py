from django.shortcuts import render
from html.parser import HTMLParser

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    string =api
    

    return render(request, 'home.html',{'api':api})