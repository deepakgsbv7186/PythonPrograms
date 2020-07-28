
##Program Description:- Currency Converter
##Dev:- Joel Dcosta
##JSON API :- https://api.exchangeratesapi.io/latest?base=USD
##URL OPENSOURCE :- exchangeratesapi.io

json_url = "https://api.exchangeratesapi.io/latest?base=USD"

import urllib.request as r
import json

response = r.urlopen(json_url)
data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
##Specify what data you like to view
array = data['rates']
#print(list(array)[20])
x = list(array)
# print(x)
print(array['INR'])

# for k in array.keys():
#      print (k, array[k])       

