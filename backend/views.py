from django.shortcuts import render
from .models import Joinus
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse



# Create your views here.
def home(request):
    if request.method == "POST":
        Fullname=request.POST['Fullname']
        Email=request.POST['Email']
        Contact=request.POST['Contact']
        join=Joinus(Fullname=Fullname, Email=Email,Contact=Contact)
        join.save()
        messages.success(request, "Successfully Added")
        return HttpResponseRedirect("/")
    else:
        return render(request , "index.html")


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def bba(request):
    return render(request, 'BBA.html')

def bit(request):
    return render(request, 'BIT.html')

