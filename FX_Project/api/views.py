from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# Create your views here.
def main(request):
    return HttpResponse("Hello")
