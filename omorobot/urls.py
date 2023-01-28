from django.urls import path
from .views import *

app_name = "omorobot"


urlpatterns = [
    path("", landing, name="landing"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("detail/<str:pk>/", detail, name="detail"),
    path("input/<str:pk>/createmycar/", create_mycar, name="create_mycar"),
    path("input/<str:pk>/", input, name="input"),
    path("record/<str:pk>/",record, name="record"),
    path("realtime/<str:pk>/", realtime, name="realtime"),
    path("index/<str:pk>/", index, name="index"),  
    path("createuser/", create_user, name="create_user"),
    path("read_user/", read_user, name="signin"),
    path("deleteuser/<str:pk>/", delete_user, name="delete_user"),
]
