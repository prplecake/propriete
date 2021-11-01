from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import View


class BaseAddView(LoginRequiredMixin, View):
	add_another = False

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial={
			'add_another': self.add_another,
		})
		return render(
			request,
			self.template_name,
			{
				'form': form,
			}
		)

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		try:
			if request.POST['add_another'] == 'on':
				self.add_another = True
		except MultiValueDictKeyError:
			self.add_another = False
		if form.is_valid():
			form.save()	
			if self.add_another:
				pass
			else:
				return HttpResponseRedirect(reverse(self.redirect_target))
		form = self.form_class(initial={
			'add_another': self.add_another,
		})
		return render(
			request,
			self.template_name,
			{
				'form': form
			})


class BaseUpdateView(LoginRequiredMixin, View):
	def get(self, request, id, *args, **kwargs):
		obj = get_object_or_404(self.model_class, id=id)
		form = self.form_class(request.POST or None, instance=obj)
		return render(
			request,
			self.template_name,
			{
				'form': form,
				'obj': obj,
			}
		)

	def post(self, request, id, *args, **kwargs):
		obj = get_object_or_404(self.model_class, id=id)
		form = self.form_class(request.POST or None, instance=obj)
		if form.is_valid():
			form.save()	
			return HttpResponseRedirect(reverse(self.redirect_target))
		form = self.form_class()
		return render(
			request,
			self.template_name,
			{
				'form': form
			})


class BaseDeleteView(LoginRequiredMixin, View):
	def get(self, request, id, *args, **kwargs):
		obj = get_object_or_404(self.model_class, id=id)
		obj.delete()
		return HttpResponseRedirect(reverse(self.redirect_target))
