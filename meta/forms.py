from django.forms import ModelForm, TextInput

from .models import OwnerInfo, PolicyInfo


class OwnerInfoForm(ModelForm):
    class Meta:
        model = OwnerInfo
        fields = (
            "name",
            "address",
            "phone",
        )
        widgets = {
            "name": TextInput(
                attrs={
                    "autofocus": True
                })
        }


class PolicyInfoForm(ModelForm):
    class Meta:
        model = PolicyInfo
        fields = (
            "policy_number",
            "agent_name",
            "agent_phone",
            "agent_email",
            "company_name",
            "company_claims_phone",
            "company_website",
        )
        widgets = {
            "policy_number": TextInput(
                attrs={
                    "autofocus": True
                })
        }
