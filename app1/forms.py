from django.forms import ModelForm, widgets
from .models import Player,Find,Fan,Staff,Forgot,Reset, Expenses, Revenue, Report, Cart, Price, CreditCard, choicesMonth, Match, Merchandise
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


class ReportForm(ModelForm):
	class Meta:
		model = Report
		fields = ['Month','Name','Department','Email']
		widgets ={
			'Month' : forms.Select(choices=choicesMonth,attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Name",  'style':'padding: 10px 10px 10px 10px'}),
			'Name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Name",  'style':'padding: 10px 10px 10px 10px'}),
			'Department' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Department Name", 'style':'padding: 10px 10px 10px 10px'}),
			'Email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle','placeholder':"Enter Email", 'style':'padding: 10px 10px 10px 10px'}),
		}

class GetPrice(ModelForm):
	class Meta:
		model = Price
		fields = []

class CreditCardForm(ModelForm):
	class Meta:
		model = CreditCard
		fields = ['name','card_number','experation_date', 'CCV']
		widgets = {
			'name' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Your Name",  'style':'padding: 10px 10px 10px 10px'}),
			'card_number' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"____ ____ ____ ____",  'style':'padding: 10px 10px 10px 10px'}),
			'experation_date' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"YY/MM",  'style':'padding: 10px 10px 10px 10px'}),
			'CCV' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"___",  'style':'padding: 10px 10px 10px 10px'}),
		}


class AddMatch(ModelForm):
	class Meta:
		model = Match
		fields = ['team1','team1_logo', 'team2','team2_logo','location','date','priceA','priceB','priceC']
		widgets = {
			'team1' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Team 1 Name",  'style':'padding: 10px 10px 10px 10px'}),
			'team1_logo' : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
			'team2' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Team 2 Name",  'style':'padding: 10px 10px 10px 10px'}),
			'team2_logo' : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
			'date' : forms.DateInput(format='%d-%m-%Y',attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px','type': 'date'}),
			'location' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Match Location",  'style':'padding: 10px 10px 10px 10px'}),
			'priceA' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Price Zone A",  'style':'padding: 10px 10px 10px 10px'}),
			'priceB' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Price Zone B",  'style':'padding: 10px 10px 10px 10px'}),
			'priceC' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Price Zone C",  'style':'padding: 10px 10px 10px 10px'}),
		}

class AddMerchandise(ModelForm):
	class Meta:
		model = Merchandise
		fields = ['item_name','price','item_image']
		widgets = {
			'item_name' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Item Name",  'style':'padding: 10px 10px 10px 10px'}),
			'price' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Item Price",  'style':'padding: 10px 10px 10px 10px'}),
			'item_image' : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
		}


