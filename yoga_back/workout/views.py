from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import (
    WorkoutSerializer, TroubleSerializer, WorkoutCreateSerializer,
    LevelSerializer, SexSerializer, DaySerializer
)
from django.core.paginator import Paginator
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
import os
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import parsers, permissions, generics
from .models import *

@permission_classes((permissions.AllowAny,))
class TroubleAPI(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, *args, **kwargs):
        trouble = TroubleSerializer.get(
            **kwargs
        )
        domain = self.request.get_host()
        path_image = trouble.image.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        return Response(
            {
                "trouble_id": trouble.id,
                "name": trouble.name,
                "image": image_url
            }
        )

    def post(self, *args, **kwargs):
        print(self.request.data)
        trouble = TroubleSerializer.create(self.request.data)
        return Response(
            {
                "trouble_id": trouble
            }
        )

    def put(self, *args, **kwargs):
        print(self.request.data)
        data = dict(self.request.data)
        print(data)
        data['trouble_id'] = kwargs['trouble_id']
        trouble = TroubleSerializer.update(data)
        domain = self.request.get_host()
        path_image = trouble.image.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        return Response(
            {
                "trouble_id": trouble.id,
                "name": trouble.name,
                "image": image_url
            }
        )

    def delete(self, *args, **kwargs):
        trouble = TroubleSerializer.delete(
            **kwargs
        )
        return Response(
            {
                "trouble_id": trouble[0]
            }
        )
@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class TroubleList(APIView):
    def get(self, *args, **kwargs):
        troubles = TroubleSerializer.getTroubleList()
        troubles_list = troubles.values()
        domain = self.request.get_host()
        for ind, trouble in enumerate(troubles_list):
            path_image = troubles[ind].image.url

            image_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_image)
            troubles_list[ind]['image'] = image_url
        return Response(
            {
                "results": troubles_list,
            }
        )

@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class TroubleListAPI(APIView):
    def get(self, *args, **kwargs):
        troubles = TroubleSerializer.getTroubleList()
        troubles_list = troubles.values()
        domain = self.request.get_host()
        for ind, trouble in enumerate(troubles_list):
            path_image = troubles[ind].image.url

            image_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_image)
            troubles_list[ind]['image'] = image_url
        return Response(
            troubles_list
        )


@permission_classes((permissions.AllowAny,))
class WorkoutAPI(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, *args, **kwargs):
        print(*kwargs.keys())
        workout = WorkoutSerializer.getWorkout(
            **kwargs
        )
        domain = self.request.get_host()
        path_image = workout.image.url
        path_video = workout.video.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        video_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_video)
        return Response(
            {
                "workout_id": workout.id,
                "name": workout.name,
                "video": video_url,
                "duration": workout.duration,
                "periodicity": workout.periodicity.values(),
                "level": workout.level.values(),
                "description": workout.description,
                "value": workout.value,
                "image": image_url,
                "sex": workout.sex.values(),
                "troubles": workout.troubles.values()
            }
        )

    def post(self, *args, **kwargs):
        workout = WorkoutSerializer.create(self.request.data)
        return Response(
            {
                "workout_id": workout
            }
        )

    def put(self, *args, **kwargs):
        print(self.request.data)
        data = dict(self.request.data)
        print(data)
        data['workout_id'] = kwargs['workout_id']
        workout = WorkoutSerializer.update(data)
        domain = self.request.get_host()
        path_image = workout.image.url
        path_video = workout.video.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        video_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_video)
        return Response(
            {
                "workout_id": workout.id,
                "name": workout.name,
                "video": video_url,
                "duration": workout.duration,
                "periodicity": workout.periodicity,
                "level": workout.level,
                "description": workout.description,
                "value": workout.value,
                "image": image_url,
                "sex": workout.sex,
                "troubles": workout.troubles.values()
            }
        )

    def delete(self, *args, **kwargs):
        workout = WorkoutSerializer.deleteWorkout(
            **kwargs
        )
        return Response(
            {
                "workout_id": workout[0]
            }
        )


@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class WorkoutPaginatedList(APIView):
    def get(self, *args, **kwargs):
        workouts = WorkoutSerializer.getList()
        workouts_list = workouts.values('id', 'title', 'image')
        domain = self.request.get_host()
        for ind, workout in enumerate(workouts_list):
            path_image = workouts[ind].image.url
            image_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_image)
            workouts_list[ind]['image'] = image_url

        pg = Paginator(workouts_list, per_page=1)
        page = pg.page(kwargs['page_num'])

        return Response(
            {
                "page": kwargs['page_num'],
                "total_pages": pg.num_pages,
                "results": page.object_list,
                "page_numbers": {
                    "next": page.next_page_number() if page.has_next() else kwargs['page_num'],
                    "prev": page.previous_page_number() if page.has_previous() else kwargs['page_num'],
                }
            }
        )


@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class WorkoutInfo(APIView):
    parser_classes = (MultiPartParser,)
    def get(self, *args, **kwargs):
        level = self.request.query_params.get('workoutSearch', None)
        if level:
            workouts = WorkoutSerializer.getList(filter_param=level)
        else:
            workouts = WorkoutSerializer.getList()

        workouts_list = workouts.values()
        domain = self.request.get_host()
        for ind, workout in enumerate(workouts_list):
            path_image = workouts[ind].image.url
            path_video = workouts[ind].video.url
            image_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_image)
            video_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_video)
            workouts_list[ind]['image'] = image_url
            workouts_list[ind]['video'] = video_url

        return Response(
            {
                "results": workouts_list
            }
        )


@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class WorkoutInfoAPI(APIView):
    parser_classes = (MultiPartParser,)
    def get(self, *args, **kwargs):
        level = self.request.query_params.get('workoutSearch', None)
        if level:
            workouts = WorkoutSerializer.getList(filter_param=level)
        else:
            workouts = WorkoutSerializer.getList()

        workouts_list = workouts.values()
        domain = self.request.get_host()
        for ind, workout in enumerate(workouts_list):
            path_image = workouts[ind].image.url
            path_video = workouts[ind].video.url
            image_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_image)
            video_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_video)
            workouts_list[ind]['image'] = image_url
            workouts_list[ind]['video'] = video_url

        return Response(
            {
                "results": workouts_list
            }
        )


@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class WorkoutFilteredList(APIView):
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    def get(self, *args, **kwargs):
        workouts = WorkoutSerializer.getFilteredList(self.request.data)
        workouts_list =  workouts.values('id', 'name', 'image')
        domain = self.request.get_host()
        for ind, workout in enumerate(workouts_list):
            path_image = workouts[ind].image.url
            image_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_image)
            workouts_list[ind]['image'] = image_url

        return Response(
            {
                "results": workouts_list,
            }
        )


@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class WorkoutFilteredListAPI(APIView):
    parser_classes = (MultiPartParser,)
    def get(self, *args, **kwargs):
        workouts = WorkoutSerializer.getFilteredList(self.request.data)
        print(workouts)
        workouts_list = workouts.values('id', 'name', 'image')
        domain = self.request.get_host()
        for ind, workout in enumerate(workouts_list):
            path_image = workout.image.url
            image_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_image)
            workouts_list[ind]['image'] = image_url

        return Response(
            workouts_list
        )




class CreateWorkout(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Workout.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = WorkoutCreateSerializer

class UpdateWorkout(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Workout.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser)
    serializer_class = WorkoutCreateSerializer

class DayAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Day.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = DaySerializer

class SexAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Sex.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = SexSerializer

class LevelAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Level.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = LevelSerializer


