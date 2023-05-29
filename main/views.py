from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewList
from .models import ToDoList


# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.all()[0]
    return HttpResponse("<h1> %s </h1><p>%s</p>" %(ls.name, str(item.text)))


def v1(response):
    return HttpResponse("<h1>View 1</h1>")


def home(response):
    return render(response, "main/home.html", {"name": "John"})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            #t = ToDoList(name=n)
            #form.save()
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

