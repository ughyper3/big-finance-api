from django.shortcuts import render
from django.views.generic import TemplateView


class Documentation(TemplateView):
    template_name = "documentation.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
