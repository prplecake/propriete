from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView, TemplateView

from .forms import (
	OwnerInfoForm,
	PolicyInfoForm,
)

from .models import (
	OwnerInfo,
	PolicyInfo,
	Item
)


class IndexView(LoginRequiredMixin, TemplateView):
	template_name = 'inventory/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			context['ownerinfo'] = OwnerInfo.objects.get(pk=1)
		except OwnerInfo.DoesNotExist:
			print("Error!")
		try:
			context['policyinfo'] = PolicyInfo.objects.get(pk=1)
		except PolicyInfo.DoesNotExist:
			print("Error!")
		return context


@login_required
def owner_info_create(request):
	if request.method == 'POST':
		form = OwnerInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	form = OwnerInfoForm()
	return render(request, 'inventory/owner_info_form.html', {'form': form})


@login_required
def owner_info_update(request):
	ownerinfo = get_object_or_404(OwnerInfo, id=1)
	form = OwnerInfoForm(request.POST or None, instance=ownerinfo)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/')

	return render(request, 'inventory/owner_info_form.html', {'form': form})


@login_required
def policy_info_create(request):
	if request.method == 'POST':
		form = PolicyInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	form = PolicyInfoForm()
	return render(request, 'inventory/policy_info_form.html', {'form': form})


@login_required
def policy_info_update(request):
	policyinfo = get_object_or_404(PolicyInfo, id=1)
	form = PolicyInfoForm(request.POST or None, instance=policyinfo)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/')

	return render(request, 'inventory/policy_info_form.html', {'form': form})


class InventoryView(LoginRequiredMixin, ListView):
	model = Item
