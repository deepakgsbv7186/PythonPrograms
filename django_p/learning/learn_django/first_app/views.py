from django.shortcuts import render

# Create your views here.

def f_page(request):
    return render(request, 'first/info.html', {'fm':'First App'})