from rest_framework import serializers
from employee.models import Employee
from news.models import News
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import EventsIndex
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
        fields = ('id', 'employee_name', 'employee_dob', 'employee_email','employee_mobile',
                  'employee_doj','employee_designation','employee_photo','employee_bloodgroup',
                  'employee_address','employee_aadhar_id','employee_experience_in_years',
                  'employee_device_id','employee_department_name')

class EventsSerializer(HaystackSerializer):
    # id = serializers.CharField(allow_blank=False, write_only=True)
    # events_title = serializers.CharField(allow_blank=False, write_only=True)
    # events_description = serializers.CharField(allow_blank=False, write_only=True)
    # events_location_for_map = serializers.CharField(allow_blank=False, write_only=True)
    # events_date = serializers.CharField(allow_blank=False, write_only=True)
    # events_video = serializers.CharField(allow_blank=False, write_only=True)
    # events_image = serializers.CharField(allow_blank=False, write_only=True)
    # events_document = serializers.CharField(allow_blank=False, write_only=True)
    class Meta:
        index_classes = [EventsIndex]
        # exclude = ('page', 'per_page', )
        fields = ('id', 'events_title', 'events_description', 'events_location_for_map','events_venue',
            'events_date','events_image','events_video','events_document')

        # fields = ('events_title', 'events_description', 'events_date')
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     queryset = EmptySearchQuerySet()
    #     if request.GET.get('q') is not None:
    #         query = request.GET.get('q')
    #         queryset = SearchQuerySet().all()
    #     return [i.object for i in queryset]

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'news_title', 'news_description', 'news_image','news_video','news_document')