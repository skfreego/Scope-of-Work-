from django.shortcuts import render
from django.http import HttpResponse
from num2words import num2words



def index(request):
    return render(request,'form.html')
# Create your views here.


def result(request):
    try:
        if 'nmb' in request.POST:
            numer = request.POST['nmb']
            result = num2words(numer)
        else:
            result = 'You have not entered any values please enter a value and comeback'
        return render(request,'display.html',{"result": result})
    except Exception as e:
        error_message = "Invalid request"
        return render(request,'form.html',{"invalid": error_message})