from django.http import request
from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, AdminSerializer
from rest_framework import permissions, parsers
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes


@permission_classes((permissions.AllowAny,))
class UserAPI(APIView):
    parser_classes = (MultiPartParser,)
    def get(self, *args, **kwargs):
        print(*kwargs.keys())
        user = UserSerializer.getProfile(**kwargs)
        domain = self.request.get_host()
        path_image = user.image.url
        image_url = 'http://{domain}{path}'.format(domain=domain, path=path_image)
        return Response(
            {
                "user_id": user.id,
                "image": image_url,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "sex": user.sex
            }
        )

    def post(self, *args, **kwargs):
        
        print(self.request.data)
        user_id = UserSerializer.create(self.request.data)
        return Response(
            {
                "user_id": user_id
            }
        )

    def put(self, *args, **kwargs):
        print(self.request.data)
        data = dict(self.request.data)
        print(data)
        data['user_id'] = kwargs['user_id']
        user = UserSerializer.update(data)
        domain = self.request.get_host()
        path_image = user.image.url
        image_url = 'http://{domain}{path}'.format(domain=domain, path=path_image)
        return Response(
            {
                "user_id": user.id,
                "image": image_url,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "sex": user.sex
            }
        )

    def delete(self, *args, **kwargs):
        user = UserSerializer.deleteUser(
            **kwargs
        )
        return Response(
            {
                "user_id": user[0]
            }
        )

@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class UserListAPI(APIView):
    def get(self,*args, **kwargs):
        users = UserSerializer.getList()
        users_list = users.values()
        domain = self.request.get_host()
        for ind, user in enumerate(users_list):
            path_image = users[ind].image.url
            image_url = 'http://{domain}{path}'.format(domain=domain, path=path_image)
            users_list[ind]['image'] = image_url

        return Response(
            {
                "results": users_list
            }
        )

@permission_classes((permissions.AllowAny,))
class AdminAPI(APIView):
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    def post(self, *args, **kwargs):
        admin = AdminSerializer.get(self.request.data)
        if admin:
            return Response(
                {
                    'success': True,
                    'admin': admin.email,
                    'auth_token': 'tset'
                }
            )
        else:
            return Response(
                {
                    "success": False,
                    "auth_token": "fwefew"
                }
            )
