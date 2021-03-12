# https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-4.php

import requests
geo_url = 'https://maps.googleapis.com/maps/api/geocode/json'
my_address = {'address': 'vrundavan society, thane', 
             'language': 'en'}
response = requests.get(geo_url, params = my_address)
results = response.json()['results']
print(results)
exit();
my_geo = results[0]['geometry']['location']
print("Longitude:",my_geo['lng'],"\n","Latitude:",my_geo['lat'])