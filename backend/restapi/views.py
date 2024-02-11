from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer


# view for company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # custom api
    # url = http://localhost:8000/api/v1/companies/{companyId}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            employees_serializer = EmployeeSerializer(
                employees,
                many=True,
                context={'request': request}
            )
            return Response(employees_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'success': False,
                'message': 'company not found || Error'
            })

# view for employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
