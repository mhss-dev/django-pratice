from django.shortcuts import render
from .models import myCourses
from django.template import loader
from django.http import HttpResponse
from .formCourses import formulaireCourses
# Create your views here.

def afficherCours(request):
    cours=myCourses.objects.all().values()
    template=loader.get_template("cours.html")
    context={"cours":cours}
    return HttpResponse(template.render(context,request))

def saveCours(request): 
    if request.method == 'POST':
        form = formulaireCourses(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('save successfully')
    else:
        form = formulaireCourses()

    template = loader.get_template('formulaireCours.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
