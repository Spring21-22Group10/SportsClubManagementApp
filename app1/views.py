from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CreatePlayerForm,FindPlayerForm,CreateFanForm,FindFanForm,FindStaffForm,ForgotPlayerForm,ForgotFanForm,ForgotStaffForm
from .models import Player,Fan, Staff
from django.contrib import messages


def index(request):
	return render(request,'index.html')

def home(request):
	return render(request,'HOME.html',)

def player_login(request):
	if request.method == 'POST':
		form = FindPlayerForm(request.POST)
		if form.is_valid():
			Playerform = form.cleaned_data
			Player_username = Playerform['Player_username']
			password = Playerform['password']
			for e in Player.objects.all():
				if e.Player_username==Player_username and e.password==password:
					A=e
					return render(request, 'HOME.html', { 'user': A.Player_username })
		form = FindPlayerForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Player-Login.html', {'form': form, 'message':message})
	form = FindPlayerForm()
	S = Player.objects.all()
	return render(request, 'Player-Login.html', {'form': form,'S':S})

def player_signup(request):
	if request.method == 'POST':
		form = CreatePlayerForm(request.POST)
		if form.is_valid():
			Playerform = form.cleaned_data
			Player_name = Playerform['Player_name']
			Player_username = Playerform['Player_username']
			password = Playerform['password']
			confirm_password = Playerform['confirm_password']
			email = Playerform['email']
			next_id = 1
			if(Player.objects.all()):
				next_id = Player.objects.last().Player_id + 1
			Player.objects.create(Player_id=next_id,Player_name=Player_name,Player_username=Player_username,password=password,confirm_password=confirm_password,email=email)
			for e in Player.objects.all():
				if e.Player_username==Player_username and e.password==password:
					A=e
					return render(request, 'HOME.html', { 'user': A.Player_username })
	form = CreatePlayerForm()
	S = Player.objects.all()
	return render(request, 'Player-Signup.html', {'form': form,'S':S})

def fan_login(request):
	if request.method == 'POST':
		form = FindFanForm(request.POST)
		if form.is_valid():
			Fanform = form.cleaned_data
			Fan_username = Fanform['Fan_username']
			password = Fanform['password']
			for e in Fan.objects.all():
				if e.Fan_username==Fan_username and e.password==password:
					A=e
					return render(request, 'HOME.html', { 'user': A.Fan_username })
		form = FindFanForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Fan-Login.html', {'form': form, 'message':message})
	form = FindFanForm()
	S = Fan.objects.all()
	return render(request, 'Fan-Login.html', {'form': form,'S':S})

def Fan_signup(request):
	if request.method == 'POST':
		form = CreateFanForm(request.POST)
		if form.is_valid():
			Fanform = form.cleaned_data
			Fan_name = Fanform['Fan_name']
			Fan_username = Fanform['Fan_username']
			password = Fanform['password']
			confirm_password = Fanform['confirm_password']
			email = Fanform['email']
			next_id = 1
			if(Fan.objects.all()):
				next_id = Player.objects.last().Fan_id + 1
			Fan.objects.create(Fan_id=next_id,Fan_name=Fan_name,Fan_username=Fan_username,password=password,confirm_password=confirm_password,email=email)
			for e in Fan.objects.all():
				if e.Fan_username==Fan_username and e.password==password:
					A=e
					return render(request, 'HOME.html', { 'user': A.Fan_username })
	form = CreateFanForm()
	S = Fan.objects.all()
	return render(request, 'Fan-Signup.html', {'form': form,'S':S})

def staff_login(request):
	if request.method == 'POST':
		form = FindStaffForm(request.POST)
		if form.is_valid():
			Staffform = form.cleaned_data
			Staff_username = Staffform['Staff_username']
			password = Staffform['password']
			for e in Staff.objects.all():
				print("test")
				if e.Staff_username==Staff_username and e.password==password:
					A=e
					return render(request, 'HOME.html', { 'user': A.Staff_username })
		form = FindStaffForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Staff-Login.html', {'form': form,'message':message})
	form = FindStaffForm()
	S = Staff.objects.all()
	return render(request, 'Staff-Login.html', {'form': form,'S':S})

def forgot_password_player(request):
	if request.method == 'POST':
		form = ForgotPlayerForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Player.objects.all():
				if e.email==email:
					A=e
					message = "email sent to : " + A.email
					form = ForgotPlayerForm()
					return render(request, 'Forgot-Password-Player.html', {'form': form, 'message':message})
		form = ForgotPlayerForm()
		print("test2")
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Player.html', {'form': form,'message':message})
	form = ForgotPlayerForm()
	return render(request, 'Forgot-Password-Player.html', {'form': form})

def forgot_password_fan(request):
	if request.method == 'POST':
		form = ForgotFanForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Fan.objects.all():
				if e.email==email:
					A=e
					message = "email sent to : " + A.email
					form = ForgotFanForm()
					return render(request, 'Forgot-Password-Fan.html', {'form': form, 'message':message})
		form = ForgotFanForm()
		print("test2")
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Fan.html', {'form': form,'message':message})
	form = ForgotFanForm()
	return render(request, 'Forgot-Password-Fan.html', {'form': form})

def forgot_password_staff(request):
	if request.method == 'POST':
		form = ForgotStaffForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Staff.objects.all():
				if e.email==email:
					A=e
					message = "email sent to : " + A.email
					form = ForgotStaffForm()
					return render(request, 'Forgot-Password-Staff.html', {'form': form, 'message':message})
		form = ForgotStaffForm()
		print("test2")
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Staff.html', {'form': form,'message':message})
	form = ForgotStaffForm()
	return render(request, 'Forgot-Password-Staff.html', {'form': form})



		