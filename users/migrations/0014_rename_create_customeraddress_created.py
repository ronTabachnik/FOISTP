# Generated by Django 3.2.9 on 2021-12-09 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_customer_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeraddress',
            old_name='create',
            new_name='created',
        ),
    ]