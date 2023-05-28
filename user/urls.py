from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth

urlpatterns = [
    path("", views.index, name="index")
]
