from django.urls import path
from users.views import *


urlpatterns = [
    path("login/", LogInView.as_view()),
    path("logout/", LogOutView.as_view()),
]
