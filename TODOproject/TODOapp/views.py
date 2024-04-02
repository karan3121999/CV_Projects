from django.shortcuts import render,redirect
from. models import Todo
from .forms import Todoform
from django.contrib import messages
# Create your views here.






def index(request):
  item_list=Todo.objects.order_by("-date")
  if request.method=="POST":
    fm=Todoform(request.POST)
    if fm.is_valid():
      fm.save()
      messages.success(request,"Your data is added")
      return redirect('/')
      
  fm=Todoform()
  page={
    "forms":fm,
    "list":item_list,
    "title":"TODO LIST"
    
  }
  return render(request,'index.html',page)



#remove krne k lie
def remove(request,item_id):
  item=Todo.objects.get(id=item_id)
  item.delete()
  messages.info(request,"item removed")
  return redirect("/")


