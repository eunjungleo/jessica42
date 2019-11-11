from django.shortcuts import render
from django.views.generic import TemplateView


class ResumeView(TemplateView):
    template_name = 'resume_page.html'
