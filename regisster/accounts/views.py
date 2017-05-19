from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Home(LoginRequiredMixin,TemplateView):
	login_url = 'registration/login.html'
	template_name = 'home.html'

class front(TemplateView):
	template_name = "base.html"

	