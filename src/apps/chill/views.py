from django.views.generic import TemplateView


class ChillView(TemplateView):
    template_name = 'index.html'
