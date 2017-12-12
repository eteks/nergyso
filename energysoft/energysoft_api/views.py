# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
# from oauth2_provider.views.generic import ProtectedResourceView
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
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

# ViewSets define the view behavior.
class EmployeeSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	pagination_class = StandardResultsSetPagination
	# lookup_field = 'department_name'
	# permission_classes = [IsAuthenticated]

# class ApiEndpoint(ProtectedResourceView):
# 	def get(self, request, *args, **kwargs):
# 		return HttpResponse('Hello, OAuth2!')

# ViewSets define the view behavior.
# class EventsSet(HaystackViewSet,APIView):
class EventsSet(HaystackViewSet):
	index_models = [Events]
	# sqs = SearchQuerySet().filter(content_auto=request.GET.get('q', ''))
	serializer_class = EventsSerializer
	pagination_class = StandardResultsSetPagination

	# permission_classes = [IsAuthenticated]
	# renderers = renderers.JSONRenderer
	# parsers = parsers.JSONParser
	# renderer_classes = (XMLRenderer, JSONRenderer, )
	# @list_route(methods=['post'])
	@list_route()
	def recent_events(self, request):
		print "recent-events"
		queryset = SearchQuerySet()[:10]
		print queryset
		# events = get_object_or_404(queryset, pk=pk)
		# events = get_object_or_404(queryset)
		serializer = EventsSerializer(queryset)
		return Response(serializer.data)

class NewsSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsSerializer
	pagination_class = StandardResultsSetPagination
	# permission_classes = [IsAuthenticated]

	



