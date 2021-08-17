from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("<h1>welcome to my django demo app</h1>")
    return render(request,"login.html")

def calculate(request):
    x=request.GET['num1']
    y=request.GET['num2']
    z=int(x)+int(y)
    return  render(request,"login.html",{"x":x,"y":y,"z":z})
