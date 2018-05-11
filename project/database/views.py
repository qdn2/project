# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django import template
from django.template.loader import get_template 
from database.models import Z_Restaurant, Recipe
import random

###########################################################################################################################################################################################################################################
def search_restaurants(request):
    template = get_template('search.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

###########################################################################################################################################################################################################################################
def search_recipes(request):
    template = get_template('search2.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


###########################################################################################################################################################################################################################################
def results_restaurants(request):

	template = get_template('restaurant_results1.html')

	query = request.GET['q']
	exact_name= Z_Restaurant.objects.filter(r_name= query)
	r_id= None
	r_name= None
	food_type= None
	r_city= None
	r_address= None
	r_menu= None
	r_cost= None
	r_image= None
	r_rating= None
	template_num=0
	resultlis=[]
	rr_link=None


	if(exact_name):
		r_name=exact_name[0].r_name
		food_type=exact_name[0].food_type
		r_city=exact_name[0].r_city
		r_address=exact_name[0].r_address
		r_menu=exact_name[0].r_menu
		r_cost=exact_name[0].r_cost
		r_image=exact_name[0].r_image
		r_rating=exact_name[0].r_rating
		template_num=1


		word=food_type.split(",")
		rr_link='http://127.0.0.1:8000/database/results_recipes?q='+ 'special' + word[0]





		####
		##rr_list=None
		##list_of_cuisines=food_type.split(",")
		##for item in list_of_cuisines:
		##	if(Recipe.objects.filter(food_type__icontains= query)):
		##		rr_list=Recipe.objects.filter(food_type__icontains= query)
		##		break
		##if(not(rr_list)):
		##	random_recipes=Recipe.objects.all()
		##	upper_bound=len(random_recipes)
		##	number_lis=range(upper_bound)
		##	number=random.sample(number,5)

		##	counter=0
		##	for i in number:
		##		if(counter == 5):
		##			break
		##		rr_list.append(random_recipes[i])
		##		counter+=1
		####		
	

	elif(Z_Restaurant.objects.filter(food_type__icontains= query)):

		results=Z_Restaurant.objects.filter(food_type__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_restaurants?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'city':some_object.r_city,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2

	elif(Z_Restaurant.objects.filter(r_city__icontains= query)):
		results=Z_Restaurant.objects.filter(r_city__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_restaurants?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'city':some_object.r_city,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2	
	


	elif(Z_Restaurant.objects.filter(r_name__icontains= query)):
		results=Z_Restaurant.objects.filter(r_name__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+")
			name=name.replace("&", "%26") 
			link='http://127.0.0.1:8000/database/results_restaurants?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'city':some_object.r_city,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2		




	context = { 'r_name': r_name,'food_type': food_type, 'r_city':r_city, 'r_address':r_address, 'r_menu':r_menu, 'r_cost':r_cost,"r_image":r_image,'r_rating':r_rating , 'template_num':template_num, 'resultlis':resultlis,'rr_link':rr_link}
	return HttpResponse(template.render(context,request))



###########################################################################################################################################################################################################################################

def results_recipes(request):

	template = get_template('recipes_results1.html')

	query = request.GET['q']
	exact_name= Recipe.objects.filter(r_name= query)
	r_name= None
	food_type= None
	r_ingredients= None
	r_time= None
	r_image= None
	r_rating= None
	template_num=0
	resultlis=[]


	if(exact_name):
		r_name=exact_name[0].r_name
		food_type=exact_name[0].food_type
		r_ingredients=exact_name[0].r_ingredients
		r_ingredients=r_ingredients.replace('+',', ')


		r_time=exact_name[0].r_time
		r_image=exact_name[0].r_image
		r_rating=exact_name[0].r_rating
		template_num=1
	
	elif(Recipe.objects.filter(food_type__icontains= query)):

		results=Recipe.objects.filter(food_type__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_recipes?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2


	elif(Recipe.objects.filter(r_name__icontains= query)):

		results=Recipe.objects.filter(r_name__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_recipes?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2	


	elif(Recipe.objects.filter(r_ingredients__icontains= query)):

		results=Recipe.objects.filter(r_ingredients__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_recipes?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2	
	





	context = { 'r_name': r_name,'food_type': food_type,'r_ingredients':r_ingredients, 'r_time':r_time,"r_image":r_image,'r_rating':r_rating , 'template_num':template_num, 'resultlis':resultlis}
	return HttpResponse(template.render(context,request))



