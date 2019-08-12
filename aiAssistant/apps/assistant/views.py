from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def one_method(request):
  return HttpResponse("bears~")
def another_method(request, my_val):
  return HttpResponse("bears~" + my_val)

def yet_another(request, name):
  pass

def one_more(request, color):
  pass