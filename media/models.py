from django.db import models
from django.utils import timezone


class Tag(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, editable=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Album(models.Model):
	description = models.CharField(max_length=500)
	artist = models.CharField(max_length=255)
	notes = models.TextField(blank=True)
	serial_number = models.CharField(max_length=200, blank=True)
	purchase_date = models.DateField(null=True, blank=True)
	created_at = models.DateTimeField(default=timezone.now)
	purchase_location = models.CharField(max_length=200, blank=True)
	purchase_price = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	current_value = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	tags = models.ManyToManyField(Tag, related_name='album', blank=True)

	def __str__(self):
		return self.description

	class Meta:
		ordering = ['artist', 'description']


class Book(models.Model):
	description = models.CharField(max_length=500)
	author = models.CharField(max_length=255)
	notes = models.TextField(blank=True)
	serial_number = models.CharField(max_length=200, blank=True)
	purchase_date = models.DateField(null=True, blank=True)
	created_at = models.DateTimeField(default=timezone.now)
	purchase_location = models.CharField(max_length=200, blank=True)
	purchase_price = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	current_value = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	tags = models.ManyToManyField(Tag, related_name='book', blank=True)

	def __str__(self):
		return self.description

	class Meta:
		ordering = ['author', 'description']


class Movie(models.Model):
	description = models.CharField(max_length=500)
	year = models.IntegerField()
	notes = models.TextField(blank=True)
	serial_number = models.CharField(max_length=200, blank=True)
	purchase_date = models.DateField(null=True, blank=True)
	created_at = models.DateTimeField(default=timezone.now)
	purchase_location = models.CharField(max_length=200, blank=True)
	purchase_price = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	current_value = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	tags = models.ManyToManyField(Tag, related_name='movie', blank=True)

	def __str__(self):
		return self.description

	class Meta:
		ordering = ['year', 'description']
