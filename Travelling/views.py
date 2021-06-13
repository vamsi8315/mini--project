from django.shortcuts import render,redirect
from django.http import HttpResponse
from Travelling.forms import UsReg,Updf,Imp,Busdata,Upbus,usdate,PassData
from HappyJourney import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Travelling.models import ImPfle,Data,PassengerData
from django.db import connection
#cursor = connection.cursor()

# Create your views here.

def home(request):
	return render(request,'ta/home.html')

def register(request):
	if request.method == "POST":
		t = UsReg(request.POST)
		if t.is_valid():
			user=t.save()
			messages.success(request,"User registered Successfully")
			#return redirect('/lg')
			adml = user.email
			pas = user.password
			msg = "Hi {} {}, your registeration is completed successfully your username is {} and password is {}. Don't share your passwords to any annoymous persons".format(user.first_name,user.last_name,user.username,user.password)
			sub = "Mail from Indian Travels"
			sd = settings.EMAIL_HOST_USER
			to = send_mail(sub,msg,sd,[adml])
			if to == 1:
				return redirect('/login')
				messages.primary("A mail sent to your account don't share your password to anyone")
			messages.warning(request,'mail not sent')
		messages.error(request,'Registation failed')
	t = UsReg()
	return render(request,'ta/register.html',{'y':t})

@login_required
def pfle(request):
	return render(request,'ta/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p = Updf(request.POST,instance=request.user)
		k = Imp(request.POST,request.FILES,instance=request.user.impfle)
		if p.is_valid() and k.is_valid():
			p.save()
			k.save()
			messages.info(request,'{} profile updated successfully'.format(request.user.username))
			return redirect('/profile')
	p = Updf(instance=request.user)
	y =Imp(instance=request.user.impfle)
	return render(request,'ta/upfle.html',{'h':p,'u':y})

@login_required
def bus_search(request):
	return render(request,'ta/bus_search.html')

@login_required
def bus(request):
	results = Data.objects.all()
	if request.method == "POST":
		c = usdate(request.POST,instance=request.user)
		if c.is_valid():
			so = request.POST.get('source')
			de = request.POST.get('destination')
			busobj = Data.objects.raw('select * from data where source="'+so+'" and destination="'+de+'"')
			print(busobj)
			c.save()
			return render(request,'ta/bus_search.html',{'Data':busobj})
	c = usdate(instance=request.user)
	return render(request,'ta/bus.html',{'places':results,'d':c})

@login_required
def upbus(request,rq):
	n = Data.objects.get(id=rq)
	if request.method == "POST":
		k = Busdata(request.POST,instance=n)
		p = Upbus(request.POST,request.FILES,instance=request.user)
		if k.is_valid() and p.is_valid():
			k.save()
			p.save()
			messages.success(request,' Bus is updated successfully')
		else:
			messages.error(request,'Bus added failed')
	k = Busdata(instance=n)
	p = Upbus(instance=request.user)
	return render(request,'ta/upbus.html',{'d':k,'e':p})


@login_required
def addbus(request):
	if request.method == "POST":
		w = Busdata(request.POST,request.FILES)
		if w.is_valid():
			w.save()
			messages.success(request,"Bus are added successfully")
			return redirect('/disp')
		else:
			messages.error(request,"Bus added failed")
	w =Busdata()
	return render(request,'ta/addbus.html',{'d':w})

@login_required
def disbus(request,pq):
	return render(request,'ta/disbus.html',{'vi':Data.objects.get(id=pq)})

@login_required
def disp(request):
	return render(request,'ta/disp.html',{'dis':Data.objects.all()})

@login_required
def dele(request,de):
	c = Data.objects.get(id=de)
	if request.method == "POST":
		c.delete()
		return redirect('/disp')
	return render(request,'ta/delete.html',{'fe':c})

@login_required
def dashbord(request):
	return render(request,'ta/dashboard.html')

@login_required
def bookticket(request,pt):
	if request.method == "POST":
		m = PassengerData.objects.filter(m_id=request.user.id)
		r = PassData(request.POST)
		if r.is_valid():
			t = r.save(commit=False)
			t.m_id = request.user.id
			t.save()
			messages.success(request,"Successfully ticket booked")
			return redirect('/pasdata')
		messages.info(request,"Payment Failed")
		return redirect('/pasdata')
	r = PassData()
	return render(request,'ta/bookticket.html',{'bot':Data.objects.get(id=pt),'d':r})

@login_required
def pasdata(request):
	p = PassengerData.objects.filter(m_id=request.user.id)
	return render(request,'ta/pasdata.html',{'y':p})


@login_required
def delet(request,det):
	c = PassengerData.objects.get(id=det)
	if request.method == "POST":
		c.delete()
		return redirect('/pasdata')
	return render(request,'ta/delet.html',{'fe':c})