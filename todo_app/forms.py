from django import forms
from .models import TasksModel, FeedbackModel

class TasksForm(forms.ModelForm):
	class Meta:
		model = TasksModel
		widgets = {'completed': forms.CheckboxInput(attrs={'style':'width:18px; height:18px;'}),}
		fields = '__all__'

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = FeedbackModel
		fields = '__all__'
