# Generated by Django 3.2.9 on 2021-12-12 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='items.item'),
        ),
    ]