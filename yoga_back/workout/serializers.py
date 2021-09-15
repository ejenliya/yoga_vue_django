from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from .models import Sex, Workout, Trouble, Day, Level
from django.shortcuts import get_object_or_404
from django.db.models import Q, fields
import psycopg2
import ast


class TroubleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trouble
        fields = (
            'id',
            'name'
        )

    @staticmethod
    def get(trouble_id):
        trouble = get_object_or_404(Trouble, pk=trouble_id)
        return trouble

    @staticmethod
    def create(validated_data):
        trouble = Trouble(
            name=validated_data['name'],
            image=validated_data['image']
        )
        trouble.save()
        return trouble.id

    @staticmethod
    def update(validated_data):
        trouble = get_object_or_404(Trouble, pk=validated_data['trouble_id'])
        trouble.name = validated_data['name'][0]
        try:
            trouble.image = validated_data['image'][0]
        except KeyError:
            trouble.image = trouble.image
        trouble.save()
        return trouble

    @staticmethod
    def getTroubleList():
        troubles = Trouble.objects.all()
        return troubles

    @staticmethod
    def delete(trouble_id):
        trouble = get_object_or_404(Trouble, pk=trouble_id)
        trouble = trouble.delete()
        return trouble


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = (
            'id',
            'name',
            'video',
            'duration',
            'periodicity',
            'level',
            'description',
            'value',
            'image',
            'sex',
            'troubles'
        )

    @staticmethod
    def create(validated_data):
        print(validated_data['troubles'])
        print(ast.literal_eval(validated_data['troubles']))
        troubles_id = []
        for trouble_id in ast.literal_eval(validated_data['troubles']):
            try:
                troubles_id.append(int(trouble_id))
            except TypeError:
                continue
        troubles = [Trouble.objects.get(pk=trouble_id)
                    for trouble_id in troubles_id]
        workout = Workout.objects.create(
            name=validated_data['name'][0],
            video=validated_data['video'],
            duration=validated_data['duration'][0],
            periodicity=validated_data['periodicity'],
            level=validated_data['level'],
            description=validated_data['description'][0],
            value=validated_data['value'][0],
            image=validated_data['image'],
            sex=validated_data['sex'],
        )
        for trouble in troubles:
            workout.troubles.add(trouble)
        # workout.save()
        return workout.id

    @staticmethod
    def update(validated_data):
        print(validated_data['troubles'])
        print(ast.literal_eval(validated_data['troubles'][0]))
        troubles_id = []
        for trouble_id in ast.literal_eval(validated_data['troubles'][0]):
            try:
                troubles_id.append(int(trouble_id))
            except TypeError:
                continue
        troubles = Trouble.objects.filter(pk__in=troubles_id)
        print(troubles_id)
        workout = get_object_or_404(Workout, pk=validated_data['workout_id'])
        workout.name = validated_data['name'][0]
        workout.duration = validated_data['duration'][0]
        workout.periodicity = validated_data['periodicity'][0]
        workout.level = validated_data['level'][0]
        workout.description = validated_data['description'][0]
        workout.value = validated_data['value'][0]
        workout.sex = validated_data['sex'][0]
        workout.troubles.set(troubles)
        try:
            workout.video = validated_data['video'][0]
        except KeyError:
            workout.video = workout.video
        try:
            workout.image = validated_data['image'][0]
        except KeyError:
            workout.image = workout.image
        workout.save()
        return workout

    @staticmethod
    def getWorkout(workout_id):
        workout = get_object_or_404(Workout, pk=workout_id)
        return workout

    @staticmethod
    def getList(filter_param=None):
        if filter_param:
            workouts = Workout.objects.all().filter(level=filter_param)
        else:
            workouts = Workout.objects.all()
        return workouts

    @staticmethod
    def deleteWorkout(workout_id):
        workout = get_object_or_404(Workout, pk=workout_id)
        workout = workout.delete()
        return workout

    @staticmethod
    def getFilteredList(filters={}):
        if filters:
            filters = dict(filters)
            print(filters)
            workouts = Workout.objects.filter(
                Q(sex__pk__in=filters['sex']) &
                Q(periodicity__pk__in=filters['periodicity']) &
                Q(level__pk__in=filters['level']) &
                Q(troubles__pk__in=filters['troubles'])
            ).distinct()

            return workouts
        else:
            return WorkoutSerializer.getList()


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Day

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Sex


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Level


class WorkoutCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    
    class Meta:
        fields = '__all__'
        model = Workout
