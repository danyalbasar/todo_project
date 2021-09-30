from django import forms
from .models import TasksModel, FbModel

class TasksForm(forms.ModelForm):
	class Meta:
		model = TasksModel
		widgets = {'completed': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),}
		fields = '__all__'

class FbForm(forms.ModelForm):
	class Meta:
		model = FbModel
		widgets = {'feedback': forms.Textarea(attrs={'rows':6, 'cols':22, 'style':'resize:none;'}),}
		fields = '__all__'
