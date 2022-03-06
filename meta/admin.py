from django.contrib import admin

from .models import (
    OwnerInfo,
    PolicyInfo,
)


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'agent_name', 'company_name',)


admin.site.register(OwnerInfo)
admin.site.register(PolicyInfo, PolicyAdmin)
