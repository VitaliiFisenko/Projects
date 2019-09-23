from django.shortcuts import render
from django.views import generic

from main.models import Student


class Index(generic.ListView):
    template_name = 'main/index.html'
    model = Student
    context_object_name = 'group'

    def get_queryset(self):
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return self.model.objects.get(user=self.request.user).group
