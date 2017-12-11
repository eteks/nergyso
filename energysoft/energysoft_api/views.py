# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from rest_framework import viewsets
from energysoft_api.serializers import EmployeeSerializer, EventsSerializer,NewsSerializer
from employee.models import Employee
from events.models import Events
from employee.models import Employee
from news.models import News
from haystack.query import SearchQuerySet,EmptySearchQuerySet
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.permissions import IsAuthenticated
from energysoft_api.pagination import StandardResultsSetPagination


# ViewSets define the view behavior.
class EmployeeSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	pagination_class = StandardResultsSetPagination
	# permission_classes = [IsAuthenticated]

class ApiEndpoint(ProtectedResourceView):
	def get(self, request, *args, **kwargs):
		return HttpResponse('Hello, OAuth2!')

# ViewSets define the view behavior.
class EventsSet(HaystackViewSet):
	index_models = [Events]
	# sqs = SearchQuerySet().filter(content_auto=request.GET.get('q', ''))
	serializer_class = EventsSerializer
	pagination_class = StandardResultsSetPagination
	permission_classes = [IsAuthenticated]

class NewsSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsSerializer
	pagination_class = StandardResultsSetPagination
	# permission_classes = [IsAuthenticated]

	



