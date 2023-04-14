from django.shortcuts import render

from budget.models import Project

def project_list(request):
  project_list = Project.objects.all()
  return render(request, 'budget/project-list.html', {'project_list': project_list})
