
from django.views import generic

from main.models import Student


class StudentProfile(generic.ListView):
    template_name = 'profile.html'
    model = Student
    context_object_name = 'student'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Create your views here.
