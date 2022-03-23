# Generated by Django 3.2.12 on 2022-03-23 12:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], max_length=5),
        ),
        migrations.AlterField(
            model_name='listing',
            name='type_listing',
            field=models.CharField(choices=[('Records', 'Records'), ('Clothing', 'Clothing'), ('Posters', 'Posters'), ('Miscellaneous', 'Miscellaneous')], max_length=26),
        ),
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]
