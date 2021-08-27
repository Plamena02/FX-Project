from django.urls import path
from django.contrib import admin 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chart/', views.chart, name='chart')
]
    # path('admin/', admin.site.urls),
