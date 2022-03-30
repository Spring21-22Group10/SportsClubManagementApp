from django.db import models

# Create your models here.


class Player(models.Model):
    Player_id= models.IntegerField(primary_key=True)
    Player_name = models.CharField(max_length=30)
    Player_username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Player2(models.Model):
    Player_username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)

class Fan(models.Model):
    Fan_id= models.IntegerField(primary_key=True)
    Fan_name = models.CharField(max_length=30)
    Fan_username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Fan2(models.Model):
    Fan_username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)

class Staff(models.Model):
    Staff_username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)