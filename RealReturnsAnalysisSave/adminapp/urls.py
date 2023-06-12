from django.urls import path
from adminapp.views import *

app_name = "adminapp"

urlpatterns = [
    path("", admin_home, name="admin-home"),
]
