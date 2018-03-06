# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
# from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from energysoft_api.serializers import EmployeeSerializer, EventsSerializer,NewsSerializer, FeedbackSerializer,ShoutoutSerializer,PasswordChangeSerializer,NotificationSerializer,BannerSerializer,GallerySerializer,EmployeeParticularSerializer,LiveTelecastSerializer,PollsSerializer,PollsPostResultSerializer,NotificationListSerializer,CEOMessageSerializer,SearchSerializer
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
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.translation import ugettext_lazy as _
from push_notifications.models import APNSDevice, GCMDevice
from banner.models import Banner
from gallery.models import Gallery
from livetelecast.models import Livetelecast
import datetime
from polls.models import PollsAnswer,PollsQuestion,PollsResult
from master.models import Notification,CEOMessage
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)

# ViewSets define the view behavior.
class EmployeeSet(viewsets.ModelViewSet):
	queryset = Employee.objects.filter(active_status=1)
	serializer_class = EmployeeSerializer
	pagination_class = StandardResultsSetPagination
	# lookup_field = 'department_name'
	# permission_classes = [IsAuthenticated]

	@list_route()
	def employee_tag_details(self, request):
		queryset = Employee.objects.filter(active_status=1).order_by('-id')
		# for querysets in queryset:
		# 	print querysets.events_title
		# events = get_object_or_404(queryset, pk=pk)
		# events = get_object_or_404(queryset)
		# serializer = EventsSerializer(queryset)
		# return Response(serializer.data)
		return Response(EmployeeParticularSerializer(queryset,many=True).data)

	@list_route()
	def employee_today_birthday(self, request):
		today = datetime.date.today()
		print today
		queryset = Employee.objects.filter(employee_dob__month=today.month,
			employee_dob__day=today.day).order_by('-id')
		# queryset = Employee.objects.filter(employee_dob=today).order_by('-id')
		print queryset
		return Response(EmployeeParticularSerializer(queryset,many=True).data)

	@list_route()
	def employee_upcoming_birthday(self, request):
		today = datetime.date.today()
		print today
		queryset = Employee.objects.filter(Q(employee_dob__month__gt=today.month)|
			(Q(employee_dob__month=today.month)&Q(employee_dob__day__gt=today.day))).order_by('employee_dob','id')[:30]
		# queryset = Employee.objects.filter(employee_dob=today).order_by('-id')
		print queryset
		return Response(EmployeeParticularSerializer(queryset,many=True).data)

	@list_route()
	def employee_today_anniversary(self, request):
		today = datetime.date.today()
		print today
		queryset = Employee.objects.filter(employee_doj__month=today.month,
			employee_doj__day=today.day).order_by('-id')
		# queryset = Employee.objects.filter(employee_dob=today).order_by('-id')
		print queryset
		return Response(EmployeeParticularSerializer(queryset,many=True).data)

	@list_route()
	def employee_upcoming_anniversary(self, request):
		today = datetime.date.today()
		print today
		queryset = Employee.objects.filter(Q(employee_doj__month__gt=today.month)|
			(Q(employee_doj__month=today.month)&Q(employee_doj__day__gt=today.day))).order_by('employee_doj','id')[:30]
		# queryset = Employee.objects.filter(employee_dob=today).order_by('-id')
		print queryset
		return Response(EmployeeParticularSerializer(queryset,many=True).data)

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
	queryset = Events.objects.filter(active_status=1)
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
		queryset = Events.objects.filter(active_status=1).order_by('-id')[:3]
		# for querysets in queryset:
		# 	print querysets.events_title
		# events = get_object_or_404(queryset, pk=pk)
		# events = get_object_or_404(queryset)
		# serializer = EventsSerializer(queryset)
		# return Response(serializer.data)
		return Response(EventsSerializer(queryset,many=True).data)  

	@list_route()
	def search_events(self, request, search_string):
		print "search_string"
		print search_string
		queryset = Events.objects.filter((Q(events_title__icontains=search_string)|Q(events_description__icontains=search_string))&Q(active_status=1)).order_by('-id')
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
	queryset = News.objects.filter(active_status=1)
	serializer_class = NewsSerializer
	pagination_class = StandardResultsSetPagination
	# permission_classes = [IsAuthenticated]

	@list_route()
	def recent_news(self, request):
		queryset = News.objects.filter(active_status=1).order_by('-id')[:3]
		return Response(NewsSerializer(queryset,many=True).data)

	@list_route()
	def search_news(self, request, search_string):
		queryset = News.objects.filter((Q(news_title__icontains=search_string)|Q(news_description__icontains=search_string))&Q(active_status=1)).order_by('-id')
		return Response(NewsSerializer(queryset,many=True).data)

class FeedbackSet(viewsets.ModelViewSet):
	queryset = Feedback.objects.filter(active_status=1)
	serializer_class = FeedbackSerializer
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response({"success": "Feedback posted successfully"}, status=status.HTTP_201_CREATED, headers=headers)

class ShoutoutPostSet(viewsets.ModelViewSet):
	queryset = Shoutout.objects.filter(active_status=1)
	serializer_class = ShoutoutSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response({"success": "Shoutout posted successfully"}, status=status.HTTP_201_CREATED, headers=headers)

class ShoutoutListSet(viewsets.ModelViewSet):
	queryset = Shoutout.objects.filter(active_status=1).order_by('-id')
	serializer_class = ShoutoutSerializer
	pagination_class = StandardResultsSetPagination

	@list_route()
	def search_shoutout(self, request, search_string):
		queryset = Shoutout.objects.filter(Q(shoutout_description__icontains=search_string)&Q(shoutout_approval_status=1)).order_by('-id')
		return Response(ShoutoutSerializer(queryset,many=True).data)

class GalleryListSet(viewsets.ModelViewSet):
	queryset = Gallery.objects.filter(active_status=1).order_by('-id')
	serializer_class = GallerySerializer
	pagination_class = StandardResultsSetPagination

class PasswordChangeView(GenericAPIView):
    """
    Calls Django Auth SetPasswordForm save method.

    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordChangeView, self).dispatch(*args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": _("New password has been saved.")})

class NotificationSet(viewsets.ModelViewSet):
	serializer_class = NotificationSerializer	

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=False)
		# print serializer.data		
		try:
			check_exists = GCMDevice.objects.get(user_id=serializer.data['user'])
		except GCMDevice.DoesNotExist:
			check_exists = GCMDevice()
			check_exists.user_id = serializer.data['user']
		check_exists.name = serializer.data['name']
		check_exists.registration_id = serializer.data['registration_id']
		check_exists.application_id = serializer.data['application_id']
		check_exists.device_id = serializer.data['device_id']
		check_exists.cloud_message_type = "FCM"
		check_exists.save()
		return Response({"success": "Device data stored successfully"})

	@list_route()
	def send_notification(self, *args, **kwargs):
		print "send_notification"
		devices = GCMDevice.objects.all()
		print devices
		for q in devices:
			print q.application_id
			print q.registration_id
			# q.application_id = "test"
			q.send_message("This is a test message after checked", title="Test Notification")
		# serializer = self.get_serializer()
		# serializer.is_valid(raise_exception=True)
		# self.perform_create(serializer)
		# headers = self.get_success_headers(serializer.data)
		# return Response({"success": "Message sent successfully"}, status=status.HTTP_201_CREATED, headers=headers)
		return Response({"success": "Message sent successfully"})
		# return Response(NotificationSerializer(queryset,many=True).data)

class BannerSet(viewsets.ModelViewSet):
	queryset = Banner.objects.filter(active_status=1).order_by('-id')
	serializer_class = BannerSerializer
	# pagination_class = StandardResultsSetPagination

class LiveTelecastSet(viewsets.ModelViewSet):
	queryset = Livetelecast.objects.filter(active_status=1)
	serializer_class = LiveTelecastSerializer
	pagination_class = StandardResultsSetPagination

class PollsSet(viewsets.ModelViewSet):
	queryset = PollsQuestion.objects.filter(active_status=1)
	serializer_class = PollsSerializer
	# pagination_class = StandardResultsSetPagination

	# @list_route()
	# def get_queryset(self, *args, **kwargs):
	# 	return Response(PollsSerializer(many=True).data)

class PollsResultPostSet(viewsets.ModelViewSet):
	queryset = PollsResult.objects.all()
	serializer_class = PollsPostResultSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=False)
		print serializer.data
		pollsresult,created = PollsResult.objects.get_or_create( 
			pollsresult_question=PollsQuestion.objects.get(id=serializer.data['pollsresult_question']), 
			pollsresult_employee=Employee.objects.get(user_ptr_id=serializer.data['pollsresult_employee']), 
			defaults={
			'pollsresult_answer': PollsAnswer.objects.get(id=serializer.data['pollsresult_answer']), 
			}
		)
		if created:
			return Response({"success": "Polls Result posted successfully"})
		else:
			pollsresult.pollsresult_question = PollsQuestion.objects.get(id=serializer.data['pollsresult_question'])
			pollsresult.pollsresult_employee = Employee.objects.get(user_ptr_id=serializer.data['pollsresult_employee'])
			pollsresult.pollsresult_answer = PollsAnswer.objects.get(id=serializer.data['pollsresult_answer'])
			pollsresult.save()
			return Response({"success": "Polls Result Updated successfully"})

	def retrieve(self, request, pk=None):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=False)
		# print serializer.data
		# print "data"+serializer.data['pollsresult_question']
		try:
			pollsresult = PollsResult.objects.values('pollsresult_answer').get( 
				pollsresult_question=PollsQuestion.objects.get(id=serializer.data['pollsresult_question']), 
				pollsresult_employee=Employee.objects.get(user_ptr_id=serializer.data['pollsresult_employee'])
			)
			# print pollsresult['pollsresult_answer']
		except PollsResult.DoesNotExist:
			pollsresult = None
		if pollsresult:		
			return Response({"exists": "1","answer_id":pollsresult['pollsresult_answer']})
		else:
			return Response({"exists": "0"})

class NotificationListSet(viewsets.ModelViewSet):
	queryset = Notification.objects.all()
	serializer_class = NotificationListSerializer
	pagination_class = StandardResultsSetPagination

	def retrieve(self, request, pk=None):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=False)
		notification_result = Notification.objects.filter( 
				notification_employee=Employee.objects.get(user_ptr_id=serializer.data['notification_employee'])
		).order_by('-notification_created_date')[:50]
		return Response(NotificationListSerializer(notification_result,many=True).data)

	@list_route()
	def notification_status(self, request, pk=None):
		try:
			notification_status = Notification.objects.get(pk=pk)
		except Notification.DoesNotExist:
			notification_status = None
		print notification_status
		if notification_status:
			if notification_status.notification_read_status is False:
				notification_status.notification_read_status = True
				notification_status.save()
				return Response({"success": "Notification read status has been active"})
		else:
			return Response({"error": "ID not found"})
		return Response({"success": "Notification read status has been already active"})
		
class CEOMessageSet(viewsets.ModelViewSet):
	queryset = CEOMessage.objects.filter(active_status=1).order_by('-created_date')
	serializer_class = CEOMessageSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		devices = GCMDevice.objects.all()
		for q in devices:
			q.send_message(serializer.data['ceo_message'],title="New message got from CEO",extra={"category":"ceo"})
		return Response({"success": "CEO message posted successfully"}, status=status.HTTP_201_CREATED, headers=headers)

class SearchSet(viewsets.ModelViewSet):
	# queryset = News.objects.all()
	serializer_class = SearchSerializer