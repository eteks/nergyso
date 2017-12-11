from rest_framework import serializers
from employee.models import Employee
from news.models import News
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import EventsIndex
# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'employee_dob', 'employee_email')

class EventsSerializer(HaystackSerializer):
    class Meta:
        index_classes = [EventsIndex]
        exclude = ('page', 'per_page', )
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
        fields = ('id', 'news_title', 'news_description', 'news_image','news_video','news_document',)