from django.forms import BooleanField, ModelForm, TextInput

from .models import (
	OwnerInfo,
	PolicyInfo,
	Item,
	Location,
	Clothing,
)


class OwnerInfoForm(ModelForm):
	class Meta:
		model = OwnerInfo
		fields = (
			'name',
			'address',
			'phone',
		)
		widgets = {
			'name': TextInput(
				attrs={
					'autofocus': True
				})
		}


class PolicyInfoForm(ModelForm):
	class Meta:
		model = PolicyInfo
		fields = (
			'policy_number',
			'agent_name',
			'agent_phone',
			'agent_email',
			'company_name',
			'company_claims_phone',
			'company_website',
		)
		widgets = {
			'policy_number': TextInput(
				attrs={
					'autofocus': True
				})
		}


class ItemForm(ModelForm):
	add_another = BooleanField(required=False)

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
			'add_another',
		)
		widgets = {
			'description': TextInput(
				attrs={
					'autofocus': True
				})
		}


class LocationForm(ModelForm):
	add_another = BooleanField(required=False)

	class Meta:
		model = Location
		fields = (
			'name',
			'add_another',
		)
		widgets = {
			'name': TextInput(
				attrs={
					'autofocus': True
				})
		}


class ClothingForm(ModelForm):
	add_another = BooleanField(required=False)

	class Meta:
		model = Clothing
		fields = (
			'description',
			'brand',
			'quantity',
			'notes',
			'add_another',
		)
		widgets = {
			'description': TextInput(
				attrs={
					'autofocus': True
				})
		}
