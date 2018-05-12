# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django import template
from django.template.loader import get_template 
from database.models import Z_Restaurant, Recipe
import random

###########################################################################################################################################################################################################################################

## The following function setups the user forum to get input to search over the restaurant database. After the User clicks the search button user's search query is sent to the results_restaurants function
## which then preforms the actual query over the database. This function is here to setup the html template to have users enter in text input to search restaurants


def search_restaurants(request):
    template = get_template('search.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

###########################################################################################################################################################################################################################################

## The following function setups the user forum to get input to search over the recipe database. After the User clicks the search button user's search query is sent to the results_recipes function
## which then preforms the actual query over the database. This function is here to setup the html template to have users enter in text input to search recipes


def search_recipes(request):
    template = get_template('search2.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


###########################################################################################################################################################################################################################################

## The following function preforms query over restaurant database, it first looks to see if the input matches an exact restaurant name, if no results are found then the function checks if the user
## input is a cuisine type and if this is the case and there are restaurants with this cuisine type then the function returns a list of restaurants with this specific cuisine type. If no results are found
## from the cuisine type then we check if the user input is a city and if so we will return the restaurants that have the particular city (user input) set as their location. Finally if this does not
## yeild any results we check if the user input is a substring of the restaurant name and if so return all restaurants that have this substring as part of their restaurant name 



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



## If we have exact match meaning user put in the exact name of the restaurant then we must also provide the special recipe url which will take this restaurants cuisine type and then find all 
## recipes that match this restaurants cuisine type. Note the http link is connected to the click here for recommendations link on the bottom of a restaurant page that was found through the search
## engine

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

	
## check if query is a cuisine type
	elif(Z_Restaurant.objects.filter(food_type__icontains= query)):

		results=Z_Restaurant.objects.filter(food_type__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_restaurants?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'city':some_object.r_city,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2

## check if query is a location type
	elif(Z_Restaurant.objects.filter(r_city__icontains= query)):
		results=Z_Restaurant.objects.filter(r_city__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_restaurants?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'city':some_object.r_city,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2	
	

## check if query is a substring in restaurant name type
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

## The following function takes the search query of user input for finding recipes and first checks if the query is the special query meaning that this query is the one where the user
## clicked on a restaurant's page recommendation feature and so we check if the keyword special is in the query and if so we parse that word out and get the cuisine type which is attached to this specific
## query and then look for matching recipes that have this cusine type. If we do not have a special query then we check if the user input is an exact name of a recipe in the database and if so we redirect the user
## to a recipe detail page that has basic information of a specific recipe which includes: name, rating, time to cook in minutes and ingredients. If the user input is not an exact name we check if the user input is
## a cuisine type and if so we return a list of recipes that match the specific input cuisine type. If the user input is not a cuisine type then we check if the user input is a substring of a recipe name and if matches are
## found we return the list of recipe. If the user input is an ingredient type then we return all recipes that have the follow user input ingredient


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


	## check if query is special type and if so find all matching recipes with the specific restaurant cuisine type that is attached with the word special in the query
	if(query.find('special') == 0):
		query=query.replace("special","")
		####
		rr_list=None
		if(Recipe.objects.filter(food_type__icontains= query)):
			
			results=Recipe.objects.filter(food_type__icontains= query)
			
			for some_object in results:
				name=some_object.r_name.replace(" ", "+") 
				name=name.replace("&", "%26")
				link='http://127.0.0.1:8000/database/results_recipes?q=' + name
				info= {'image':some_object.r_image,'name':some_object.r_name,'food_type':some_object.food_type, 'link':link}
				resultlis.append(info)
			
			template_num=2

		## If no recipes match the specific restaurant reccomendation cusisine then by default we return a random list of five recipes that change everytime but still provide a forum of reccomendation even though the user's restaurant recommendation cuisine is not in the recipe database 	
		else:
			rr_list=[]	
			random_recipes=Recipe.objects.all()
			upper_bound=len(random_recipes)
			number_lis=range(upper_bound)
			some_numbers=random.sample(number_lis,5)

			counter=0
			for i in some_numbers:
				if(counter == 5):
					break
				rr_list.append(random_recipes[i])
				counter+=1

			for some_object in rr_list:
				name=some_object.r_name.replace(" ", "+") 
				name=name.replace("&", "%26")
				link='http://127.0.0.1:8000/database/results_recipes?q=' + name
				info= {'image':some_object.r_image,'name':some_object.r_name,'food_type':some_object.food_type, 'link':link}
				resultlis.append(info)
			
			template_num=2	
			

## check if query is exact recipe name
	elif(exact_name):
		r_name=exact_name[0].r_name
		food_type=exact_name[0].food_type
		r_ingredients=exact_name[0].r_ingredients
		r_ingredients=r_ingredients.replace('+',', ')


		r_time=exact_name[0].r_time
		r_image=exact_name[0].r_image
		r_rating=exact_name[0].r_rating
		template_num=1
## check if query is cuisine type	
	elif(Recipe.objects.filter(food_type__icontains= query)):

		results=Recipe.objects.filter(food_type__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_recipes?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2

## check if query is a recipe substring of recipe name
	elif(Recipe.objects.filter(r_name__icontains= query)):

		results=Recipe.objects.filter(r_name__icontains= query)
		for some_object in results:
			name=some_object.r_name.replace(" ", "+") 
			name=name.replace("&", "%26")
			link='http://127.0.0.1:8000/database/results_recipes?q=' + name
			info= {'image':some_object.r_image,'name':some_object.r_name,'food_type':some_object.food_type, 'link':link}
			resultlis.append(info)
		template_num=2	

## check if query is an ingredient 
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



