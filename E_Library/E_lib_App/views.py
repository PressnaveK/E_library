from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
def functioncall(request,a,b):
    dict = {
        "name": a,
        "age" : b

    }
    return JsonResponse(dict)

