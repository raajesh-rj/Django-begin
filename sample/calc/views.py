from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def add(request):
    val1 = eval(request.POST['num1'])
    val2 = eval(request.POST['num2'])
    
    return render(request,'result.html',{'numbers':[val1,val2],'res':val1+val2})


def home(request):
    context = {
        'name': 'KOK'
    }

    return render(request,'home.html', context)