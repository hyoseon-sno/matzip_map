"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from app import views


urlpatterns = [
    path("main/", views.main),
    path("category_data/", views.category_data),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('article/write/', views.write),
    path('article/list/', views.list),
    path('article/detail/<int:id>/', views.detail),
    path('article/update/<int:id>/', views.update),
    path('article/delete/<int:id>/', views.delete),
    path('contact/', views.contact),
    path('page/', views.page),


    path('insert/', views.insert),
    path('index1/', views.main),
    path('map/', include('app.urls')),
]
