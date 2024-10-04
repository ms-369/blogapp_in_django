from django.contrib import admin
from django.urls import path
from.views import homepage, newblog, readblog

urlpatterns = [
    path('', homepage, name='homepage'),
    path('new/', newblog, name='addnewblog'),
    path('readblog/<str:key>/', readblog, name='readblog'),

]
