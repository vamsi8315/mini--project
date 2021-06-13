from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from Travelling.models import ImPfle,Data,PassengerData

class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		widgets = {
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter First name"
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter last name"
			}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your username",
			}),
		'email':forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your email"
			})
		}

class Updf(ModelForm):
	class Meta:
		model = User
		fields =["username","email","first_name","last_name"]
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Email id",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name",
			}),
		}

class Imp(ModelForm):
	class Meta:
		model = ImPfle
		fields = ["date_of_birth","im","mb","gender","Address"]
		widgets = {
		"date_of_birth":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			"placeholder":"DD/MM/YYYY",
			"required":True,
			}),
		"mb":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update mobile number",
			"required":True,
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"title":"Select your gender"
			}),
		"Address":forms.Select(attrs={
			"class":"form-control",
			"title":"Select your Address",
			}),
		}


class Busdata(forms.ModelForm):
	class Meta:
		model = Data
		fields = ["source","destination","busid","busclass","timmings","distance","cost","busim","da"]
		widgets = {
		"source":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Source location",
			"required":True,
			}),
		"destination":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Destination location",
			"required":True,
			}),
		"busid":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Bus number",
			"required":True,
			}),
		"busclass":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select class",
			"required":True,
			}),
		"timmings":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Bus Timmings",
			"required":True,
			}),
		"distance":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter the distance",
			}),
		"cost":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter cost",
			}),
		}

class Upbus(forms.ModelForm):
	class Meta:
		model = Data
		fields = ["busclass","distance","cost","busim"]
		widgets = {
		"busclass":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select class",
			"required":True,
			}),
		"distance":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter the distance",
			}),
		"cost":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter cost",
			}),
		}

class usdate(ModelForm):
	class Meta:
		model = Data
		fields = ["da"]

class PassData(forms.ModelForm):
	class Meta:
		model = PassengerData
		fields = ["pname","sorce","destnation","bustype","date","busid"]
		widgets = {
		"sorce":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Source location",
			"required":True,
			}),
		"pname":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Passenger Name",
			"required":True,
			}),
		"destnation":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Destination location",
			"required":True,
			}),
		"bustype":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select Bus class",
			}),
		"busid":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your Busid",
			"required":True,
			})
		}