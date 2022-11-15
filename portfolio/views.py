from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def contactme(request):
    if request.method == "GET":
        return render(request, 'portfolio/contactme.html')
    else:
        try:
            subject=request.POST.get('subject')
            msg=request.POST.get('mailid')
            #send_mail('Subject here','Here is the message.','from@example.com',['to@example.com'],fail_silently=False,)
            return render(request, 'portfolio/contactme.html',{'datashow':"Details submitted. You shall be contacted soon."})
        except ValueError:
                return render(request,'portfolio/contactme.html',{'datashow':"Bad data passed in. Try Again"})
