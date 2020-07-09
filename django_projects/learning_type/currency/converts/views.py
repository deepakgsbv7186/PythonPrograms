from django.shortcuts import render
from django.http import HttpResponse
from . import form
json_url = "https://api.exchangeratesapi.io/latest?base=USD"

import urllib.request as r
import json
response = r.urlopen(json_url)
data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
##Specify what data you like to view

array = data['rates']

# Create your views here.
def index(request):
    if request.method=='POST':
        inr = array['INR']
        print('*'*30)
        print(inr)
        usd=request.POST['usd']
        inr=float(inr)
        usd=float(usd)
        x=inr*usd
        

        fm=form.inrTousd(initial={'inr':x})
        # return HttpResponse(x)
        return render(request,'index.html',{'form':fm})

    if request.method == 'GET':
        fm=form.inrTousd()
    return render(request,'index.html',{'form':fm})