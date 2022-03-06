from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import (
    OwnerInfo,
    PolicyInfo,
)


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up OwnerInfo
        name = "Test McTesterton"
        address = """1234 Simple Street
        Simpletown, PA 12345"""
        phone = "(555) 555-8008"
        OwnerInfo.objects.create(name=name, address=address, phone=phone)

        # Set up PolicyInfo
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

        # Create the user
        User.objects.create_user(
            username='test',
            password='secret',
        )

        authenticated_client = Client()
        authenticated_client.login(username='test', password='secret')
        cls.authenticated_client = authenticated_client

    def test_owner_info_exists(self):
        response = self.authenticated_client.get(reverse('meta:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('owner_info' in response.context)

    def test_policy_info_exists(self):
        response = self.authenticated_client.get(reverse('meta:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('policy_info' in response.context)

    def test_view_url_unauthenticated(self):
        url = '/'
        response = self.client.get(url)
        self.assertRedirects(
            response,
            expected_url=f'/accounts/login/?next={url}',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.authenticated_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.authenticated_client.get(reverse('meta:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meta/index.html')


class OwnerInfoCreateViewTest(TestCase):
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
        url = '/meta/owner_info_create/'
        response = self.client.get(url)
        self.assertRedirects(
            response,
            expected_url=f'/accounts/login/?next={url}',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.authenticated_client.get('/meta/owner_info_create/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.authenticated_client.get(
            reverse('meta:owner_info_create')
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.authenticated_client.get(
            reverse('meta:owner_info_create')
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meta/generic_form.html')

    def test_valid_post(self):
        response = self.authenticated_client.post(
            reverse('meta:owner_info_create'),
            {
                'name': 'Test McTesterson',
                'phone_0': '(555) 555-8008',
                'address': 'address',
            }
        )
        self.assertRedirects(
            response,
            expected_url=reverse('meta:index'),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )


class PolicyInfoCreateViewTest(TestCase):
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
        url = '/meta/policy_info_create/'
        response = self.client.get(url)
        self.assertRedirects(
            response,
            expected_url=f'/accounts/login/?next={url}',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.authenticated_client.get('/meta/policy_info_create/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.authenticated_client.get(
            reverse('meta:policy_info_create')
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.authenticated_client.get(
            reverse('meta:policy_info_create')
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meta/generic_form.html')

    def test_valid_post(self):
        response = self.authenticated_client.post(
            reverse('meta:policy_info_create'),
            {
                'policy_number': '12-ER-41798-P',
                'agent_name': 'Mx. Insurance',
                'agent_phone_0': '(555) 237-3119',
                'agent_email': 'mxinsurance@insuran.ce',
                'company_name': 'MxInsurance',
                'company_claims_phone_0': '(800) 111-0000',
                'company_website': 'http://insuran.ce',
            }
        )
        self.assertRedirects(
            response,
            expected_url=reverse('meta:index'),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )


class OwnerInfoUpdateViewTestNoData(TestCase):
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
        url = '/meta/owner_info_update/'
        response = self.client.get(url)
        self.assertRedirects(
            response,
            expected_url=f'/accounts/login/?next={url}',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.authenticated_client.get('/meta/owner_info_update/')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.authenticated_client.get(
            reverse('meta:owner_info_update')
        )
        self.assertEqual(response.status_code, 404)


class PolicyInfoUpdateViewTestNoData(TestCase):
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
        url = '/meta/policy_info_update/'
        response = self.client.get(url)
        self.assertRedirects(
            response,
            expected_url=f'/accounts/login/?next={url}',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.authenticated_client.get('/meta/policy_info_update/')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.authenticated_client.get(
            reverse('meta:policy_info_update')
        )
        self.assertEqual(response.status_code, 404)


class OwnerInfoUpdateViewTestWithData(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up OwnerInfo
        name = "Test McTesterton"
        address = """1234 Simple Street
        Simpletown, PA 12345"""
        phone = "(555) 555-8008"
        OwnerInfo.objects.create(name=name, address=address, phone=phone)

        # Create the user
        User.objects.create_user(
            username='test',
            password='secret',
        )

        authenticated_client = Client()
        authenticated_client.login(username='test', password='secret')
        cls.authenticated_client = authenticated_client

    def test_view_url_unauthenticated(self):
        url = '/meta/owner_info_update/'
        response = self.client.get(url)
        self.assertRedirects(
            response,
            expected_url=f'/accounts/login/?next={url}',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.authenticated_client.get('/meta/owner_info_update/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.authenticated_client.get(
            reverse('meta:owner_info_update')
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.authenticated_client.get(
            reverse('meta:owner_info_update')
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meta/generic_form.html')

    def test_valid_post(self):
        response = self.authenticated_client.post(
            reverse('meta:owner_info_update'),
            {
                'name': 'Test McTesterson',
                'phone_0': '(555) 555-8008',
                'address': 'address',
            }
        )
        self.assertRedirects(
            response,
            expected_url=reverse('meta:index'),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )


class PolicyInfoUpdateViewTestWithData(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up PolicyInfo
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

        # Create the user
        User.objects.create_user(
            username='test',
            password='secret',
        )

        authenticated_client = Client()
        authenticated_client.login(username='test', password='secret')
        cls.authenticated_client = authenticated_client

    def test_view_url_unauthenticated(self):
        url = '/meta/policy_info_update/'
        response = self.client.get(url)
        self.assertRedirects(
            response,
            expected_url=f'/accounts/login/?next={url}',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.authenticated_client.get('/meta/policy_info_update/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.authenticated_client.get(
            reverse('meta:policy_info_update')
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.authenticated_client.get(
            reverse('meta:policy_info_update')
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meta/generic_form.html')

    def test_valid_post(self):
        response = self.authenticated_client.post(
            reverse('meta:policy_info_update'),
            {
                'policy_number': '12-ER-41798-P',
                'agent_name': 'Mx. Insurance',
                'agent_phone_0': '(555) 237-3119',
                'agent_email': 'mxinsurance@insuran.ce',
                'company_name': 'MxInsurance',
                'company_claims_phone_0': '(800) 111-0000',
                'company_website': 'http://insuran.ce',
            }
        )
        self.assertRedirects(
            response,
            expected_url=reverse('meta:index'),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )
