"""shoppy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.productView, name = '/'),
    path('api/products/',views.ProductApiView.as_view()),
    path('api/products/create/',views.ProductCreateApiView.as_view()),
    path('api/products/delete/<int:id>',views.ProductDeleteApiView.as_view()),
    path('api/category/',views.CategoryApiView.as_view()),
    path('api/category/create/',views.CategoryCreateApiView.as_view()),
    path('api/category/delete/<int:id>',views.CategoryDeleteApiView.as_view()),
    path('api/cards/',views.CardApiView.as_view()),
    path('api/cards/create/',views.CardCreateApiView.as_view()),
    path('api/cards/delete/<int:id>',views.CardDeleteApiView.as_view()),
]