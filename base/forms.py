from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
	
	class Meta:
		model = CustomUser
		fields =['name','bio','profile_picture']



class CreateUserForm(forms.ModelForm):

	class Meta:
		model=CustomUser
		fields=['name','email','password']		
