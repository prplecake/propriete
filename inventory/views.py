import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View

from generic.views import (
    BaseAddView,
    BaseDeleteView,
    BaseUpdateView,
)

from .forms import (
    ClothingAddForm,
    ClothingUpdateForm,
    ItemAddForm,
    ItemUpdateForm,
    LocationAddForm,
    LocationUpdateForm,
)

from .models import (
    Clothing,
    Item,
    Location,
)


logger = logging.getLogger(__name__)

class ItemAdd(BaseAddView):
    form_class = ItemAddForm
    template_name = 'inventory/item_form.html'
    redirect_target = 'inventory:inventory'


class ItemUpdate(BaseUpdateView):
    model_class = Item
    form_class = ItemUpdateForm
    template_name = 'inventory/item_form.html'
    redirect_target = 'inventory:inventory'


class ItemDelete(BaseDeleteView):
    model_class = Item
    redirect_target = 'inventory:inventory'


class LocationList(LoginRequiredMixin, ListView):
    model = Location


class LocationAdd(BaseAddView):
    form_class = LocationAddForm
    template_name = 'inventory/location_form.html'
    redirect_target = 'inventory:location_list'


class LocationDetail(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
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


class LocationUpdate(BaseUpdateView):
    model_class = Location
    form_class = LocationUpdateForm
    template_name = 'inventory/location_form.html'
    redirect_target = 'inventory:location_list'


class LocationDelete(BaseDeleteView):
    model_class = Location
    redirect_target = 'inventory:location_list'


class ClothingList(LoginRequiredMixin, ListView):
    model = Clothing


class ClothingAdd(BaseAddView):
    form_class = ClothingAddForm
    template_name = 'inventory/clothing_form.html'
    redirect_target = 'inventory:clothing_list'


class ClothingUpdate(BaseUpdateView):
    model_class = Clothing
    form_class = ClothingUpdateForm
    template_name = 'inventory/clothing_form.html'
    redirect_target = 'inventory:clothing_list'


class ClothingDelete(BaseDeleteView):
    model_class = Clothing
    redirect_target = 'inventory:clothing_list'


class InventoryView(LoginRequiredMixin, ListView):
    model = Item
