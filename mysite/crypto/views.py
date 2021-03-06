from django.shortcuts import render
from html.parser import HTMLParser

# Create your views here.
def home(request):
    import requests
    import json

    #Grab Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD")
    price = json.loads(price_request.content)



    #Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html',{'api':api,'price':price})