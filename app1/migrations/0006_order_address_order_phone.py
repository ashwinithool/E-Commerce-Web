# Generated by Django 4.1.3 on 2022-12-31 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]