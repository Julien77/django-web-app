from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
# Create your views here.

def listings(request):
	body = """<h1>Listings</h1>
	<ul>
		<li>Mon premier article</li>
		<li>Mon second article</li>
	</ul>
	"""
	return HttpResponse(body)

def contact_us(request):
	body = """<h1>Contact form</h1>
	<p>Don't hesitate to contact us</p>
	"""
	return HttpResponse(body)


def hello(request):
	bands = Band.objects.all()
	body = "<table>"
	body += "<tr><th>ID</th><th>Name</th></tr>"
	for band in bands:
		body += "<tr>"
		body += "<td>" + str(band.id) + "</td>"
		body += "<td>" + str(band.name) + "</td>"
		body += "<tr>"
	body += "</table>"
	return HttpResponse(body)
