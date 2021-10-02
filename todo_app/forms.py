from django import forms
from .models import TasksModel, FeedbackModel

class TasksForm(forms.ModelForm):
	class Meta:
		model = TasksModel
		fields = '__all__'

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = FeedbackModel
		fields = '__all__'
