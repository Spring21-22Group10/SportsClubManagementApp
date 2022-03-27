from django.forms import ModelForm, widgets
from .models import Player,Course_Taken,Player2
from django import forms

# Create the form class.
class CreatePlayerForm(ModelForm):
	class Meta:
		model = Player
		fields = ['Player_name', 'email', 'password', 'confirm_password']
		widgets ={
			'Player_name' : forms.TextInput(attrs={'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white u-input', 'placeholder':"Enter your name", 'name':'Player'}),
			'email' : forms.TextInput(attrs={'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white u-input', 'placeholder':"Enter your email"}),
			'password' : forms.TextInput(attrs={'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white u-input', 'placeholder':"Enter a password"}),
			'confirm_password' : forms.TextInput(attrs={'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white u-input', 'placeholder':"Reenter a password"}),

		}

class FindPlayerForm(ModelForm):
	class Meta:
		model = Player2
		fields = ['Player_name', 'password']
		widgets ={
			'Player_name' : forms.TextInput(attrs={'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white u-input', 'placeholder':"Enter your name", 'name':'Player2'}),
			'password' : forms.TextInput(attrs={'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white u-input', 'placeholder':"Enter a password"}),

		}
# Create the form class.
class CreateCourseForm(ModelForm):
	class Meta:
		model = Course_Taken
		fields = ['Player_id', 'Course_id', 'Semester','Number_of_credits','Grade']

