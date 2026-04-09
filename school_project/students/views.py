from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def profile(request):
#    return HttpResponse("I am in student profile")

def profile(request):
   return render(request,'students/index.html')