from django.shortcuts import render, redirect, get_object_or_404

from resumes.forms import ResumeForm
from resumes.models import Resume


def get_my_resume(request):
    try:
        resume = get_object_or_404(Resume, pk=request.user.id)
    except Resume.DoesNotExist:
        resume = None

    context = {
        "resume": resume
    }
    return render(request, "profile.html", context)


def create_resume(request):
    try:
        Resume.objects.get(owner=request.user)
        return redirect("my-resume")
    except Resume.DoesNotExist:
        form = ResumeForm(request.POST or None, request.FILES or None)
        if request.POST:
            if form.is_valid():
                resume = form.save(commit=False)
                resume.owner = request.user
                resume.save()
            else:
                print(form.errors)
            return redirect("my-resume")
        context = {
            "form": form
        }
        return render(request, "resume.html", context)


def update_resume(request):
    resume = Resume.objects.get(owner=request.user)
    print(resume)
    form = ResumeForm(request.POST or None, request.FILES or None, instance=resume)
    if request.POST:
        if form.is_valid():
            resume = form.save(commit=False)
            resume.owner = request.user
            resume.save()
        else:
            print(form.errors)
        return redirect("my-resume")
    context = {
        "form": form,
        "resume": resume
    }
    return render(request, "resume.html", context)
