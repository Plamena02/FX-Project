from .models import Forex_quotes
from flask import render_template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import sqlite3
import pandas as pd

# Create your views here.
def home (request): 

   conn = sqlite3.connect('db-forex.sqlite3')
   c = conn.cursor()

   variables = {
      "USD": [],
      "AUD": [],
      "CHF": [],
      "CAD": [],
      "EUR": [],
      "GBP": [],
      "JPY": []
   }

   queries = {
      "USD": [111, 2, 1034, 62, 61, 75],
      "CHF": [7, 14, 33, 10, 11, 12],
      "EUR": [52, 44, 4, 45, 47, 49],
      "GBP": [67, 1528, 6, 105, 72, 104],
   }

   for key in queries:
      for item in queries[key]:
         c.execute(f'SELECT rate FROM api_forex_quotes WHERE forex_id = {item} ORDER BY date DESC LIMIT 1')
         value = c.fetchone()
         variables[key].append(value[0])

   variables["AUD"].append(f'{1/variables["USD"][0]:0.6f}')
   variables["AUD"].append(f'{1/variables["CHF"][1]:0.6f}')
   variables["AUD"].append(round(variables["USD"][2]/variables["USD"][0], 6))
   variables["AUD"].append(f'{1/variables["EUR"][1]:0.6f}')
   variables["AUD"].append(f'{1/variables["GBP"][1]:0.6f}')
   variables["AUD"].append(round(variables["USD"][5]/variables["USD"][0],6)) 

   variables["CAD"].append(f'{1/variables["USD"][2]:0.6f}')
   variables["CAD"].append(f'{1/variables["AUD"][2]:0.6f}')
   variables["CAD"].append(f'{1/variables["CHF"][2]:0.6f}')
   variables["CAD"].append(f'{1/variables["EUR"][3]:0.6f}')
   variables["CAD"].append(f'{1/variables["GBP"][3]:0.6f}')
   variables["CAD"].append(round(variables["USD"][5]/variables["USD"][2],6))

   variables["JPY"].append(f'{1/variables["USD"][5]:0.6f}')
   variables["JPY"].append(f'{1/variables["AUD"][5]:0.6f}')
   variables["JPY"].append(f'{1/variables["CHF"][5]:0.6f}')
   variables["JPY"].append(f'{1/variables["CAD"][5]:0.6f}')   
   variables["JPY"].append(f'{1/variables["EUR"][5]:0.6f}')
   variables["JPY"].append(f'{1/variables["GBP"][5]:0.6f}')

   i = 0
   for key in variables:
      variables[key].insert(i, '')
      i += 1

   conn.close()
   
   return render(request, 'api/index.html', variables) 

def chart (request):

   conn = sqlite3.connect('db.sqlite3')
   c = conn.cursor()

   variables = {
      "dict":[]
      }

   c.execute('SELECT * FROM api_currency')
   query = c.fetchall()
   for item in query:
      variables["dict"].append([item[0], f'{item[2]} ({item[1]})', item[3]])
   # print(variables["dict"][0][1])

   conn.close()

   return render(request,'api/chart_page.html',variables)
