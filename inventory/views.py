from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView, TemplateView

from .forms import (
	OwnerInfoForm,
	PolicyInfoForm,
	ItemForm,
	LocationForm,
	ClothingForm,
)

from .models import (
	OwnerInfo,
	PolicyInfo,
	Item,
	Location,
	Clothing,
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


@login_required
def item_add(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/inventory/')
	form = ItemForm()
	return render(request, 'inventory/item_form.html', {'form': form})


@login_required
def item_update(request, id):
	item = get_object_or_404(Item, id=id)
	form = ItemForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/inventory/')

	return render(
		request,
		'inventory/item_form.html',
		{
			'form': form,
			'item': item,
		}
	)


@login_required
def item_delete(request, id):
	item = get_object_or_404(Item, id=id)
	item.delete()
	return HttpResponseRedirect('/inventory/')


@login_required
def location_list(request):
	locations = Location.objects.order_by('name')
	return render(
		request,
		'inventory/location_list.html',
		{
			'locations': locations,
		}
	)


@login_required
def location_add(request):
	if request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/inventory/locations/')
	form = LocationForm()
	return render(request, 'inventory/location_form.html', {'form': form})


@login_required
def location_detail(request, id):
	location = get_object_or_404(Location, id=id)
	items = None
	try:
		items = Item.objects.filter(location_id=location.id)
	except Item.DoesNotExist:
		pass

	return render(
		request,
		'inventory/location_detail.html',
		{
			'location': location,
			'item_list': items,
		}
	)


@login_required
def location_delete(request, id):
	location = get_object_or_404(Location, id=id)
	location.delete()
	return HttpResponseRedirect('/inventory/locations/')


class InventoryView(LoginRequiredMixin, ListView):
	model = Item


@login_required
def clothing_list(request):
	clothing = Clothing.objects.order_by('description')
	return render(
		request,
		'inventory/clothing_list.html',
		{
			'clothing_list': clothing,
		}
	)


@login_required
def clothing_add(request):
	if request.method == 'POST':
		form = ClothingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/inventory/clothing/')
	form = ClothingForm()
	return render(request, 'inventory/clothing_form.html', {'form': form})


@login_required
def clothing_update(request, id):
	clothing = get_object_or_404(Clothing, id=id)
	form = ClothingForm(request.POST or None, instance=clothing)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/inventory/clothing/')

	return render(
		request,
		'inventory/clothing_form.html',
		{
			'form': form,
			'clothing': clothing,
		}
	)
