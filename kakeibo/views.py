from django.shortcuts import render
from .models import Expense

def index(request):
    expenses = Expense.objects.all()
    return render(request, 'kakeibo/index.html', {'expenses': expenses})
