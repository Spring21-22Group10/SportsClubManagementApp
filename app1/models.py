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
