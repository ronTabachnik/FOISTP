# Generated by Django 3.2.9 on 2021-12-16 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_customer_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='status',
        ),
    ]
