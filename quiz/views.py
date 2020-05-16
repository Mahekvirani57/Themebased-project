from django.shortcuts import render
from .models import Quiz
# Create your views here.

def quiz(request):
	
	dests = Quiz.objects.all()
	return render(request,'quiz.html',{'dests' : dests})
