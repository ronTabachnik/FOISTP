# Generated by Django 3.2.9 on 2021-12-09 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20211202_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='create',
            new_name='created',
        ),
    ]
