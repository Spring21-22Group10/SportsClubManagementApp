from tkinter import CENTER
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import CreateForm,FindForm,ForgotForm,ResetForm, ExpenseForm, ReportForm, GetPrice, CreditCardForm
from .models import Player, Fan, Staff, Match, Expenses, Revenue, News, Cart, Price, CreditCard, Merchandise, Purchases, Report, Streaming
from django.contrib import messages
from django.core.mail import send_mail
from django.http import FileResponse
from reportlab.platypus import Table, Frame, Paragraph, Spacer, SimpleDocTemplate, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import pandas as pd
from datetime import date, datetime
import pytz
import csv
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet


def index(request):
	request.session['user'] = None
	request.session['match'] = None
	request.session['buying'] = None
	Cart.objects.all().delete()
	return render(request,'index.html')

def home_main(request):
	return render(request,'HOME.html',)

def leagues(request):
	return render(request, 'leagues.html',)


def home_staff(request):
	return render(request,'HOME_Staff.html',)

def merch(request):
	merch = Merchandise.objects.all()
	user = request.session['user']
	return render(request,'Merchandise.html', { 'merch':merch, 'user':user})

def item(request,id):
	user = request.session['user']
	item = Merchandise.objects.all().filter(id=id).first()
	next_id = 1
	if(Cart.objects.all()):
		next_id = Cart.objects.last().id + 1
	if Cart.objects.all().filter(item=item.item_name).first() is None:
		Cart.objects.create(id=next_id,user_id=user,item = item.item_name, price = item.price, amount = 1)
	total = 0
	for e in Cart.objects.all().filter(user_id=int(user)):
		total += e.price*e.amount
	form = CreditCardForm()
	cart = Cart.objects.all().filter(user_id=int(user))
	return render(request,'buy.html',{'cart':cart , 'total':total, 'form':form })

def add(request,id):
	user = request.session['user']
	for e in Cart.objects.all():
				if e.user_id==user and e.id == id:
					e.amount += 1
					e.save()
	cart = Cart.objects.all().filter(user_id=int(user))
	return HttpResponseRedirect('buyA')

def remove(request,id):
	user = request.session['user']
	for e in Cart.objects.all():
				if e.user_id==user and e.id == id and e.amount !=0:
					e.amount -= 1
					e.save()
	cart = Cart.objects.all().filter(user_id=int(user))
	return HttpResponseRedirect('buyA')

def buyA(request):
	user = request.session['user']
	if request.method =='POST':
		form=CreditCardForm(request.POST)
		if form.is_valid():
			PurchaseForm = form.cleaned_data
			name = PurchaseForm['name']
			card_number = PurchaseForm['card_number']
			experation_date = PurchaseForm['experation_date']
			CCV = PurchaseForm['CCV']
			for e in Cart.objects.all().filter(user_id=int(user)):
				next_id = 1
				if(Purchases.objects.all()):
					next_id = Purchases.objects.last().id + 1
				Purchases.objects.create(id=next_id,user_id=user,item = e.item, price = e.price, amount = e.amount)
			form = CreditCardForm()
			message = "Reported expense successfully"
			cart = Cart.objects.all().filter(user_id=int(user))
			total = 0
			for e in Cart.objects.all().filter(user_id=int(user)):
				total += e.price*e.amount
			form = CreditCardForm()
			message = 'Purchase completed succesfuly'
			return render(request,'buy.html',{'cart':cart , 'total':total, 'form':form, 'message':message })
	cart = Cart.objects.all().filter(user_id=int(user))
	total = 0
	for e in Cart.objects.all().filter(user_id=int(user)):
		total += e.price*e.amount
	form = CreditCardForm()
	return render(request,'buy.html',{'cart':cart , 'total':total, 'form':form })

def buyB(request):
	return render(request,'HOME.html')

def buyC(request):
	return render(request,'HOME.html')

def news(request):
	news = News.objects.order_by('news_date').all()
	user = request.session['user']
	return render(request,'News.html',{ 'user':user, 'news':news})

def make_table(department, month):
	df1 = pd.DataFrame(Expenses.objects.all().values()) 
	df2 = pd.DataFrame(Revenue.objects.all().values())
	df1 = df1[df1["department_name"] == department] 
	df2 = df2[df2["department_name"] == department]
	df1 = df1[["expense_date","department_expense","expense_name"]]
	df1 = df1[df1["expense_date"].str.contains(month)]
	df1.rename(columns={"expense_name":"Expense Name", "department_expense":"Expense Amount","expense_date": "Expense Date"},inplace=True)
	total0 = int(df1["Expense Amount"].astype(int).sum(axis=0))
	df2_temp = df2[["merch_name", "merch_date","merch_price"]]
	df2_temp2 = df2[["ticket_name", "ticket_date","ticket_price"]]
	df2_temp = df2_temp[df2_temp["merch_date"].str.contains(month)]
	df2_temp2 = df2_temp2[df2_temp2["ticket_date"].str.contains(month)]
	total1 = int(df2_temp["merch_price"].astype(int).sum(axis=0))
	total2 = int(df2_temp2["ticket_price"].astype(int).sum(axis=0))
	df2 = pd.concat([df2_temp,df2_temp2],axis=1)
	df2.rename(columns={"merch_name":"Merch Name", "merch_price":"Merch Price","merch_date": "Merch Date","ticket_name":"Ticket Name", "ticket_price":"Ticket Price","ticket_date": "Ticket Date"},inplace=True)
	df = pd.concat([df1.reset_index(drop=True), df2.reset_index(drop=True)],axis=1)
	df.to_csv("report.csv",index=False)
	totalRevenue = total1 + total2
	totalExpenses = total0
	return {"OverallExpenses": totalExpenses,"OverallRevenue": totalRevenue}

def stream(request):
	stream = Streaming.objects.all()
	context = {
	'stream': stream,
	}
	return  render(request, 'stream.html', context)

def stream_detail(request,pk):
	stream = Streaming.objects.get(pk=pk)
	context = {
	'stream': stream,
	}
	return  render(request, 'stream_detail.html', context)		


def report(request):
	if request.method == 'POST':
		form = ReportForm(request.POST)
		if form.is_valid():
			reportForm = form.cleaned_data
			month = reportForm['Month']
			name = reportForm['Name']
			department = reportForm['Department']
			email = reportForm['Email']
			doc = SimpleDocTemplate(month + " report for " + department + ".pdf",pagesize=(1000,1000),
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
			Story=[]
			styles=getSampleStyleSheet()
			styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER, fontSize=20))
			ptext = month + " Report for " + department
			Story.append(Paragraph(ptext, styles["Center"]))
			Story.append(Spacer(60, 60))
			tz_BEY = pytz.timezone('Asia/Beirut') 
			datetime_BEY = datetime.now(tz_BEY)
			Date = date(day=datetime_BEY.day, month=datetime_BEY.month, year=datetime_BEY.year).strftime('%A %d %B %Y')
			styles=getSampleStyleSheet()
			styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY,fontSize=16))
			ptext = '%s' % Date
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext = 'Department of %s' % department
			Story.append(Paragraph(ptext, styles["Justify"]))         
			Story.append(Spacer(40, 40))
			ptext = 'This report comprises of the revenues and expenses for the department of %s:' % department
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(50, 50))
			info = make_table(department,month)
			totalExpenses = info["OverallExpenses"]
			totalRevenue = info["OverallRevenue"]
			with open('report.csv', "r") as csvfile:
				data = list(csv.reader(csvfile))
			all_cells = [(0, 0), (-1, -1)]
			header = [(0, 0), (-1, 0)]
			column0 = [(0, 0), (0, -1)]
			column1 = [(1, 0), (1, -1)]
			column2 = [(2, 0), (2, -1)]
			column3 = [(3, 0), (3, -1)]
			column4 = [(4, 0), (4, -1)]
			column5 = [(5, 0), (5, -1)]
			column6 = [(6, 0), (6, -1)]
			column7 = [(7, 0), (7, -1)]
			column8 = [(8, 0), (8, -1)]
			column9 = [(9, 0), (9, -1)]
			column10 = [(10, 0), (10, -1)]
			table_style = TableStyle([
				('VALIGN', all_cells[0], all_cells[1], 'TOP'),
				('LINEBELOW', header[0], header[1], 1, colors.black),
				('INNERGRID', (0,0), (-1,-1), 1, colors.black),
				('ALIGN', column0[0], column0[1], 'CENTER'),
				('ALIGN', column1[0], column1[1], 'CENTER'),
				('ALIGN', column2[0], column2[1], 'CENTER'),
				('ALIGN', column3[0], column3[1], 'CENTER'),
				('ALIGN', column4[0], column4[1], 'CENTER'),
				('ALIGN', column5[0], column5[1], 'CENTER'),
				('ALIGN', column6[0], column6[1], 'CENTER'),
				('ALIGN', column7[0], column7[1], 'CENTER'),
				('ALIGN', column8[0], column8[1], 'CENTER'),
				('ALIGN', column9[0], column9[1], 'CENTER'),
				('ALIGN', column10[0], column10[1], 'CENTER'),
				('fontSize', column0[0], column0[1], 14),
				('fontSize', column1[0], column1[1], 14),
				('fontSize', column2[0], column2[1], 14),
				('fontSize', column3[0], column3[1], 14),
				('fontSize', column4[0], column4[1], 14),
				('fontSize', column5[0], column5[1], 14),
				('fontSize', column6[0], column6[1], 14),
				('fontSize', column7[0], column7[1], 14),
				('fontSize', column8[0], column8[1], 14),
				('fontSize', column9[0], column9[1], 14),
				('fontSize', column10[0], column10[1], 14),
			])

			colWidths = [
				3.5 * cm,  # Column 0
				3.5 * cm,  # Column 1
				3.5 * cm,  # Column 2
				3.5 * cm,  # Column 3
				3.5 * cm,  # Column 4
				3.5 * cm,  # Column 5
				3.5 * cm,  # Column 6
				3.5 * cm,  # Column 7
				3.5 * cm,  # Column 8
				3.5 * cm,  # Column 9
				3.5 * cm,  # Column 10
			]
			t = Table(data, colWidths=colWidths)
			t.setStyle(table_style)
			Story.append(t)
			Story.append(Spacer(40, 40))
			ptext =  'Overall Revenue made: ' + str(totalRevenue)
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext =  'Overall Expenses cost: ' + str(totalExpenses)
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext =  'Calculated difference (profit): ' + str(totalRevenue - totalExpenses)
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext =  'This report was issued by %s' % name
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext =  'Email: %s' % email
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			doc.build(Story)
			next_id = 1
			if(Report.objects.all()):
				next_id = Report.objects.last().id + 1
			Report.objects.create(id=next_id,Month=month,Name=name,Department=department,Email = email)
			return FileResponse(open(month + " report for " + department + ".pdf", 'rb'), content_type='application/pdf',as_attachment=True)
	form = ReportForm()
	S = Report.objects.all()
	return render(request, 'Report.html', {'form': form,'S':S})


def record_expense(request):
	if request.method == 'POST':
		form = ExpenseForm(request.POST)
		if form.is_valid():
			expenseForm = form.cleaned_data
			department_expense = expenseForm['department_expense']
			department_name = expenseForm['department_name']
			expense_name = expenseForm['expense_name']
			expense_date = expenseForm['expense_date']
			next_id = 1
			if(Expenses.objects.all()):
				next_id = Expenses.objects.last().id + 1
			Expenses.objects.create(id=next_id,department_expense=department_expense,department_name=department_name,expense_name=expense_name,expense_date=expense_date)
			form = ExpenseForm()
			message = "Reported expense successfully"
			return render(request, 'Expenses.html', { 'form': form, "message": message })
	form = ExpenseForm()
	S = Expenses.objects.all()
	return render(request, 'Expenses.html', {'form': form,'S':S})

	
def home_staff(request):
	return render(request,'HOME_Staff.html')

def matches(request):
	user = request.session['user']
	today=date.today()
	today = datetime.strptime(str(today), '%Y-%m-%d')
	match = Match.objects.all().filter(date__range=[today, "3000-01-01"])
	return render(request,'Matches.html',{ 'user':user, 'match':match })

def past_matches(request):
	user = request.session['user']
	today=date.today()
	today = datetime.strptime(str(today), '%Y-%m-%d')
	#match = Match.objects.all().filter(date=today)
	match = Match.objects.all().filter(date__range=["1800-01-01", today])
	return render(request,'Past-Matches.html',{ 'user':user, 'match':match })

def tickets(request):
	user = request.session['user']
	if request.method == 'POST':
		form = GetPrice(request.POST)
		if form.is_valid():
			price = request.POST.get('price')
			if price is not None:
				next_id = 1
				if(Cart.objects.all()):
					next_id = Cart.objects.last().id + 1
				
				Cart.objects.all().filter(item='Tickets').filter(user_id=user).delete()
				Cart.objects.create(id=next_id,user_id=user,item = 'Tickets', price = price, amount = 1)
				cart = Cart.objects.all().filter(user_id=user)
				return HttpResponseRedirect('buyA')
	request.session['buying'] = True
	match = None
	if request.session['match'] is None:
		match = Match.objects.order_by('date').first()
		request.session['match'] = match.id
	else:
		match = Match.objects.get(id = request.session['match'])
	team1 = match.team1
	team1_logo = match.team1_logo
	team2 = match.team2
	team2_logo = match.team2_logo
	date = match.date
	Stadium = match.location
	priceA = match.priceA
	priceB = match.priceB
	priceC = match.priceC
	form = GetPrice()
	return render(request,'Tickets.html',{'form':form, 'user':user, 'team1':team1, 'team1_logo':team1_logo,'team2':team2, 'team2_logo':team2_logo,'date':date,'Stadium':Stadium, 'priceA':priceA,'priceB':priceB,'priceC':priceC })

def ticket(request,id):
	user = request.session['user']
	if request.method == 'POST':
		form = GetPrice(request.POST)
		if form.is_valid():
			price = request.POST.get('price')
			if price is not None:
				next_id = 1
				if(Cart.objects.all()):
					next_id = Cart.objects.last().id + 1
				
				Cart.objects.all().filter(item='Tickets').filter(user_id=user).delete()
				Cart.objects.create(id=next_id,user_id=user,item = 'Tickets', price = price, amount = 1)
				cart = Cart.objects.all().filter(user_id=user)
				return HttpResponseRedirect('buyA')
				return render(request,'buy.html',{'cart':cart , 'total':price })
	request.session['buying'] = True
	match = Match.objects.get(id = id)
	team1 = match.team1
	team1_logo = match.team1_logo
	team2 = match.team2
	team2_logo = match.team2_logo
	date = match.date
	Stadium = match.location
	priceA = match.priceA
	priceB = match.priceB
	priceC = match.priceC
	form = GetPrice()
	return render(request,'Tickets.html',{'form':form, 'user':user, 'team1':team1, 'team1_logo':team1_logo,'team2':team2, 'team2_logo':team2_logo,'date':date,'Stadium':Stadium, 'priceA':priceA,'priceB':priceB,'priceC':priceC })

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
					request.session['user'] = A.id
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
					request.session['user'] = A.id
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
					request.session['user'] = A.id
					if request.session['buying'] is not None:
						return HttpResponseRedirect('tickets')
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
					request.session['user'] = A.id
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
					request.session['user'] = A.id
					return render(request, 'HOME_Staff.html', { 'user': A.username })
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
		