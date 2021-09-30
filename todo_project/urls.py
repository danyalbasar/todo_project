from django.contrib import admin
from django.urls import path
from todo_app.views import usignup, ulogin, ulogout, uforgotpass, home, create, view, edit, delete, feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path("usignup/", usignup, name="usignup"),
    path("ulogin/", ulogin, name="ulogin"),
    path("ulogout/", ulogout, name="ulogout"),
    path("uforgotpass/", uforgotpass, name="uforgotpass"),    
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("view/", view, name="view"),
    path("edit/<str:id>", edit, name="edit"),
    path("delete/<str:id>", delete, name="delete"),
    path("feedback/", feedback, name="feedback"),
]
