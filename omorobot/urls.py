from django.urls import path
from .views import *

urlpatterns = [
    path("", landing, name="landing"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("index/", index, name="index"),
    path("detail/", detail, name="detail"),
    path("input/", input, name="input"),
    path("record/",record, name="record"),
    path("realtime/", realtime, name="realtime")
]
