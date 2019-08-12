"""first_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pages import views

urlpatterns = [

    path('match/', views.match),
    path('cube/<int:num>/', views.cube),
    path('lotto/', views.lotto),
    path('home/', views.home),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]

# @app.route('/cube/<num>/')
# def cube(num)
    # 끝에 있는 데 / 붙이는 게 장고의 컨벤션