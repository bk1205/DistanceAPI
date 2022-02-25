import requests
from django.conf import settings

'''
    The function getCords returns the coordinates (latitude, longitude) of given city/locality/sub-city by making an 
    api call to Bing Map Third party API.
    
    The function getDistance returns the travel distance between given cities/localities/sub-cities by 
    making an api call to Bing Map Third party API.
'''

apikey = settings.API_KEY
def getCords(city):
    url = f'http://dev.virtualearth.net/REST/v1/Locations?query={city}&o=json&key={apikey}'
    res = requests.get(url)
    resp = res.json()
    data = resp['resourceSets'][0]['resources']
    coords = []
    if len(data):
        coords = data[0]['geocodePoints'][0]['coordinates']
    return coords

def getDistance(loc1, loc2):
    url = f'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key={apikey}'
    data = {
            "origins": [{
                "latitude": loc1[0],
                "longitude": loc1[1]
            },
            ],
            "destinations": [{
                "latitude": loc2[0],
                "longitude": loc2[1]
            },
            ],
            "travelMode": "driving"
        }
    headers = {'Content-type': 'application/json', 'Content-Length': '450'}
    resp = requests.post(url = url, json = data, headers=headers).json()
    dist = resp['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']
    return dist



