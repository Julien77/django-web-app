# Generated by Django 4.0.3 on 2022-03-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20220323_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='band',
            name='record_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
