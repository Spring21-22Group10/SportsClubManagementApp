from django.forms import ModelForm, widgets
from .models import Player,Find,Fan,Staff,Forgot,Reset, Expenses, Revenue
from django import forms

# Create the form class.
class CreateForm(ModelForm):
	class Meta:
		model = Player
		fields = ['name','username', 'email', 'password', 'confirm_password']
		widgets ={
			'name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your name", 'style':'padding: 10px 10px 10px 10px'}),
			'username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a User Name", 'style':'padding: 10px 10px 10px 10px'}),
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your email", 'style':'padding: 10px 10px 10px 10px'}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),
			'confirm_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Re-enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),

		}

class FindForm(ModelForm):
	class Meta:
		model = Find
		fields = ['username', 'password']
		widgets ={
			'username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your User Name"}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password'}),

		}

class ForgotForm(ModelForm):
	class Meta:
		model = Forgot
		fields = ['email']
		widgets ={
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your User Name"}),

		}
class ResetForm(ModelForm):
	class Meta:
		model = Reset
		fields = ['email','new_password','confirm_new_password']
		widgets ={
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your email", 'style':'padding: 10px 10px 10px 10px'}),
			'new_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),
			'confirm_new_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Re-enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),

		}

class ExpenseForm(ModelForm):
	class Meta:
		model = Expenses
		fields = ['department_expense','department_name','expense_name','expense_date']
		widgets ={
			'department_expense' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter the expense amount", 'style':'padding: 10px 10px 10px 10px'}),
			'department_name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your department name",  'style':'padding: 10px 10px 10px 10px'}),
			'expense_name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter the type of expense", 'style':'padding: 10px 10px 10px 10px'}),
			'expense_date' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter the date of expense", 'style':'padding: 10px 10px 10px 10px'}),

		}

