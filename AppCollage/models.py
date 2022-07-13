from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CorceModel(models.Model):
    Course_Name=models.CharField(max_length=70)
    Course_Fees=models.IntegerField()

class TechrsModel(models.Model):
    Teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Course=models.ForeignKey(CorceModel,on_delete=models.CASCADE,null=True)
    Teacher_Address=models.CharField(max_length=200)
    Teacher_Gender=models.CharField(max_length=10)
    Teacher_Age=models.IntegerField()
    Teacher_Photo=models.ImageField(null=True,blank=True,upload_to='image/')

class StdntsModel(models.Model):
    Course=models.ForeignKey(CorceModel,on_delete=models.CASCADE,null=True)
    Std_Name=models.CharField(max_length=100)
    Std_Address=models.CharField(max_length=200)
    Std_Age=models.IntegerField()
    Join_Date=models.DateField(auto_now_add=True)