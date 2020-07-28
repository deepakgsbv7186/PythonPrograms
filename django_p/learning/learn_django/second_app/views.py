from django.shortcuts import render

# Create your views here.

def s_page(request):
    return render(request, 'second/info.html', {'sm':'Second App'})