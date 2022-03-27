from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CreatePlayerForm,CreateCourseForm,FindPlayerForm
from .models import Player,Course_Taken


def index(request):
	return render(request,'index.html')
def add_player(request):
	return render(request, 'Player-Login.html', {'form': form,'S':S})
def home(request):
	return render(request,'HOME.html')

def player_login(request):
	if request.method == 'POST':
		print("test")
		if request.POST.get('form_type')=='form':
			print("test1")
			form = CreatePlayerForm(request.POST)
			if form.is_valid():
				courseform = form.cleaned_data
				second = courseform['Player_name']
				third = courseform['password']
				forth = courseform['confirm_password']
				last = courseform['email']
				next_id = Player.objects.last().Player_id + 1
				Player.objects.create(Player_id=next_id,Player_name=second,password=third,confirm_password=forth,email=last)
			return render(request,'index.html')
		if request.POST.get('form_type') == 'form1':
			print("test2")
			form = findPlayerForm(request.POST)
			if form.is_valid():
				courseform = form.cleaned_data
				Player_name = courseform['Player_name']
				password = courseform['password']
				for e in Player.objects.all():
					if e.Player_name==Player_name and e.password==password:
						A=e
						return render(request, 'index.html', { 'form': form,'A':A})
			return render(request,'index.html', { 'form': form })
	form = CreatePlayerForm()
	form1 = FindPlayerForm()
	S = Player.objects.all()
	return render(request, 'Player-Login.html', {'form': form, 'form1': form1,'S':S})

		