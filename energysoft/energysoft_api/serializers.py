from rest_framework import serializers
from employee.models import Employee
from news.models import News
from events.models import Events
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import EventsIndex
from rest_framework.authtoken.models import Token
from feedback.models import Feedback
from shoutout.models import Shoutout
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.conf import settings
from push_notifications.models import APNSDevice, GCMDevice
from banner.models import Banner
from gallery.models import Gallery
from livetelecast.models import Livetelecast

# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_department_name = serializers.CharField(source='employee_department.department_name')
    employee_photo = serializers.SerializerMethodField()
    employee_email = serializers.CharField(source='user_ptr.email')

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
        fields = ('id','employee_id','employee_name', 'employee_dob','employee_mobile','employee_email',
                  'employee_doj','employee_designation','employee_photo','employee_bloodgroup',
                  'employee_address','employee_experience_in_years',
                  'employee_device_id','employee_department_name','created_date')

class EmployeeParticularSerializer(serializers.HyperlinkedModelSerializer):   
    class Meta:
        model = Employee
        fields = ('id','employee_name','employee_photo','employee_dob')

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

class FeedbackSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Feedback
        fields = ('id','feedback_description','feedback_queries','feedback_employee', 'feedback_rating_count')

# class ShoutoutPostSerializer(serializers.ModelSerializer): 
#     class Meta:
#         model = Shoutout
#         fields = ('id','shoutout_description','shoutout_employee_from','shoutout_employee_to')

class ShoutoutSerializer(serializers.ModelSerializer): 
    employee_from_name = serializers.ReadOnlyField(source='shoutout_employee_from.employee_name')
    employee_to_name = serializers.ReadOnlyField(source='shoutout_employee_to.employee_name')
    employee_from_profile = serializers.CharField(source='shoutout_employee_from.employee_photo',read_only=True)
    employee_to_profile = serializers.CharField(source='shoutout_employee_to.employee_photo',read_only=True)
    class Meta:
        model = Shoutout
        fields = ('id','shoutout_description','shoutout_employee_from','shoutout_employee_to','employee_from_name','employee_to_name','employee_from_profile','employee_to_profile')

class GallerySerializer(serializers.HyperlinkedModelSerializer):  
    gallery_image = serializers.CharField()  
    class Meta:
        model = Gallery
        fields = ('id','gallery_title','gallery_image')

#Override the inbuild password change serializer to add our custom fields(id) in serialization
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    id = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = getattr(
            settings, 'OLD_PASSWORD_FIELD_ENABLED', False
        )
        self.logout_on_password_change = getattr(
            settings, 'LOGOUT_ON_PASSWORD_CHANGE', False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        if not self.old_password_field_enabled:
            self.fields.pop('old_password')

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value)
        )

        if all(invalid_password_conditions):
            raise serializers.ValidationError('Invalid password')
        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(self.request, self.user)

class NotificationSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = GCMDevice
        # fields = '__all__'
        fields = ('id','registration_id','cloud_message_type')

class BannerSerializer(serializers.HyperlinkedModelSerializer):    
    banner_image = serializers.SerializerMethodField()
    def get_banner_image(self, instance):
        # returning image url if there is an image else blank string
        return instance.banner_image.url if instance.banner_image else ''
    class Meta:
        model = Banner
        # fields = '__all__'
        fields = ('id','banner_image')

class LiveTelecastSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Livetelecast
        fields = ('id', 'livetelecast_url')