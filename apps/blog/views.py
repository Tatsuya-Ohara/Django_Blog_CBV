from django.views.generic import TemplateView, DetailView
from .models import Blog


class HomeView(TemplateView):
    template_name = "index.html"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by("created_at")
        return context


class ArticleView(DetailView):
    template_name = "detail.html"
    model = Blog
