# Generated by Django 3.2.9 on 2021-12-09 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_customer_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraddress',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.customeraddress'),
            preserve_default=False,
        ),
    ]