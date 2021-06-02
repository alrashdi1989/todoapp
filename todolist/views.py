from todolist.models import Todolist
from django.shortcuts import render
from .models import Todolist
# Create your views here.
def index(requset):
    todo_items = Todolist.objects.order_by('id') 
    context ={'todo_items' : todo_items}
    return render(requset,'todolist\index.html',context)

def home(requset):
    todo_items = Todolist.objects.order_by('id') 
    context ={'todo_items' : todo_items}
    return render(requset,'todolist\Home.html',context)
