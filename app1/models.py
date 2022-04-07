from asyncio import constants
from tokenize import ContStr
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.


class Player(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    email = models.CharField(max_length=30,unique=True)

class Find(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)

class Fan(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30,unique=True)

class Forgot(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=30,unique=True)

class Reset(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=30,unique=True)
    new_password = models.CharField(max_length=30)
    confirm_new_password = models.CharField(max_length=30)

class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateField()
    priceA = models.IntegerField()
    priceB = models.IntegerField()
    priceC = models.IntegerField()

class Expenses(models.Model):
    id = models.IntegerField(primary_key=True)
    department_expense = models.CharField(max_length=30)
    department_name = models.CharField(max_length=30)
    expense_name = models.CharField(max_length=30)
    expense_date = models.CharField(max_length=30)


class Revenue(models.Model):
    id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30,default="hi")
    merch_name = models.CharField(max_length=30)
    merch_date = models.CharField(max_length=30)
    merch_price = models.CharField(max_length=30)
    ticket_name = models.CharField(max_length=30)
    ticket_date = models.CharField(max_length=30)
    ticket_price = models.CharField(max_length=30)

choicesMonth = [
    ('January', 'January'),
    ('February',"February"),
    ('March',"March"),
    ('April',"April"),
    ('May',"May"),
    ('June',"June"),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December')
]



class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    Month = models.CharField(max_length=30,choices= choicesMonth)
    Name = models.CharField(max_length=30)
    Department = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    
class News(models.Model):
    id = models.IntegerField(primary_key=True)
    news_title = models.CharField(max_length=100)
    news_main= models.CharField(max_length=500)
    news_date = models.DateField(null=True)
    news_image = models.ImageField(upload_to= 'news')
    news_number=models.IntegerField()