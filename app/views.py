from django.shortcuts import render  ,redirect# Make sure to import render
from .models import Student
def home(request):
    
    data=Student.objects.all()
    context={"data":data}
    return render(request, 'index.html',context)  # Render the 'index.html' template


def insertData(request):
    
   
    
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        print(name,age,gender,email)
        
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
    return render(request,"index.html")


def DeleteData(request,id):
    
    data=Student.objects.all()
    context={"data":data}
    return render(request, 'index.html',context)
def UpdateData(request,id):
    
    
    
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        age=request.POST["age"]
        gender=request.POST["gender"]
        print(name,age,gender,email)
        
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        d=Student.objects.get(id=id)g
        context={"d":d}
        
        return redirect("/")
        
    return render(request, 'edit.html',context)