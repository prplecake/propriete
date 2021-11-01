from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
	path('', views.InventoryView.as_view(), name='inventory'),
	
	path('item/add/', views.item_add, name='item_add'),
	path('item/<int:id>/edit/', views.item_update, name='item_update'),
	path('item/<int:id>/delete/', views.item_delete, name='item_delete'),

	path('locations/', views.location_list, name='location_list'),
	path('locations/add/', views.location_add, name='location_add'),
	path('locations/<int:id>/', views.location_detail, name='location_detail'),
	path('locations/<int:id>/delete/', views.location_delete, name='location_delete'),

	path('clothing/', views.clothing_list, name='clothing_list'),
	path('clothing/add/', views.clothing_add, name='clothing_add'),
	path('clothing/<int:id>/edit/', views.clothing_update, name='clothing_update'),
	path('clothing/<int:id>/delete/', views.clothing_delete, name='clothing_delete'),
]
