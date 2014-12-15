from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *


class StudiesView(generic.ListView):
    template_name = 'AssistMe/studies.html'
    context_object_name = "studies"

    def get_queryset(self):
        """
        Returns the 27 Studies
        can be accessed with study_list in templates
        """
        return Study.objects.all()


#The DetailView generic view expects the primary key value
#captured from the URL to be called 'pk'

class DisciplinesView(generic.DetailView):
	model = Study
	template_name = 'AssistMe/disciplines.html'

class MajorsView(generic.DetailView):
	model = Discipline
	template_name = 'AssistMe/majors.html'

class ArticulationsView(generic.DetailView):
	model = Major
	template_name = 'AssistMe/articulations.html'

def animateView(request):
    context = {}
    return render(request, 'AssistMe/animations.html', context) 



