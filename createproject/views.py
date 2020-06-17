from django.shortcuts import render
# my import
from.models import createproject
from .models import Create
from django import forms
# Create your views here.
# my def 

def createproject(request):
    createproject = createproject.objects.get()

    if request.method=='POST':
       form = Create(request.POST)
       if form.is_valid():
           form = form.save()
    else :
        form = Create()
    context = {'createproject' : createproject , 'form':form}
    return render (request,'createproject.html',context)
 