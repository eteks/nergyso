from django.contrib import admin
from models import PollsAnswer,PollsQuestion,PollsResult
from energysoft.action import export_as_csv_action
# Register your models here.
class PollsAnswerAdmin(admin.ModelAdmin):
	model = PollsAnswer
	list_display = ('answer','created_date','get_questions')
	list_filter = ('created_date',)
	search_fields = ('answer',)
	actions = [export_as_csv_action("CSV Export", fields=['id','answer','created_date'])]

class PollsQuestionAdmin(admin.ModelAdmin):
	model = PollsQuestion
	list_display = ('question','created_date',)
	list_filter = ('created_date',)
	search_fields = ('question',)
	actions = [export_as_csv_action("CSV Export", fields=['id','question','created_date'])]

class PollsResultAdmin(admin.ModelAdmin):
	model = PollsResult
	list_display = ('pollsresult_employee','pollsresult_question','pollsresult_answer')
	list_filter = ('created_date','pollsresult_employee','pollsresult_question','pollsresult_answer')
	def has_add_permission(self, request):
		return False
	# search_fields = ('question',)
	# actions = [export_as_csv_action("CSV Export", fields=['id','question','created_date'])]

admin.site.register(PollsAnswer,PollsAnswerAdmin)	
admin.site.register(PollsQuestion,PollsQuestionAdmin)
admin.site.register(PollsResult,PollsResultAdmin)