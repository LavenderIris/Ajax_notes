from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
import random
from .models import Note

def index(request):
    return render(request,'index.html')

def create(request):
    Note.objects.create(title=request.POST['note'])
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes':notes})

def add_desc(request, id):
    print "IN DESC"
    print "DESC", request.POST
    Note.objects.filter(id=id).update(desc=request.POST['desc'])
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes':notes})


def delete(request, id):
    Note.objects.filter(id=id).delete()
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes':notes})

def toggle_desc(request,id):
    note = Note.objects.get(id=id)
    print('desc', note.desc)
    return HttpResponse('toggle desc')

def edit_desc(request, id):
    notes = Note.objects.all()
    return render(request,'index.html', {'notes':notes})