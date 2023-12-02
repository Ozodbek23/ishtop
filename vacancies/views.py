from django.shortcuts import render, redirect
from professions.models import ProfessionArea, Profession
from resumes.models import Resume
from vacancies.models import Vacancy, Application
from django.core.paginator import Paginator


def get_vacancies(request):
    PER_PAGE = 6

    search = request.GET.get("search", "")
    profession_area = request.GET.get("profession_area", "0")
    profession = request.GET.get("profession", "0")
    page = request.GET.get("page", 1)

    profession_areas = ProfessionArea.objects.all()
    professions = Profession.objects.filter(profession_area_id=profession_area)

    page_obj = get_objects(
        page=page,
        per_page=PER_PAGE,
        profession_area_id=int(profession_area),
        profession_id=int(profession)
    )

    context = {
        "profession_areas": profession_areas,
        "professions": professions,
        "page_obj": page_obj,
        "search": search,
        "profession": int(profession),
        "profession_area": int(profession_area)
    }
    return render(request, "vacancies.html", context)


def get_objects(page, per_page=25, profession_area_id=None, profession_id=None, ):
    filters = {
        "is_active": True,
    }
    if profession_id:
        filters["profession_id"] = profession_id
    else:
        if profession_area_id:
            filters["profession__profession_area_id"] = profession_area_id

    vacancies = Vacancy.objects.filter(
        **filters
    ).order_by(
        "-created_at", "-updated_at"
    )
    print(filters, vacancies)
    paginator = Paginator(vacancies, per_page)
    page_obj = paginator.get_page(page)
    return page_obj


def apply_to_vacancy(request, pk=None):
    vacancy = Vacancy.objects.get(pk=pk)
    resume = Resume.objects.get(owner=request.user)
    application = Application.objects.create(
        vacancy=vacancy,
        resume=resume
    )
    return redirect("vacancies")


def get_applies_vacancies(request):
    PER_PAGE = 6

    search = request.GET.get("search", "")
    profession_area = request.GET.get("profession_area", "0")
    profession = request.GET.get("profession", "0")
    page = request.GET.get("page", 1)

    profession_areas = ProfessionArea.objects.all()
    professions = Profession.objects.filter(profession_area_id=profession_area)
    vacancies = list(
        Application.objects.filter(resume__owner=request.user).values_list("vacancy_id", flat=True)
    )
    print(vacancies, type(vacancies))
    page_obj = get_applied_objects(
        page=page,
        per_page=PER_PAGE,
        profession_area_id=int(profession_area),
        profession_id=int(profession),
        vacancies=vacancies
    )

    context = {
        "profession_areas": profession_areas,
        "professions": professions,
        "page_obj": page_obj,
        "search": search,
        "profession": int(profession),
        "profession_area": int(profession_area)
    }
    return render(request, "vacancies.html", context)


def get_applied_objects(page, per_page=25, profession_area_id=None, profession_id=None, vacancies=None):
    filters = {}
    if vacancies:
        filters["id__in"] = vacancies
    if profession_id:
        filters["profession_id"] = profession_id
    else:
        if profession_area_id:
            filters["profession__profession_area_id"] = profession_area_id

    vacancies = Vacancy.objects.filter(
        **filters
    ).order_by(
        "-created_at", "-updated_at"
    )
    print(filters, vacancies)
    paginator = Paginator(vacancies, per_page)
    page_obj = paginator.get_page(page)
    return page_obj