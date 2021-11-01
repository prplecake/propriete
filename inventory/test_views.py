from random import randint

from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from inventory.models import (
	Item,
	Location,
	Clothing,
)


class ItemListViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create items for tests
		number_of_items = 100

		for item_number in range(number_of_items):
			photo = False
			if item_number % 2:
				photo = True
			Item.objects.create(
				description=f'Item {item_number}',
				photo=photo,
			)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(reverse('inventory:inventory'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(reverse('inventory:inventory'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/item_list.html')

	def test_list_all_objects(self):
		response = self.authenticated_client.get(reverse('inventory:inventory'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['item_list']), 100)


class ItemAddViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/item/add/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/item/add/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(reverse('inventory:item_add'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(reverse('inventory:item_add'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/item_form.html')

	def test_valid_post(self):
		response = self.authenticated_client.post(
			reverse('inventory:item_add'),
			{
				'description': 'my item',
				'photo': False,
			}
		)
		self.assertRedirects(
			response,
			expected_url=reverse('inventory:inventory'),
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)


class ItemUpdateViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create an item
		Item.objects.create(
			description="my item",
			photo=False
		)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/item/1/edit/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/item/1/edit/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(
			reverse('inventory:item_update', args=[1])
		)
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(
			reverse('inventory:item_update', args=[1])
		)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/item_form.html')

	def test_valid_post(self):
		response = self.authenticated_client.post(
			reverse('inventory:item_update', args=[1]),
			{
				'description': 'new item description',
			}
		)
		self.assertRedirects(
			response,
			expected_url=reverse('inventory:inventory'),
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)


class ItemDeleteViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create an item
		Item.objects.create(
			description="my item",
			photo=False
		)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/item/1/delete/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/item/1/delete/')
		self.assertRedirects(
			response,
			expected_url='/inventory/',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(
			reverse('inventory:item_delete', args=[1])
		)
		self.assertRedirects(
			response,
			expected_url='/inventory/',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_404_delete_nonexistent_item(self):
		response = self.authenticated_client.get(
			reverse('inventory:item_delete', args=[2])
		)
		self.assertEqual(response.status_code, 404)


class LocationListViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create locations for tests
		number_of_locations = 10

		for loc_number in range(number_of_locations):
			Location.objects.create(
				name=f'Location {loc_number}',
			)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/locations/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/locations/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(reverse('inventory:location_list'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(reverse('inventory:location_list'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/location_list.html')

	def test_list_all_objects(self):
		response = self.authenticated_client.get(reverse('inventory:location_list'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['locations']), 10)


class LocationAddViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/item/add/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/locations/add/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(reverse('inventory:location_add'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(reverse('inventory:location_add'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/location_form.html')

	def test_valid_post(self):
		response = self.authenticated_client.post(
			reverse('inventory:location_add'),
			{'name': 'location'}
		)
		self.assertRedirects(
			response,
			expected_url=reverse('inventory:location_list'),
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)


class LocationDetailViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create locations for tests
		Location.objects.create(
			name='Location 1',
		)

		# Create items for tests
		number_of_items = 100

		for item_number in range(number_of_items):
			photo = False
			if item_number % 2:
				photo = True
			Item.objects.create(
				description=f'Item {item_number}',
				photo=photo,
				location=Location.objects.get(id=1),
			)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/locations/1/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/locations/1/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(
			reverse('inventory:location_detail', args=[1])
		)
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(
			reverse('inventory:location_detail', args=[1])
		)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/location_detail.html')

	def test_list_all_objects(self):
		response = self.authenticated_client.get(
			reverse('inventory:location_detail', args=[1])
		)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['item_list']), 100)


class LocationDeleteViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create a alocation
		Location.objects.create(
			name="my location"
		)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/locations/1/delete/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/locations/1/delete/')
		self.assertRedirects(
			response,
			expected_url='/inventory/locations/',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(
			reverse('inventory:location_delete', args=[1])
		)
		self.assertRedirects(
			response,
			expected_url='/inventory/locations/',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_404_delete_nonexistent_item(self):
		response = self.authenticated_client.get(
			reverse('inventory:location_delete', args=[2])
		)
		self.assertEqual(response.status_code, 404)


class ClothingListViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create locations for tests
		number_of_clothing_items = 100

		for item_number in range(number_of_clothing_items):
			Clothing.objects.create(
				description=f'Clothing item {item_number}',
				quantity=randint(1, 100)
			)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/clothing/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/clothing/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(reverse('inventory:clothing_list'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(reverse('inventory:clothing_list'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/clothing_list.html')

	def test_list_all_objects(self):
		response = self.authenticated_client.get(reverse('inventory:clothing_list'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['clothing_list']), 100)


class ClothingAddViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/clothing/add/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/clothing/add/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(reverse('inventory:clothing_add'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(reverse('inventory:clothing_add'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/clothing_form.html')

	def test_valid_post(self):
		response = self.authenticated_client.post(
			reverse('inventory:clothing_add'),
			{
				'description': 'new clothing item',
				'quantity': 12,
			}
		)
		self.assertRedirects(
			response,
			expected_url=reverse('inventory:clothing_list'),
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)


class ClothingUpdateViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create clothing item for tests
		Clothing.objects.create(
			description='Clothing item',
			quantity=randint(1, 100)
		)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/clothing/1/edit/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/clothing/1/edit/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(
			reverse('inventory:clothing_update', args=[1])
		)
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.authenticated_client.get(
			reverse('inventory:clothing_update', args=[1])
		)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'inventory/clothing_form.html')

	def test_valid_post(self):
		response = self.authenticated_client.post(
			reverse('inventory:clothing_update', args=[1]),
			{
				'description': 'new clothing item description',
				'quantity': 122,
			}
		)
		self.assertRedirects(
			response,
			expected_url=reverse('inventory:clothing_list'),
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)


class ClothingDeleteViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create a alocation
		Clothing.objects.create(
			description="clothing item",
			quantity=randint(1, 100)
		)

		# Create the user
		User.objects.create_user(
			username='test',
			password='secret',
		)

		authenticated_client = Client()
		authenticated_client.login(username='test', password='secret')
		cls.authenticated_client = authenticated_client

	def test_view_url_unauthenticated(self):
		url = '/inventory/clothing/1/delete/'
		response = self.client.get(url)
		self.assertRedirects(
			response,
			expected_url=f'/accounts/login/?next={url}',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_exists_at_desired_location(self):
		response = self.authenticated_client.get('/inventory/clothing/1/delete/')
		self.assertRedirects(
			response,
			expected_url='/inventory/clothing/',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_url_accessible_by_name(self):
		response = self.authenticated_client.get(
			reverse('inventory:clothing_delete', args=[1])
		)
		self.assertRedirects(
			response,
			expected_url='/inventory/clothing/',
			status_code=302,
			target_status_code=200,
			fetch_redirect_response=True
		)

	def test_view_404_delete_nonexistent_item(self):
		response = self.authenticated_client.get(
			reverse('inventory:clothing_delete', args=[2])
		)
		self.assertEqual(response.status_code, 404)
