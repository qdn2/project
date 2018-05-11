# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Z_Restaurant(models.Model):
   r_id = models.CharField(max_length=200, null= True)
   r_name= models.CharField(max_length= 200, null= True)
   food_type= models.CharField(max_length = 200, null= True)
   r_city=models.CharField(max_length = 200, null= True)
   r_address=models.CharField(max_length = 200, null= True)
   r_menu=models.CharField(max_length = 200, null= True)
   r_cost=models.CharField(max_length = 200, null= True)
   r_image=models.CharField(max_length = 200, null= True)
   r_rating=models.CharField(max_length = 200, null= True)

class Recipe(models.Model):
	r_name= models.CharField(max_length= 200, null= True)
	food_type= models.CharField(max_length = 200, null= True)
	r_ingredients=models.CharField(max_length = 1024, null= True)
	r_time=models.CharField(max_length = 200, null= True)
	r_image=models.CharField(max_length = 200, null= True)
	r_rating=models.CharField(max_length = 200, null= True) 	


