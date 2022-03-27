from django.db import models

# Create your models here.


class Player(models.Model):
    Player_id= models.IntegerField(primary_key=True)
    Player_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)


class Course_Taken(models.Model):
    Player_id=models.ForeignKey(Player,on_delete=models.CASCADE)
    Course_id= models.IntegerField()
    Semester=models.CharField(max_length=100)
    Number_of_credits= models.IntegerField()
    Grade = models.IntegerField()

class Player2(models.Model):
    Player_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
