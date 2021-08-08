from django.contrib import admin

from .models import (
	OwnerInfo,
	PolicyInfo,
	Tag,
	Item,
	Clothing,
	Location,
)


class PolicyAdmin(admin.ModelAdmin):
	list_display = ('policy_number', 'agent_name', 'company_name',)


admin.site.register(OwnerInfo)
admin.site.register(PolicyInfo, PolicyAdmin)
admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(Clothing)
admin.site.register(Location)
