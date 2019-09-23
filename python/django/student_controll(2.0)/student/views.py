from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

import main
from main.models import Student


class StudentProfile(generic.ListView):
    template_name = 'profile.html'
    model = Student
    context_object_name = 'students'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Create your views here.
