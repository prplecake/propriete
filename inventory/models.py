from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Tag(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, editable=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Location(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, editable=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name, allow_unicode=True)
		super().save(*args, **kwargs)


class Item(models.Model):
	description = models.CharField(max_length=500)
	notes = models.TextField(blank=True)
	serial_number = models.CharField(max_length=200, blank=True)
	purchase_date = models.DateField(null=True, blank=True)
	created_at = models.DateTimeField(default=timezone.now)
	photo = models.BooleanField()
	purchase_location = models.CharField(max_length=200, blank=True)
	purchase_price = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	current_value = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
	make = models.CharField(max_length=255, blank=True)
	tags = models.ManyToManyField(Tag, related_name='item', blank=True)

	def __str__(self):
		return self.description

	class Meta:
		ordering = ['location', 'description']


class Clothing(models.Model):
	description = models.CharField(max_length=500)
	brand = models.CharField(max_length=200, blank=True)
	quantity = models.IntegerField()
	notes = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = "clothing"

	def __str__(self):
		return self.description
