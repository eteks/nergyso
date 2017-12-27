from rest_framework import serializers
from employee.models import Employee
from news.models import News
from events.models import Events
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import EventsIndex
from rest_framework.authtoken.models import Token
from feedback.models import Feedback
from shoutout.models import Shoutout

# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_department_name = serializers.CharField(source='employee_department.department_name')
    employee_photo = serializers.SerializerMethodField()

    def get_employee_photo(self, instance):
        # returning image url if there is an image else blank string
        return instance.employee_photo.url if instance.employee_photo else ''
        
    class Meta:
        model = Employee
        # fields = '__all__'
        # lookup_field = 'department_name'
        # extra_kwargs = {
        #     'department_name': {'lookup_field': 'department_name'}
        # }
        fields = ('id','employee_id','employee_name', 'employee_dob','employee_mobile',
                  'employee_doj','employee_designation','employee_photo','employee_bloodgroup',
                  'employee_address','employee_experience_in_years',
                  'employee_device_id','employee_department_name','created_date')
#Commented because of haystack not working properly while indexing
# class EventsSerializer(HaystackSerializer):
#     # id = serializers.CharField(allow_blank=False, write_only=True)
#     # events_title = serializers.CharField(allow_blank=False, write_only=True)
#     # events_description = serializers.CharField(allow_blank=False, write_only=True)
#     # events_location_for_map = serializers.CharField(allow_blank=False, write_only=True)
#     # events_date = serializers.CharField(allow_blank=False, write_only=True)
#     # events_video = serializers.CharField(allow_blank=False, write_only=True)
#     # events_image = serializers.CharField(allow_blank=False, write_only=True)
#     # events_document = serializers.CharField(allow_blank=False, write_only=True)
#     class Meta:
#         index_classes = [EventsIndex]
#         # exclude = ('page', 'per_page', )
#         fields = ('id', 'events_title', 'events_description', 'events_location_for_map','events_venue',
#             'events_date','events_image','events_video','events_document','created_date')

#         # fields = ('events_title', 'events_description', 'events_date')
#     # def get_queryset(self, *args, **kwargs):
#     #     request = self.request
#     #     queryset = EmptySearchQuerySet()
#     #     if request.GET.get('q') is not None:
#     #         query = request.GET.get('q')
#     #         queryset = SearchQuerySet().all()
#     #     return [i.object for i in queryset]

class EventsSerializer(serializers.HyperlinkedModelSerializer):
    events_image = serializers.SerializerMethodField()
    events_video = serializers.SerializerMethodField()
    events_document = serializers.SerializerMethodField()

    def get_events_image(self, instance):
        return instance.events_image.url if instance.events_image else ''
    def get_events_video(self, instance):
        return instance.events_video.url if instance.events_video else ''
    def get_events_document(self, instance):
        return instance.events_document.url if instance.events_document else ''

    class Meta:
        model = Events
        fields = ('id', 'events_title', 'events_description', 'events_location_for_map','events_venue',
                'events_date','events_image','events_video','events_document','created_date')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    news_image = serializers.SerializerMethodField()
    news_video = serializers.SerializerMethodField()
    news_document = serializers.SerializerMethodField()

    def get_news_image(self, instance):
        # returning image url if there is an image else blank string
        return instance.news_image.url if instance.news_image else ''
    def get_news_video(self, instance):
        return instance.news_video.url if instance.news_video else ''
    def get_news_document(self, instance):
        return instance.news_document.url if instance.news_document else ''

    class Meta:
        model = News
        fields = ('id', 'news_title', 'news_description', 'news_image','news_video','news_document','created_date')

class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    class Meta:
        model = Token
        fields = ('key', 'user','username','email')

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Feedback
        fields = ('id','feedback_description','feedback_queries','feedback_employee', 'feedback_category', 'feedback_rating_count')

class ShoutoutSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Shoutout
        fields = ('id','shoutout_description','shoutout_employee')