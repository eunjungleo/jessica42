from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'mainpage_home.html'

class AboutView(TemplateView):
    template_name = 'mainpage_about.html'

