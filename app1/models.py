from asyncio import constants
from tokenize import ContStr
from django.db import models

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
    score = models.CharField(max_length=30)

class Expenses(models.Model):
    id = models.IntegerField(primary_key=True)
    department_expense = models.CharField(max_length=30)
    department_name = models.CharField(max_length=30)
    expense_name = models.CharField(max_length=30)
    expense_date = models.CharField(max_length=30)


class Revenue(models.Model):
    id = models.IntegerField(primary_key=True)
    merch_name = models.CharField(max_length=30)
    merch_date = models.CharField(max_length=30)
    merch_price = models.CharField(max_length=30)
    ticket_name = models.CharField(max_length=30)
    ticket_date = models.CharField(max_length=30)
    ticket_price = models.CharField(max_length=30)

choicesMonth = [
    ('January', 'January'),
    ('February',"Fenruary"),
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
    Revenue= models.BooleanField(max_length=30)
    Expenses = models.BooleanField(max_length=30)
    Customer_Purchases = models.BooleanField(max_length=30)
    Development_Cost = models.BooleanField(max_length=30)
    Calculated_Difference = models.BooleanField(max_length=30)

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



