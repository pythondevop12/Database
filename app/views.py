from django.shortcuts import render
from .models import Mydb

def home(request):
 data = Mydb.objects.all()
 return render(request, 'index.html', {'data':data})
