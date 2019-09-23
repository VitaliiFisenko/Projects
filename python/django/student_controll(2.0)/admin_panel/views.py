from django.shortcuts import render
from django.views import generic

from main.models import Departament, Teacher


class AdminPanel(generic.TemplateView):
    template_name = 'permission_error.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.template_name = 'admin_panel.html'
        return super().dispatch(request, *args, **kwargs, )


class Connection(generic.ListView):
    template_name = 'connecting.html'
    model = Teacher

    def get_context_data(self, *args, **kwargs):
        return {'departament': Departament.objects.all(),
                'choice_departament': kwargs.get('choiced_departament'),
                'teachers': Teacher.objects.filter(departament=kwargs.get('departament'))}