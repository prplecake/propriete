from django.forms import BooleanField, ModelForm, TextInput

from .models import (
    Item,
    Location,
    Clothing,
)


class BaseItemForm(ModelForm):
    class Meta:
        model = Item
        fields = (
            'description',
            'location',
            'make',
            'serial_number',
            'purchase_date',
            'purchase_location',
            'purchase_price',
            'current_value',
            'photo',
            'notes',
        )
        widgets = {
            'description': TextInput(
                attrs={
                    'autofocus': True
                })
        }


class ItemAddForm(BaseItemForm):
    add_another = BooleanField(required=False)

    class Meta:
        model = Item
        fields = BaseItemForm.Meta.fields + ('add_another',)


class ItemUpdateForm(BaseItemForm):
    pass


class BaseLocationForm(ModelForm):
    class Meta:
        model = Location
        fields = (
            'name',
        )
        widgets = {
            'name': TextInput(
                attrs={
                    'autofocus': True
                })
        }


class LocationAddForm(BaseLocationForm):
    add_another = BooleanField(required=False)

    class Meta:
        model = Location
        fields = BaseLocationForm.Meta.fields + ('add_another',)


class LocationUpdateForm(BaseLocationForm):
    pass


class BaseClothingForm(ModelForm):
    class Meta:
        model = Clothing
        fields = (
            'description',
            'brand',
            'quantity',
            'notes',
        )
        widgets = {
            'description': TextInput(
                attrs={
                    'autofocus': True
                })
        }


class ClothingAddForm(BaseClothingForm):
    add_another = BooleanField(required=False)

    class Meta:
        model = Clothing
        fields = BaseClothingForm.Meta.fields + ('add_another',)


class ClothingUpdateForm(BaseClothingForm):
    pass
