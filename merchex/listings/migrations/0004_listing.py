# Generated by Django 4.0.3 on 2022-03-19 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=280)),
                ('sold', models.BooleanField(default=False)),
                ('year', models.IntegerField(verbose_name=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]))),
                ('type_listing', models.CharField(max_length=26, verbose_name=[('Records', 'Records'), ('Clothing', 'Clothing'), ('Posters', 'Posters'), ('Miscellaneous', 'Miscellaneous')])),
            ],
        ),
    ]
