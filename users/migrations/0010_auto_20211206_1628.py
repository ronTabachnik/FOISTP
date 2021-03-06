# Generated by Django 3.2.9 on 2021-12-06 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0003_auto_20211202_0237'),
        ('users', '0009_alter_registeredcustomer_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcustomer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='registered_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registeredcustomer',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='items.Item'),
        ),
    ]
