# Generated by Django 4.0.3 on 2022-03-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20220323_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='hometown',
            field=models.CharField(max_length=100, null=True),
        ),
    ]