from django.db import models

# Create your models here.

class User(models.Model):
	user_name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	
	
class Administrator(models.Model):
	user = models.ForeignKey(User)

class Applicant(models.Model):
	user = models.ForeignKey(User)
	
class Bidder(models.Model):
	user = models.ForeignKey(User)
	
class Revisor(models.Model):
	user = models.ForeignKey(User)
	
class Offer(models.Model):
	bidder = models.ForeignKey(Bidder)
	revisor = models.ManyToManyField(Revisor)
	
class Application(models.Model):
	applicant = models.ForeignKey(Applicant)
	offer = models.ForeignKey(Offer)
		
class Tag(models.Model):
	tag_name = models.CharField(max_length=200)
	tag_description = models.CharField(max_length=200)
	

class Item(models.Model):
	tag = models.ForeignKey(Tag) 
	item_name = models.CharField(max_length=200)
	item_description = models.CharField(max_length=200)
	file = models.FileField(upload_to='files/') 
