from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from main.forms import StudentSearching
from main.models import Student, Group


class Index(generic.ListView):
    model = Student
    template_name = 'main/index.html'


class Search(generic.FormView):
    template_name = 'main/search.html'
    form_class = StudentSearching

    def form_valid(self, form):
        data = form.clean()
        student_name = data['name']
        student_surname = data['surname']
        qs = Student.objects.filter(name=student_name, surname=student_surname)
        return self.render_to_response(self.get_context_data(student=qs))





# Create your views here.
