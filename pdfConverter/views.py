from django.shortcuts import render
from django_xhtml2pdf.utils import generate_pdf
from django.http import HttpResponse
from forms.models import Form

# Create your views here.

def myview(response):
 resp = HttpResponse(content_type='application/pdf')
 result = generate_pdf('webpages/resume1.html',file_object=resp)
 return result

def myview2(response):
 resp = HttpResponse(content_type='application/pdf')
 result = generate_pdf('webpages/resume2.html', file_object=resp)
 return result

