from django.urls import path
from .views import MainView, AboutView

urlpatterns  = [
    path('', MainView.as_view()),
    path('about/', AboutView.as_view()),
]