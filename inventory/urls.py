from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.InventoryView.as_view(), name="inventory"),

    path("item/add/", views.ItemAdd.as_view(), name="item_add"),
    path(
        "item/<int:id>/edit/",
        views.ItemUpdate.as_view(),
        name="item_update"
    ),
    path(
        "item/<int:id>/delete/",
        views.ItemDelete.as_view(),
        name="item_delete"
    ),

    path("locations/", views.LocationList.as_view(), name="location_list"),
    path("locations/add/", views.LocationAdd.as_view(), name="location_add"),
    path(
        "locations/<int:id>/",
        views.LocationDetail.as_view(),
        name="location_detail"
    ),
    path(
        "locations/<int:id>/delete/",
        views.LocationDelete.as_view(),
        name="location_delete"
    ),

    path("clothing/", views.ClothingList.as_view(), name="clothing_list"),
    path("clothing/add/", views.ClothingAdd.as_view(), name="clothing_add"),
    path(
        "clothing/<int:id>/edit/",
        views.ClothingUpdate.as_view(),
        name="clothing_update"
    ),
    path(
        "clothing/<int:id>/delete/",
        views.ClothingDelete.as_view(),
        name="clothing_delete"
    ),
]
