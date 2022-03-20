from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests
from .models import *
from django.contrib import messages

# Create your views here.
# def home(request):
#     data= Teacher.objects.all()
#     if request.method == "POST":
#         Fullname=request.POST['Fullname']
#         Email=request.POST['Email']
#         Contact=request.POST['Contact']
#         join=Joinus(Fullname=Fullname, Email=Email,Contact=Contact)
#         join.save()
#         messages.success(request, "Successfully Added")
#         return HttpResponseRedirect("/",{'data':data})
#     else:
#         return render(request , "index.html",{'data':data})


def home(request):
    if request.method == "POST":
        Fullname=request.POST['Fullname']
        Email=request.POST['Email']
        Contact=request.POST['Contact']
        form=Joinus(request.POST)
        check=Joinus.objects.filter(Email=Email)
        if check:
            messages.error(request, "Email already registered.")
            return HttpResponseRedirect("/")
        else:
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

def inquiry(request):
    if request.method=="POST":
        # print("aaaa")
        StdiD=request.POST['StudentId']
        # print(StdiD)
        St=Bill.objects.filter(StdiD=StdiD)
        if len(St) != 0:
            print(StdiD)
            return HttpResponseRedirect('/info/'+StdiD+'/')
            # return HttpResponse("k xa")
        else:
            messages.error(request, "Student ID not found")
            return HttpResponseRedirect("/inquiry/")
    return render(request, "khalti.html")

def info(request,id):
    information=Bill.objects.get(StdiD=id)
    return render(request, "info.html",{"info":information})
# def index_page(request):
#     price = 27000
#     return render(request,"html/index.html",{'price':price})


@csrf_exempt
def khalti(request):
   data = request.POST
   product_id = data['product_identity']
   token = data['token']
   amount = data['amount']

   url = "https://khalti.com/api/v2/payment/verify/"
   payload = {
   "token": token,
   "amount": amount
   }
   headers = {
   "Authorization": "test_public_key_dc74e0fd57cb46cd93832aee0a390234"
   }
   
   response = requests.post(url, payload, headers = headers)
   
   response_data = json.loads(response.text)
   status_code = str(response.status_code)

   if status_code == '400':
      response = JsonResponse({'status':'false','message':response_data['detail']}, status=500)
      return response

   import pprint 
   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(response_data)
   
   return JsonResponse(f"Payment Success !! . {response_data['user']['idx']}",safe=False)


# def login(request):
#     return render(request, "login_temp.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = users.authenticate(username=username, password=password)
        if user is not None:
            users.login(request, user)
            return redirect("/register/")
        else:
            messages.error(request, "Invalid Credentials. Try Again Please!")
            return redirect("/ad/")

    else:
        return render(request, "login_temp.html")


def registration(request):
    data=Joinus.objects.all()
    return render(request , "registration.html",{'data':data})

def deleteReg(request,id):
    if request.method =="POST":
        regId = Joinus.objects.get(pk=id)
        regId.delete()
        messages.error(request, "Successfully Deleted")
        return HttpResponseRedirect("/register/")