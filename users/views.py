from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from users.models import User
from users.serializers import UserSerializer

@api_view(["GET", "POST", "PUT", "DELETE"])
@parser_classes([JSONParser])
def users(request):
    try:
        if request.method == 'GET':
            print('1. GET으로 들어옴')
            print(JsonResponse)
            return JsonResponse({'get users': 'SUCCESS'})
        elif request.method == 'POST':
            print('2. POST로 들어옴')
            new_user = request.data
            serializer = UserSerializer(data=new_user)
            if serializer.is_valid():
                print(serializer)
                serializer.save()
            return JsonResponse({'join': 'SUCCESS'})
        elif request.method == 'PUT':
            return JsonResponse({'update': 'SUCCESS'})
        elif request.method == 'DELETE':
            return JsonResponse({'delete': 'SUCCESS'})
    except:
        return JsonResponse({'users': 'fail'})