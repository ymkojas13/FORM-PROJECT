from django.shortcuts import render
from .form import Student
from .models import mode

# Create your views here.
def formfun(request):
    fm=Student()
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        datastore=mode(name=name,password=password,email=email,contact=contact)
        datastore.save()
    return render(request,'formhtml.html',{'formkey':fm})
