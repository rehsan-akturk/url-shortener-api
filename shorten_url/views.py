from django.core.exceptions import ObjectDoesNotExist
from shorten_url.models import ShortUrlModel
from shorten_url.serializers import ShortUrlSerializer
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



"""Shorten a URL."""
@api_view(['GET', 'POST'])
def shorten_url( request):
        if request.method == 'POST':
            data = {
               'url': request.data.get('url'),
               'short_url': ShortUrlModel.generate_short_url(),
            }

            serializer = ShortUrlSerializer(data=data)

            # if raised exception, it automatically
            # returns a 400 response with errors
            if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response(serializer.data, 201)

        #get all url and urls detail      
        elif request.method == 'GET':
           items = ShortUrlModel.objects.all()
           serializer = ShortUrlSerializer(items, many=True)
           return Response(serializer.data)



"""Decode a URL short url into a the Original URL."""
def getOriginalUrl( request,short_url):
        try:
            obj = ShortUrlModel.objects.get(short_url=short_url)
            obj.increase_short_url_counter()
        except ObjectDoesNotExist:
            return Response({'error': 'Short url id does not exist.'}, 400)
        
        if obj is not None:
           return redirect(obj.url)


     
