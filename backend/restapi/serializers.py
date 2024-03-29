from rest_framework import serializers
from .models import Company, Employee


# company serializer
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"


# employee serializer
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"
