from django.shortcuts import render
import todo_app.models
from todo_app.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
# view act as interface between model(database) and template(frontend)
# MVT => Model => View => Template / URL
def todo_list(request):
   todos = Todo.objects.all()
   return render(
      request,
      "bootstrap/todo_list.html",
      {"todos": todos},
    

   )

def todo_delete(request,id):
   todo = Todo.objects.get(id=id) #queryset ORM # select * from todo where id=id
   todo.delete()
   return HttpResponseRedirect("/") #  go to the home page after deletion

def todo_create(request):
   print(request.POST,request.method)
   # request.POST["title"]
   if request.method == "GET": 
      return render(request,"bootstrap/todo_create.html") 
   else:
      Todo.objects.create(title=request.POST["title"])
      return HttpResponseRedirect("/")
      
def todo_update(request,id):
   if request.method=="GET":
      todo=Todo.objects.get(id=id)
      return render(
         request,
         "bootstrap/todo_update.html",
         {"todo":todo},
      )
   else:
      todo=Todo.objects.get(id=id)
      todo.title=request.POST["title"]
      todo.save()
      return HttpResponseRedirect("/")
   

   
