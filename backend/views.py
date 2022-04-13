from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import random
import json
import numpy as np 
import nltk
import pickle
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
from django.contrib.auth.models import User

# Create your views here.


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
        if 'inquiry' in request.POST:
            StdiD=request.POST['StudentId']
            Password=request.POST['Password']
            St=Student.objects.filter(StdiD=StdiD)
            if len(St) != 0:
                print(StdiD)
                print(Password)
                authpass=Student.objects.filter(Password=Password)
                if authpass:
                    return HttpResponseRedirect('/info/'+StdiD+'/')
                else:
                    messages.error(request, "Student ID Password doesnot match")
                # return HttpResponse("k xa")
            else:
                messages.error(request, "Student ID not found")
                return HttpResponseRedirect("/inquiry/")
        if 'update' in request.POST:
            if request.method=='POST':
                StdiD=request.POST['stid']
                pass_ = Student.objects.get(StdiD = StdiD)
                Current_Password=request.POST['currentpass']
                if (pass_.Password==Current_Password):
                    newpass=request.POST['newpass']
                    newpass1=request.POST['newpass1']
                    if Password==Password and newpass==newpass1:
                        data = Student.objects.filter(StdiD=StdiD).update(Password=newpass1)
                        data.save()
                    else:
                        messages.error(request, "Password doesnot match")
                else:
                    messages.error(request, "Password doesnot match")
    return render(request, "khalti.html")

def info(request,id):
    information=Student.objects.get(StdiD=id)
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


# def registration(request):
#     data=Joinus.objects.all()
#     return render(request , "registration.html",{'data':data})

# def deleteReg(request,id):
#     if request.method =="POST":
#         regId = Joinus.objects.get(pk=id)
#         regId.delete()
#         messages.error(request, "Successfully Deleted")
#         return HttpResponseRedirect("/register/")




lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read()) #read intends file

words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model=load_model('chatbot model.model')

def clean_up_sentence(sentence):
    sentence_words= nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words



def bag_of_words(sentence):
    sentence_words=clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word== w:
                bag[i]=1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results= [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability':str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    
    for i in list_of_intents:
        if i['tag'] == tag:
            result= random.choice(i['responses'])
            break
    return result

print("HI! How may I help you!")


@csrf_exempt
def receiveMessage(request):
    print(json.loads(request.body)['message'])
    res = 'nothing'
    message=json.loads(request.body)['message']
    ints=predict_class(message)
    res=get_response(ints, intents)
    print(res)
    return JsonResponse({"status":res})

# def changePassword(request, id):
#     if request.method == "POST":
#         pk=Bill.objects.get(pk=id)
#         form=MenuForm(request.POST,instance=pk)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/Bill/")
#     else:
#         pk=Menu.objects.get(pk=id)
#         form=MenuForm(instance=pk)
#         return render(request , "menuupdate.html",{'form':form})



# def changepass(request):
#     if request.method == "POST":
#         stid=request.POST['stid']
#         currentpass=request.POST['currentpass']
#         password=request.POST['newpass']
#         repassword=request.POST['newpass1']
#         # fm=PasswordChangeForm(user=request.user, date=request)
#         # if fm.is_valid():
#         #     fm.save()
#         #     return HttpResponse('/info/')
#         # else:
#         #     fm=PasswordChangeForm(user=request.user)  
#         # return render (request, "khalti.html",{"form":fm})
#         print(stid)
#         print(currentpass)
#         print(password)
#         print(repassword)