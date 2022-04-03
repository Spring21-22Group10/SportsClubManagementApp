from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CreateForm,FindForm,ForgotForm,ResetForm
from .models import Player,Fan,Staff,Match
from django.contrib import messages
from django.core.mail import send_mail
import datetime


def index(request):
	request.session['user'] = None
	request.session['buying'] = None
	return render(request,'index.html')

def home_main(request):
	return render(request,'HOME.html',)

def home_staff(request):
	return render(request,'HOME_Staff.html',)

def report(request):
	user = request.session['user']
	return render(request,'Report.html',{ 'user':user })

def buyA(request):
	return render(request,'HOME.html')

def buyB(request):
	return render(request,'HOME.html')

def buyC(request):
	return render(request,'HOME.html')

def news(request):
	user = request.session['user']
	return render(request,'News.html',{ 'user':user })

def tickets(request):
	request.session['buying'] = True
	match = Match.objects.order_by('date').first()
	user = request.session['user']
	team1 = match.team1
	team2 = match.team2
	date = match.date
	Stadium = match.location
	priceA = match.priceA
	priceB = match.priceB
	priceC = match.priceC
	return render(request,'Tickets.html',{ 'user':user, 'team1':team1, 'team2':team2, 'date':date,'Stadium':Stadium, 'priceA':priceA,'priceB':priceB,'priceC':priceC })

def player_login(request):
	if request.method == 'POST':
		form = FindForm(request.POST)
		if form.is_valid():
			Playerform = form.cleaned_data
			username = Playerform['username']
			password = Playerform['password']
			for e in Player.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.username
					return render(request, 'HOME.html', { 'user': A.username })
		form = FindForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Player-Login.html', {'form': form, 'message':message})
	form = FindForm()
	S = Player.objects.all()
	return render(request, 'Player-Login.html', {'form': form,'S':S})

def player_signup(request):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			Playerform = form.cleaned_data
			name = Playerform['name']
			username = Playerform['username']
			password = Playerform['password']
			confirm_password = Playerform['confirm_password']
			email = Playerform['email']
			next_id = 1
			if(Player.objects.all()):
				next_id = Player.objects.last().id + 1
			Player.objects.create(id=next_id,name=name,username=username,password=password,confirm_password=confirm_password,email=email)
			for e in Player.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.username
					return render(request, 'HOME.html', { 'user': A.username })
	form = CreateForm()
	S = Player.objects.all()
	return render(request, 'Player-Signup.html', {'form': form,'S':S})

def reset_password_player(request):
	if request.method == 'POST':
		form = ResetForm(request.POST)
		if form.is_valid():
			resetForm = form.cleaned_data
			email = resetForm['email']
			new_password = resetForm['new_password']
			confirm_new_password = resetForm['confirm_new_password']
			for e in Player.objects.all():
				if e.email==email:
					e.password = new_password
					e.confirm_password = confirm_new_password
					e.save()
					message = 'Password reset succesfuly'
					form = ResetForm()
					return render(request, 'Reset-Password-Player.html', {'form': form, 'message':message})

	form = ResetForm()
	return render(request, 'Reset-Password-Player.html', {'form': form})

def fan_login(request):
	if request.method == 'POST':
		form = FindForm(request.POST)
		if form.is_valid():
			Fanform = form.cleaned_data
			username = Fanform['username']
			password = Fanform['password']
			for e in Fan.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.username
					if request.session['buying'] is not None:
						return tickets(request)
					return render(request, 'HOME.html', { 'user': A.username })
		form = FindForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Fan-Login.html', {'form': form, 'message':message})
	form = FindForm()
	S = Fan.objects.all()
	return render(request, 'Fan-Login.html', {'form': form,'S':S})

def Fan_signup(request):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			Fanform = form.cleaned_data
			name = Fanform['name']
			username = Fanform['username']
			password = Fanform['password']
			confirm_password = Fanform['confirm_password']
			email = Fanform['email']
			next_id = 1
			if(Fan.objects.all()):
				next_id = Player.objects.last().id + 1
			Fan.objects.create(id=next_id,name=name,username=username,password=password,confirm_password=confirm_password,email=email)
			for e in Fan.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.username
					return render(request, 'HOME.html', { 'user': A.username })
	form = CreateForm()
	S = Fan.objects.all()
	return render(request, 'Fan-Signup.html', {'form': form,'S':S})

def reset_password_fan(request):
	if request.method == 'POST':
		form = ResetForm(request.POST)
		if form.is_valid():
			resetForm = form.cleaned_data
			email = resetForm['email']
			new_password = resetForm['new_password']
			confirm_new_password = resetForm['confirm_new_password']
			for e in Fan.objects.all():
				if e.email==email:
					e.password = new_password
					e.confirm_password = confirm_new_password
					e.save()
					message = 'Password reset succesfuly'
					form = ResetForm()
					return render(request, 'Reset-Password-Fan.html', {'form': form, 'message':message})

	form = ResetForm()
	return render(request, 'Reset-Password-Fan.html', {'form': form})

def staff_login(request):
	if request.method == 'POST':
		form = FindForm(request.POST)
		if form.is_valid():
			Staffform = form.cleaned_data
			username = Staffform['username']
			password = Staffform['password']
			for e in Staff.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.username
					return render(request, 'HOME.html', { 'user': A.username })
		form = FindForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Staff-Login.html', {'form': form,'message':message})
	form = FindForm()
	S = Staff.objects.all()
	return render(request, 'Staff-Login.html', {'form': form,'S':S})

def reset_password_staff(request):
	if request.method == 'POST':
		form = ResetForm(request.POST)
		if form.is_valid():
			resetForm = form.cleaned_data
			email = resetForm['email']
			new_password = resetForm['new_password']
			confirm_new_password = resetForm['confirm_new_password']
			for e in Staff.objects.all():
				if e.email==email:
					e.password = new_password
					e.confirm_password = confirm_new_password
					e.save()
					message = 'Password reset succesfuly'
					form = ResetForm()
					return render(request, 'Reset-Password-Staff.html', {'form': form, 'message':message})

	form = ResetForm()
	return render(request, 'Reset-Password-Staff.html', {'form': form})

def forgot_password_player(request):
	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Player.objects.all():
				if e.email==email:
					A=e
					message_to_send = 'Hello ' + A.username + ',\n\n Please use the link below to reset your email. \n\n http://localhost:8000/reset_password_player'
					send_mail(
    						'Reset Password',
    						message_to_send,
    						'obazarbachi@gmail.com',
    						['obazarbachi@gmail.com'],
    						fail_silently=False,
					)
					message = "email sent to: " + A.email
					form = ForgotForm()
					return render(request, 'Forgot-Password-Player.html', {'form': form, 'message':message})
		form = ForgotForm()
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Player.html', {'form': form,'message':message})
	form = ForgotForm()
	return render(request, 'Forgot-Password-Player.html', {'form': form})

def forgot_password_fan(request):
	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Fan.objects.all():
				if e.email==email:
					A=e
					message_to_send = 'Hello ' + A.username + ',\n\n Please use the link below to reset your email. \n\n http://localhost:8000/reset_password_fan'
					send_mail(
    						'Reset Password',
    						message_to_send,
    						'obazarbachi@gmail.com',
    						['obazarbachi@gmail.com'],
    						fail_silently=False,
					)
					message = "email sent to: " + A.email
					form = ForgotForm()
					return render(request, 'Forgot-Password-Fan.html', {'form': form, 'message':message})
		form = ForgotForm()
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Fan.html', {'form': form,'message':message})
	form = ForgotForm()
	return render(request, 'Forgot-Password-Fan.html', {'form': form})

def forgot_password_staff(request):
	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Staff.objects.all():
				if e.email==email:
					A=e
					message_to_send = 'Hello ' + A.username + ',\n\n Please use the link below to reset your email. \n\n http://localhost:8000/reset_password_staff'
					send_mail(
    						'Reset Password',
    						message_to_send,
    						'obazarbachi@gmail.com',
    						['obazarbachi@gmail.com'],
    						fail_silently=False,
					)
					message = "email sent to: " + A.email
					form = ForgotForm()
					return render(request, 'Forgot-Password-Staff.html', {'form': form, 'message':message})
		form = ForgotForm()
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Staff.html', {'form': form,'message':message})
	form = ForgotForm()
	return render(request, 'Forgot-Password-Staff.html', {'form': form})
		