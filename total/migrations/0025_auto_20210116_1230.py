# Generated by Django 3.0.5 on 2021-01-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total', '0024_auto_20210116_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
