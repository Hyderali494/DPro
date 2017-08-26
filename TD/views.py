from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from TD.models import Register
import json
def test(request):
    return HttpResponse("you are in TD")
def showLogin(request):
    return render_to_response('login.html')
@csrf_exempt
def getLogin(request):
    name = request.POST['name']
    pwd = request.POST['pwd']
    if name and pwd:
        user = Register.objects.filter(username= name,password = pwd)
        if user:
            return HttpResponse("Dashboard")
        else:
            return HttpResponse("Please register now")
    else:
        return HttpResponse("Please Enter both Username & Password")
def showRegister(request):
    return render_to_response('register.html')
@csrf_exempt
def getRegister(request):
    rname = request.POST['rname']
    rpwd = request.POST['rpwd']
    rmail = request.POST['rmail']
    rphone = request.POST['rphone']
    if rname and rpwd and rmail and rphone:
        ruser = Register.objects.filter(username = rname,password = rpwd)
        if ruser: 
            return HttpResponse("User already Exists")
        else:
            ruser = Register(username = rname,password = rpwd,Email = rmail,Phone_no = rphone)
            ruser.save()
            return HttpResponse("user Registered Sucessfully. Please login into your Account")
    else:
        return HttpRespone("Please enter all the fields")

def jsonview(request):
    data = {"name":"imran","age":24}
    return HttpResponse(json.dumps(data), content_type = 'application/json')
# Create your views here.
