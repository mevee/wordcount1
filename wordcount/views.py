from django.http import HttpResponse
from django.shortcuts import render




def home(request):
	return render(request,'home.html',{'hlo':'chhoiya jhai tu'})

def employess(request):
	return HttpResponse('all employees are')

def profile(request):
	return HttpResponse('Great profile')

def status(request):
	return HttpResponse('<h1>you are in status<h1>')
	