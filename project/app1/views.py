from django.shortcuts import render , redirect
from django.views.generic import TemplateView, ListView
from app1.forms import registrationform,contform,baseform
from app1.models import prod
from app1.models import *
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib import messages
#Create your views here.

# class homeview(TemplateView):
    # template_name="home.html"
class baseview(TemplateView):
    template_name="base.html"
class formview(TemplateView):
    template_name="form.html"
# class bhartiview(TemplateView):
    # template_name="bharti.html"
class poetriesview(TemplateView):
    template_name="poetries.html"
# class catview(TemplateView):
    # template_name="cat.html"
class aboutview(TemplateView):
    template_name="about.html"
class cusview(TemplateView):
    template_name="cus.html"
class tscview(TemplateView):
    template_name="tsc.html"
class prcyview(TemplateView):
    template_name="prcy.html"
class contview(TemplateView):
    template_name="cont.html"
class shipview(TemplateView):
    template_name="ship.html"
class payview(TemplateView):
    template_name="pay.html"
class grntview(TemplateView):
    template_name="grnt.html"
class prodview(ListView):
    template_name="prod.html"
    def get_queryset(self):
        return prod.objects.all()

def insertform(request):
    if request.method=='POST':
        form=registrationform(request.POST,request.FILES)
        if form.is_valid():
            print('inside form is valid')
            form.save()
            return redirect('/form/')
    else:
        form=registrationform()
    return render(request,"form.html",{'form':form})
    
def insertcont(request):
    if request.method=='POST':
        form=contform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cont/')
    else:
        form=contform()
    return render(request,"cont.html",{'form':form})

def insertbase(request):
    if request.method=='POST':
        form=baseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/poetries/')
    else:
        form=baseform()
    return render(request,"base.html",{'form':form})



# form=contform(request.POST,request.FILES)

def signin(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('/login/')
            else:
                messages.error(request, 'Username and password do not match')
                return redirect('/login/')  # or render a template with the error message
        else:
            return render(request, 'login.html')
    # return render(request, "login.html")	


def signout(request):
    logout(request)
    return redirect('/login/')	


def registration(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('signin')

	return render(request, 'signup.html', {"form": form})