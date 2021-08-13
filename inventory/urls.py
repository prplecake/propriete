from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('inventory/', views.InventoryView.as_view(), name='inventory'),
	
	path('inventory/owner_info_create/', views.owner_info_create, name='owner_info_create'),
	path('inventory/policy_info_create/', views.policy_info_create, name='policy_info_create'),
	path('inventory/owner_info_update/', views.owner_info_update, name='owner_info_update'),
	path('inventory/policy_info_update/', views.policy_info_update, name='policy_info_update'),
	
	path('inventory/item/add/', views.item_add, name='item_add'),
	path('inventory/item/<int:id>/edit/', views.item_update, name='item_update'),
	path('inventory/item/<int:id>/delete/', views.item_delete, name='item_delete'),

	path('inventory/locations/', views.location_list, name='location_list'),
	path('inventory/locations/add/', views.location_add, name='location_add'),
	path('inventory/locations/<int:id>/', views.location_detail, name='location_detail'),
	path('inventory/locations/<int:id>/delete/', views.location_delete, name='location_delete'),

	path('inventory/clothing/', views.clothing_list, name='clothing_list'),
	path('inventory/clothing/add/', views.clothing_add, name='clothing_add'),
	path('inventory/clothing/<int:id>/edit/', views.clothing_update, name='clothing_update'),
	path('inventory/clothing/<int:id>/delete/', views.clothing_delete, name='clothing_delete'),
]
