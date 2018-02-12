# import csv
# from django.http import HttpResponse

# def export_as_csv_action(description="Export selected objects as CSV file",
#                          fields=None, exclude=None, header=True):
#     """
#     This function returns an export csv action
#     'fields' and 'exclude' work like in django ModelForm
#     'header' is whether or not to output the column names as the first row
#     """
#     def export_as_csv(modeladmin, request, queryset):
#         """
#         Generic csv export admin action.
#         based on http://djangosnippets.org/snippets/1697/
#         """
#         from django.utils.encoding import smart_str
#         opts = modeladmin.model._meta
#         field_names = set([field.name for field in opts.fields])
#         if fields:
#             fieldset = set(fields)
#             field_names = field_names & fieldset
#         elif exclude:
#             excludeset = set(exclude)
#             field_names = field_names - excludeset

        
#         response = HttpResponse(content_type='text/csv')        
#         response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
#         writer = csv.writer(response, csv.excel)
#         response.write(u'\ufeff'.encode('utf8'))
#         # writer = csv.writer(response)
#         if header:
#             writer.writerow(list(field_names))
#         for obj in queryset:
#             writer.writerow([unicode(getattr(obj, field)).encode("utf-8","replace") for field in field_names])
#         return response
#     export_as_csv.short_description = description
#     return export_as_csv
import csv
from django.http import HttpResponse

def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        opts = modeladmin.model._meta
        field_names = set([field.name for field in opts.fields])
        if fields:
            fieldset = set(fields)
            field_names = field_names & fieldset
        elif exclude:
            excludeset = set(exclude)
            field_names = field_names - excludeset

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % str(opts).replace('.', '_')

        writer = csv.writer(response)
        if header:
            writer.writerow(list(field_names))
        for obj in queryset:
            writer.writerow([unicode(getattr(obj, field)).encode("utf-8","replace") for field in field_names])
        return response
    export_as_csv.short_description = description
    return export_as_csv

import os
from django.core.files.storage import default_storage
from django.db.models import FileField
def file_cleanup(sender, **kwargs):
    for fieldname in sender._meta.get_all_field_names():
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None
            if field and isinstance(field, FileField):
                inst = kwargs['instance']
                f = getattr(inst, fieldname)
                m = inst.__class__._default_manager
            if hasattr(f, 'path') and os.path.exists(f.path)\
            and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)})\
            .exclude(pk=inst._get_pk_val()):
                try:
                    default_storage.delete(f.path)
                except:
                    pass