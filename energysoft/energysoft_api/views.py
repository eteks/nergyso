# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from rest_framework import viewsets
from energysoft_api.serializers import EmployeeSerializer
from employee.models import Employee

# Create your views here.

# ViewSets define the view behavior.
class EmployeeSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
