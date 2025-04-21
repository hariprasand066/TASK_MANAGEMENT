from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import task
from .serializers import TaskSerializer
from rest_framework.views import APIView


class Dashboard(APIView):
    permission_classes =[IsAuthenticated]

    def get(self,request):
        User = request.User

        if User.role =='Admin':
            tasks=task.objects.all()
        elif User.role =='Key Manager':
            tasks=task.objects.filter(assign_to=User)
        elif User.role == 'Manager':
            tasks=task.objects.filter(assign_by='Key Manager')| task.objects.filter(assign_to='Team Lead')
        elif User.role == 'Team Lead':
            tasks=task.objects.filter(assign_by='Manager')| task.objects.filter(assign_to='Employee')
        else:
            tasks=task.objects.none()

        Serializer=TaskSerializer(tasks, many=True)
        return Response(Serializer.data)
            
        

