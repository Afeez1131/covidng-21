# Generated by Django 3.0.5 on 2021-01-07 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('total', '0006_auto_20210106_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='total',
            name='day',
        ),
    ]
