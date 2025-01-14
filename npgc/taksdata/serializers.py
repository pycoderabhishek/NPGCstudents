from rest_framework import serializers
from .models import Department  # Import your model here

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'  # Include all fields from the Department model
