import os
from django.core.wsgi import get_wsgi_application
import httplib
import json
import urllib
import requests
from urllib import urlencode

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
application = get_wsgi_application()
from database.models import Z_Restaurant

def get_images(search_type):
    search_term = search_type
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    subscription_key = '64673499523c43e7b1278b861e799690'
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "license": "public", "imageType": "photo"}

    response = requests.get(search_url, headers=headers, params=params)
    search_results = response.json()
    
    try:
        for i in search_results['queryExpansions']:
            image_url= i['thumbnail']['thumbnailUrl']
            break
    except: 
        image_url= 'http://hdriblog.com/wp-content/themes/gridview/img/no-image.png'
        
    return image_url






header = {
"User-agent": "curl/7.43.0",
'X-Zomato-API-Key': '4903b587901a5352f403a3a97da3543a'
}

url='https://developers.zomato.com/api/v2.1/search?entity_id=685&entity_type=city&count=100'
response = requests.get(url, headers=header)
food_places=response.json()
food_places=food_places['restaurants']
idx=0

for i in food_places:
    food_place=food_places[idx]
    restaraunt_id=food_place['restaurant']['id']
    r_id=restaraunt_id
    r_name=food_place['restaurant']['name']
    food_type=food_place['restaurant']['cuisines']
    r_image=get_images(food_type)
    r_city=food_place['restaurant']['location']['city']
    r_address=food_place['restaurant']['location']['address']
    r_menu=food_place['restaurant']['menu_url']
    r_cost=food_place['restaurant']['average_cost_for_two']
    
    url='https://developers.zomato.com/api/v2.1/restaurant?res_id=' + restaraunt_id
    response = requests.get(url, headers=header)
    food_info=response.json() 
    r_rating=(food_info['user_rating']['aggregate_rating'])
    
    
    
    idx+=1
    print(r_id) 
    print(r_name)
    print(food_type ) 
    print(r_city ) 
    print(r_address ) 
    print(r_menu ) 
    print(r_cost ) 
    print(r_image) 
    print(str(r_rating))

    entry=Z_Restaurant(r_id=r_id,r_name= r_name,food_type= food_type,r_city= r_city,r_address=r_address,r_menu=r_menu, r_cost=r_cost, r_image=r_image,r_rating=str(r_rating))
    entry.save()


