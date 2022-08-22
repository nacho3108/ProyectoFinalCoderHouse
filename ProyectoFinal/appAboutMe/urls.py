from django.urls import path
from appAboutMe.views import aboutMe


urlpatterns = [
    path('aboutMe/', aboutMe, name="AboutMe"),
]
