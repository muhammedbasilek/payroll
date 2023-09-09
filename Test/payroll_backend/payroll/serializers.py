from rest_framework import serializers
from .models import *
class EmployeeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"