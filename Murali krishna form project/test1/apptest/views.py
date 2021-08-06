from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    var = {1:1,2:2,3:5}
    return render(request,'first.html',{"v":var})


def wish2(request):
    a="<h1>what the string</h1>"
    return HttpResponse(a)

def wish3(request):
    b=10
    c=30
    d=b+c
    return HttpResponse(d)