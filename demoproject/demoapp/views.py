from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Product,Employee

def index(request):
    return render(request,"employee.html")

def uploadresume(request):
    if request.method == 'POST':
        obj = Employee.objects.create(name=request.POST['employeename'],resume=request.FILES['resume'])
        obj.save()

        return render(request,'employee.html',{'data':Employee.objects.all()})

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


    # return HttpResponse("Account has been created successfully")
    return render(request,"register.html",{"msg":"Account has been created successfully"})


def retrieve(request):
    users=User.objects.all()
    return render(request,"displayuser.html",{"data":users})
    # return HttpResponse(f"{users[0].name} {users[0].mobile} {users[0].email} {users[0].type} {users[0].password}")
#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

def login(request):
    return  render(request,"login1.html",{})

def welcome(request):
    return  HttpResponse("<h1>Welcome to Home Page</h1>")

def checklogin(request):
    username=request.POST['uname']
    password=request.POST['Password']
    user=User.objects.filter(name=username,password=password)
    if user:
        return redirect(welcome)
    else:
        return redirect(login)

def product(request):
    return render(request,"products.html")

def addproduct(request):
    product=Product(name=request.POST['name'],price=request.POST['price'],qty=request.POST['qty'])
    product.save()
    return render(request,"product.html",{})

def searchproduct(request):
    product=Product.objects.filter(name=request.POST['name'])
    for i in product:
        name=i.name
        price=i.price
        qty=i.qty
    if product:
        return render(request,"product.html",{'name':name,'price':price,"qty":qty})


def updateproduct(request):

    product=Product.objects.filter(name=request.POST['name'].strip())

    for i in product:

        id=i.id

    Product.objects.filter(id=id).update(price=request.POST['price'],qty=request.POST['qty'])
    return  render(request,"product.html")

# def deleteproduct(request):
#     # product=Product.objects.filter(name=request.POST['name'].strip())
#     #
#     # for i in product:
#     #     id=i.id
#     #
#     # Product.objects.filter(id=id).delete()
#     #send_mail("Test Mail",f"Product Id : {id} has been delete from db",settings.EMAIL_HOST_USER,['se.murugaiyan@gmail.com'])
#     email=EmailMessage("Test Mail","<h1 style='color:pink;border:solid'>Welcome to Test Mail</h1>",settings.EMAIL_HOST_USER,["se.murugaiyan@gmail.com"])
#     email.content_subtype='html'
#     email.send()
#     return render(request,"product.html")


def saveproduct(request):
    name = request.GET['product']
    price = request.GET['price']
    qty = request.GET['qty']

    obj = Product(name=name,price=price,qty=qty)
    obj.save()

    data = Product.objects.all()
    return render(request,"products.html",{"data":data})

def editproduct(request):
    id= request.GET['id']
    name = request.GET['product']
    price = request.GET['price']
    qty = request.GET['qty']

    data = Product.objects.get(id=id)
    data.price=price
    data.qty = qty
    data.save()
    data = Product.objects.all()
    return render(request, "products.html", {"data": data})

def deleteproduct(request):
    id = request.GET['id']


    data = Product.objects.get(id=id)

    data.delete()
    data = Product.objects.all()
    return render(request, "products.html", {"data": data})





