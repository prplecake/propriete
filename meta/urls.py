from django.urls import path

from . import views

app_name = 'meta'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path(
        'meta/owner_info_create/',
        views.OwnerInfoCreate.as_view(),
        name='owner_info_create'
    ),
    path(
        'meta/policy_info_create/',
        views.PolicyInfoCreate.as_view(),
        name='policy_info_create'
    ),
    path(
        'meta/owner_info_update/',
        views.OwnerInfoUpdate.as_view(),
        name='owner_info_update'
    ),
    path(
        'meta/policy_info_update/',
        views.PolicyInfoUpdate.as_view(),
        name='policy_info_update'
    ),
]
