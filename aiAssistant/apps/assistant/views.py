from django.shortcuts import render, HttpResponse, redirect
def index(request):
  context = {
    "name": "Noelle",
    "favorite_color": "turquoise",
    "pets": ["Bruce", "Fitz", "Georgie"]
  }
  return render(request, "assistant/index.html", context)
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request, my_val):
  return HttpResponse("placeholder to display blog number " + my_val)
def edit(request, my_val):
  return HttpResponse("placeholder to edit blog " + my_val)


  
def one_method(request):
  return HttpResponse("bears~")
def another_method(request, my_val):
  return HttpResponse("bears~" + my_val)

def yet_another(request, name):
  pass

def one_more(request, color):
  pass