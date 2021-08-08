from django.forms import ModelForm

from .models import (
	OwnerInfo,
	PolicyInfo,
	Item,
)


class OwnerInfoForm(ModelForm):
	class Meta:
		model = OwnerInfo
		fields = (
			'name',
			'address',
			'phone',
		)


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


class ItemForm(ModelForm):
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
