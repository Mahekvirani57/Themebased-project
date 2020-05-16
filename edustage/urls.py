from django.urls import path

from . import views
urlpatterns = [
	path("",views.index,name="index"),
	path("finance",views.finance,name = "finance"),
	path("public",views.public,name = "public"),
	path("economics",views.economics,name = "economics"),
	path("writing",views.writing,name = "writing"),
	path("managment",views.managment,name = "managment"),
	path("marketing",views.marketing,name = "marketing"),
	
]
