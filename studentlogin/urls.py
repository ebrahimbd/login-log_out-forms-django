from django.contrib import admin
from django.urls import path
from userinfo import views as a

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', a.home, name='home'),
    #  path('products/', a.products, name='products'),
  

    path('catlogin', a.catlogin, name='catlogin'),
    path('catvai', a.catvai, name='catvai'),
    path('login/', a.catlogin, name="login"),  
	path('logout/', a.logoutUser, name="logout"),
	# path('userinfo', a.userinfo, name="userinfo"),


]
