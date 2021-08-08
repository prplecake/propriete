from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('inventory/', views.InventoryView.as_view(), name='inventory'),
]
