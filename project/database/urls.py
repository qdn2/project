from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'search_restaurants', views.search_restaurants, name='search_restaurants'),
    url(r'results_restaurants', views.results_restaurants, name='results_restaurants'),
    url(r'search_recipes', views.search_recipes, name='search_recipes'),
    url(r'results_recipes', views.results_recipes, name='results_recipes')
]