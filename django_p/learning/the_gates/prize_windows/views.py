from django.shortcuts import render, HttpResponse
from .models import contacting
from datetime import datetime
# Create your views here.

def index(request):
    con = {
        'var1': 'this  get value'
    }
    return render(request,'index.html',con)

def login(request):
    return render(request,'login.html')
def welcome(request):
    return render(request,'welcome.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        ct = contacting(email = email, desc = desc, date = datetime.today())
        ct.save()
    # else:
    #     return render(request,'login.html')
    return render(request,'contact.html')