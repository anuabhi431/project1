from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    res=HttpResponse("""<html><body bgcolor=orange><h1><center> WELCOME TO ANURVESH PROJECT</center></h1></body></html>""")
    return res
