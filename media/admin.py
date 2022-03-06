from django.contrib import admin

from .models import (
    Album,
    Book,
    Movie,
    Tag,
)

admin.site.register(Album)
admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Tag)
