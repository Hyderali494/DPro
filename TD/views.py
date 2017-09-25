from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from TD.models import Register,Contact
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
        user = User.objects.filter(username= name,password = pwd)
        if user:
            return render_to_response('dashboard.html')
        else:
            return HttpResponse("Please register now")
    else:
        return HttpResponse("Please Enter both Username & Password")
def showRegister(request):
    return render_to_response('register.html')
@csrf_exempt
def getRegister(request):
    rname = request.POST['name'];
    rpwd = request.POST['pwd'];
    rmail = request.POST['email'];
    if rname and rpwd and rmail:
        ruser = User.objects.filter(username = rname,password = rpwd);
        if ruser: 
            data = "User Already Exists";
            return HttpResponse(data);
        else:
            ruser = User(username = rname,password = rpwd,email = rmail)
            ruser.save()
            data = "User Registered Sucessfully";
            return HttpResponse(data);
    else:
        data = "Please enter all the fields";
        return HttpResponse(data)
def showContact(request):
    return render_to_response('contact.html');
@csrf_exempt
def getContact(request):
    name = request.POST['name'];
    nname = request.POST['nname'];
    phone_no = int(request.POST['phone_no']);
    email = request.POST['email'];
    company = request.POST['cmp'];
    if name and phone_no:
        cont = Contact.objects.filter(Username = name,Phone_no = phone_no);
        if cont:
            data = "Contact Already Exists";
            return HttpResponse(data);
        else:
            cont = Contact(Username = name,Nickname = nname,Phone_no = phone_no,Email = email,Company = company);
            cont.save()
            data = "Contact Saved Sucessfully";
            return HttpResponse(data);
    else:
        data = "Please fill atleast Username and Phone Number Fields";
        return HttpResponse(data);
def jsonview(request):
    data = {'name':'Imran','address':'Kormangla'};
    return HttpResponse(json.dumps(data));

def dispContacts(request):
    data = Contact.objects.all()
    return render(request,'showcontacts.html',{'data' : data}) 
