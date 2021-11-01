from django.test import TestCase

from .models import (
	Tag,
	Location,
	Item,
	Clothing
)


class TagTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		name = "my tag"
		Tag.objects.create(name=name)

	def test_name_label(self):
		tag = Tag.objects.get(id=1)
		field_label = tag._meta.get_field('name').verbose_name
		self.assertEqual(field_label, 'name')

	def test_slug_label(self):
		tag = Tag.objects.get(id=1)
		field_label = tag._meta.get_field('slug').verbose_name
		self.assertEqual(field_label, 'slug')

	def test_created_at_label(self):
		tag = Tag.objects.get(id=1)
		field_label = tag._meta.get_field('created_at').verbose_name
		self.assertEqual(field_label, 'created at')

	def test_object_name_is_name(self):
		tag = Tag.objects.get(id=1)
		expected_object_name = tag.name
		self.assertEqual(str(tag), expected_object_name)


class LocationTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		name = "my room"
		Location.objects.create(name=name)

	def test_name_label(self):
		location = Location.objects.get(id=1)
		field_label = location._meta.get_field('name').verbose_name
		self.assertEqual(field_label, 'name')

	def test_slug_label(self):
		location = Location.objects.get(id=1)
		field_label = location._meta.get_field('slug').verbose_name
		self.assertEqual(field_label, 'slug')

	def test_created_at_label(self):
		location = Location.objects.get(id=1)
		field_label = location._meta.get_field('created_at').verbose_name
		self.assertEqual(field_label, 'created at')

	def test_object_name_is_name(self):
		location = Location.objects.get(id=1)
		expected_object_name = location.name
		self.assertEqual(str(location), expected_object_name)


class ItemTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		description = "my item"
		photo = False
		Item.objects.create(description=description, photo=photo)

	def test_description_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('description').verbose_name
		self.assertEqual(field_label, 'description')

	def test_slug_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('location').verbose_name
		self.assertEqual(field_label, 'location')

	def test_created_at_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('created_at').verbose_name
		self.assertEqual(field_label, 'created at')

	def test_serial_number_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('serial_number').verbose_name
		self.assertEqual(field_label, 'serial number')

	def test_purchase_date_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('purchase_date').verbose_name
		self.assertEqual(field_label, 'purchase date')

	def test_notes_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('notes').verbose_name
		self.assertEqual(field_label, 'notes')

	def test_photo_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('photo').verbose_name
		self.assertEqual(field_label, 'photo')

	def test_purchase_location_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('purchase_location').verbose_name
		self.assertEqual(field_label, 'purchase location')

	def test_purchase_price_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('purchase_price').verbose_name
		self.assertEqual(field_label, 'purchase price')

	def test_current_value_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('current_value').verbose_name
		self.assertEqual(field_label, 'current value')

	def test_make_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('make').verbose_name
		self.assertEqual(field_label, 'make')

	def test_tags_label(self):
		item = Item.objects.get(id=1)
		field_label = item._meta.get_field('tags').verbose_name
		self.assertEqual(field_label, 'tags')

	def test_object_name_is_description(self):
		item = Item.objects.get(id=1)
		expected_object_name = item.description
		self.assertEqual(str(item), expected_object_name)


class ClothingTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		description = "my clothing item"
		quantity = 1
		Clothing.objects.create(description=description, quantity=quantity)

	def test_description_label(self):
		clothing = Clothing.objects.get(id=1)
		field_label = clothing._meta.get_field('description').verbose_name
		self.assertEqual(field_label, 'description')

	def test_slug_label(self):
		clothing = Clothing.objects.get(id=1)
		field_label = clothing._meta.get_field('brand').verbose_name
		self.assertEqual(field_label, 'brand')

	def test_created_at_label(self):
		clothing = Clothing.objects.get(id=1)
		field_label = clothing._meta.get_field('quantity').verbose_name
		self.assertEqual(field_label, 'quantity')

	def test_serial_number_label(self):
		clothing = Clothing.objects.get(id=1)
		field_label = clothing._meta.get_field('notes').verbose_name
		self.assertEqual(field_label, 'notes')

	def test_object_name_is_description(self):
		clothing = Clothing.objects.get(id=1)
		expected_object_name = clothing.description
		self.assertEqual(str(clothing), expected_object_name)
