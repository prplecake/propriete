from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, DetailView, ListView, TemplateView

from .models import (
	OwnerInfo,
	PolicyInfo,
	Item
)


class IndexView(LoginRequiredMixin, TemplateView):
	template_name = 'inventory/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['ownerinfo'] = OwnerInfo.objects.get(pk=1)
		context['policyinfo'] = PolicyInfo.objects.get(pk=1)
		return context


class InventoryView(LoginRequiredMixin, ListView):
	model = Item
