from django.forms import BooleanField, ModelForm, TextInput

from .models import (
	Album,
	Book,
	Movie,
	Tag,
)


class BaseAlbumForm(ModelForm):
	class Meta:
		model = Album
		fields = (
			'description',
			'artist',
			'serial_number',
			'purchase_date',
			'purchase_location',
			'purchase_price',
			'current_value',
			'notes',
		)
		widgets = {
			'description': TextInput(
				attrs={
					'autofocus': True
				})
		}


class AlbumAddForm(BaseAlbumForm):
	add_another = BooleanField(required=False)

	class Meta:
		model = Album
		fields = BaseAlbumForm.Meta.fields + ('add_another',)


class AlbumUpdateForm(BaseAlbumForm):
	pass


class BaseBookForm(ModelForm):
	class Meta:
		model = Book
		fields = (
			'description',
			'author',
			'serial_number',
			'purchase_date',
			'purchase_location',
			'purchase_price',
			'current_value',
			'notes',
		)
		widgets = {
			'description': TextInput(
				attrs={
					'autofocus': True
				})
		}


class BookAddForm(BaseBookForm):
	add_another = BooleanField(required=False)

	class Meta:
		model = Book
		fields = BaseBookForm.Meta.fields + ('add_another',)


class BookUpdateForm(BaseBookForm):
	pass


class BaseMovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = (
			'description',
			'year',
			'serial_number',
			'purchase_date',
			'purchase_location',
			'purchase_price',
			'current_value',
			'notes',
		)
		widgets = {
			'description': TextInput(
				attrs={
					'autofocus': True
				})
		}


class MovieAddForm(BaseMovieForm):
	add_another = BooleanField(required=False)

	class Meta:
		model = Movie
		fields = BaseMovieForm.Meta.fields + ('add_another',)


class MovieUpdateForm(BaseMovieForm):
	pass


class BaseTagForm(ModelForm):
	class Meta:
		model = Tag
		fields = (
			'name',
		)
		widgets = {
			'name': TextInput(
				attrs={
					'autofocus': True
				})
		}


class TagAddForm(BaseTagForm):
	add_another = BooleanField(required=False)

	class Meta:
		model = Tag
		fields = BaseTagForm.Meta.fields + ('add_another',)


class TagUpdateForm(BaseTagForm):
	pass
