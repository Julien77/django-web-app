from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Advert
from datetime import date
# Create your views here.

def listings(request):
	#get adverts
	adverts = Advert.objects.all()
	bands = Band.objects.all()
	return render(request, 'listings.html', context={
		'adverts':adverts,
		'bands':bands,
		})

def contact_us(request):
	return render(request, 'contact-us.html')


def hello(request):
	bands = Band.objects.all()
	return render(request, 'hello.html', context={
		'bands':bands,
		'date': date.today()
		})
