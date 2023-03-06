from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Form
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def form(request):
 if request.method=='POST':
  first_name=request.POST['firstname']
  last_name=request.POST['lastname']
  objective=request.POST['objective']
  projects=request.POST['projects']
  skills=request.POST['skills']
  location=request.POST['location']
  regards=request.POST['regards']
  resumeTemplate=request.POST['resumes']
  userId=request.POST['userId']
  formData=Form(userId=userId,first_name=first_name,last_name=last_name,objective=objective,projects=projects,skills=skills,location=location,regards=regards,tempdata=resumeTemplate)
  formData.save()
  messages.success(request,'Successfully submitted')
  
 return render(request,'webpages/form.html')


# @login_required()
def dashboard(request,id):
 data=Form.objects.all()
 form={
  'form':data
 }
 return render (request,'webpages/dashboard.html',form)

def formUpdate(request,id):
 formData=Form.objects.get(id=id)
 return render (request,'webpages/formUpdate.html',{"Form":formData})

def requpdate(request, id):
    if request.method == "POST":
        if request.POST.get('userId') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('objective') and request.POST.get('projects') and request.POST.get('skills') and request.POST.get('location') and request.POST.get('tempdata') and request.POST.get:

            updatereq = Form.objects.get(id=id)
            updatereq.first_name = request.POST.get('first_name')
            updatereq.last_name = request.POST.get('last_name')
            updatereq.objective = request.POST.get('objective')
            updatereq.projects = request.POST.get('projects')
            updatereq.skills = request.POST.get('skills')
            updatereq.location = request.POST.get('location')
            updatereq.tempdata = request.POST.get('tempdata')
            updatereq.save()
            messages.success(request, "The Record ** " +
                             updatereq.name+" ** is saved successfully!!!")
            # return render(request, "criminal.html")
            results = Form.objects.all()
            return render(request, "webpages/dashboard.html", {"Form": results})
    else:
        return render(request, "webpages/dashboard.html")

def delData(request, id):
    data = Form.objects.get(id=id)
    data.delete()
    results = Form.objects.all()
    return render(request, "webpages/form.html", {"Form": results})