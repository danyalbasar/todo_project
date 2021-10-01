from django.contrib import admin
from .models import TasksModel, FeedbackModel

class TasksAdmin(admin.ModelAdmin):
	list_display = ('task', 'completed', 'created')
	list_filter = ('created', 'completed')

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'feedback', 'created')
	list_filter = ('created',)

admin.site.register(TasksModel, TasksAdmin)
admin.site.register(FeedbackModel, FeedbackAdmin)
