from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import  *



@login_required(login_url='login') 
def home(request):

 return render(request, 'main/eb.html')

 
def catvai(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = catname()
		if request.method == 'POST':
			form = catname(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('home')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

 
def logoutUser(request):
	logout(request)
	return redirect('login')








def catlogin(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			
			last_name =request.POST.get('last_name')
			 


			user = authenticate(request, username=username, password=password ) 

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/catlogin.html', context)



@login_required(login_url='login') 
def  hotel_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('f')
	else:
		form = HotelForm()
	return render(request, 'hotel_image_form.html', {'form' : form})

 


@login_required(login_url='login') 
def displayimages(request):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
        return render(request, 'display_hotel_images.html',
                     {'hotel_images' : Hotels})




@login_required(login_url='login') 
def bookvai(request):
	 
		form = AuthorForm()
		if request.method == 'POST':
			form = AuthorForm(request.POST)
			if form.is_valid():
				form.save()
				# user = form.cleaned_data.get('username')
				# messages.success(request, 'Account was created for ' + user)

				return redirect('sem')
			

		context = {'form':form}
		return render(request, 'main/catbook.html', context)





@login_required(login_url='login') 
def sem(request):
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        book = Author.objects.all()
        return render(request, 'main/eb.html', {'Author' : book})
  
  


















# def catlogin(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	# else:
# 	# 	if request.method == 'POST':
# 	# 		username = request.POST.get('username')
# 	# 		password =request.POST.get('password')

# 	# 		user = authenticate(request, username=username, password=password)

# 	# 		if user is not None:
# 	# 			login(request, user)
# 	# 			return redirect('home')
# 	# 		else:
# 	# 			messages.info(request, 'Username OR password is incorrect')
       
# 	objt=catname() 
# 	context = { 'form':objt }
# 	return render(request, 'main/catlogin.html', context)



# @login_required(login_url='login') 
# def userinfo(request):
# 	username = request.POST('username')
# 	password =request.POST('password')

# 	Savedata = Savedata( username= user.username, password= user.password)
# 	Savedata.save()
# 	return render(request, 'main/eb.html', { 'username' : username, 'password': password } )


