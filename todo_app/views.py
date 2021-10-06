from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from random import randrange
from .forms import FeedbackForm
from .models import TasksModel

def user_signup(request):
	if request.method == "POST":
		user_name = request.POST.get("user_name")
		em = request.POST.get("em")
		try:
			user = User.objects.get(email=em)
			return render(request, "user_signup.html", {"msg":"Email already registered"})
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
			user = User.objects.create_user(username=user_name, email=em, password=pw)
			user.save()
			return render(request, "user_signup.html", {"msg":"Password has been sent to your Email Address"})
	else:
		return render(request, "user_signup.html")

def user_login(request):
	if request.method == "POST":
		user_name = request.POST.get("user_name")

		if '@' in user_name:
			user_name = User.objects.get(email=user_name).username
		else:
			user_name = user_name

		pw = request.POST.get("pw")
		remember_me = request.POST.get('remember_me')
		user = authenticate(username=user_name, password=pw)

		if user is not None:
			login(request, user)
			if remember_me == None:
			    request.session.set_expiry(0)

			return redirect("home")
		else:
			return render(request, "user_login.html", {"msg":"Invalid Login"})
	else:
		return render(request, "user_login.html")

def user_forgotpass(request):
	if request.method == "POST":
		em = request.POST.get("em")
		try:
			user = User.objects.get(email=em)
			pw = ""
			text = "abcdefghijklmnopqrstuvwxyz0123456789"
			for i in range(8):
				pw = pw + text[randrange(len(text))]
			subject = "Welcome back to Task App"
			msg = "Your new password is " + str(pw)
			host = 'mail.task.webapp@gmail.com'
			recepient = [em]
			send_mail(subject, msg, host, recepient)
			user.set_password(pw)
			user.save()
			return render(request, "user_forgotpass.html", {"msg":"New Password has been sent to your registered Email Address"})
		except User.DoesNotExist:
			return render(request, "user_forgotpass.html", {"msg":"Not Registered"})
	else:
		return render(request, "user_forgotpass.html")

def user_logout(request):
	logout(request)
	return redirect("user_login")

def home(request):
	if request.user.is_authenticated:
		return render(request, "home.html")
	else:
		return redirect("user_login")

@login_required(login_url="user_login")
def create(request):
	if request.method == "POST":
		task = request.POST['task']
		task_data = TasksModel.objects.create(user=request.user, task=task)
		task_data.save()
		return render(request, "create.html", {"msg":"Task Added"})
	else:
		return render(request, "create.html")

@login_required(login_url="user_login")
def view(request):
	view_tasks = TasksModel.objects.filter(user=request.user)
	return render(request, "view.html", {"view_tasks":view_tasks})

def edit(request, id):
    edit_task = TasksModel.objects.get(task=id)

    if request.method == "POST":
        edit_task.task= request.POST['edit_task']
        completed = request.POST.get('checked', '') == 'on'
        TasksModel.objects.filter(task=id).update(task=edit_task.task, completed=completed)
        return redirect("view")

    return render(request, "edit.html", {"edit_task":edit_task})

def delete(request, id):
	delete_task = TasksModel.objects.filter(task=id).first()
	delete_task.delete()
	return redirect("view")

def feedback(request):
	if request.method == "POST":
		feedback_data = FeedbackForm(request.POST)
		if feedback_data.is_valid():
			feedback_data.save()
			fm = FeedbackForm()
			return render(request, "feedback.html", {"fm":fm, "msg":"Your feedback has been submited"})
		else:
			return render(request, "feedback.html", {"fm":feedback_data, "msg":"Issue"})
	else:
		fm = FeedbackForm()
		return render(request, "feedback.html", {"fm":fm})
