from django.shortcuts import render

# Create your views here.

def Observed_Variable_View(request):
    return render(request, 'Observed_Variable.html')
