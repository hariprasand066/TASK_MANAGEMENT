from rest_framework import serializers
from .models import task

class taskserializers(serializers.ModelSerializer):
    class Meta:
        models = task
        fields = ['id', 'date', 'client_name', 'task_name', 'assign_by', 'assign_to', 'status', 'working_hours', 'remarks']