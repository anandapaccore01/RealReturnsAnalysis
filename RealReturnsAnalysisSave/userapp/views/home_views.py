from django.shortcuts import render
from userapp.models import *

# Create your views here.


def home(request):
    users = Users.objects.all()
    roles = Roles.objects.all()
    return render(
        request, template_name="home.html", context={"users": users, "roles": roles}
    )
