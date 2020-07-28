from django.shortcuts import render
from .forms import uploadform
from .models import uploadimg

# Create your views here.
def index(request):
    if request.method == 'POST':
        form=uploadform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:        
        form = uploadform()
    return render(request,'index.html',{'form':form})


def show(request):
    data = uploadimg.objects.filter(catagory='wall')
    return render(request,'show.html',{'data':data})   

