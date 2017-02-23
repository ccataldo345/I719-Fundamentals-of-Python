import requests
from pprint import pprint

r = requests.get("http://api.coindesk.com/v1/bpi/currentprice.json")
r.json()

my_dict = r.json()['bpi']['EUR']
pprint(my_dict)
