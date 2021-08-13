from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import studentSerializer
from drfapp.models import student

class TestView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = student.objects.all()
        student1 = qs.first()
        serializer = studentSerializer(student1)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)