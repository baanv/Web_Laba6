# Generated by Django 5.0.6 on 2024-05-24 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('china', '0020_alter_china_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='china',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='china.category', verbose_name='Категории'),
        ),
    ]
