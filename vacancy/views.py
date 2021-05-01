from django.shortcuts import render
from django.views import View
from .models import Vacancy
from .forms import CreateVacancyForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/vacancy.html',
                      context={'vacancies': vacancies, 'is_staff': User.is_staff}
                      )


class NewVacancyView(View):
    vacancies = Vacancy.objects.all()

    def get(self, request, *args, **kwargs):
        if not User.is_staff:
            return render(request, 'vacancy/new.html',
                          context={'form': CreateVacancyForm, }
                          )
        else:
            return HttpResponse(status=403)

    def post(self, request, *args, **kwargs):
        if not User.is_staff:
            form = CreateVacancyForm(request.POST)
            if form.is_valid():
                author = request.user
                description = form.cleaned_data['description']
                vacancy = Vacancy.objects.create(description=description, author=author)
                return redirect("/home")
        else:
            return HttpResponse(status=403)
