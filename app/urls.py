from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('chi/', views.chi),
    path('kor/', views.kor),
    path('bun/', views.bun),
    path('wes/', views.wes),
    path('caf/', views.caf),
    path('jap/', views.jap),
    path('json/', views.data_list),
    

]