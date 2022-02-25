from django.urls import path
from api.restapp.views import GetDistance

'''
    Here url endpoint '.../distance' is defined
'''
urlpatterns = [
    path('distance/', GetDistance.as_view()),
]
