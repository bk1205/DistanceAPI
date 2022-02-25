from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from api.restapp.utils import getCords, getDistance
from api.restapp.serializers import DistanceSerializer
from  api.restapp.models import Distance


'''
    Here GetDistance class contains get function which will be called when '../distance?city1=...&city2=...' endpoint is hit
'''

class GetDistance(APIView):
    def get(self, request):
        city1 = request.GET.get('city1', '').strip('/')
        city2 = request.GET.get('city2', '').strip('/')
        if(city1 == '' or city2 == ''):
            return Response({'status': 'Error 404, City 1 or City 2 cannot be null'}, status=status.HTTP_404_NOT_FOUND)
        try:
            inst = Distance.objects.get(city1=city1, city2=city2)
            response = DistanceSerializer(inst).data
        except Distance.DoesNotExist:
            loc1 = getCords(city1)
            loc2 = getCords(city2)
            if (len(loc1) == 0 or len(loc2) == 0):
                raise NotFound(detail="Error 404, one or more entries are invalid", code=404)
            dist = getDistance(loc1, loc2)

            response = {
                'city1': city1.title(),
                'city2': city2.title(),
                'distance': f'{dist} km'
            }

            serializer = DistanceSerializer(data=response)
            if serializer.is_valid():
                serializer.save()

        return Response(response)
