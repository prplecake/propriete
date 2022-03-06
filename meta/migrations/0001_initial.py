# Generated by Django 3.2.6 on 2021-11-01 03:26

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', phone_field.models.PhoneField(max_length=31)),
            ],
            options={
                'verbose_name': 'Owner',
            },
        ),
        migrations.CreateModel(
            name='PolicyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=200)),
                ('agent_name', models.CharField(max_length=200)),
                ('agent_phone', phone_field.models.PhoneField(max_length=31)),
                ('agent_email', models.CharField(max_length=200)),
                ('agent_website', models.CharField(blank=True, max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('company_claims_phone', phone_field.models.PhoneField(max_length=31)),
                ('company_website', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Policy',
                'verbose_name_plural': 'Policies',
            },
        ),
    ]