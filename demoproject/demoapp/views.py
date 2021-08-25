from django.http import HttpResponse
from django.shortcuts import render
from .models import User
# from .models import Product
# # Create your views here.
# def index(request):
#     #return HttpResponse("<h1>welcome to my django demo app</h1>")
#     # obj=Product(102,"kitkat",52,15)
#     # obj.save()
#     data=Product.objects.all()
#     res= {}
#     for i in data:
#         res[i.id]={"name":i.name,"price":i.price,"qty":i.qty}
#     print(res)
#     return render(request,"index.html",{'data':res})

def calculate(request):
    x=request.POST['num1']
    y=request.POST['num2']
    z=int(x)+int(y)
    return  render(request,"login.html",{"x":x,"y":y,"z":z})

def register(request):
    return render(request,"register.html")

def save(request):
    fname=request.GET['fname']
    mobile=request.GET['mobile']
    email=request.GET['email']
    job=request.GET['job']
    password=request.GET['password']
    obj=User(name=fname,mobile=mobile,email=email,type=job,password=password)
    obj.save()
    return HttpResponse("Account has been created successfully")

def retrieve(request):
    users=User.objects.all()
    return render(request,"displayuser.html",{"data":users})
    # return HttpResponse(f"{users[0].name} {users[0].mobile} {users[0].email} {users[0].type} {users[0].password}")
#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