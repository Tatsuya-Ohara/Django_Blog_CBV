from django.urls import path
from .views import ToppageView


urlpatterns = [
    path('', ToppageView.as_view(), name='toppage'),
]
