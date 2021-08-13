from django.test import TestCase

from inventory.models import (
	OwnerInfo,
	PolicyInfo,
	Tag,
	Location,
	Item,
	Clothing
)


class OwnerInfoTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all the test methods
		name = "Test McTesterton"
		address = """1234 Simple Street
		Simpletown, PA 12345"""
		phone = "(555) 555-8008"
		OwnerInfo.objects.create(name=name, address=address, phone=phone)

	def test_name_label(self):
		owner = OwnerInfo.objects.get(id=1)
		field_label = owner._meta.get_field('name').verbose_name
		self.assertEqual(field_label, 'name')

	def test_address_label(self):
		owner = OwnerInfo.objects.get(id=1)
		field_label = owner._meta.get_field('address').verbose_name
		self.assertEqual(field_label, 'address')

	def test_phone_label(self):
		owner = OwnerInfo.objects.get(id=1)
		field_label = owner._meta.get_field('phone').verbose_name
		self.assertEqual(field_label, 'phone')

	def test_object_name_is_owner_name(self):
		owner = OwnerInfo.objects.get(id=1)
		expected_object_name = owner.name
		self.assertEqual(str(owner), expected_object_name)


class PolicyInfoTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all the test methods
		policy_number = "12-ER-41798-P"
		agent_name = "Mx. Insurance"
		agent_phone = "(555) 237-3119"
		agent_email = "mxinsurance@insuran.ce"
		company_name = "MxInsurance"
		company_claims_phone = "(800) 111-0000"
		company_website = "http://insuran.ce"
		PolicyInfo.objects.create(
			policy_number=policy_number,
			agent_name=agent_name,
			agent_phone=agent_phone,
			agent_email=agent_email,
			company_name=company_name,
			company_claims_phone=company_claims_phone,
			company_website=company_website
		)

	def test_policy_number_label(self):
		policy = PolicyInfo.objects.get(id=1)
		field_label = policy._meta.get_field('policy_number').verbose_name
		self.assertEqual(field_label, 'policy number')

	def test_agent_name_label(self):
		policy = PolicyInfo.objects.get(id=1)
		field_label = policy._meta.get_field('agent_name').verbose_name
		self.assertEqual(field_label, 'agent name')

	def test_agent_phone_label(self):
		policy = PolicyInfo.objects.get(id=1)
		field_label = policy._meta.get_field('agent_phone').verbose_name
		self.assertEqual(field_label, 'agent phone')

	def test_agent_email_label(self):
		policy = PolicyInfo.objects.get(id=1)
		field_label = policy._meta.get_field('agent_email').verbose_name
		self.assertEqual(field_label, 'agent email')

	def test_company_name_label(self):
		policy = PolicyInfo.objects.get(id=1)
		field_label = policy._meta.get_field('company_name').verbose_name
		self.assertEqual(field_label, 'company name')

	def test_company_claims_phone_label(self):
		policy = PolicyInfo.objects.get(id=1)
		field_label = policy._meta.get_field('company_claims_phone').verbose_name
		self.assertEqual(field_label, 'company claims phone')

	def test_company_website_label(self):
		policy = PolicyInfo.objects.get(id=1)
		field_label = policy._meta.get_field('company_website').verbose_name
		self.assertEqual(field_label, 'company website')

	def test_policy_name_label(self):
		policy = PolicyInfo.objects.get(id=1)
		field_label = policy._meta.get_field('policy_number').verbose_name
		self.assertEqual(field_label, 'policy number')

	def test_object_name_is_policy_number(self):
		policy = PolicyInfo.objects.get(id=1)
		expected_object_name = policy.policy_number
		self.assertEqual(str(policy), expected_object_name)


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
