import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from budget.forms import ExpenseForm

from budget.models import Category, Expense, Project

def project_list(request):
  project_list = Project.objects.all()
  return render(request, 'budget/project-list.html', {'project_list': project_list})

def project_detail(request, project_slug):
  project = get_object_or_404(Project, slug=project_slug)
  
  if request.method == 'GET':
    category_list = Category.objects.filter(project=project)
    return render(
      request,
      'budget/project-detail.html',
      {
        'project': project, 
        'expense_list': project.expenses.all(),
        'category_list': category_list
      }
    )
  
  elif request == 'POST':
    form = ExpenseForm(request.POST)
    
    if form.is_valid():
      title = form.cleaned_data['title']
      amount = form.cleaned_data['amount']
      category_name = form.cleaned_data['category']
      
      category = get_object_or_404(Category, project=project, name=category_name)
      
      Expense.objects.create(
        project=project,
        title=title,
        amount=amount,
        category=category
      )
  
  elif request.method == 'DELETE':
    id = json.loads(request.body)['id']
    expense = Expense.objects.get(id=id)
    expense.delete
    
    return HttpResponse(status=204)
  
  return redirect(project)
