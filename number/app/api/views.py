from django.shortcuts import render
from django.http import HttpResponse
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class Numbers(APIView):
    def gets(self, request , *args, **kwargs):
        
        urls = request.query_params.getlist('url')
        
        r = {'numbers': []}
        for u in urls:
            try:
                rs = requests.get(u)
                if rs.status_code == 200:
                    for i in rs.json()['numbers']:
                        r['numbers'].append(i)
                else:
                    pass
            except Exception as e:
                pass
        
        sortedArr = sorted(r['numbers'])
        
        num = set(sortedArr)
        
        final = list(num)
        r['numbers'] = final        
        return Response(r,   status=status.HTTP_200_OK)
