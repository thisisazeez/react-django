from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSeriallizer
from .models import Task

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSeriallizer
    queryset = Task.objects.all()
    