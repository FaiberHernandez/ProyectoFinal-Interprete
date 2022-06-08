from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Interprete.static.Interprete.py import principal


# Create your views here.
def home(request):
    return render(request, 'vistaInterprete.html')

def validar(request):
    if(request.method == 'GET'):
        return JsonResponse({ "resultado": principal.validar(request.GET['codigo']) })
    else:
        return HttpResponse("holi pvto")

def ejecutar(request):
    if(request.method == 'GET'):
        return JsonResponse({ "resultado": principal.ejecutar(request.GET['codigo']) })
    else:
        return HttpResponse("holi pvto")