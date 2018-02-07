from haystack import indexes
from events.models import Events
from django.utils import timezone

class EventsIndex(indexes.SearchIndex, indexes.Indexable):
    id = indexes.CharField(model_attr='pk', indexed=False)
    text = indexes.CharField(document=True, use_template=True)
    events_title = indexes.CharField(model_attr='events_title')
    events_description = indexes.CharField(model_attr='events_description')
    events_location_for_map = indexes.CharField(model_attr='events_location_for_map')
    events_date = indexes.DateTimeField(model_attr='events_date',null=True)
    events_image = indexes.CharField(model_attr='events_image')
    events_video = indexes.CharField(model_attr='events_video')
    events_document = indexes.CharField(model_attr='events_document')

    autocomplete = indexes.EdgeNgramField()

    # content_auto = indexes.EdgeNgramField(model_attr='content')

    # @staticmethod
    # def prepare_autocomplete(obj):
    #     return " ".join((
    #         obj.address, obj.city, obj.zip_code
    #     ))

    # def prepare(self, obj):
    #     self.prepared_data = super(EventsIndex, self).prepare(obj)
    #     # exps = obj.experience_set.all()
    #     # self.prepared_data['events_image'] = join(settings.IMAGES_ROOT).obj.events_image
    #     self.prepared_data['events_image'] = obj.events_image.prepend(settings.IMAGES_ROOT)
    #     # self.prepared_data['exp_companies'] = ','.join([e.company for e in exps])
    #     # self.prepared_data['exp_post_names'] = ','.join([e.post_name for e in exps])

    #     return self.prepared_data

    # def prepare_events_image(self, obj):
    #     test = self.events_image.split(",")
    #     print test
    #     # for obj.events_image.split(",") in e:
    #     #     print e
    #     # events_set = [e.path for obj.events_image.split(",") in e] 
    #     return self.events_image.path

    def get_model(self):
        return Events

    def autoUpdateRebuild_index(self):
        update_index.Command().handle()
        rebuild_index.Command().handle()
    
    def index_queryset(self, **kwargs):
        return self.get_model().objects.all().order_by('-id')

    # def index_queryset(self, using=None):
    #     # return self.get_model().objects.filter(
    #     #     created_date__lte=timezone.now()
    #     # )
    #     return self.get_model().objects.all()