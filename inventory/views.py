from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView

from .forms import (
	ItemForm,
	LocationForm,
	ClothingForm,
)

from .models import (
	Item,
	Location,
	Clothing,
)


@login_required
def item_add(request):
	add_another = False
	if request.method == 'POST':
		form = ItemForm(request.POST)
		try:
			if request.POST['add_another'] == 'on':
				add_another = True
		except MultiValueDictKeyError:
			add_another = False
		if form.is_valid():
			form.save()
			if add_another:
				pass
			else:
				return HttpResponseRedirect('/inventory/')
	form = ItemForm(
		initial={
			'add_another': add_another,
		})
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
	add_another = False
	if request.method == 'POST':
		form = LocationForm(request.POST)
		try:
			if request.POST['add_another'] == 'on':
				add_another = True
		except MultiValueDictKeyError:
			add_another = False
		if form.is_valid():
			form.save()
			if add_another:
				pass
			else:
				return HttpResponseRedirect('/inventory/locations/')
	form = LocationForm(
		initial={
			'add_another': add_another,
		})
	return render(request, 'inventory/location_form.html', {'form': form})


@login_required
def location_detail(request, id):
	location = get_object_or_404(Location, id=id)
	items = Item.objects.filter(location_id=location.id)

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
	add_another = False
	if request.method == 'POST':
		form = ClothingForm(request.POST)
		try:
			if request.POST['add_another'] == 'on':
				add_another = True
		except MultiValueDictKeyError:
			add_another = False
		if form.is_valid():
			form.save()
			if add_another:
				pass
			else:
				return HttpResponseRedirect('/inventory/clothing/')
	form = ClothingForm(
		initial={
			'add_another': add_another,
		})
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


@login_required
def clothing_delete(request, id):
	clothing = get_object_or_404(Clothing, id=id)
	clothing.delete()
	return HttpResponseRedirect('/inventory/clothing/')
