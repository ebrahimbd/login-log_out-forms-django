from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


 
class catname(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'last_name' ]



class HotelForm(forms.ModelForm):

	class Meta:
		model = Hotel
		fields = ['name', 'hotel_Main_Img']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
 