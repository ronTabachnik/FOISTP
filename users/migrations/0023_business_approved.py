# Generated by Django 3.2.9 on 2021-12-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
