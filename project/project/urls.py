"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView





## The following code is to direct url's to the correct html page note the following
## http://127.0.0.1:8000/home_page takes you to the home page of the web application
##	http://127.0.0.1:8000/database/search_restaurants takes you to the restaurants search engine
##	http://127.0.0.1:8000/database/search_recipes takes you to the recipes search engine


urlpatterns = [
	url(r'home_page', TemplateView.as_view(template_name='home_page.html'), name='home_page'),
    url(r'^database/', include('database.urls')),
    url(r'^admin/', admin.site.urls),
]
