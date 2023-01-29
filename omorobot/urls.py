from django.urls import path
from .views import *

app_name = "omorobot"


urlpatterns = [
    path("", landing, name="landing"),
    path("signin/", signin, name="signin"),
    path("signin/read_user/", read_user, name="signin"),
    path("signup/", signup, name="signup"),
    path("signup/createuser/", create_user, name="create_user"),
    path("detail/<str:pk>/", detail, name="detail"),
    path("input/<str:pk>/createmycar/", create_mycar, name="create_mycar"),
    path("input/<str:pk>/", input, name="input"),
    path("record/<str:fk>/deletemycar/<int:pk>", delete_mycar, name="delete_mycar"),
    path("record/<str:pk>/",record, name="record"),
    path("realtime/<str:pk>/", realtime, name="realtime"),
    path("index/<str:fk>/deletemycar/<int:pk>", delete_mycar_index, name="delete_mycar_index"),
    path("index/<str:pk>/", index, name="index"),  
    path("deleteuser/<str:pk>/", delete_user, name="delete_user"),
]
