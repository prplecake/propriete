from django.test import TestCase

from .models import (
    OwnerInfo,
    PolicyInfo,
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
        field_label = owner._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_address_label(self):
        owner = OwnerInfo.objects.get(id=1)
        field_label = owner._meta.get_field("address").verbose_name
        self.assertEqual(field_label, "address")

    def test_phone_label(self):
        owner = OwnerInfo.objects.get(id=1)
        field_label = owner._meta.get_field("phone").verbose_name
        self.assertEqual(field_label, "phone")

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
        field_label = policy._meta.get_field("policy_number").verbose_name
        self.assertEqual(field_label, "policy number")

    def test_agent_name_label(self):
        policy = PolicyInfo.objects.get(id=1)
        field_label = policy._meta.get_field("agent_name").verbose_name
        self.assertEqual(field_label, "agent name")

    def test_agent_phone_label(self):
        policy = PolicyInfo.objects.get(id=1)
        field_label = policy._meta.get_field("agent_phone").verbose_name
        self.assertEqual(field_label, "agent phone")

    def test_agent_email_label(self):
        policy = PolicyInfo.objects.get(id=1)
        field_label = policy._meta.get_field("agent_email").verbose_name
        self.assertEqual(field_label, "agent email")

    def test_company_name_label(self):
        policy = PolicyInfo.objects.get(id=1)
        field_label = policy._meta.get_field("company_name").verbose_name
        self.assertEqual(field_label, "company name")

    def test_company_claims_phone_label(self):
        policy = PolicyInfo.objects.get(id=1)
        field_label = policy._meta.get_field(
            "company_claims_phone"
        ).verbose_name
        self.assertEqual(field_label, "company claims phone")

    def test_company_website_label(self):
        policy = PolicyInfo.objects.get(id=1)
        field_label = policy._meta.get_field("company_website").verbose_name
        self.assertEqual(field_label, "company website")

    def test_policy_name_label(self):
        policy = PolicyInfo.objects.get(id=1)
        field_label = policy._meta.get_field("policy_number").verbose_name
        self.assertEqual(field_label, "policy number")

    def test_object_name_is_policy_number(self):
        policy = PolicyInfo.objects.get(id=1)
        expected_object_name = policy.policy_number
        self.assertEqual(str(policy), expected_object_name)
