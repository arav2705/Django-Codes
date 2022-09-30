from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the ICOPE Screening Tool HomePage for Geri Care Hospital ")

def about(request):
    return HttpResponse("This is a software engineering project developed by Team Pythons.")
    
def paths(request):
    context = {
        'heading' : " ICOPE Screening Tool ",
        'content'   : " This is a web based application to be used by the elderly so they may be assessed through various criteria according to the ICOPE screening standards"
    }