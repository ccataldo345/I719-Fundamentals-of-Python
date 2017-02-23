import requests
from django.http import HttpResponse

def my_view(request):
    r = requests.get("http://api.coindesk.com/v1/bpi/currentprice.json")
    data = r.json()
    price = data['bpi']['EUR']['rate']
    response = HttpResponse(price)
    return response
