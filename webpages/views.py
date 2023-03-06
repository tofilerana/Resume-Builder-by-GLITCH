from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from forms.models import Form 


# Create your views here.

def index(request):
 return render (request,'webpages/index.html')





def detailedView(request,id):
 data=Form.objects.filter(id=id)
 form={
  'form':data
 }
 return render (request,'webpages/detailedView.html',form)

def click(request,id):
 data=Form.objects.filter(id=id)
 form={
  'form':data
 }
 return render (request,'webpages/resume1.html',form)

# def click2(request,id):
#  data=Form.objects.filter(id=id)
#  form={
#   'form':data
#  }
#  return render (request,'webpages/template2.html',form)