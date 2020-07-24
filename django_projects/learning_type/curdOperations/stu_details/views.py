from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentReg
from .models import User
# Create your views here.

def welcome(request):
    return render(request, 'index.html', {'wm': 'Register Yourself'})


def add_show(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email = em, password = pw)
            reg.save()
            
            fm = StudentReg()
    else:
        fm = StudentReg()
    stud = User.objects.all()
    return render(request, 'student/add_student.html', {'regform': fm, 'st':stud})


def delete_data(request, id):
    if request.method == 'POST':
        de = User.objects.get(pk=id)
        de.delete()
    return HttpResponseRedirect(redirect_to='add/')


def update_show(request, id):
    if request.method == 'POST':
        up = User.objects.get(pk=id)
        f = StudentReg(request.POST, instance = up)
        if f.is_valid():
            f.save()
    else:
        up = User.objects.get(pk=id)
        f = StudentReg(instance = up)
    return render(request, 'student/update_student.html', {'form': f})