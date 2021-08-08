from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('inventory/', views.InventoryView.as_view(), name='inventory'),
	
	path('inventory/owner_info_create/', views.owner_info_create),
	path('inventory/policy_info_create/', views.policy_info_create),
	path('inventory/owner_info_update/', views.owner_info_update),
	path('inventory/policy_info_update/', views.policy_info_update),
	
	path('inventory/item/add/', views.item_add, name='item_add'),
	path('inventory/item/<int:id>/edit/', views.item_update, name='item_update'),
	path('inventory/item/<int:id>/delete/', views.item_delete, name='item_delete'),
]
