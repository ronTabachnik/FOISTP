# Generated by Django 3.2.9 on 2021-12-12 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_registeredcustomer_saved_address'),
        ('items', '0011_auto_20211212_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.registeredcustomer'),
            preserve_default=False,
        ),
    ]
