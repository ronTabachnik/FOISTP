# Generated by Django 3.2.9 on 2021-12-17 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_remove_order_total_price'),
        ('requests_', '0007_returnrequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='returnrequest',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
