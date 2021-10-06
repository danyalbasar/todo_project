from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.urls import path
from todo_app.views import user_signup, user_login, user_forgotpass, user_logout, home, create, view, edit, delete, feedback

urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path("user_signup/", user_signup, name="user_signup"),
    path("user_login/", user_login, name="user_login"),
    path("user_forgotpass/", user_forgotpass, name="user_forgotpass"),
    path("user_logout/", user_logout, name="user_logout"),
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("view/", view, name="view"),
    path("edit/<str:id>", edit, name="edit"),
    path("delete/<str:id>", delete, name="delete"),
    path("feedback/", feedback, name="feedback"),    
]
