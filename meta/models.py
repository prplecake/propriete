from django.db import models

from phone_field import PhoneField

from utils.urlutils import add_url_protocol


class OwnerInfo(models.Model):
	name = models.CharField(max_length=200)
	address = models.TextField()
	phone = PhoneField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Owner"


class PolicyInfo(models.Model):
	policy_number = models.CharField(max_length=200)
	agent_name = models.CharField(max_length=200)
	agent_phone = PhoneField()
	agent_email = models.CharField(max_length=200)
	agent_website = models.CharField(max_length=200, blank=True)
	company_name = models.CharField(max_length=200)
	company_claims_phone = PhoneField()
	company_website = models.CharField(max_length=200)

	class Meta:
		verbose_name = "Policy"
		verbose_name_plural = "Policies"

	def __str__(self):
		return self.policy_number

	def save(self, *args, **kwargs):
		self.company_website = add_url_protocol(self.company_website)
		super().save(*args, **kwargs)
