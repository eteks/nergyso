# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
# from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from rest_framework import viewsets
from energysoft_api.serializers import EmployeeSerializer, EventsSerializer,NewsSerializer, FeedbackSerializer,ShoutoutSerializer,NotificationSerializer
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
from feedback.models import Feedback
from rest_framework import status
from shoutout.models import Shoutout
from push_notifications.models import APNSDevice, GCMDevice

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
# class EventsSet(HaystackViewSet):
# 	index_models = [Events]
# 	# sqs = SearchQuerySet().filter(content_auto=request.GET.get('q', ''))
# 	serializer_class = EventsSerializer
# 	pagination_class = StandardResultsSetPagination

# 	# permission_classes = [IsAuthenticated]
# 	# renderers = renderers.JSONRenderer
# 	# parsers = parsers.JSONParser
# 	# renderer_classes = (XMLRenderer, JSONRenderer, )
# 	# @list_route(methods=['post'])
# 	@list_route()
# 	def recent_events(self, request):
# 		print "recent-events"
# 		queryset = SearchQuerySet()[:10]
# 		print queryset
# 		# events = get_object_or_404(queryset, pk=pk)
# 		# events = get_object_or_404(queryset)
# 		serializer = EventsSerializer(queryset)
# 		return Response(serializer.data)

class EventsSet(viewsets.ModelViewSet):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer
	pagination_class = StandardResultsSetPagination
	# permission_classes = [IsAuthenticated]

	# permission_classes = [IsAuthenticated]
	# renderers = renderers.JSONRenderer
	# parsers = parsers.JSONParser
	# renderer_classes = (XMLRenderer, JSONRenderer, )
	# @list_route(methods=['post'])
	@list_route()
	def recent_events(self, request):
		queryset = Events.objects.all().order_by('-id')[:10]
		# for querysets in queryset:
		# 	print querysets.events_title
		# events = get_object_or_404(queryset, pk=pk)
		# events = get_object_or_404(queryset)
		# serializer = EventsSerializer(queryset)
		# return Response(serializer.data)
		return Response(EventsSerializer(queryset,many=True).data)

	# @list_route()
	# def similar_events(self, request):
	# 	print "recent-events"
	# 	queryset = Events.objects.get(pk=pk)
	# 	for querysets in queryset:
	# 		print querysets.events_title
	# 	# events = get_object_or_404(queryset, pk=pk)
	# 	# events = get_object_or_404(queryset)
	# 	# serializer = EventsSerializer(queryset)
	# 	# return Response(serializer.data)
	# 	return Response(EventsSerializer(queryset,many=True).data)

class NewsSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsSerializer
	pagination_class = StandardResultsSetPagination
	# permission_classes = [IsAuthenticated]

	@list_route()
	def recent_news(self, request):
		queryset = News.objects.all().order_by('-id')[:10]
		return Response(NewsSerializer(queryset,many=True).data)

class FeedbackSet(viewsets.ModelViewSet):
	queryset = Feedback.objects.all()
	serializer_class = FeedbackSerializer
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response({"success": "Feedback posted successfully"}, status=status.HTTP_201_CREATED, headers=headers)

class ShoutoutSet(viewsets.ModelViewSet):
	queryset = Shoutout.objects.all()
	serializer_class = ShoutoutSerializer
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response({"success": "Shoutout posted successfully"}, status=status.HTTP_201_CREATED, headers=headers)

class NotificationSet(viewsets.ModelViewSet):	
	serializer_class = NotificationSerializer	
	@list_route()
	def get_queryset(self, *args, **kwargs):
		queryset = GCMDevice.objects.all()
		queryset.send_message("This is a test message", title="Test Notification")
		# serializer = self.get_serializer()
		# serializer.is_valid(raise_exception=True)
		# self.perform_create(serializer)
		# headers = self.get_success_headers(serializer.data)
		# return Response({"success": "Message sent successfully"}, status=status.HTTP_201_CREATED, headers=headers)
		return Response({"success": "Message sent successfully"})
		# return Response(NotificationSerializer(queryset,many=True).data)



