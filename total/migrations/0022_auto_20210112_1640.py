# Generated by Django 3.0.5 on 2021-01-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total', '0021_auto_20210112_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='day',
            field=models.DateField(max_length=200),
        ),
    ]
