from django.shortcuts import render
from .models import Destination

def index(request):
	
	dests = Destination.objects.all()
	return render(request,'index.html',{'dests' : dests})

# Create your views here.
 		
def finance(request):
	return render(request,'finance.html')
def managment(request):
	return render(request,'managment.html')
def public(request):
	return render(request,'public.html')
def economics(request):
	return render(request,'economics.html')
def writing(request):
	return render(request,'writing.html')
def marketing(request):
	return render(request,'marketing.html')

	