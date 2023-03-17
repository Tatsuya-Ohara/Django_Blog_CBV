from django.views.generic import TemplateView
from .models import Blog


class ToppageView(TemplateView):
    template_name = "index.html"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context
