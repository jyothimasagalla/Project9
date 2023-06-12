from django.shortcuts import render
from django.views import View
import requests
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from Project9.settings import EMAIL_HOST_USER
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Reg(View):
    def post(self,request):
        otp=str(random.randint(10000000,999999999))
        mobno=request.POST["t7"]
        emailid=request.POST["t6"]
        resp = requests.post('https://textbelt.com/text', {
            'phone': mobno,
            'message': otp,
            'key': 'deb651692eabe6a8c4dc2bf4c540d840302c14beufATt5cvEXUzaN5EDcNM17S9q'
        })
        print(resp.json())
        send_mail("otp for registration",otp,EMAIL_HOST_USER,[emailid],fail_silently=True)
        return HttpResponse("otp sent to mobileno and email")

