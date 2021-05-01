from django.shortcuts import render
from django.views import View
from .models import Resume
from .forms import CreateResumeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.


class ResumeView(View):

    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume/resume.html',
                      context={'resumes': resumes, 'is_staff': User.is_staff}
                      )


class NewResumeView(View):
    resumes = Resume.objects.all()

    def get(self, request, *args, **kwargs):

        return render(request, 'resume/new.html',
                      context={'form': CreateResumeForm, }
                      )

    def post(self, request, *args, **kwargs):
        form = CreateResumeForm(request.POST)
        if form.is_valid():
            author = request.user
            description = form.cleaned_data['description']
            resume = Resume.objects.create(description=description, author=author)
            return redirect("/home")
