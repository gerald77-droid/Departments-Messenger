from django.db import models
from django.contrib.auth.models import  AbstractUser





from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
	name=models.CharField(max_length=20,unique=True)
	bio=models.TextField(max_length=255, unique=True, null=True)
	profile_picture=models.ImageField(upload_to='images/',null=True,default='images/avatar.svg')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)


	def  __str__(self):
		return self.name
	
class UserProfile(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user_profile')
	bio=models.TextField(max_length=255, unique=True, null=True)
	profile_picture=models.ImageField(upload_to='images/',null=True,default='images/avatar.svg')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
 

	def	__str__(self):
		return self.user.name

	
class Role(models.Model):
	name=models.CharField(max_length=100)

	def	__str__(self):
		return self.name



class Department(models.Model):
	dept_leader=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	role=models.ForeignKey(Role, on_delete=models.CASCADE)
	members=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members',blank=True)
	description=models.TextField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name
	

class Message(models.Model):
	Title=models.CharField(max_length=20)
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
	department=models.ForeignKey(Department,on_delete=models.CASCADE)
	content=models.TextField(max_length=400)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)	

	def  __str__(self):
		return self.Title
	


