from django.db import models

class TasksModel(models.Model):
	task = models.CharField(max_length=150)
	completed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.task

class FbModel(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	feedback = models.TextField()
	created = models.DateTimeField(auto_now_add=True)