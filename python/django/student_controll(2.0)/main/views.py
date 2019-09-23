from django.shortcuts import render
from django.views import generic

from main.models import Student


class Index(generic.TemplateView):
    template_name = 'main/index.html'

    def dispatch(self, request, *args, **kwargs):
        print(self.request.user)
        try:
            return render(request,
                          self.template_name,
                          {'group': Student.objects.get(user=self.request.user).group})
        except:
            return render(request,
                          self.template_name,
                          {})
