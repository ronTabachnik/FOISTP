# Generated by Django 3.2.9 on 2021-12-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20211209_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Shipped'), ('2', 'Ordered'), ('3', 'Delivered'), ('4', 'Processing'), ('5', 'Error')], default='5', max_length=2),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]
