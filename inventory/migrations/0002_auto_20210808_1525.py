# Generated by Django 3.2.6 on 2021-08-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothing',
            name='name',
        ),
        migrations.AddField(
            model_name='clothing',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
