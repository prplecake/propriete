from django.urls import path

from . import views

app_name = 'meta'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),

	path('meta/owner_info_create/', views.owner_info_create, name='owner_info_create'),
	path('meta/policy_info_create/', views.policy_info_create, name='policy_info_create'),
	path('meta/owner_info_update/', views.owner_info_update, name='owner_info_update'),
	path('meta/policy_info_update/', views.policy_info_update, name='policy_info_update'),
]
