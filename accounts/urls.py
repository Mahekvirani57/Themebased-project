from django.urls import path

from . import views
urlpatterns = [
	path("register",views.register,name ="register"),
	path("finance",views.finance,name = "finance"),
	path("login",views.login,name="login"),
	path("logout",views.logout,name="logout"),
	path("about",views.about,name="about"),
	path("home",views.home,name="home"),
	path("contact",views.contact,name="contact"),
	
]
