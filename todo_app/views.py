from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from random import randrange
from django.urls import reverse
from .forms import TasksForm, FbForm
from .models import TasksModel, FbModel

def usignup(request):
	if request.method == "POST":
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username=em)
			return render(request, "usignup.html", {"msg":"Already Registered"})
		except User.DoesNotExist:
			pw = ""
			text = "abcdefghijklmnopqrstuvwxyz0123456789"
			for i in range(8):
				pw = pw + text[randrange(len(text))]
			subject = "Welcome to Task App"
			msg = "Your password is " + str(pw)
			host = 'mail.task.webapp@gmail.com'
			recepient = [em]
			send_mail(subject, msg, host, recepient)
			usr = User.objects.create_user(username=em, password=pw)
			usr.save()
			return redirect("ulogin")
	else:
		return render(request, "usignup.html")

def ulogin(request):
	if request.method == "POST":
		em = request.POST.get("em")
		pw = request.POST.get("pw")
		usr = authenticate(username=em, password=pw)
		if usr is not None:
			login(request, usr)
			return redirect("home")
		else:
			return render(request, "ulogin.html", {"msg":"Invalid Login"})
	else:
		return render(request, "ulogin.html")

def uforgotpass(request):
	if request.method == "POST":
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username=em)
			pw = ""
			text = "abcdefghijklmnopqrstuvwxyz0123456789"
			for i in range(8):
				pw = pw + text[randrange(len(text))]
			subject = "Welcome back to Task App"
			msg = "Your new password is " + str(pw)
			host = 'mail.task.webapp@gmail.com'
			recepient = [em]
			send_mail(subject, msg, host, recepient)
			usr.set_password(pw)
			usr.save()
			return redirect("ulogin")
		except User.DoesNotExist:
			return render(request, "uforgotpass.html", {"msg":"Not Registered"})
	else:
		return render(request, "uforgotpass.html")

def ulogout(request):
	logout(request)
	return redirect("ulogin")

def home(request):
	if request.user.is_authenticated:
		return render(request, "home.html")
	else:
		return redirect("ulogin")
def create(request):
	if request.method == "POST":
		task = TasksForm(request.POST)
		if task.is_valid():
			task.save()
			fm = TasksForm()
			return render(request, "create.html", {"fm":fm, "msg":"Task Added"})
		else:
			return render(request, "create.html", {"fm":task, "msg":"Check Issue"})
	else:
		fm = TasksForm()
		return render(request, "create.html", {"fm":fm})

def view(request):
	view_tasks = TasksModel.objects.all()
	return render(request, "view.html", {"view_tasks":view_tasks})

def edit(request, id):
	edit_task = TasksModel.objects.get(task=id)

	fm = TasksForm(instance=edit_task)

	if request.method == "POST":
		task = TasksForm(request.POST, instance=edit_task)
		if task.is_valid():
			task.save()
			fm = TasksForm()
			return redirect("view")
			#view_tasks = TasksModel.objects.all()
			#return render(request, "view.html", {"view_tasks":view_tasks, "msg":"Edited"})

	return render(request, "edit.html", {"fm":fm})

def delete(request, id):
	delete_task = TasksModel.objects.get(task=id)
	delete_task.delete()
	return redirect("view")

def feedback(request):
	if request.method == "POST":
		data = FbForm(request.POST)
		if data.is_valid():
			data.save()
			fm = FbForm()
			return render(request, "feedback.html", {"fm":fm, "msg":"Your feedback has been submited"})
	else:
		fm = FbForm()
		return render(request, "feedback.html", {"fm":fm})