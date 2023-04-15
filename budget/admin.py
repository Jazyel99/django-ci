from django.contrib import admin

from budget.models import Category, Expense, Project

admin.site.register(Project)
admin.site.register(Expense)
admin.site.register(Category)
