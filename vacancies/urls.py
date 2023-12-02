from django.urls import path
from vacancies import views

urlpatterns = [
    path("", views.get_vacancies, name="vacancies"),
    path("applies/", views.get_applies_vacancies, name="applied_vacancies"),
    path("<int:pk>/apply/", views.apply_to_vacancy, name="apply"),
]
