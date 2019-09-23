from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

import main


class StudentProfile(generic.ListView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        return render(request, self.template_name, {'student_qs': main.models.Student.objects.filter(user=request.user),
                'user_qs': User.objects.filter(username=request.user)})

# Create your views here.
