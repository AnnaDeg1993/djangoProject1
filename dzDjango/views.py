from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from dzDjango.models import ModelAnna


def nad(request):
    return render(request, 'anna.html')


@csrf_exempt
def koko(request):
    anna = ModelAnna()
    if request.method == 'POST':
        anna.pole = 'Hello world'
        anna.email = request.POST['email']
        anna.password = request.POST['password']
        anna.save()
        return HttpResponse('Email'+' '+anna.email+' '+"успешно зарегистрирован!")
    return render(request, 'anna.html', {'name': anna.email})

