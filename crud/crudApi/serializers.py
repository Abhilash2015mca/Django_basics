from rest_framework import serializers
from crudApi.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'address', 'email', 'ph', 'city', 'cd']
