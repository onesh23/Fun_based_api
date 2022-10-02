
from django.shortcuts import render
from rest_framework.decorators import api_view
from first_api.models import Student
from first_api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

@api_view(['GET','POST','DELETE','PUT'])
def get_student(request,id=None):
    if request.method == 'GET':
        if id:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        stu = Student.objects.get(id= id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stu = Student.objects.get(id=id)
        # serializer = StudentSerializer(stu)
        stu.delete()    
        return Response({'msg':"Deleted"},status=status.HTTP_204_NO_CONTENT)
