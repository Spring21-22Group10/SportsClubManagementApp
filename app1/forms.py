from django.forms import ModelForm, widgets
from .models import Player,Player2,Fan,Fan2,Staff
from django import forms

# Create the form class.
class CreatePlayerForm(ModelForm):
	class Meta:
		model = Player
		fields = ['Player_name','Player_username', 'email', 'password', 'confirm_password']
		widgets ={
			'Player_name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your name", 'style':'padding: 10px 10px 10px 10px'}),
			'Player_username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a User Name", 'style':'padding: 10px 10px 10px 10px'}),
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your email", 'style':'padding: 10px 10px 10px 10px'}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),
			'confirm_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Re-enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),

		}

class FindPlayerForm(ModelForm):
	class Meta:
		model = Player2
		fields = ['Player_username', 'password']
		widgets ={
			'Player_username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your User Name"}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password'}),

		}

class CreateFanForm(ModelForm):
	class Meta:
		model = Fan
		fields = ['Fan_name','Fan_username', 'email', 'password', 'confirm_password']
		widgets ={
			'Fan_name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your name"}),
			'Fan_username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a User Name"}),
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your email"}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password'}),
			'confirm_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Re-enter a password", 'type':'password'}),

		}

class FindFanForm(ModelForm):
	class Meta:
		model = Fan2
		fields = ['Fan_username', 'password']
		widgets ={
			'Fan_username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your User Name"}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password'}),

		}

class FindStaffForm(ModelForm):
	class Meta:
		model = Staff
		fields = ['Staff_username', 'password']
		widgets ={
			'Staff_username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your User Name"}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password'}),

		}


