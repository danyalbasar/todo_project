from django.db import models
from django.contrib.auth.models import User

class TasksModel(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	task = models.TextField()
	completed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.task

class FeedbackModel(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	feedback = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
