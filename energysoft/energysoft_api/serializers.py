from rest_framework import serializers
from employee.models import Employee
# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'employee_dob', 'employee_email')