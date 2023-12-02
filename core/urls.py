from django.urls import path, include
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("vacancies/", include("vacancies.urls")),
    path("resumes/", include("resumes.urls"))
]
