from asyncio import constants
from tokenize import ContStr
from unittest.mock import DEFAULT
from django.db import models
from  embed_video.fields  import  EmbedVideoField

# Create your models here.


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
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
    team1_logo = models.ImageField(null=True,blank=True,upload_to='matches')
    team2 = models.CharField(max_length=30)
    team2_logo = models.ImageField(null=True,blank=True,upload_to='matches')
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
    department_name = models.CharField(max_length=30)
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
    news_main = models.CharField(max_length=500)
    news_date = models.DateField(null=True)
    news_image = models.ImageField(null=True,blank=True,upload_to='news')
    news_number = models.IntegerField()

class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    item = models.CharField(max_length=30,unique=True)
    price = models.IntegerField()
    amount = models.IntegerField()

class Price(models.Model):
    id = models.IntegerField(primary_key=True)

class CreditCard(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    card_number = models.IntegerField()
    experation_date = models.CharField(max_length=5)
    CCV = models.IntegerField()

class Merchandise(models.Model):
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=30)
    price = models.IntegerField()
    news_image = models.ImageField(upload_to= 'merch')

class Purchases(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    item = models.CharField(max_length=30)
    price = models.IntegerField()
    amount = models.IntegerField()

class  Streaming(models.Model):
	streaming_title = models.CharField(max_length=200)
	streaming_body = models.TextField()
	streaming_video = EmbedVideoField()
	class  Meta:
		verbose_name_plural = "Streaming"
	def  __str__(self):
		return  str(self.streaming_title) if  self.streaming_title  else  " "

class Leagues(models.Model):
    id = models.IntegerField(primary_key=True)
    league_team1= models.CharField(max_length=100)
    league_team2= models.CharField(max_length=100)
    league_team3= models.CharField(max_length=100)
    league_team4= models.CharField(max_length=100)
    league_team5= models.CharField(max_length=100)
    league_t1_points=models.IntegerField()
    league_t2_points=models.IntegerField()
    league_t3_points=models.IntegerField()
    league_t4_points=models.IntegerField()
    league_t5_points=models.IntegerField()

