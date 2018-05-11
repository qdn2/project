import os
from django.core.wsgi import get_wsgi_application
import httplib
import json
import urllib
import requests
from urllib import urlencode

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
application = get_wsgi_application()
from database.models import Recipe

header = {
 "Content-Type": "application/json",
 "X-Yummly-App-ID": "5edc9616",
 "X-Yummly-App-Key": "8c3a2a8a3d72cd5a68d97d92b84dc8cc",
 "Access-Control-Allow-Origin": 'true'
}


#datas
recipeName = []
minutes = []
rating = []
ingredients = []
cuisines = ["cuisine^cuisine-spanish","cuisine^cuisine-american", "cuisine^cuisine-italian", "cuisine^cuisine-mexican","cuisine^cuisine-thai",
            "cuisine^cuisine-japanese", "cuisine^cuisine-indian", "cuisine^cuisine-greek", "cuisine^cuisine-hawaiin", "cuisine^cuisine-french",
            "cuisine^cuisine-german", "cuisine^cuisine-swedish", "cuisine^cuisine-barbecue", "cuisine^cuisine-irish", "cuisine^cuisine-mediterranean"]


for j in cuisines:
    idx = 0
    param = {"allowedCuisine[]": j}
    url='https://api.yummly.com/v1/api/recipes'
    response = requests.get(url, headers=header, params=param)
    yummly = response.json()
    print(yummly)
    matches = yummly['matches']        
    for recipe in yummly['matches']:
        
        print(recipe['recipeName'])
        r_name=recipe['recipeName']
        
        print(recipe['attributes']['cuisine'][0])
        food_type='spanish'
        
        print(recipe['rating'])
        r_rating=str(recipe['rating'])
        
        items= ""
        first=True  
        for item in recipe['ingredients']:
            if(first):
                items= items+item
                first=False
            else:
                items= items+"+" +item

        r_ingredients=items
        
        print(str(recipe['totalTimeInSeconds']/60)+ " Minutes")
        r_time=str(recipe['totalTimeInSeconds']/60)+ " Minutes"
        
        print(recipe['imageUrlsBySize']['90'])
        r_image=str(recipe['imageUrlsBySize']['90'])

        entry= Recipe(r_name= r_name,food_type= food_type,r_ingredients=r_ingredients, r_time=r_time, r_image=r_image,r_rating=r_rating)
        entry.save()
    
    break