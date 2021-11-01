from django.contrib import admin

from .models import (
	Tag,
	Item,
	Clothing,
	Location,
)


admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(Clothing)
admin.site.register(Location)
