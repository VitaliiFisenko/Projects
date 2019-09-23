from django.shortcuts import render
from django.views import generic

from main.models import Departament, Teacher


class AdminPanel(generic.ListView):
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_superuser:
            return render(request, 'admin_panel.html')
        else:
            return render(request, 'permission_error.html')


class Connection(generic.ListView):
    template_name = 'connecting.html'
    model = Teacher

    def get_context_data(self, object_list=None, **kwargs):
        try:
            if kwargs['departament'].get():
                print(kwargs['departament'])
                return {'departament': Departament.objects.all(),
                        'choice_departament': kwargs['choiced_departament'],
                        'teachers': Teacher.objects.filter(departament=kwargs['departament'])}
        except:
            return {'departament': Departament.objects.all()}