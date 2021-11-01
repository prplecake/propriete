from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .forms import (
	OwnerInfoForm,
	PolicyInfoForm,
)

from .models import (
	OwnerInfo,
	PolicyInfo,
)


class IndexView(LoginRequiredMixin, TemplateView):
	template_name = 'meta/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			context['owner_info'] = OwnerInfo.objects.get(pk=1)
		except OwnerInfo.DoesNotExist:
			pass
		try:
			context['policy_info'] = PolicyInfo.objects.get(pk=1)
		except PolicyInfo.DoesNotExist:
			pass
		return context


@login_required
def owner_info_create(request):
	if request.method == 'POST':
		form = OwnerInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	form = OwnerInfoForm()
	return render(request, 'meta/generic_form.html', {'form': form})


@login_required
def owner_info_update(request):
	ownerinfo = get_object_or_404(OwnerInfo, id=1)
	form = OwnerInfoForm(request.POST or None, instance=ownerinfo)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/')

	return render(request, 'meta/generic_form.html', {'form': form})


@login_required
def policy_info_create(request):
	if request.method == 'POST':
		form = PolicyInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	form = PolicyInfoForm()
	return render(request, 'meta/generic_form.html', {'form': form})


@login_required
def policy_info_update(request):
	policyinfo = get_object_or_404(PolicyInfo, id=1)
	form = PolicyInfoForm(request.POST or None, instance=policyinfo)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/')

	return render(request, 'meta/generic_form.html', {'form': form})
