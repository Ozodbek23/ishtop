from django.urls import path
from resumes import views

urlpatterns = [
    path("", views.get_my_resume, name="my-resume"),
    path("create/", views.create_resume, name="create-resume"),
    path("update/", views.update_resume, name="update-resume"),
]