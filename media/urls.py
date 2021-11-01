from django.urls import path

from . import views

app_name = 'media'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),

	path('albums/', views.AlbumList.as_view(), name='album_list'),
	path('album/add/', views.AlbumAdd.as_view(), name='album_add'),
	path('album/<int:id>/edit/', views.AlbumUpdate.as_view(), name='album_update'),
	path('album/<int:id>/delete/', views.AlbumDelete.as_view(), name='album_delete'),

	path('books/', views.BookList.as_view(), name='book_list'),
	path('book/add/', views.BookAdd.as_view(), name='book_add'),
	path('book/<int:id>/edit/', views.BookUpdate.as_view(), name='book_update'),
	path('book/<int:id>/delete/', views.BookDelete.as_view(), name='book_delete'),

	path('movies/', views.MovieList.as_view(), name='movie_list'),
	path('movie/add/', views.MovieAdd.as_view(), name='movie_add'),
	path('movie/<int:id>/edit/', views.MovieUpdate.as_view(), name='movie_update'),
	path('movie/<int:id>/delete/', views.MovieDelete.as_view(), name='movie_delete'),

	path('tags/', views.TagList.as_view(), name='tag_list'),
	path('tag/add/', views.TagAdd.as_view(), name='tag_add'),
	path('tag/<int:id>/edit/', views.TagUpdate.as_view(), name='tag_update'),
	path('tag/<int:id>/delete/', views.TagDelete.as_view(), name='tag_delete'),
]
